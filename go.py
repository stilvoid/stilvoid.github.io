import os
import datetime
import frontmatter, markdown
from html import escape
import shutil

POSTS = "posts"
DOCS = "docs"
STATIC = "static"

NOW = datetime.datetime.utcnow().isoformat()[:19]+"Z"

with open("templates/post.html") as f:
    HTML_TEMPLATE = f.read()

with open("templates/entry.xml") as f:
    ENTRY_TEMPLATE = f.read()

with open("templates/feed.xml") as f:
    FEED_TEMPLATE = f.read()

def to_html(post):
    return HTML_TEMPLATE.format(**post)

def to_rss(post):
    post["entry"] = escape(post["html"])
    return ENTRY_TEMPLATE.format(**post, categories="\n".join(f"<category term=\"{tag}\" />" for tag in post["tags"].split(" ")))

def process(fn):
    """1234-56-78-foo-bar.md"""

    post = frontmatter.load(f"{POSTS}/{fn}")
    post["path"] = f"{fn[0:4]}/{fn[5:7]}/{fn[8:10]}/{fn[11:-3]}/"
    post["now"] = NOW
    post["date"] = fn[:10]
    post["slug"] = fn[11:-3]
    post["html"] = markdown.markdown(post.content, extensions=["fenced_code", "codehilite"])

    print(post["path"])
    
    os.makedirs(os.path.dirname(f"{DOCS}/{post['path']}"))
    with open(f"{DOCS}/{post['path']}index.html", "w") as f:
        f.write(to_html(post))
    
    return to_rss(post)

def main():
    shutil.rmtree(DOCS)
    shutil.copytree(STATIC, DOCS)

    entries=[process(fn) for fn in sorted(os.listdir(POSTS), reverse=True)]

    with open(f"{DOCS}/feed.xml", "w") as f:
        f.write(FEED_TEMPLATE.format(now=NOW, entries="\n".join(entries)))

if __name__ == "__main__":
    main()
