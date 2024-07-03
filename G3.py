import mysql.connector
import random
db = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password@123',
    'database':'computer'}
connection = mysql.connector.connect(**db)
cursor = connection.cursor()


f=open('file#3.txt','a')




def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    cursor.execute('select * from tic')
    players =cursor.fetchone()
    turn = 0

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        player = players[turn % 2]
        j=input(f"Player {player}, enter your move (row col): ")
        move = j.split()
        row, col = map(int,move) 
        f.write(j)

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif all(cell != " " for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break
            else:
                turn += 1
        else:
            print("Cell already occupied. Try again.")


