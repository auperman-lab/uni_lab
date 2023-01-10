import json
import re
import nltk
from nltk.corpus import stopwords
import csv


with open('/Lab PSA 3/lab3/tweets.json') as f:
    data = json.load(f)

word_connection = {}
for i in range(len(data)):
    if 2600 <= i < 2800:
        cleartxt = data[i]['text']
        cleartxt = cleartxt.replace('RT', '')
        cleartxt = re.sub("@[A-Za-z0-9_]+", "", cleartxt)
        cleartxt = re.sub("#[A-Za-z0-9_]+", "", cleartxt)
        cleartxt = re.sub(r'http\S+', '', cleartxt)
        cleartxt = re.sub('[()!?]', ' ', cleartxt)
        cleartxt = re.sub('\[.*?]', ' ', cleartxt)
        cleartxt = re.sub("[^a-zA-Z]", " ", cleartxt)
        cleartxt = nltk.tokenize.word_tokenize(cleartxt)
        cleartxt = list(set(cleartxt))
        cleartxt = [word.lower() for word in cleartxt if not word.lower() in stopwords.words('english')]
        for word in cleartxt:
            connection = list(cleartxt)
            connection.remove(word)
            if word in word_connection and word:
                no_copies = list(set(word_connection[word]+connection))
                word_connection[word] = list(no_copies)
            else:
                word_connection[word] = connection
connection_count = {}
for word in word_connection:
    connection_count[word] = len(word_connection[word])

for word in word_connection:
    for conn in word_connection[word]:
        if word in word_connection[conn]:
            word_connection[conn].remove(word)

with open('word_edges', 'w') as csv_file:
    field_names = ['node', 'edges', 'count']
    filecsv = csv.DictWriter(csv_file, fieldnames=field_names)

    filecsv.writeheader()

    for word in word_connection:
        for conn in word_connection[word]:
            filecsv.writerow({'node': word, 'edges': conn, 'count': connection_count[word]})
