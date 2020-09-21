####################################################################
# num_guessing_game.py by Mark Fontenot
#
# A number guessing game. 
# 
# The user will have up to 4 tries to guess a number between
# 1 and 20.  
#
# This program gives you some ideas about how to handle looping
# the UI so the user can continue to play the game. You'll use
# it for Project 3
####################################################################


num_wrong_guesses = 0
current_guess = 0

secret_number = 14

# The user will either enter a guess between 1 & 20 (inclusive)
# or enter -1 to end the game

print('Let\'s Play the Number Guessing Game')
print('You\'ll have 4 chances to guess the secret number. ')
print('The secret number is between 1 and 20.')
print('If you\'d like to end the game early, enter -1.\n')


# This while loop will continue looping until the user enters
# -1 to quit or exceeds 4 wrong guesses
while current_guess != -1 and num_wrong_guesses < 4:
    
    # Prompt the user to enter a guess or -1 to end the program
    print('Please enter your guess (or -1 to end) --> ', end = '')
    # Read the input from the user and convert it to an int
    current_guess = int(input())

    # If the user doesn't enter -1, we need to check to see if they
    # entered the secret number or not
    if current_guess != -1:

        # If the number entered is equal to the secret number, tell them
        # how great they are and then change current_guess to -1 so the
        # while loop will stop executing.
        if current_guess == secret_number:
            print('Congratulations, you found the secret number!')
            print('Play again soon!')
            current_guess = -1
        
        # If the user doesn't guess correctly, then increment num_wrong_guesses
        # so they only get a 4 guesses. 
        else:
            print('Sorry, that wasn\'t the correct answer.\n')
            num_wrong_guesses += 1

# If the loop ends and the user has made 4 incorrect guesses, give them
# a little pep talk. 
if num_wrong_guesses == 4:
    print('Better luck next time!')