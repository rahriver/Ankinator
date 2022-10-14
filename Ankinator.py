#!/bin/python3
from PyDictionary import PyDictionary
import re

# <--------- METADATA ----------> #
TEMPLATE = "/home/core/Documents/Notes/Template.md"
NORDS = "/home/core/Documents/Notes/Nords_list.md"
WORDS = "/home/core/TPO.txt"
PATTERN1 = re.compile(r'Meaning:')
PATTERN2 = re.compile(r'Expression:')
PATTERN3 = re.compile(r'TITLE')
DIR = "/home/core/Temp/MEGA/Obsidian/Broadest/Vocab/"

# <--------- Clean List ----------> #
with open(NORDS, 'r') as f:
    L1 = f.read().strip().split(' ')

L2 = [word.capitalize() for word in L1]
L3 = [word + 's' for word in L2]
L4 = sorted(L1 + L2 + L3)

with open(WORDS, 'r') as f:
    words = f.read().strip().split()

word_list = sorted(list(set([word.capitalize() for word in words if word not in L4 and len(word) > 1])))
# Remove any word from word_list that is word + 's'
for word in word_list:
    if word + 's' in word_list:
        word_list.remove(word + 's')

# <--------- Get Definitions ----------> #
dictionary = PyDictionary()
# dictionary = MultiDictionary()
# dictionary.set_words_lang('en')
print(f"<<Found {len(word_list)} Words>>\n")

for word in word_list:
    define = str(dictionary.meaning(word, disable_errors=True))
    if define != "None":
        with open(DIR + word + ".md", "w") as f:
            f.write(word)
            print(f"Found {word} {word_list.index(word)}/{len(word_list)}")
        # Copying the template to the new file
        with open(TEMPLATE, "r") as f:
            with open(f"{DIR}{word}.md", "a") as f2:
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

print("\n### Finished ###")
