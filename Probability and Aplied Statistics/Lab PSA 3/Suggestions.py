import json
import re
import nltk

word = input()
dict = {}
txt = ''
with open('/Probability and Aplied Statistics/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

for elem in data:
    count = 0
    cleartxt = elem['text'].lower()
    cleartxt = cleartxt.replace('\n', ' ')

    cleartxt = cleartxt.replace('rt', '')
    cleartxt = re.sub("’", "", cleartxt)
    cleartxt = re.sub("'", "", cleartxt)
    cleartxt = re.sub("@[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub("#[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub(r'http\S+', '', cleartxt)
    cleartxt = re.sub('[()!?]', ' ', cleartxt)
    cleartxt = re.sub('\[.*?\]', ' ', cleartxt)
    cleartxt = re.sub("[^a-z0-9A-Z]", " ", cleartxt)
    cleartxt = nltk.tokenize.word_tokenize(cleartxt)
    #cleartxt = [nltk.stem.WordNetLemmatizer().lemmatize(word, pos='n') for word in cleartxt]
    for i in cleartxt:
        if i.startswith(word) and len(i) > len(word):
            txt = txt + ' ' + i

print(nltk.FreqDist(nltk.tokenize.word_tokenize(txt)).most_common(3))
