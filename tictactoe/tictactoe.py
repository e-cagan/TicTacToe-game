import random

# We must display the board
# We must decide who's turn it's gonna be
# We must provide the user and computer makes their moves
# We must check the winning conditions

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def display_board():
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")

def reset_board():
    for key in board:
        board[key] = ' '
    
def main():
    while True:
        user_input = int(input("Enter a number between 1 to 9: "))
        while board[user_input] != ' ':
            print("Invalid position. Please try again.")
            user_input = int(input("Enter a number between 1 to 9: "))

        print(f"User makes it's move to point {user_input}")
        board[user_input] = 'X'

        # Tie situation (We are checking right after user makes it's move because computer makes it's move immediately)
        if ' ' not in board.values():
            print("It'a tie!!!")
            break

        computer_input = random.randint(1, 9)
        while board[computer_input] != ' ':
            computer_input = random.randint(1, 9)

        print(f"Computer makes it's move to point {computer_input}")
        board[computer_input] = 'O'

        display_board()
        
        # Checking same row
        if board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
            print("User wins!")
            break
        elif board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
            print("User wins.")
            break
        elif board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
            print("User wins.")
            break
        elif board[1] == 'O' and board[2] == 'O' and board[3] == 'O':
            print("Computer wins!")
            break
        elif board[4] == 'O' and board[5] == 'O' and board[6] == 'O':
            print("Computer wins!")
            break
        elif board[7] == 'O' and board[8] == 'O' and board[9] == 'O':
            print("Computer wins!")
            break
        
        # Checking same column
        elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            print("User wins!")
            break
        elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
            print("User wins!")
            break
        elif board[3] == 'X' and board[6] == 'X' and board[9] == 'X':
            print("User wins!")
            break
        elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
            print("Computer wins!")
            break
        elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
            print("Computer wins!")
            break
        elif board[3] == 'O' and board[6] == 'O' and board[9] == 'O':
            print("Computer wins!")
            break
        
        #Checking diagonals
        elif board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
            print("User wins!")
            break
        elif board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
            print("User wins!")
            break
        elif board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
            print("Computer wins!")
            break
        elif board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
            print("Computer wins!")
            break
        

    user_response = input("Wanna play again? 'yes' or 'no': ").lower()
    
    if user_response == 'yes':
        reset_board()
        main()
    elif user_response == 'no':
        print("Come again sometime :)")
    else:
        print("Invalid response.")

main()
