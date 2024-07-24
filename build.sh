#!/bin/bash

for f in wiki/diary/20*; do date="$(basename -s .wiki $f | sed -e 's/-//g')0000"; touch -mt $date $f; done

vim "+VimwikiDiaryIndex 2" "+VimwikiDiaryGenerateLinks" "+VimwikiAll2HTML!" "+VimwikiRss" "+q"
