# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
secert_num=0
attempt=0
gameno=0

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secert_num
    global attempt
    global gameno
    gameno=100
    attempt=attempt_cal(0,100)
    secert_num=random.randrange(0,100)
    print "new game started,guess the number between 1 to 100"
    print
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global secert_num
    global attempt
    global gameno
    gameno=1000
    attempt=attempt_cal(0,100)
    secert_num=random.randrange(0,1000)
    print "new game started,guess the number between 1 to 1000"
    print
    
def get_input(guess):
    # main game logic goes here
    print "your guess is",guess
    global attempt
    if attempt<1:
        print "sorry you loss"
        print
        current_game()
    elif int(guess)==secert_num :
        print "correct ,you won"
        print
        current_game()
    elif int(guess)>secert_num:
        print "lower ,","the no. of guess remaining",attempt
    elif int(guess)<secert_num:
        print "higger ,","the no. of guess remaining",attempt
    
    attempt-=1
       
def attempt_cal(low,high):
    return math.ceil(math.log(high-low+1,2))

def current_game():
    if gameno==100:
        range100()
    else:
        range1000()

    

range100()   
# create frame

guess_fram=simplegui.create_frame("guess game",100,200)
# register event handlers for control elements
guess_fram.add_button("range from 1 to 100",range100)
guess_fram.add_button("range from 1 to 1000",range1000)
guess_fram.add_input("enter your guess",get_input,100)
# start frame
guess_fram.start()

# always remember to check your completed program against the grading rubric
