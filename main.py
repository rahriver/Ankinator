import csv
from nltk import pos_tag
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from collections import Counter
from gtts import gTTS

WORDS = "/home/<path_to_your_text>"
NORDS = "/home/<path_to_not_word_list>"

# download NLTK data
nltk.download('wordnet')
nltk.download('punkt')
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

with open(WORDS, "r") as f:
    input_text = f.read()
    
tokens = word_tokenize(input_text)
lemmatized_words = []
for token in tokens:
    wordnet_pos = get_wordnet_pos(token)
    lemma_word = wordnet_lemmatizer.lemmatize(token, pos=wordnet_pos)
    lemmatized_words.append(lemma_word)

filtered_words = [word for word in lemmatized_words if word.isalpha()]
capitalizeed_words = [word.capitalize() for word in filtered_words]
pure_words = [word for word in capitalizeed_words if word not in nords]

word_count = Counter(pure_words)

# write to a csv file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for word, frequency in word_count.items():
        definitions, synonyms = get_word_info(word)
        if synonyms or definitions:
            writer.writerow([word.capitalize(), '\n'.join(synonyms), '\n'.join(definitions), frequency])
            print(f"Found {word}")
    print(f"\n Saved {len(word_count.items())} words in word_info.csv")
