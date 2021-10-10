from Questions import Questions
from player import Player
from displayer import Displayer  

class Game:
    def __init__(self, Player, Questions):
        #Object that contains and controls the objects player and questions, it has the relevant
        #information to comunicate with the front end and to allow easy use

        self.player = Player
        self.round = Player.round
        self.score = Player.score
        self.userName = Player.name
        self.questions = Questions
        self.displayer = Displayer
    
    def playGame(self):
        #Initiates the game and controls the flow the game, telling the game which round should be played

        while(self.round <= 5):
            newQuestion = self.questions.getRandomQuestion(self.round)
            userInput = self.displayer.displayQuestion(newQuestion)
            checkPass = self.checkQuestion(newQuestion, userInput)
            if(checkPass):
                self.displayer.displayCorrectMessage()
                self.updateScore(self.round)
                self.savePlayerScore(self.player)
                continue

            else:
                self.displayer.displayGameOver()
                self.resetScore()
                self.savePlayerScore(self.player)
                continue
        self.displayer.congratulations()
            
    def checkQuestion(self, question, userInput):
        #Checks if question is answered correctly

        if(question[1] == userInput):
            self.round += 1
            return True
        else:
            return False

    def updateScore(self, round):
        #Updates player score

        if(round == 5):
            self.score += 10000
        else:
            self.score += round*100
            print(self.score, self.round, self.userName)
    
    def resetScore(self):
        #Resets player score to the first level

        self.score = 0
        self.round = 1
        
    def savePlayerScore(self, player):
        #Conection to player object, updates the info on that object

        player.savePlayerInfo(self.userName, self.score, self.round)

    
