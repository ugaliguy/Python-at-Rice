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
LEFT = False
RIGHT = True

ball_pos = [WIDTH/2, HEIGHT/2]
vel = [0, 0]
paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel # these are vectors stored as lists
    vel[0] = random.randrange(120,240)/60
    vel[1] = random.randrange(60,180)/60

    ball_pos = [WIDTH/2, HEIGHT/2]
    if (direction == RIGHT):
        vel[0] = vel[0]
        vel[1] = -vel[1]
    else:
        vel[0] = -vel[0]
        vel[1] = -vel[1]



# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    direction = random.choice([RIGHT, LEFT])
    print "direction =", direction
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # Collision with floor and ceiling
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS):
        vel[1] = - vel[1]

    # Collision with gutters and paddles
    if (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)) and ((ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT))):
        vel[0] = -vel[0]
    elif (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)):
        spawn_ball(RIGHT)
    elif (ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS) and ((ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT)):
        vel[0] = -vel[0]
    elif (ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS):
        spawn_ball(LEFT)        
        
        
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel >= 0) and (paddle1_pos + paddle1_vel <= HEIGHT - PAD_HEIGHT):
        paddle1_pos += paddle1_vel
        
    if (paddle2_pos + paddle2_vel >= 0) and (paddle2_pos + paddle2_vel <= HEIGHT - PAD_HEIGHT):
        paddle2_pos += paddle2_vel  
    
    # draw paddles
    #Left Paddle
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH - 1, paddle1_pos], [PAD_WIDTH - 1, paddle1_pos + PAD_HEIGHT], [0, paddle1_pos + PAD_HEIGHT]], 1, 'White', 'White')
    #Right Paddle
    canvas.draw_polygon([[WIDTH -1, paddle2_pos], [WIDTH - PAD_WIDTH - 1, paddle2_pos], [WIDTH - PAD_WIDTH - 1, paddle2_pos + PAD_HEIGHT], [WIDTH - 1, paddle2_pos + PAD_HEIGHT]], 1, 'White', 'White')
 
    
    # determine whether paddle and ball collide   
    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    paddle_vel = 4
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
        
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel
   
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_vel, paddle2_vel
    paddle_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
        
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
