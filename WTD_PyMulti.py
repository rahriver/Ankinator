#!/bin/python3
from PyMultiDictionary import MultiDictionary
import re

# <--------- METADATA ----------> #
TEMPLATE = "/home/core/Documents/Notes/Template.md"
NORDS = "/home/core/Documents/Notes/Nords_list.md"
WORDS = "/home/core/Documents/Notes/Vocab.md"
PATTERN1 = re.compile(r'Meaning:')
PATTERN2 = re.compile(r'Expression:')
PATTERN3 = re.compile(r'TITLE')
DIR = "/home/core/Temp/Words/"

# <--------- Clean List ----------> #
with open(NORDS, 'r') as f:
    L1 = f.read().split(' ')
L2 = []
for i in L1:
    L2.append(i.capitalize())
with open(WORDS, 'r') as f:
    words = f.read().strip().split(" ")
L3 = set([*L1, *L2])

word_list = []
for word in words:
    if word not in L3:
        word_list.append(word.capitalize())
word_list = list(set(word_list))

# <--------- Get Definitions ----------> #
dictionary = MultiDictionary()
print("Getting Definitions...\n")
for word in word_list:
    try:
        define = str(dictionary.meaning('en', word))
    except IndexError:
        print("No definition for " + word)
        continue
    # Creating a file for each word
    if len(define) > 12:
        with open(DIR + word + ".md", "w") as f:
            f.write(word)
            print(f"{word} Done")
        # Copying the template to the new file
        with open(TEMPLATE, "r") as f:
            with open(DIR + word + ".md", "a") as f2:
                f2.write(f.read())
        # Finding patterns and replacing them with the word and definition
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
    else:
        print(f"\n<<No definition for {word}>>\n")
print("\n### Finished ###")
