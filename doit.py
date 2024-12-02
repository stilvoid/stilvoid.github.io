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

def make_nav(index):
    nav_template = Template(open(os.path.join(TEMPLATES, "nav.html")).read())
    item_template = Template(open(os.path.join(TEMPLATES, "nav-item.html")).read())

    return nav_template.substitute(children="\n".join([
            item_template.substitute(uri=item[0], title=item[1], extra=" class=\"selected\"" if item[2] else "")
            for item in index
        ])
    )

def make_sections(index, fn):
    parts = [""] + os.path.relpath(fn, SRC).split("/")[:-1]

    web_path = "/" + os.path.relpath(to_outfn(fn), OUT)

    out = []
    cur = index

    for i, part in enumerate(parts):
        if part != "":
            cur = cur[part]

        section = []
        for key, value in cur.items():
            path = parts[:i+1] + [key]
            name = value
            selected = False

            path = "/".join(path)

            if web_path.startswith(path):
                selected = True

            if not isinstance(value, str):
                path += "/index.html"
                name = value["index.html"]

            if i == 0 or key != "index.html":
                section.append((path, name, selected))

        if part == "blog":
            section = reversed(section)

        out.append(section)

    return out

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

    index = make_index(mds)

    for fn in mds:
        make_sections(index, fn)

    for fn in mds:
        convert(fn, site_title="engledow.me", nav="\n".join([
            make_nav(section)
            for section 
            in make_sections(index, fn)
        ]))

    copy_static() 

    serve()

if __name__ == "__main__":
    main()
