import mysql.connector
db = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password@123',
    }
connection = mysql.connector.connect(**db)
cursor = connection.cursor()



import G1  # Import the module for game 1
import G2  # Import the module for game 2
import G3  # Import the module for game 3
import G4  # Import the module for game 4

while True:
    print('WELCOME TO MY FINAL PROJECT !')
    print('IN THIS PROJECT I HAVE DESIGNED 4 GAMES')
    print('These 4 games include :\n',
          '1) THE ADVENTURE\n',
          '2) ROCK, PAPER, SCISSORS\n',
          '3) TIC, TAC, TOE\n',
          '4) GUESS-THE-NUMBER')

    a = int(input('ENTER YOUR NO. FROM ABOVE CHOICE: '))

    if a == 1:
        G1.game()
    elif a == 2:
        G2.rock_paper_scissors()
    elif a == 3:
        G3.tic_tac_toe()
    elif a == 4:
        G4.guessing_game()
    else:
        print('Please enter a valid choice.')


