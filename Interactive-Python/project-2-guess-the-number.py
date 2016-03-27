# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

number_range = 100
player_guess = 0
secret_number = 0
number_of_guesses = 7
counter = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number_of_guesses, secret_number, counter
    secret_number = random.randrange(0, number_range)
    # print "Secret number is",secret_number
    print "New game."
    print "Range is from 0 to",number_range
    counter = number_of_guesses
    print "Number of remaining guesses is",number_of_guesses
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_range, number_of_guesses
    number_range = 100 
    number_of_guesses = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number_range, number_of_guesses 
    number_range = 1000 
    number_of_guesses = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global player_guess, number_of_guesses, counter
    player_guess = int(guess)
    print "Guess was",player_guess
    counter = counter - 1
    if (player_guess < secret_number) and (counter > 0):
        #counter = counter - 1
        print "Number of remaining guesses is",counter
        print "Higher"
        print ""
    elif (player_guess > secret_number) and (counter > 0):
       # counter = counter - 1
        print "Number of remaining guesses is",counter
        print "Lower"
        print ""
    elif (counter == 0) and (player_guess != secret_number):
        print "You have run out of guesses."
        print "The correct answer is",secret_number
        print ""
        new_game()
    else:
        print "Correct"
        print ""
        new_game()
    
# create frame
f = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame
f.add_button('Range is [0, 100)', range100, 200)
f.add_button('Range is [0, 1000)', range1000, 200)
f.add_input('Enter a guess', input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
