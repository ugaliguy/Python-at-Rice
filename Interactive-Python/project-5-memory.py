# implementation of card game - Memory

import simplegui
import random

# construct the deck of cards
deck = range(8)+range(8)
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
matches = []

counter = 0

# helper function to initialize globals
def new_game():
    global state, counter, matches
    state = 0
    counter = 0
    matches = []
    label.set_text("Turns = " + str(counter))    
    random.shuffle(deck)
    for index in range(len(deck)):
        exposed[index] = False
        
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, matches, state, index1, index2, last1, last2, counter
    mouse_pos = list(pos)
    chosen = mouse_pos[0]//50

    if(state == 0):    
        index1 = chosen
        exposed[index1] = True
        state = 1
    elif (state == 1):
        index2 = chosen
        if (index2 != index1):
            exposed[index2] = True
            counter += 1
            label.set_text("Turns = " + str(counter))         
            state = 2
    else:
        last1 = index1
        last2 = index2
        if (chosen == last1) or (chosen == last2) or (deck[chosen] in matches):
            state = 2
        elif (deck[last1] == deck[last2]):
            exposed[last1] = True
            exposed[last2] = True
            matches.append(deck[last1])
            matches.append(deck[last2])
            index1 = chosen
            exposed[index1] = True
            state = 1  
        elif (deck[chosen] not in matches):        
            exposed[last1] = False
            exposed[last2] = False
            index1 = chosen
            exposed[index1] = True
            state = 1
          
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(deck)):
        card_pos = 50*card_index + 12
        if exposed[card_index] == False:
            left = 50*card_index
            right = left + 50
            canvas.draw_polygon([[left,0],[right,0],[right,99],[left,99]],2,"Orange","Green")
        else:
            canvas.draw_text(str(deck[card_index]),(card_pos,70),60,"White")



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric