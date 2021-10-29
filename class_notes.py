# Import random module
import random

# to generate random number between 1-20 by calling randrange method from random module
# random_number = random.randrange(1,20)

# make a temporary "random" number for testing:
random_number = 5
# convert the random number read as a string
random_number = str(random_number)
# prompt user for input "Guess a number between 1-20"
user_input = input("Guess a number between 1-20: ")
guess_count = 0
game_end_flag = False

# Create a while loop to make the game continue until the user enters "Quit"
while user_input != "Quit" and game_end_flag == False:
    # if game_end_flag == True:
    #     guess_count = 0
    if guess_count == 5 and user_input != random_number:
        print("You ran out of guesses!")
        game_end_flag == True
        user_input = input("Would you like to play again? (Y/N) ")
        if user_input == "Y":
            user_input = input("Guess a number between 1-20: ")
            guess_count == 0
            game_end_flag == False
        elif user_input == "N":
            user_input == "Quit" and game_end_flag == True
# compare user input to random number
# # input will always be interpretated as a string, so we need to convert it to a number to be able to compare it to our random number
#     user_input = int(user_input)

# if user guesses correct number, output "You got it right!"
    if user_input == random_number:
        guess_count += 1
        print(guess_count)
        print("You got it right!")
        game_end_flag == True
        user_input = input("Would you like to play again? (Y/N) ")
        if user_input == "Y":
            user_input = input("Guess a number between 1-20: ")
            guess_count == 0
            game_end_flag == False
        elif user_input == "N":
            user_input == "Quit" and game_end_flag == True
# if the user guesses incorrectly, check if the number is higher or lower than the random number
    if user_input != random_number:
        guess_count += 1
        print(guess_count)
        if user_input > random_number:
            user_input = input("Your guess was too high! Guess again: ")
            # user_input = int(user_input)
        elif user_input < random_number:
            user_input = input("Your guess was too low! Guess again: ")
    else:
        user_input = input("Guess a number between 1-20: ")
# if user   
