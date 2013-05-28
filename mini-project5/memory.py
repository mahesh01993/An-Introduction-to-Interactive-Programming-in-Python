# implementation of card game - Memory

import simplegui
import random
                
click1=0
click2=0
#exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
# helper function to initialize globals
def init():
    global card,exposed,state,moves
    moves=0
    state=0
    exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    card=range(0,8)
    card.extend(range(0,8))
    random.shuffle(card)
    
    
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed,card,click1,click2,state,moves
    ini=0
    end=50
    for i in range(16):
        if pos[0]>=ini and pos[0]<=end:
            if exposed[i]==False:
                if state==0 :
                    moves+=1
                    exposed[i]=True
                    click1=i   
                    state=1
                elif state==1 and not click1==i:
                    exposed[i]=True
                    click2=i   
                    state=2
                else:
                    moves+=1
                    state=1
                    if not(card[click1]==card[click2]):
                        exposed[click1]=False
                        exposed[click2]=False
                    exposed[i]=True
                    click1=i 
            
        ini+=50
        end+=50
        
    
    
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card
    card_width=10
    card_height=75
    point1=[0,0]
    point2=[50,0]
    point3=[50,100]
    point4=[0,100]
    for item in card:
        canvas.draw_text(str(item),(card_width, card_height), 74, "Red")
        card_width+=50
        
        
    for open_card in exposed:
        if open_card==False:
            canvas.draw_polygon([point1, point2,point3,point4], 5, "Black","White")
        point1[0]+=50
        point2[0]+=50
        point3[0]+=50
        point4[0]+=50
    label.set_text("moves="+str(moves))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")
# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric