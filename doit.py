import glob, markdown, os, os.path, re
from string import Template

BASE="src"
OUT="docs"
TEMPLATES="templates"

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
    outfn = os.path.join(OUT, os.path.relpath(outfn, BASE))
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

    print(outfn)

# Returns [[title, path, children]]
def make_index(fns):
    out = list()

    parts = [
        [os.path.relpath(to_outfn(fn), OUT), get_title(fn)]
        for fn in fns
    ]

    for part in parts:
        if os.path.basename(part[0]) == "index.html":
            out.append([part[0], part[1], [
                child
                for child in parts
                if os.path.dirname(child[0]) == os.path.dirname(part[0])
            ]])

    return out

def main():
    mds = glob.glob(BASE + "/**/*.md", recursive=True)

    mds = sort_paths(mds)

    print(mds)

    index = make_index(mds)

    for part in index:
        print(part)

    #for fn in mds:
    #    convert(fn, site_title="engledow.me", index=index)

if __name__ == "__main__":
    main()
