#Welcome message for the Players
winner = None
markerA = "X"
markerB = "0"
currentplayer = "B"
player_mark = markerB
user_choice = 0
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

# Printing the game board
def print_board(g_board_num, marker):
    g_board[g_board_num-1] = marker
    print(" "+g_board[0]+"| "+g_board[1]+" |"+g_board[2])
    print("--|---|--")
    print(" "+g_board[3]+"| "+g_board[4]+" |"+g_board[5])
    print("--|---|--")
    print(" "+g_board[6]+"| "+g_board[7]+" |"+g_board[8])
    print("")

#switch player
def which_playerNmarker(c_player):
    if c_player == "A":
        c_player = "B"
        marker = markerB
    elif c_player == "B":
        c_player = "A"
        marker = markerA
    return c_player, marker

def player_ip():
    block_num = int(input())
    return block_num

def contains(g_board, empty_str):
	if empty_str in g_board:
		return True
	else:
		return False

# win/tie check
def winORtie(c_player, mark):
    win_lines = [
         [0,1,2],
         [3,4,5],
         [6,7,8],
         [0,3,6],
         [1,4,7],
         [2,5,8],
         [0,4,8],
         [2,4,6]
    ]
    for line in win_lines:
         if (g_board[line[0]] == g_board[line[1]] == g_board[line[2]] == mark):
              return c_player
    if (contains(g_board, " ") == False):
        return "Tie"
    return None

# win/tie check
while winner == None:
    currentplayer, player_mark = which_playerNmarker(currentplayer)
    print("Player " + currentplayer + "'s move. Choose a number from 1-9...")
    user_choice = player_ip()
    print_board(user_choice, player_mark)
    winner = winORtie(currentplayer, player_mark)

if winner == "Tie":
     print("Alas! It's a tie! Good Game ✨")
else:  
    print("Yay! We have a winner. Congratulations Player " + currentplayer +"! 🎊🥳🎉")