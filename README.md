# Ankinator
A Python script that you can run on your text files to extract new words from it and create anki flashcards out of them.

# Preview
https://user-images.githubusercontent.com/89016694/195893141-1092e973-b534-4476-9dba-f051bfeadaab.mp4
![All](https://user-images.githubusercontent.com/89016694/195787135-690eb8b1-6ac7-4210-b697-87137f0e0995.jpg)

## Dependencies
- [Obsidian](https://obsidian.md/)
- [Obsidian To Anki Plugin](https://github.com/obsidian_to_Anki)
- [PyDictionary](https://github.com/geekpradd/PyDictionary)

## Usage
- Run the `File_Cleaner` script on your text to make it clean and by making it clean I mean to remove any dots and numbers and junks from the text file to make words more accessible.
- Then you can change the `Metadata` inside the python script for your own use and run the script.
- `Ankinator.py` is the main script that uses [PyDictionary](https://github.com/geekpradd/PyDictionary) to pull definitions.
- `Ankinator_Alt.py` pulls single definition from wordnet, it's so much quicker but not as accurate as PyDictionary.
- After running the scripts on your text files, you can now put those created files inside your obsidian directory and run `Obsidian to Anki` plugin on them.

### Modify
- `TEMPLATE`: Specify the template you want to use for your notes.
- `NORDS`: AKA "Not Words", is a list of words that you don't want the script to search for, such as [but, am, i, so, for, etc.]. You can add more to this file.
- `WORDS`: Is the main text file that you want to run the script on.
- `DIR`: Directory that your flashcards will get save.

> You should also change the TARGET DECK to just DECK inside the `Obsidian to Anki` plugin.

## ☕ Support
**Give this repository a star and share it with people who care about this kind of stuff :O**

