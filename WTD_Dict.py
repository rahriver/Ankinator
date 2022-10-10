#!/bin/python3

from nltk.corpus import wordnet
import re
import subprocess as sp
import os
from nltk.util import pr

TEMPLATE = "/home/core/Documents/Notes/template.md"
PATTERN1 = re.compile(r'Meaning:')
PATTERN2 = re.compile(r'Expression:')
PATTERN3 = re.compile(r'TITLE')
DIR = "/home/core/Temp/Words/"
WORDS = "/home/core/Documents/Notes/Vocab.md"
DB = "fd-deu-eng"

# <--------- Creating a list of words to ignore ----------> #
# with open('Nords.txt', 'r') as f:
#     L1 = f.read().split(' ')

# L2 = []
# for i in L1:
#     L2.append(i.capitalize())

# NORDS = [*L1, *L2]

# <--------- Creating a clean word list ----------> #
with open(WORDS, 'r') as f:
    words = f.read().strip().split("\n")


print("Searching...\n")
for word in words:
    process = sp.Popen(['dict', '-d', DB, word], stdout=sp.PIPE, universal_newlines=True)
    define, stderr = process.communicate()
    print(f"{word} done")
    os.system(f"touch {DIR}{word.capitalize()}.md")
    os.system(f"cp {TEMPLATE} {DIR}{word.capitalize()}.md")
    with open(f"{DIR}{word.capitalize()}.md",'r') as f:
        lines = f.readlines()
    with open(f"{DIR}{word.capitalize()}.md",'w') as f:
        for line in lines:
            f.write(line)
            if PATTERN1.search(line):
                f.write(f"{define}\n")
            elif PATTERN2.search(line):
                f.write(f"{word}\n")
            elif PATTERN3.match(line):
                f.write(line.replace("TITLE",f"# {word}"))
print("<<--------- Finished --------->>")
