#!/bin/bash

# Build diary index
echo "%title Blog posts" >wiki/diary/index.wiki
for f in $(find wiki/diary/*.wiki ! -name "index.wiki" | sort -r); do
    date="$(basename -s .wiki "$f")";
    timestamp="$(echo "$date" | sed -e 's/-//g')0000";
    title=$(head -n 1 "$f" | sed -e 's/^%title //')

    touch -mt "$timestamp" "$f";

    echo "- [[$date|$date: $title]]" >>wiki/diary/index.wiki
done

# Convert to HTML and generate RSS feed
vim \
    "+VimwikiIndex 2" \
    "+VimwikiAll2HTML" \
    "+VimwikiRss" \
    "+q"

# Copy static content
cp -a static/* ./docs/
