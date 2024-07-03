import mysql.connector
import random
db = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password@123',
    'database':'computer'}
connection = mysql.connector.connect(**db)
cursor = connection.cursor()

s=('congrats! you survived ' , 'OH NO ! YOU DIED')

# connection established !

def game():
   while True:
       if connection.is_connected() :
   
            print ('welcome to our game :','THE ADVENTURE')
# use of data file for storage of inserted data !
       with open ('file#1.txt','a') as f1:
          cursor.execute('select * from scene')
          a=cursor.fetchall()                                                                               
          for i in range (len(a)):
             print(a[i][0], 'what would you do :')
             print('1.',a[i][1] )
             print('2.',a[i][2] )
             b=int(input('enter you choice no.  from above : '))
             c=random.choice(s) 
             print(c)
             if c!=s[0]:               
                   break
       print('HERE COMES  THE END OF THE GAME !')
       global t
       t=input('YOU WANNA PLAY AGAIN? y/n : ')
       if t!='y':
            print('THANKS FOR PLAYING !')
            break





    