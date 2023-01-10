import json


with open('/Users/nmacrii/Desktop/python/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

hastags = []
for elem in data:
    text = elem['text']
    text = text.split()
    for word in text:
        if '#' in word and len(word) > 1:
            word = word.lower()
            hastags.append(word)

sorted_hashtags = {}

for hash in hastags:
    if hash in sorted_hashtags:
        sorted_hashtags[hash] += 1
    else:
        sorted_hashtags[hash] = 1

sorted_hashtags = sorted(sorted_hashtags.items(), key=lambda x: x[1], reverse=True)

print(sorted_hashtags[:10])
