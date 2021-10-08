# import pyodbc
# server = 'localhost'
# database = 'sofkatest'
# username = 'root'
# password = ''
# cnxn = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM users')
# for i in cursor:
#     print(i)
from player import Player
from game import Game
from Questions import Questions


questions = Questions()
playerStatus = input("Are you new to the game?: ")
if(playerStatus == "yes"):
    playername = input("Give us your name please: ")
    ##Check if the player is indeed new
    player = Player(playername)
    
else:
    playername = input("Give us your saved name")
    player = Player(playername, score=10, round=2)



newGame = Game(player, questions)
newGame.playGame()


