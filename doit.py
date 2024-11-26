import http.server, glob, json, markdown, os, os.path, re, shutil, socketserver
from string import Template
from collections import OrderedDict

SRC="src"
OUT="docs"
TEMPLATES="templates"
STATIC="static"
PORT=8000

def sort_paths(paths):
    dirs = []
    files = []

    for path in paths:
        if "/" in path:
            dirs.append(path)
        elif path == "index.md":
            files = [path] + files
        else:
            files.append(path)

    tree = dict()

    for path in dirs:
        parts = path.split("/")
        root, path = parts[0], "/".join(parts[1:])

        if root not in tree:
            tree[root] = list()

        tree[root].append(path)

    return files + [
        root + "/" + path
        for root in sorted(tree.keys())
        for path in sort_paths(tree[root])
    ]

def get_title(fn):
    with open(fn) as f:
        md = f.read()

    return re.sub(r'^# *', '', md.split("\n")[0])

def to_outfn(fn):
    outfn = fn[:-3] + ".html"
    outfn = os.path.join(OUT, os.path.relpath(outfn, SRC))
    return outfn

def convert(fn, **kwargs):
    outfn = to_outfn(fn)

    os.makedirs(os.path.dirname(outfn), exist_ok=True)

    with open(fn) as inf:
        html = markdown.markdown(inf.read())

    template = Template(open(os.path.join(TEMPLATES, "page.html")).read())

    with open(outfn, "w") as outf:
        outf.write(template.substitute(
            page_title=get_title(fn),
            body=html,
            **kwargs,
        ))

# Returns [[title, path, children]]
def make_index(fns):
    dirs = OrderedDict()

    for fn in fns:
        dirname = os.path.dirname(os.path.relpath(fn, SRC))

        if dirname == "":
            parts = []
        else:
            parts = dirname.split("/")

        cur = dirs
        for part in parts:
            if part not in cur:
                cur[part] = OrderedDict()

            cur = cur[part]

        outfn = to_outfn(fn)

        cur[os.path.basename(outfn)] = get_title(fn)

    return dirs

def make_nav(index, path="/"):
    nav_template = Template(open(os.path.join(TEMPLATES, "nav.html")).read())
    item_template = Template(open(os.path.join(TEMPLATES, "nav-item.html")).read())

    children = []

    for key, value in index.items():
        if isinstance(value, str) and (path == "/" or key != "index.html"):
            children.append({
                "uri": os.path.join(path, key),
                "title": value,
                "children": "",
            })
        elif isinstance(value, OrderedDict):
            children.append({
                "uri": os.path.join(path, key, "index.html"),
                "title": value["index.html"],
                "children": make_nav(value, path=os.path.join(path, key)),
            })

    children="\n".join([
        item_template.substitute(**child)
        for child in children
    ])

    return nav_template.substitute(children=children)

def copy_static():
    shutil.copytree(STATIC, OUT, dirs_exist_ok=True)

def serve():
    os.chdir(OUT)
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"http://0.0.0.0:{PORT}")
        httpd.serve_forever()

def main():
    mds = glob.glob(SRC + "/**/*.md", recursive=True)

    mds = sort_paths(sorted(mds))
    print(mds)

    index = make_index(mds)
    print(json.dumps(index, indent=2))

    nav = make_nav(index)

    for fn in mds:
        convert(fn, site_title="engledow.me", nav=nav)

    copy_static()

    serve()

if __name__ == "__main__":
    main()
