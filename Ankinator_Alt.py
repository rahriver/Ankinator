#!/bin/python3
from nltk.corpus import wordnet
import re
import os

# <--------- METADATA ----------> #
TEMPLATE = "/home/core/Documents/Notes/Template.md"
NORDS = "/home/core/Documents/Notes/Nords_list.md"
WORDS = "/home/core/Documents/Notes/science.txt"
PATTERN1 = re.compile(r'Meaning:')
PATTERN2 = re.compile(r'Expression:')
PATTERN3 = re.compile(r'TITLE')
DIR = "/home/core/Temp/Words/"
NOTFOUND = "/home/core/Documents/Notes/NotFound.md"

# <--------- Clean List ----------> #
with open(NORDS, 'r') as f:
    L1 = f.read().split(' ')
L2 = []
for i in L1:
    L2.append(i.capitalize())
with open(WORDS, 'r') as f:
    words = f.read().split(" ")
L3 = [*L1, *L2]
word_list = []
for word in words:
    if word not in L3:
        word_list.append(word.capitalize())
word_list = list(set(word_list))
not_found = list(set([]))

# <--------- Get Definitions ----------> #
for word in word_list:
    try:
        syns = wordnet.synsets(str(word))
        define = str(syns[0].definition())
    except IndexError:
        # write words that are not found to a file
        not_found.append(word)
        with open(NOTFOUND, "w") as f:
            for i in not_found:
                f.write(i + " ")
        continue
    # create a markdown file with the word as the title
    os.system(f"touch {DIR}{word}.md")
    # copy the template to the new file
    os.system(f"cp {TEMPLATE} {DIR}{word}.md")
    # open the new file and append the definition after the line that matches the PATTERN1
    with open(f"{DIR}{word}.md",'r') as f:
        lines = f.readlines()
    with open(f"{DIR}{word}.md",'w') as f:
        for line in lines:
            f.write(line)
            if PATTERN1.search(line):
                f.write(f"{define}\n")
            elif PATTERN2.search(line):
                f.write(f"{word}\n")
            elif PATTERN3.match(line):
                f.write(line.replace("TITLE",f"# {word}"))

