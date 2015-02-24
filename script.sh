#!/bin/bash

date="${1}"


git add -A
git commit --date=\"$date\" -m "meow"
git push -f origin master
