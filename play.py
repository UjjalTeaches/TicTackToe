import math
import os

# Constants for the players
PLAYER = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(b):
    win_states = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for s in win_states:
        if b[s[0]] == b[s[1]] == b[s[2]] != EMPTY:
            return b[s[0]]
    if EMPTY not in b:
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing):
    res = check_winner(board)
    if res == AI: return 10 - depth
    if res == PLAYER: return depth - 10
    if res == 'Tie': return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    board = [EMPTY] * 9
    print_board(board)

    while True:
        # Player Turn
        try:
            choice = int(input("Enter move (1-9): ")) - 1
            if board[choice] != EMPTY:
                print("Space taken!")
                continue
            board[choice] = PLAYER
        except (ValueError, IndexError):
            print("Invalid input!")
            continue

        if check_winner(board): break

        # AI Turn
        print("AI is thinking...")
        ai_move = get_best_move(board)
        board[ai_move] = AI
        
        print_board(board)
        if check_winner(board): break

    print_board(board)
    winner = check_winner(board)
    if winner == 'Tie':
        print("It's a draw!")
    else:
        print(f"The winner is {winner}!")

if __name__ == "__main__":
    main()
