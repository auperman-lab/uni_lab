import json
import re
import nltk

suc = 0
txt = ''
with open('/Probability and Aplied Statistics/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

for elem in data:
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
    cleartxt = re.sub("[^a-z0-9]", " ", cleartxt)
    txt = txt + ' ' + cleartxt

print(nltk.FreqDist(nltk.tokenize.word_tokenize(txt)).most_common(10))
