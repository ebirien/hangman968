import random
# List of five favourite fruits assigned to a variable called word_list
word_list = ['grape', 'apple', 'mango', 'orange', 'kiwi']
# Print out word_list to the stadard output screen
print(word_list)

# Choose a random word from list
word = random.choice(word_list)

# Print out word to the standard output
print(word)

# Run the code several times and observe the words printed out after each run.
for i in range(6):
    print(random.choice(word_list))

# Ask the user to enter a single letter
guess = input('Guess a single letterr in the randomly chosen word:\n')

# Check that the input is a single charachter
if len(guess)==1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input')