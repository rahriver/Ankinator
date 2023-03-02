from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from collections import Counter
from rich.console import Console
from gtts import gTTS
import csv
import nltk
import argparse

parser = argparse.ArgumentParser(description='Ankinator: Extract words from your text and create Anki flashcards!')
parser.add_argument('-i', '--input', type=str, help='Input file')
parser.add_argument('-o', '--output', type=str, help='Output file', default="output.csv")
args = parser.parse_args()

NORDS = "./Nords_list.md"

# download NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

console = Console()
wordnet_lemmatizer = WordNetLemmatizer()

with open(NORDS, "r") as f:
    Not_Words = f.read().strip().split(' ')
    nords = [nord.capitalize() for nord in Not_Words]

def get_word_info(word):
    # definitions and synonyms for each word
    synsets = wordnet.synsets(word)
    definitions = [f'✅ {syn.definition().capitalize()}' for syn in synsets]
    synonyms = set([f'⏺ {lemma.name().capitalize()}' for syn in synsets for lemma in syn.lemmas()])

    # pronunciations from google translate
    tts = gTTS(text=word, lang='en', tld="us")
    tts.save(f'{word}.mp3')

    return definitions, synonyms

def get_wordnet_pos(word):
    # Map POS tag to first character used by WordNetLemmatizer
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

if args.input:
    with open(args.input, "r") as f:
        input_text = f.read()
else:
    print("Please specify the input file!")
    
tokens = word_tokenize(input_text)
lemmatized_words = []
console.log("[bold green]Starting...")
for token in tokens:
    wordnet_pos = get_wordnet_pos(token)
    lemma_word = wordnet_lemmatizer.lemmatize(token, pos=wordnet_pos)
    lemmatized_words.append(lemma_word)

filtered_words = [word for word in lemmatized_words if word.isalpha()]
capitalizeed_words = [word.capitalize() for word in filtered_words]
pure_words = [word for word in capitalizeed_words if word not in nords]

word_count = Counter(pure_words)

# write to a csv file
with open(args.output, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    console.log(f"[bold cyan]Finding words...")
    for word, frequency in word_count.items():
        definitions, synonyms = get_word_info(word)
        if synonyms or definitions:
            writer.writerow([word.capitalize(), '\n'.join(synonyms), '\n'.join(definitions), frequency])
            print(f"Found {word}")
    console.log(f"[bold green]Saved {len(word_count.items())} words in {args.output}!")
