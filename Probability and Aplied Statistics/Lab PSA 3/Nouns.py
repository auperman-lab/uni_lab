import json
import re
import nltk
from nltk.corpus import stopwords


txt = []
nountxt = []
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
    cleartxt = [word for word in cleartxt if not word.lower() in stopwords.words('english')]

    txt += cleartxt


#txt = [nltk.stem.WordNetLemmatizer().lemmatize(word, pos='n') for word in txt]

for i in nltk.pos_tag(txt):
    if 'NN' in i[1] and len(i[0]) > 1:
        nountxt.append(i[0])

frequency_distribution = nltk.FreqDist(nountxt)
print(frequency_distribution.most_common(12))
