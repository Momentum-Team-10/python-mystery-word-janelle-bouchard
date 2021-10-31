# ## Objectives
    # - Create an interactive program.
    # - Read from a file.
    # - Choose a random value.
    # - Keep track of state.
# ## Details
    # You will implement the game Mystery Word. In your game, you will be playing
    # against the computer.

    # The computer must select a word at random from the list of words in the file
    # `words.txt` from this repository.

    # The game must be interactive; the flow of the game should go as follows:

    # 1. Let the user choose a level of difficulty at the beginning of the program.
    #    Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
    #    characters; hard mode only has words of 8+ characters.

    # 2. At the start of the game, let the user know how many letters the computer's
    #    word contains.

    # 3. Ask the user to supply one guess (i.e. letter) per round. This letter can be
    #    upper or lower case and it should not matter. If a user enters more than one
    #    letter, tell them the input is invalid and let them try again.

    # 4. Let the user know if their guess appears in the computer's word.

    # 5. Display the partially guessed word, as well as letters that have not been
    #    guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
    #    and d, the screen should display:

    # ```
    # B _ _ B A _ D
    # ```

    # A user is allowed 8 guesses. Remind the user of how many guesses they have left
    # after each round.

    # _A user loses a guess only when they guess incorrectly._ If they guess a letter
    # that is in the computer's word, they do not lose a guess.

    # If the user guesses the same letter twice, do not take away a guess. Instead,
    # print a message letting them know they've already guessed that letter and ask
    # them to try again.

    # The game should end when the user constructs the full word or runs out of
    # guesses. If the player runs out of guesses, reveal the word to the user when
    # the game ends.

    # When a game ends, ask the user if they want to play again. The game begins
    # again if they reply positively.
    # Helpful tutorial: https://www.teachwithict.com/guess.html


#open txt file using "with" syntax

#put words from txt file into list of strings

#slect one word from list to use for testing

#add "level of difficulty" into the game after we get the game working

#show mystery word as underscores to user
    #ask for user guess (regardless of upper or lowercase)
    #validate user input if user enters more than one letter
        #user error: you can only guess one letter at a time
        #possible to restrict number of characters?

#show user if guess is part of word
    #replace underscore with letter

#show all letters that haven't been guess yet  
    #if guessed letter is NOT in the word, add to list of guessed letters

#limit number of user WRONG guesses to 8
    #track user guess count
    #tell the user how many guesses are left
    #may need 2 variables to indicate correct vs. incorrect guesses
    #display mystery word if user runs out of guesses
    #error message if duplicate guess is entered and do not count duplicate guesses against guess count

"""import the "random" module"""
import random
import string

alphabet_list = list(string.ascii_lowercase)
# print(alphabet_list)

with open('words.txt') as file:
    word_strings = file.readlines()
    # print(strings)

    """create an empty list to store the words in based on criteria when we open the text file"""
    words = []
    underscores = []
    guess_count = 0
    # wrong_guesses = []
    end_game = False

    for word_string in word_strings:
        words.append(word_string)

    """Assign random_word variable to a specific word to test, and normalize the "random word" so that it disregards case"""    
    random_word = words[7].lower()
    # random_word = random.choice(words).lower()
    """remove the "newline" indication, so that it's not interpreted as a character"""    
    random_word = random_word.replace("\n", "")
    # print(random_word)

    """create a new (list) variable, called display, that literally matches our random word"""
    display = random_word
    """create a loop to look at each index number and replace the existing character with an underscore so that the number of underscores matches the number of characters"""
    for index in range(len(display)):
        display = display[0:index] + "_" + display[index+1:]

    """in the display ONLY (so, only on print,) join all of the underscores with a space between them"""    
    print(" ".join(display))
    """normalize the user's input to ignore case"""
    user_input = input('Make a guess... ').lower()

    guess_count == 0
    alphabet_list = list(string.ascii_lowercase)
    
    while user_input != "Quit" and guess_count <= 8:
        alphabet_list = list(string.ascii_lowercase)
        print(alphabet_list)
        wrong_guesses = []
        for index in range(len(random_word)):    
            if user_input in random_word[index]:
                display = display[0:index] + user_input + display[index+1:]
                guess_count += 0
            # alphabet_list.remove(user_input)
        if user_input not in random_word[index]:
            guess_count += 1
        letters_remaining = alphabet_list.remove(user_input)
        print(" ".join(display))
        print(f"Remaining letters: {letters_remaining}")
        print(f"Guess count: {guess_count}")
        user_input = input('Guess again... ')

        # if user_input == "Quit":
        #     end_game == True


    # ## Create a loop to count the number of characters in the word, and populate the underscores list to reflect that number
    # # word_length = range(len(random_word))
    # for num in word_length:
    #     underscores.append('_')
    # underscores = "".join(underscores)
    # print(underscores)
    # #normalize the user's input to ignore case
    # user_input = input('Make a guess... ').lower()

    # while user_input != "Quit" and end_game == False:

    #     for index in range(len(random_word)):
    #         if random_word[index] == user_input:
    #             underscores = underscores[0:index] + user_input + underscores[index+1:]
    #     print(underscores)
    #     user_input = input('Guess again... ')
        
    #     if user_input == "Quit":
    #         end_game == True