# Jonathan Cai
# May 9, 2018

import random

################ MAD LIBS ################

# name = raw_input("What is your name?")
# date = raw_input("What is the date?")
# age = input("How old are you?")
#
# print name + " is " + str(age) + " years old on " + date

################ GUESS THE NUMBER ################

def guess_the_number(rangestart, rangestop):
    """
    Takes in two integers, rangestart and rangestop.
    Runs a game that generates a random integer from rangestart to rangestop.
    You must find the number generated based in order to win.
    """
    correct = random.randrange(rangestart, rangestop)
    flag = False
    while flag == False:
        guess = eval(input("What do you think the number is?"))
        if guess > correct:
            print("Too high.")
        elif guess < correct:
            print("Too low.")
        elif guess == correct:
            flag = True
            print("You got it! The number was " + str(correct) + ".")

### Testing:
# guess_the_number(10, 20)

################ HANGMAN ################

def hangman(word, limit):
    """
    Takes in a string, word and a integer, limit for the limit of guesses.
    Runs the game, Hangman.
    """
    display = []
    letters = []
    for letter in word:
        letters.append(letter)
        display.append("_ ")

    print("ANSWER:" + str(letters))
    guessed_letters = set()
    count = 0

    flag = False
    while flag == False:
        print(display)

        guessed_letter = eval(input("Which letter do you guess? You have " + str(limit - count) + " guesses left."))

        if len(guessed_letter) != 1 or type(guessed_letter) != str:
            print("Make sure to only input one letter.")

        if guessed_letter.lower() in guessed_letters:
            print("You've already guessed this letter!")

        else:
            guessed_letters.add(guessed_letter.lower())
            count += 1

            if guessed_letter.lower() in letters or guessed_letter.upper() in letters:
                print("You've found a letter in the word!")
                for idx in range(len(word)):
                    if word[idx] == guessed_letter.lower():
                        display[idx] = guessed_letter.lower()
                    elif word[idx] == guessed_letter.upper():
                        display[idx] = guessed_letter.upper()

            flag2 = True
            for letter in letters:
                if letter.lower() not in guessed_letters:
                    flag2 = False

            if flag2 == True:
                flag = True
                print("You've gotten all the letters! The word was " + word)
                return

            if count == limit:
                print("You've guessed too many incorrect letters and lost!")
                return

### Testing:
# hangman("Poop", 10)
# hangman("Algebra", 10)
# hangman("Oopsie", 10)

