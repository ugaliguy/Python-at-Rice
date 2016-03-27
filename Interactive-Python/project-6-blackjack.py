# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
round = 0
outcome = ""
prompt = "Hit or Stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.list = []	# create Hand object

    def __str__(self):
        s = ""
        for i in range(len(self.list)):
            ci = str(self.list[i])
            s += (" " + ci)
        return "Hand contains" + s	# return a string representation of a hand

    def add_card(self, card):
        self.list.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        aces = 0
        hvi = ""
        for i in range(len(self.list)):
            hvi = self.list[i].get_rank()
            value += VALUES.get(hvi)
            if (hvi == 'A'):
                aces += 1
        if (aces == 0):
            return value
        else:
            if(value + 10 <= 21):
                return value + 10
            else:
                return value 
         
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.list)):
            cpos = [100+72*i, pos[1]]
            self.list[i].draw(canvas, cpos)
        if (in_play == True):
            card_loc = (CARD_CENTER[0], CARD_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_SIZE, [100 + CARD_CENTER[0], 175 + CARD_CENTER[1]], CARD_SIZE)
         
            
    
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.list = []	# create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.list.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.list)    # use random.shuffle()

    def deal_card(self):
        return self.list.pop()	# deal a card object from the deck
    
    def __str__(self): # return a string representing the deck
        s = ""
        for i in range(len(self.list)):
            ci = str(self.list[i])
            s += (ci + " ")
        return "Deck contains " + s



#define event handlers for buttons
def deal():
    global outcome, prompt, score, round, cover, in_play, game_deck, player_hand, dealer_hand
    outcome = ""    
    if (prompt == "Hit or Stand?") and (round > 0):
        outcome = "Did not finish round."
        score -=1
    else:
        prompt = "Hit or Stand?"
    round += 1
    game_deck = Deck()
    player_hand = Hand() 
    dealer_hand = Hand()
    # your code goes here
    game_deck.shuffle()
    c1 = game_deck.deal_card()
    c2 = game_deck.deal_card()
    player_hand.add_card(c1)
    player_hand.add_card(c2)
    c3 = game_deck.deal_card()
    c4 = game_deck.deal_card()
    dealer_hand.add_card(c3)
    dealer_hand.add_card(c4)
    in_play = True

def hit():
    # replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global outcome, prompt, score, cover, in_play, game_deck, player_hand, dealer_hand
    if (in_play == True):
        if (player_hand.get_value() <= 21):
            player_hand.add_card(game_deck.deal_card())
            if (player_hand.get_value() > 21):
                prompt = "New Deal?"
                outcome = "You lose."
                card_loc = (CARD_CENTER[0], CARD_CENTER[1])
                in_play = False
                score -=1
    else:
        if (dealer_hand.get_value() <= 21) and (prompt != "New Deal?"):
            dealer_hand.add_card(game_deck.deal_card())
       
def stand():
    # replace with your code below 
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global outcome, prompt, cover, score, in_play, game_deck, player_hand, dealer_hand
    in_play = False
    if (prompt != ""):
        prompt = prompt
    if (player_hand.get_value() > 21):
        prompt = "New Deal?"
        outcome = "Round over."
    else:
        if (dealer_hand.get_value() > 16) and (player_hand.get_value() <= dealer_hand.get_value()):
            if (prompt == "New Deal?"):
                outcome = "Round over."
            else:
                prompt = "New Deal?"            
                outcome = "You lose."
                score -=1
        else:
            while (dealer_hand.get_value() < 17) and (prompt != "New Deal?"):
                hit()
            if (dealer_hand.get_value() > 21):
                prompt = "New Deal?"
                outcome = "You Win!"
                score +=1
            elif (player_hand.get_value() <= dealer_hand.get_value()):
                prompt = "New Deal?"
                outcome = "You lose."
                score -=1
            elif (dealer_hand.get_value() < player_hand.get_value()):
                if (prompt == "New Deal?"):
                    outcome = "Round over."
                else:
                    prompt = "New Deal?"
                    outcome = "You Win!"
                    score +=1 
        
        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack",[100,75],54,"Aqua")
    canvas.draw_text("Dealer",[100,150],36,"Black")
    canvas.draw_text("Player",[100,375],36,"Black")
    canvas.draw_text("Score: " + str(score),[398,75],36,"Black")
    canvas.draw_text(outcome,[270,150],36,"Black")    
    canvas.draw_text(prompt,[270,375],36,"Black")
    dealer_hand.draw(canvas, [100, 175])
    player_hand.draw(canvas, [100, 400])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric