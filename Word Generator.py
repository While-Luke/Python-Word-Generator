import copy
import random

file = open("words.txt")
words = file.read().splitlines()

letters = {}
for i in range(26):
    probs = {}
    for j in range(26):
        probs[chr(97+j)] = 0
    probs["end"] = 0
    probs["count"] = 0
    letters[chr(97+i)] = copy.deepcopy(probs)

for word in words:
    for l in range(len(word)):
        if l < len(word)-2:
            letters[word[l]][word[l+1]] += 1
        else:
            letters[word[l]]["end"] += 1
        letters[word[l]]["count"] += 1

while(True):
    new_word = ""
    new_word += chr(random.randint(97,122))
    index = 0
    while(True):
        rando = random.randint(0,letters[new_word[index]]["count"])
        if letters[new_word[index]]["count"] - letters[new_word[index]]["end"] <= rando:
            if len(new_word) > 4:
                break
            else:
                continue
        total = 0
        for i in range(26):
            if letters[new_word[index]][chr(97+i)] + total > rando:
                new_word += chr(97+i)
                index += 1
                break
            else:
                total += letters[new_word[index]][chr(97+i)]

    print(new_word)
    again = input("Another?")
    if again != "y":
        break
