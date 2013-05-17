
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos=[0,160]
paddle2_pos=[WIDTH,160]
ball_vel=[0,0]
paddle1_vel=[0,0]
paddle2_vel=[0,0]
speed=.8
score1=0
score2=0
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel,speed# these are vectors stored as lists
    speed=.8
    ball_pos=[WIDTH/2,HEIGHT/2]
    random_x=random.randrange(120, 240)
    random_y=random.choice([random.randrange(60, 180),-random.randrange(60, 180)])
    if right:
        ball_vel=[random_x/60,random_y/60]
    else:
        ball_vel=[-random_x/60,random_y/60]
        
def wall():
    global ball_vel,ball_pos
    if ball_pos[1]<BALL_RADIUS or ball_pos[1]>HEIGHT-BALL_RADIUS:
        ball_vel[0]=ball_vel[0]
        ball_vel[1]=-ball_vel[1]
        

def gutter():
    global ball_pos,score1,score2
    if ball_pos[0]<-BALL_RADIUS:
        score2 += 1
        ball_init(True)
    elif ball_pos[0]>WIDTH+BALL_RADIUS:
        score1 +=1
        ball_init(False)
     
        
def pad_wall():
    global ball_vel,speed
    if ball_pos[0]-BALL_RADIUS<=PAD_WIDTH and paddle1_pos[1]<=ball_pos[1]+BALL_RADIUS and paddle1_pos[1]+PAD_HEIGHT>=ball_pos[1]:
        speed+=.1
        ball_vel[0]=-ball_vel[0]
        ball_vel[1]=ball_vel[1]
        
    if ball_pos[0]+BALL_RADIUS>=WIDTH-PAD_WIDTH and paddle2_pos[1]<=ball_pos[1]+BALL_RADIUS and paddle2_pos[1]+PAD_HEIGHT>=ball_pos[1]:
        speed+=.1
        ball_vel[0]=-ball_vel[0]
        ball_vel[1]=ball_vel[1]
        
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos=[0,160]
    paddle2_pos=[WIDTH,160]
    score1=0
    score2=0
    
    ball_init(False)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global pad_vel,pad_pos
    
    
    wall()
    pad_wall()
    gutter()
 
    # update paddle's vertical position, keep paddle on the screen
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_text(str(score1), (150, 100), 50, "Red")
    c.draw_text(str(score2), (450, 100), 50, "Red")
    
    
    #update paddles
    
    
    paddle1_pos[1]+=paddle1_vel[1]
    paddle2_pos[1]+=paddle2_vel[1]
    if paddle1_pos[1]<0 :
        paddle1_vel[1]=0
        paddle1_pos[1]=0
    elif paddle1_pos[1]>HEIGHT-PAD_HEIGHT:
        paddle1_vel[1]=0
        paddle1_pos[1]=HEIGHT-PAD_HEIGHT
    
    
    if paddle2_pos[1]<0 :
        paddle2_vel[1]=0
        paddle2_pos[1]=0
    elif paddle2_pos[1]>HEIGHT-PAD_HEIGHT:
        paddle2_vel[1]=0
        paddle2_pos[1]=HEIGHT-PAD_HEIGHT
    # draw paddles
    c.draw_line(paddle1_pos,[paddle1_pos[0],paddle1_pos[1]+PAD_HEIGHT],PAD_WIDTH,"White")
    c.draw_line(paddle2_pos,[paddle2_pos[0],paddle2_pos[1]+PAD_HEIGHT],PAD_WIDTH,"White")
     
    # update ball
    
    ball_pos[0]+=ball_vel[0]*speed
    ball_pos[1]+=ball_vel[1]*speed
    
    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,5,"Red","White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1]-=7
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1]+=7
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1]-=7
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1]+=7
    
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1]=0
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1]=0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1]=0
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1]=0

        
def button():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1=frame.add_button("restart", button)
new_game()
# start frame
frame.start()
