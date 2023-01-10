import json
import re

import matplotlib.pyplot as plt
import nltk

word = input()
dict = {}
with open('/Probability and Aplied Statistics/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

for elem in data:
    cleartxt = elem['text']
    cleartxt = cleartxt.replace('RT', '')
    cleartxt = cleartxt.replace('\n', ' ')

    cleartxt = re.sub("@[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub("#[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub(r'http\S+', '', cleartxt)
    cleartxt = re.sub('[()!?]', ' ', cleartxt)
    cleartxt = re.sub('\[.*?\]', ' ', cleartxt)
    cleartxt = re.sub("[^a-z0-9A-Z]", " ", cleartxt)
    cleartxt = nltk.tokenize.word_tokenize(cleartxt)
    #cleartxt = [nltk.stem.WordNetLemmatizer().lemmatize(word, pos='n') for word in cleartxt]
    for i in cleartxt:
        if i == word:
            if elem['created_at'][0:7] in dict:
                dict[elem['created_at'][0:7]] += 1
            else:
                dict[elem['created_at'][0:7]] = 1


time = list(dict.keys())
numb = list(dict.values())
plt.plot(time, numb)
plt.show()
