ciphertext = 'OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM'


def freq_score(text, score=0):
    freqs = {
        'a': 7.8,
        'b': 2,
        'c': 4,
        'd': 3.8,
        'e': 11.16,
        'f': 1.4,
        'g': 3,
        'h': 2.3,
        'i': 7.6,
        'j': 0.21,
        'k': 0.97,
        'l': 5.3,
        'm': 2.7,
        'n': 7.2,
        'o': 6.1,
        'p': 2.8,
        'q': 0.19,
        'r': 7.3,
        's': 8.7,
        't': 9.1,
        'u': 3.3,
        'v': 1,
        'w': 0.91,
        'x': 0.27,
        'y': 1.6,
        'z': 0.44
    }

    for c in text:
        score += freqs[c.lower()]
    return score


def originaltext(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i % len(key)]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)


score = {}
with open('example.txt', 'r') as f:
    for word in f:
        word = word.replace('\n', '')
        word = word.upper()
        score[word] = freq_score(originaltext(ciphertext, word))

sortt = sorted(score.items(), key=lambda x: x[1], reverse=True)[:10]
for i in sortt:
    print(i, originaltext(ciphertext, i[0]))
print(freq_score(originaltext(ciphertext, 'VOTATION')))
