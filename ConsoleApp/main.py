from displayer import Displayer
from player import Player
from game import Game
from Questions import Questions


questions = Questions()
player = Player()
displayer = Displayer()
startGame = False
while(not(startGame)):
    playerStatus = displayer.requestPlayerStatus()
    if(playerStatus == "yes"):
        playername = displayer.requestUserName()
        isNew = player.setNewPlayer(playername)
        if(isNew):
            player.saveNewPlayer(playername)
            startGame = True
            break
        else:
            displayer.newPlayerError()
            continue
    else:
        playername = displayer.requestUserName()
        isOld = player.loadOldPlayer(playername)
        if(isOld):
            startGame = True
            break
        else:
            displayer.oldPlayerError()
            continue

newGame = Game(player, questions)
newGame.playGame()







