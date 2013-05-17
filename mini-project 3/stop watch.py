
import simplegui

# define global variables
count = tries = wins = 0
INTERVAL = 100

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    seconds = t // 10 % 60
    minutes = t // 600
    if seconds < 10:
        return str(minutes) + ":0" + str(seconds) + '.' + str(tenths)
    else:
        return str(minutes) + ":" + str(seconds) + '.' + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global wins, tries, running
    if timer.is_running():
        timer.stop()
        tries += 1
        if count % 10==0:
            wins += 1
        
def reset():
    global count, wins, tries
    timer.stop()
    count = wins = tries = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1

def draw(canvas):
    canvas.draw_text(format(count), [70, 120], 40, "White")
    canvas.draw_text(str(wins) + "/" + str(tries), [220, 30], 24, "Green")
    
# create frame
f = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(INTERVAL, timer_handler)
f.set_draw_handler(draw)

# register event handlers
f.add_button("Start", start)
f.add_button("Stop", stop)
f.add_button("Reset", reset)

# start timer and frame
f.start()