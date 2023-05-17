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
        marker = input("Player 1 choose X or O: ")

    #Player 2 is assigned opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)

# this function takes a board list object, a marker ('X', 'O') and a desired position on the board,
# returning it to be updated on the board
def place_marker(board, marker, position):
    board[position] = marker

# checking to see if anyone won the game
def win_check(board, marker):

    # row check
    if board[1] == board[2] == board[3] == marker:
            return True
    if board[4] == board[5] == board[6] == marker:
            return True
    if board[7] == board[8] == board[9] == marker:
            return True
        
    # col check
    if board[1] == board[4] == board[7] == marker:
        return True
    if board[2] == board[5] == board[8] == marker:
        return True
    if board[3] == board[6] == board[9] == marker:
        return True
        
    # diagonal checks
    if board[1] == board[5] == board[9] == marker:
        return True 
    if board[3] == board[5] == board[7] == marker:
        return True
    
    #no winner
    return False

# randomly decides what player goes first
def choose_first():
    goingFirst = random.randint(1,2)
    if goingFirst == 1:
        return "Player 1"
    else: 
        return "Player 2"
    
# checks to see whether the position specified by the user is freely available
def space_check(board, position):
    return board[position] == ' '

# checks to see if the board is full
def full_board_check(board):
    for cell in board:
        if cell == ' ':
            return False
    return True

# player chooses position
def player_choice(board):
    position = 0
    
    while not space_check(board,position) or position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input("Enter a position from 1 to 9 on the board(1 is bottom left corner, 9 is top right corner): "))
    
    return position

# player chooses whether to replay the game or not 
def replay():
    return input("Do you want to play again? (Yes or No): ").upper().startswith('Y')
    

print("Welcome to Tic Tac Toe!")

while True:

    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
    # 10 items because we want to access only indexed 1 through 9
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    game_on = True
    
    while game_on:
        #Player 1
        if turn == "Player 1":
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player1_marker,position)
    
            if win_check(game_board, player1_marker):
                display_board(game_board)
                print("Player 1 Wins!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Tie!")
                    break
                else:
                    turn = "Player 2"
        
        # Player 2 
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player2_marker,position)
    
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print("Player 2 Wins!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Tie!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
        






