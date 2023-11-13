import random

class Hangman:
    '''
    This class is used to convert temperature from Celsius to Fahrenheit. 

    Attributes:
    word_list (list)
    num_lives (int)
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature of this class. 
        '''
        self.word_list = word_list or []
        self.num_lives = num_lives
        self.word = random.choice(self.word_list) 
        self.num_letters = len(set(list(self.word))) # The number of UNIQUE letters in the word that have not been guessed yet
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []

    # Check whether the guess is in the word
    def __check_guess(self, guess):
        '''
        This function is used to check whether the guessed character is in the word. 
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in len(self.word):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f'You have {self.num_lives} lives left.')
    
    # Ask for user input
    def ask_for_input(self):
        '''
        This function is used ask for user input. It also validates if the user input is a single alphabetical character.
        '''
        while True:
            # Ask the user to enter a single letter
            guess = input('Guess a single alphabetical letter:\n')
            # Check that the input is a single alphabet
            if len(guess)>1 or guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character:\n')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.list_of_guesses.append(guess)


# Call ask_for_input method to test code
fruits = ['grape', 'apple', 'mango', 'orange', 'kiwi']
player_1 = Hangman(fruits)
player_1.ask_for_input()