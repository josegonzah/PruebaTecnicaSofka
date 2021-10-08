from Questions import Questions
from player import Player
from functions import *

class Game:
    def __init__(self, Player, Questions):
        self.player = Player
        self.round = Player.round
        self.score = Player.score
        self.questions = Questions
    
    def playGame(self):
        while(self.round < 5):
            newQuestion = self.questions.getNewQuestion(self.round)
            userInput = displayQuestion(newQuestion)
            checkPass = self.checkQuestion(newQuestion, userInput)
            if(checkPass):
                continue
            ##Save in dataBase
            else:
                break
            ##Save in database
            

    def checkQuestion(self, question, userInput):
        if(question[1] == userInput):
            self.updateScore(self.round)
            self.round += 1
            return True
        else:
            self.round = 0
            return False

    def updateScore(self, round):
        if(round == 5):
            self.score += 10000
        else:
            self.score += round*100
    


    
    # def loadPlayerData(self):
