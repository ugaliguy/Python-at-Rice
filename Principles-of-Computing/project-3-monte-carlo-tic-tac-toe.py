"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 50         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

#def new_board():
#    """
#    Creates a new board for the game.
#    """
#    dim = 3
#    first_player = provided.PLAYERX
   
#    board = provided.TTTBoard(dim)
   
#    mc_trial(board, first_player)

def mc_trial(board, player):
    """
    Plays a board with given player by making random moves
    on empty squares, alternating between players.
    """
    player = player
    game_in_progress = None
   
    while board.get_empty_squares():
        square = random.choice(board.get_empty_squares())
        board.move(square[0], square[1], player)
       
        state = board.check_win()
        if state != game_in_progress:
            break
       
        player = provided.switch_player(player)  

def mc_update_scores(scores, board, player):
    """
    Updates scores in Monte Carlo simulation
    EMPTY   = 1
    PLAYERX = 2
    PLAYERO = 3
    """
    winner = board.check_win()
    dim = board.get_dim()
   
    for row in range(dim):
        for col in range(dim):
            square = board.square(row, col)
           
            if (winner == provided.PLAYERX) and (player == provided.PLAYERX) or (winner == provided.PLAYERX) and (player == provided.PLAYERO):
                if square == provided.EMPTY:
                    scores[row][col] += 0
                elif square == provided.PLAYERX:
                    scores[row][col] += SCORE_CURRENT
                elif square == provided.PLAYERO:
                    scores[row][col] -= SCORE_OTHER
            elif (winner == provided.PLAYERO) and (player == provided.PLAYERX) or (winner == provided.PLAYERO) and (player == provided.PLAYERO):
                if square == provided.EMPTY:
                    scores[row][col] += 0
                elif square == provided.PLAYERX:
                    scores[row][col] -= SCORE_CURRENT
                elif square == provided.PLAYERO:
                    scores[row][col] += SCORE_OTHER

def get_best_move(board, scores):
    """
    Gets the best move
    """
    empty_squares = board.get_empty_squares()
    high_score = get_high_score(empty_squares, scores)
    dim = board.get_dim()
    empty_square_list = []
       
    for row in range(dim):
        for col in range(dim):
           
            if scores[row][col] == high_score:
                if board.square(row, col) == provided.EMPTY:
                    empty_square_list.append((row, col))
    return random.choice(empty_square_list)

def mc_move(board, player, trials):
    """
    Uses Monte Carlo simulation to find next move for machine player.
    """
    scores = score_grid(board.get_dim())

    for dummy_trial in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
    return get_best_move(board, scores)                    

def score_grid(dim):
    """
    Creates empty score grid for use in mc_move
    """
    return [ [0 for dummy_col in range(dim)] for dummy_row in range(dim)]

def get_high_score(empty_squares, scores):
    """
    Returns high score for get_best_move function
    """
    max_score = float("-inf")
   
    for coord in empty_squares:
        if scores[coord[0]][coord[1]] >= max_score:
            max_score = scores[coord[0]][coord[1]]
    return max_score


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
