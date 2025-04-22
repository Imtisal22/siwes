import random


board = ['' for _ in range(9)]

def print_board():
    print("\nCurrent board:") 
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[i*3 + j] 
            row.append(cell if cell != '' else str(i*3 + j + 1))  # <- FIXED: moved inside the loop
        print(' | '.join(row))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]             # diagonal
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True 
    return False

def check_tie():
    return '' not in board

def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == '':
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")


def ai_move ():
    available_moves = [i for i in range(9) if board[i] == '']
    move = random.choice(available_moves)
    board[move] = 'O'

def main():
    print("Welcome to Tic Tac Toe!")
    print("Player X goes first.")
    print("Enter your move as a number from 1 to 9, corresponding to the board positions:")
    print("1|2|3\n-----\n4|5|6\n-----\n7|8|9")

    print_board()
    
    while True:
        player_move('X')
        print_board()
        if check_winner('X'):
            print("Player X wins!")
            break
        if check_tie():
            print("It's a tie!")
            break
        
        ai_move()
        print("AI's move:")
        print_board()
        if check_winner('O'):
            print("Player O (AI) wins!")
            break
        if check_tie():
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
    print('Game over!')