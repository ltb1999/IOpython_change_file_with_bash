#!/bin/bash
file_location=oldFiles.txt
> oldFiles.txt
grep ' jane ' ../data/list.txt | cut -d ' ' -f 3 | while read -r files; do
 if test -e ../$files; then
  echo $files >> oldFiles.txt
 fi
done
