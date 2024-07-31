#!/bin/bash

cp -a static/* ./docs/

for f in wiki/diary/20*; do date="$(basename -s .wiki "$f" | sed -e 's/-//g')0000"; touch -mt "$date" "$f"; done

rm wiki/diary/index.wiki

vim \
    "+VimwikiDiaryIndex 2" \
    "+VimwikiDiaryGenerateLinks" \
    "+s/.*/%title Blog posts/" \
    "+w" \
    "+VimwikiAll2HTML" \
    "+VimwikiRss" \
    "+q"
