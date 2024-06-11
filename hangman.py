import random

class Letter:
  def __init__(self, value):
    self.value = value
    self.guessed = False

class Word:
  def __init__(self):
    self.letters = []
    self.solved = False

  def print_word(self):
    for letter in self.letters:
      print(letter.value)

# initial setup

words = open('words.txt', 'r').readlines()
r = random.randint(0, len(words) - 1)
random_word = words[r]
word = Word()

for character in random_word:
  letter = Letter(character)
  word.letters.append(letter)
