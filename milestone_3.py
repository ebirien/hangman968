import random
# Create a list of five fruits and assign it to a variable called word_list
word_list = ['grape', 'apple', 'mango', 'orange', 'kiwi']
# Print out word_list to the stadard output screen
print(word_list)

# Choose a random word from list
word = random.choice(word_list)

# Check whether the guess is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        ask_for_input()


def ask_for_input():

    while True:
        # Ask the user to enter a single letter
        guess = input('Guess a single alphabetical letter:\n')

        # Check that the input is a single alphabet
        if len(guess)==1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical letter:\n')

    check_guess(guess)


ask_for_input()
