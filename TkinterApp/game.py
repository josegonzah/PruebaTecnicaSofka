from Questions import Questions
from player import Player
  
class Game:
    def __init__(self, Player, Questions):
        self.player = Player
        self.round = Player.round
        self.score = Player.score
        self.userName = Player.name
        self.questions = Questions
        self.newQuestion = []
    
    def playGame(self):
        # while(self.round <= 5):
        self.newQuestion = self.questions.getRandomQuestion(self.round)
            # userInput = self.displayer.displayQuestion(newQuestion)
            # checkPass = self.checkQuestion(newQuestion, userInput)
            # checkPass = False
            # if(checkPass):
            #     # self.displayer.displayCorrectMessage()
            #     self.updateScore(self.round)
            #     self.savePlayerScore(self.player)
            #     continue

            # else:
            #     # self.displayer.displayGameOver()
            #     self.resetScore()
            #     self.savePlayerScore(self.player)
            #     continue
        # self.displayer.congratulations()
    
    def setNewQuestion(self):
        self.newQuestion = self.questions.getRandomQuestion(self.round)

    def MapQuestions(self, question, shuffledQuestion):
        for i in range(0,len(shuffledQuestion)):
            if(shuffledQuestion[i]==question[0]):
                return i

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
        self.savePlayerScore(self.player)
    
    def resetScore(self):
        self.score = 0
        self.round = 1
        self.savePlayerScore(self.player)
        
    def savePlayerScore(self, player):
        player.savePlayerInfo(self.userName, self.score, self.round)

    def getCurrentRound(self):
        return self.round

    def getCurrentQuestion(self):
        return self.newQuestion

    def updateRound(self):
        self.round += 1

