# Hangman
## Project Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a secret word and the user tries to guess it. The secret word will be randomly chosen by the computer from a list of words. In this implementation the list of words comprises of 5 fruits andt the number of attempts is set to 5.

The aim of this project is to demonstrate a working advanced knowledge of the Python programming language. Some Object-oriented programming (OOP) concepts employed in this project include Objects, Classes, Encapsulation, and Data Abstraction. I have also learned to apply Single Responsibility Principle (SRP), Access Modifier, Docstrings and multiple return values.


### Screenshots of Code Snippets
![Hangman Init](/hangman_init_code.png)

![Check Guess](/check_guess_code.png)

![Ask For Input](/ask_for_input_code.png)

![Play Gamet](/play_game_code.png)

## Installation Instructions
Download the file named 'hangman.py' to a folder named in your computer.

## Usage Instructions
To play the game the user will be required to guess unique single alphabetical characters which are combined to find the secret word. Only single alphabetical character is accepted as valid user input.  The user loses the game if he records a total of five incorrect guesses and will be informed with the message - 'You lost!'.
Every incorrect guess comes with a message informing the user of the number of lives (attempts) left. The user will also be informed if he guesses an aphabetical character more than once.

Follow the following instructions to play the game:
- At the command prompt, navigate to the code folder in computer.
- Type 'python hangman.py' at the command prompt.
- Type the requested user inputs and press the return key, until the game is either won or lost.

## File Structure
- hangman.py
- LICENSE file
- .gitignore file
- README.md file

## License Information
MIT License