# template for "Stopwatch: The Game"
import simplegui

# define global variables
current_time = 0
unit_time = 100
position = [100,110]
upper_right = [250,50]
win = 0
attempt = 0
on = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t//600
    sa = str(a)
    b = ((t//10)%60)//10
    sb= str(b)
    c = ((t//10)%60)%10
    sc = str(c)
    d = t%10
    sd = str(d)
    s = sa+":"+sb+sc+"."+sd
    return s

# define event handlers for buttons; "Start", "Stop", "Reset"
def restart():
    ''' Button that restarts the timer.'''
    global current_time, attempt, win
    attempt = 0
    win = 0
    current_time = 0

def start():
    ''' Button that starts the timer.'''
    timer.start()

def stop():
    ''' Button that stops the timer.'''
    global attempt, win, on
    on = timer.is_running()
    
    if on == True:
        attempt = attempt + 1
    time  = (current_time//100)%10

    if (time == 0) and (on == True):
        win = win + 1
    timer.stop()


# define event handler for timer with 0.1 sec interval
def tick():
    ''' Counts off 0.1 second.'''
    global current_time
    current_time = current_time + unit_time
#    print current_time
    return current_time

    
# define draw handler
def draw(canvas):
    time = format(current_time//100)
    score = str(win)+"/"+str(attempt)
    canvas.draw_text(score, upper_right, 30, "White")
    canvas.draw_text(time, position, 36, "White")

    
# create frame
frame = simplegui.create_frame('Stopwatch', 325, 200)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Restart", restart, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(unit_time, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
