#!/bin/python3

from nltk.corpus import wordnet
import re
import os

# <--------- Creating a list of words to ignore ----------> #
with open('Nords.txt', 'r') as f:
    L1 = f.read().split(' ')

L2 = []
for i in L1:
    L2.append(i.capitalize())

NORDS = [*L1, *L2]

# <--------- Creating a clean word list ----------> #
with open("words", 'r') as f:
    words = f.read().split(" ")

word_list = []
for word in words:
    if word not in NORDS:
        word_list.append(word)

# <--------- Creating a file for each word ----------> #
TEMPLATE = "/home/core/Documents/Notes/template.md"
PATTERN1 = re.compile(r'Meaning:')
PATTERN2 = re.compile(r'Expression:')
PATTERN3 = re.compile(r'TITLE')
DIR = "/home/core/Temp/Words/"

def main():
    for word in word_list:
        try:
            syns = wordnet.synsets(str(word))
            define = str(syns[0].definition())
        except IndexError:
            print("No definition for " + word)
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
                # find and replace the PATTERN3 with the word
                elif PATTERN3.match(line):
                    f.write(line.replace("TITLE",f"# {word}"))

if __name__ == "__main__":
    main()
