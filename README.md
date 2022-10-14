# Ankinator
A Python script that you can run on your text files to extract new words from it and create anki flashcards out of them.

![image](https://user-images.githubusercontent.com/89016694/195785109-947af3f3-9332-4fe5-adef-c276d65ae727.png)
![image](https://user-images.githubusercontent.com/89016694/195785164-038f7eaa-be3f-4814-94d1-6027f5350ea8.png)
![image](https://user-images.githubusercontent.com/89016694/195785408-d934c2c5-2802-4957-b371-75a2030bfd2e.png)
![image](https://user-images.githubusercontent.com/89016694/195785468-01d2744e-a0d5-4d18-b210-118c42e8211b.png)


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

> You should also change the TARGET DECK to just DECK inside the `Obsidian to Anki` plugin.

## Support
**Give this repository a star and share it with people who care about this :O**

