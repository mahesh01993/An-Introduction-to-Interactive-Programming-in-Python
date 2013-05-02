# Rock-paper-scissors-lizard-Spock
# by Christophe Quentel
# 10/20/2012, Paris, France

# Optimized for CodeSkulptor (http://www.codeskulptor.org)
# A mini-project programmed for "An Introduction to Interactive Programming in Python"
# …A Coursera Course (http://www.coursera.org)


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# Let's import what we need

import random

# Helper functions

def number_to_name(number):
    """Convert the given number into the name of the corresponding tool"""
    
    # A simple if/elif/else game...

    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"
    return name

    
def name_to_number(name):
    """Convert the given name into the number of the corresponding tool"""

    # A simple if/elif/else game...

    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    else:
        number = 4
    return number

# main function

def rpsls(player_guess):
    """Compare the player's choice to the choice of the computer, determine who is the winner and print the result"""


    # convert name to player_number using name_to_number
    
    player_number = name_to_number(player_guess)
    
    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0, 5)
    
    # compute difference of player_number and comp_number modulo five
   
    difference = (player_number - comp_number) % 5
   
    # use if/elif/else to determine winner (but don't forget that players can tie !)
    
    if difference == 1 or difference == 2:
        result = "Player wins"
    elif difference == 3 or difference == 4:
        result = "Computer wins"
    else:
        result = "Player and computer tie!"
    
    # convert comp_number to name using number_to_name
    
    comp_guess = number_to_name(comp_number)
    
    # print results
    
    print "Player chooses", player_guess
    print "Computer chooses", comp_guess
    print result
    print
    
# Let's play RPSLS (and test our code...) !

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")