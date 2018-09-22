#!/bin/bash

cat 192_words.txt |  perl -pe 's/\\n//g' | perl -pe 's/\s+/\n/g' | sed  '/^$/d' | sort | uniq -c | sort -k2 -n -r |awk '{print $2" "$1}'


## Breakdown of commands

# 1. first perl, remove the '\n' strings
# 2. second perl, replace the space with newline
# 3. sed remove the empty lines
# 4. sort the words
# 5. uniq count the repeated words in adjacent lines
# 6. sort the word counts
# 7. print with format


