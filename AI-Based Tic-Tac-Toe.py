import math

# Initialize board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

# Check for a winner
def check_winner(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in pattern) for pattern in win_patterns)

# Check if board is full
def is_full():
    return " " not in board

# Minimax Algorithm for AI
def minimax(is_maximizing):
    if check_winner("X"): return -1
    if check_winner("O"): return 1
    if is_full(): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI chooses the best move
def ai_move():
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# User makes a move
def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Enter a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    for turn in range(9):
        if turn % 2 == 0:
            player_move()
        else:
            ai_move()
        
        print_board()
        
        if check_winner("X"):
            print("Congratulations! You win! 🎉")
            return
        if check_winner("O"):
            print("AI wins! Better luck next time. 🤖")
            return
        if is_full():
            print("It's a draw! 🤝")
            return

# Start the game
play_game()
