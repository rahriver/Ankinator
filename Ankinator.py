#!/bin/python3
from PyDictionary import PyDictionary
from nltk.stem import WordNetLemmatizer
import re

# <--------- METADATA ----------> #
TEMPLATE = "/home/core/Documents/Notes/Template.md"
NORDS = "/home/core/Documents/Notes/Nords_list.md"
WORDS = "/home/core/Content.md"
PATTERN1 = re.compile(r'Meaning:')
PATTERN2 = re.compile(r'Expression:')
DIR = "/home/core/Temp/Words/"

# <--------- NLP Lemmatization ----------> #
lemmatizer = WordNetLemmatizer()

with open(NORDS, 'r') as f:
    Not_Words = f.read().strip().split(' ')

with open(WORDS, 'r') as f:
    words = f.read().strip().split()

initial_list = list(
    set([word for word in words if word not in Not_Words and len(word) > 1]))
word_list = sorted(
    list(set([lemmatizer.lemmatize(word.capitalize()) for word in initial_list])))

# <--------- Get Definitions ----------> #
dictionary = PyDictionary()

print(f"<<Found {len(word_list)} Words>>\n")
for word in word_list:
    define = str(dictionary.meaning(word, disable_errors=True))
    if define != "None":
        with open(DIR + word + ".md", "w") as f:
            pass
            print(f"Found {word} {word_list.index(word) + 1}/{len(word_list)}")
        # Copying the template to the new file
        with open(TEMPLATE, "r") as f:
            with open(f"{DIR}{word}.md", "a") as f2:
                f2.write(f.read())
        # Finding patterns and replacing them with the word and definition
        with open(f"{DIR}{word}.md", 'r') as f:
            lines = f.readlines()
        with open(f"{DIR}{word}.md", 'w') as f:
            for line in lines:
                f.write(line)
                if PATTERN1.search(line):
                    f.write(f"{define}\n")
                elif PATTERN2.search(line):
                    f.write(f"{word}\n")

print("\n### Finished ###")
