from IPython.display import clear_output 
import random

# this function displays the board
def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

# this function decides who player 1 wants to be, assigning both players
def player_input():
    marker = ''

    #Player 1 chooses X or O
    while marker not in ['X', 'O']:
        marker = input("Player1 choose X or O: ")

    #Player 2 is assigned opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)

def place_marker(board, marker, position):
    pass

test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)

players = player_input()
player1 = players[0]
player2 = players[1]
print(player1, player2)
