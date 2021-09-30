import random
import string

smth = string.ascii_letters
smth += string.digits
smth += string.punctuation
file = open("Dictionary", "w")

dictionary = dict()
for i in smth:
    randomizer = ""
    for i2 in range(3):
        randomizer += random.choice(smth)
    while randomizer in dictionary:
        randomizer = ""
        for i2 in range(3):
            randomizer += random.choice(smth)
    dictionary [randomizer] = i
for key in dictionary:
    file.write(key + dictionary[key] + "\n")
file.close()

