import random

words = open('words.txt', 'r').readlines()
r = random.randint(0, len(words) - 1)
word = words[r]
