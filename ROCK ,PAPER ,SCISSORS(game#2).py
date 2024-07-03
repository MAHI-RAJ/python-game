import mysql.connector
import random
db = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password@123',
    'database':'computer'}
connection = mysql.connector.connect(**db)
cursor = connection.cursor()

f=open('file#2.txt','a')


def rock_paper_scissors():
    b=0
    d=0
    cursor.execute('select * from rock')
    a=cursor.fetchone()    
    
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        f.write(user_choice)
        computer_choice = random.choice(a)
        d+=1

        print(f"Computer chose: {computer_choice}")

        if user_choice in a :
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (
                (user_choice == "rock" and computer_choice == "scissors") or
                (user_choice == "paper" and computer_choice == "rock") or
                (user_choice == "scissors" and computer_choice == "paper")
            ):
                print("You win!")
                b+=1
            else:
                print("You lose!")
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
        c=input('you want to continue ? y/n :')
        if c=='n':
            break 
    print('your final score :',b,'/',d)
rock_paper_scissors()
f.close()
cursor.close()
connection.close()

