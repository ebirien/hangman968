import random

class Hangman:
    '''
    This class contains the methods which are used to play the game.

    Parameters:
    -----------
    word_list: list
        A list of words that can be guessed by the player.

    num_lives: int
        Number of guess attempts left.

    Methods:
    --------
    __check_guess(guess)
        Checks whether the guessed character is in the word.
    
    ask_for_input(s)
        Asks for user input and also validates if the user input is a single alphabetical character.
    ''' 

    def __init__(self, word_list, num_lives=5):

        self.word_list = word_list or []
        self.num_lives = num_lives
        self.word = random.choice(self.word_list) 
        self.num_letters = len(set(list(self.word)))
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []

    def __check_guess(self, guess):
        '''This method is checks whether the guessed character is in the word.      
              
        Parameters:
        -----------
        guess: str
            A single alphabetical character guessed by the user.
        ''' 
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                   self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f'You have {self.num_lives} lives left.')
    
    def ask_for_input(self):
        '''This method is asks for the user input. It also validates if the user input is a single alphabetical character.
        
        Returns:
        --------
        tuple
            number of attempts left and number of letters left.
        '''
        while True:
            guess = input('Guess a single alphabetical letter:\n')

            if len(guess)>1 or guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character:\n')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.list_of_guesses.append(guess)        
                self.__check_guess(guess)
                return self.num_lives, self.num_letters
            

if __name__ == "__main__":

    def play_game(word_list):
        '''
        This function is used to create an instance of the Hangman class and plays the game by calling the ask_for_input method.  
        
        Parameters:
        -----------
        word_list: list
            A list of words that can be guessed by the player.
        '''
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            num_lives, num_letters = game.ask_for_input()
            if num_lives == 0:
                print('You lost!')
            if num_letters > 0:
                continue
            if num_lives!=0 and num_letters<=0:
                print('Congratulations. You won the game!')            


    play_game(['grape', 'apple', 'mango', 'orange', 'kiwi'])