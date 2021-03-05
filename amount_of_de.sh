#!/bin/bash

# Before you randomly run this code, first read the readme (link here:)
# https://github.com/hacxpiont/Introduction_to_research_methods/blob/main/README.md

# gets the wikipedia page and puts the wikipedia page in a variable
WIKIPEDIA_PAGE=`wiki-cli -Pl nl Rijksuniversiteit Groningen`

# this line creates an empty (temporary) file named de_in_rug_nl.txt
touch de_in_rug_nl.txt
FILEPATH=./de_in_rug_nl.txt

# -f checks if the file exists and is a normal file, since the file is created above here, it exists.
# the lines basically put only the text in the file to make things less complicated.
if [ -f "$FILEPATH" ]
then 
    echo "$WIKIPEDIA_PAGE" > "$FILEPATH"
fi

# the first line puts every word on a seperate line
# the second line counts every line that is 'de' and prints the amount to the terminal
grep -E -o '\w+' de_in_rug_nl.txt | \
  grep -w 'de' | wc -l

# removes the file de_in_rug_nl.txt so you don't have to
rm de_in_rug_nl.txt
