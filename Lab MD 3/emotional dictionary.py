import nltk
import json
import re

with open('/Users/nmacrii/Desktop/python/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

d = open('/Users/nmacrii/Desktop/python/Lab PSA 3/lab3/AFINN-111.txt')

lines = [line.split() for line in d]

emotional_value = {}

for line in lines:
    if not 48 <= ord(line[1][-1]) <= 57:
        line[0] = ' '.join(line[:-1])
        if len(line) > 3:
            line.remove(line[1])
        line.remove(line[1])
    emotional_value[line[0]] = int(line[1])

value_tweet = {}
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
    value_tweet[elem['id']] = 0
    for word in cleartxt:
        for wrd in emotional_value:
            if word == wrd:
                value_tweet[elem['id']] += emotional_value[wrd]
                break

stats = open('tweets stats', 'w')

for id in value_tweet:
    txtx = str(id) +' : ' + str(value_tweet[id]) + '\n'
    stats.write(txtx)

possitive_top10 = sorted(value_tweet.items(), key=lambda x: x[1], reverse=True)[:10]
negative_top10 = sorted(value_tweet.items(), key=lambda x: x[1])[:10]

print('\nTop 10 most possitive tweets\n\n')

for tweet in possitive_top10:
    for elem in data:
        if elem['id'] == tweet[0]:
            print(tweet[0], tweet[1])
            print(elem['text'], '\n')


print('\nTop 10 most negative tweets\n\n')

for tweet in negative_top10:
    for elem in data:
        if elem['id'] == tweet[0]:
            print(tweet[0], tweet[1])
            print(elem['text'], '\n')
