import random
import os

from common_words import word_list
from art import stages
from art import logo

class Hangman:

    def __init__(self):
        self.secret_word = ''
        self.word_length = 0
        self.gameover = False
        self.lives = 6
        self.output = []
        self.guess = ''

    def setup(self):
        os.system('clear')
        print(logo)
        self.secret_word = random.choice(word_list)
        self.word_length = len(self.secret_word)
        self.gameover = False
        self.lives = 6
        self.output = []
        self.guess = ''
        for _ in range(self.word_length):
            self.output += "_"
        # print(self.secret_word) # uncomment to reveal the word for testing purposes

    def getGuess(self):
        self.guess = input('Guess a letter: ').lower()
        if self.guess in self.output:
            self.printGame()
            print(f'You already guessed {self.guess}')
            self.getGuess()

    def isValidGuess(self):
        for i in range(self.word_length):
            letter = self.secret_word[i]
            if letter == self.guess:
                self.output[i] = letter
        self.isWrongGuess()

    def isWrongGuess(self):
        if self.guess not in self.secret_word:
            self.lives -= 1
            self.printGame()
            print(f'Wrong guess! Lives left: {self.lives}')
            if self.lives <= 0:
                self.gameover = True
                print('You lose!')
                print(f'Correct word was: {self.secret_word}')
        else:
            self.printGame()

    def printGame(self):
        print('\n\n')
        print(stages[self.lives])
        print(' '.join(self.output), '\n')

    def checkWinCondition(self):
        if '_' not in self.output:
            self.gameover = True
            self.printGame()
            print('You win!')

    def newGamePrompt(self):
        if self.gameover:
            print('\n\n')
            newgame = input('Start a new game? Y/N: ').lower()
            if newgame == 'y':
                self.setup()

    def start(self):
        self.setup()
        self.printGame()
        while not self.gameover:
            self.getGuess()
            self.isValidGuess()
            self.checkWinCondition()
            self.newGamePrompt()

h = Hangman()
h.start()

