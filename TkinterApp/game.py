from Questions import Questions
from player import Player
from displayer import Displayer  

class Game:
    def __init__(self, Player, Questions):
        self.player = Player
        self.round = Player.round
        self.score = Player.score
        self.userName = Player.name
        self.questions = Questions
        self.displayer = Displayer
    
    def playGame(self):
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
        if(question[1] == userInput):
            self.round += 1
            return True
        else:
            return False

    def updateScore(self, round):
        if(round == 5):
            self.score += 10000
        else:
            self.score += round*100
            print(self.score, self.round, self.userName)
    
    def resetScore(self):
        self.score = 0
        self.round = 1
        
    def savePlayerScore(self, player):
        player.savePlayerInfo(self.userName, self.score, self.round)

    
