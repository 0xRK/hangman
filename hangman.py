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
    print('Word: ', end = "")
    for letter in self.letters:
      if letter.guessed:
        print(letter.value, end = "")
      else:
        print('_', end = "")

  def check_solved(self):
    for letter in self.letters:
      if not letter.guessed:
        return
    self.solved = True

def check_guess(guess, word, guesses_remaining):
  is_present = False
  for letter in word.letters:
    if letter.value == guess:
      letter.guessed = True
      is_present = True
  if is_present:
    print(f'Good guess, {guess} is in the word!')
  else:
    print(f'Sorry, {guess} is not in the word.')
    guesses_remaining -= 1

def print_alphabet(alphabet, guessed_list):
  print('\nAvailable letters: ', end = "")
  for letter in alphabet:
    if letter in guessed_list:
      print('_', end = "")
    else:
      print(letter, end = "")

  

# initial setup
guessed_list = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

words = open('words.txt', 'r').readlines()
r = random.randint(0, len(words) - 1)
random_word = words[r][:-1]
word = Word()

for character in random_word:
  letter = Letter(character)
  word.letters.append(letter)

guesses_remaining = 26
print('\n\nWelcome to Hangman!')



while not word.solved or guesses_remaining == 0:
  print(f'You have {guesses_remaining} guesses left.')
  word.print_word()
  print_alphabet(alphabet, guessed_list)
  valid_input = False
  while not valid_input:
    guess = input('\nGuess a letter: ')
    if not (len(guess) == 1):
      print('Input must be one character long!')
    elif not guess.isalpha():
      print('Guess must be a letter!')
    elif guess in guessed_list:
      print('You already guessed that letter!')
    else:
      valid_input = True
  check_guess(guess, word, guesses_remaining)
  guessed_list.append(guess)
  print('\n---------------------------------\n')
  word.check_solved()
  if word.solved:
    print('The word is: ')
    word.print_word()
    print('Congratulations! You solved the word!')



