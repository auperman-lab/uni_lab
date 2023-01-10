import json
import re
import nltk
from nltk.corpus import stopwords


dict = {}
nouns = {}
txt = ''

with open('/Probability and Aplied Statistics/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

for elem in data:

    stat = [1, int(elem['retweets']), int(elem['likes'])]

    cleartxt = elem['text']
    cleartxt = cleartxt.replace('RT', '')
    cleartxt = cleartxt.replace('\n', ' ')

    cleartxt = re.sub("@[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub("#[A-Za-z0-9_]+", "", cleartxt)
    cleartxt = re.sub(r'http\S+', '', cleartxt)
    cleartxt = re.sub('[()!?]', ' ', cleartxt)
    cleartxt = re.sub('\[*?\]', ' ', cleartxt)
    cleartxt = re.sub("[^a-z0-9A-Z]", " ", cleartxt)
    cleartxt = nltk.tokenize.word_tokenize(cleartxt)
    cleartxt = [word for word in cleartxt if not word.lower() in stopwords.words('english')]

    for word in cleartxt:
        if word in dict:
            result = []
            for i1, i2 in zip(stat, dict[word]):
                result.append(i1 + i2)
            dict[word] = result
        else:
            dict[word] = stat


for word in dict:
    if 'NN' in nltk.pos_tag(word)[0][1]:
        nouns[word] = dict[word][0] * (1.4 + dict[word][1]) * (1.2 + dict[word][2])

print(sorted(nouns.items(), key=lambda x: x[1], reverse=True)[:10])
