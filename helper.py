import json
import sys

def do_item(section):
    if "Chapter" in section:
        if section["Chapter"]["path"].startswith("diary/"):
            parts = section["Chapter"]["content"].split("\n")
            parts.insert(1, "\n")
            parts.insert(2, "*published " + section["Chapter"]["path"][6:16] + "*")

            section["Chapter"]["content"] = "\n".join(parts)
            
        for item in section["Chapter"]["sub_items"]:
            do_item(item)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports": 
            sys.exit(0)

    context, book = json.load(sys.stdin)

    for section in book["sections"]:
        do_item(section)

    print(json.dumps(book))
