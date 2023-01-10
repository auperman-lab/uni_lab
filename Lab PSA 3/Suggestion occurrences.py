import json
import re
import nltk

dict = {}
word = input()
txt = ''
with open('/Users/nmacrii/Desktop/python/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

for elem in data:
    count = 0
    cleartxt = elem['text']
    cleartxt = cleartxt.replace('\n', ' ')

    cleartxt = re.sub("@[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub("#[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub(r'http\S+', '', cleartxt)
    cleartxt = re.sub('[()!?]', ' ', cleartxt)
    cleartxt = re.sub('\[.*?\]', ' ', cleartxt)
    cleartxt = re.sub("[^a-z0-9A-Z]", " ", cleartxt)
    cleartxt = nltk.tokenize.word_tokenize(cleartxt)
    #cleartxt = [nltk.stem.WordNetLemmatizer().lemmatize(word, pos='n') for word in cleartxt]
    twowrd = []
    for i in range(len(cleartxt)-1):
        twowrd.append(cleartxt[i])
        twowrd.append(cleartxt[i + 1])
        if twowrd[0] == word:
            txt = txt + ' ' + twowrd[1]
        twowrd = []



print(nltk.FreqDist(nltk.tokenize.word_tokenize(txt)).most_common(3))
