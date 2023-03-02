# Ankinator: Extract, Lemmatize, Define, and Pronounce Words for Anki
Ankinator is a Python script that extracts words from your text and uses NLP lemmatization to normalize them. Then, it finds definitions and synonyms for each word using WordNet and gets the pronunciations from Google Translate with the gTTS library. Finally, it saves the results into a CSV file that you can import into Anki, a popular spaced repetition flashcard program.

## Getting Started
### Prerequisites
- [Anki](https://apps.ankiweb.net/)
- Python 3.x
- [Natural Language Toolkit (NLTK)](https://www.nltk.org/)
- [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/en/latest/)

### Installing
Clone this repository to your local machine using `git clone https://github.com/rahriver/Ankinator.git`

### Usage
1. Navigate to the Ankinator directory.
2. Run python `main.py` with the following options:
`-i` or `--input`: The path to your input text file.
`-o` or `--output`: The path to save the resulting CSV file. If not specified, it will be saved as output.csv in the current directory.
Import the resulting CSV file into Anki using the import feature.

### Example
Suppose you have a file called `sample.txt` with the following content:

```
The quick brown fox jumped over the lazy dog. The dog didn't seem to care.
```

You can run the script with the following command:

```
python ankinator.py -i sample.txt -o output.csv
```

This will create a file called `output.csv` with the following content:


| Word        | Definition  | Synonyms                  |
| ----------- | ----------- | -------------------------|
| quick       | moving fast or doing something in a short time | agile, nimble, lively   |
| brown       | of a color produced by mixing red, yellow, and blue, as of dark wood or rich soil |    |
| fox         | a carnivorous mammal of the dog family with a pointed muzzle and bushy tail |    |
| jump        | push oneself off a surface and into the air by using the muscles in one's legs and feet | leap, spring, bound      |
| lazy        | unwilling to work or use energy | idle, indolent, slothful  |
| dog         | a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice |    |
| care        | the provision of what is necessary for the health, welfare, maintenance, and protection of someone or something | concern, attention, caution|


You can then import this file into Anki and start studying!

### ☕ Support
Give this repo a star and share it with people who care about this :O
