#Welcome message for the Players
print("")
print("Hey! Welcome to the Tik-Tak-Toe game board.")
print("")
print("Tic-tac-toe is played on a three-by-three grid by two players, who alternately place the marks X and O in one of the nine spaces in the grid.")
print("")
print("Player A will be marked as X")
print("")
print("Player B will be marked as 0")
print("")
print("The board has 9 blocks. To make a move each player must select the block number by choosing any number between 1 and 9 (inclusive). Below is a representation of how the game board looks...")
print("")
g_board = [" ", " ", " ",
           " ", " ", " ",
           " ", " ", " "]
print("")
print("Player A begins. Choose a number from 1-9...")
print("")
winner = None
markerA = "X"
markerB = "0"
currentplayer = "A"
block_num = 1


# Printing the game board
def print_board(g_board_num, marker):
    g_board[g_board_num-1] = marker
    print(" "+g_board[0]+"| "+g_board[1]+" |"+g_board[2])
    print("--|---|--")
    print(" "+g_board[3]+"| "+g_board[4]+" |"+g_board[5])
    print("--|---|--")
    print(" "+g_board[6]+"| "+g_board[7]+" |"+g_board[8])
    print("")

player_choice = int(input())
print_board(player_choice, markerA)