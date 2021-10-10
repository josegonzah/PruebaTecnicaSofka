from Questions import Questions
from player import Player
  
class Game:
    def __init__(self, Player, Questions):
        #Object that contains and controls the objects player and questions, it has the relevant
        #information to comunicate with the front end and to allow easy use

        self.player = Player
        self.round = Player.round
        self.score = Player.score
        self.userName = Player.name
        self.questions = Questions
        self.newQuestion = []
    
    def setNewQuestion(self):
        #Returns a random question from the round that is currently set insie the game object

        self.newQuestion = self.questions.getRandomQuestion(self.round)

    def MapQuestions(self, question, shuffledQuestion):
        #Returns the place of the correct answer in a shuffled set of options given the default order

        for i in range(0,len(shuffledQuestion)):
            if(shuffledQuestion[i]==question[0]):
                return i

    def updateScore(self):
        #Updates Score of the current game and then updates the round
        #and updates the info on the player object

        if(self.round == 5):
            self.score += 10000
        else:
            self.score += self.round*100
        self.updateRound()
        self.savePlayerScore(self.player)
    
    def resetScore(self):
        #Resets score and updates info on that player object

        self.score = 0
        self.round = 1
        self.savePlayerScore(self.player)
        
    def savePlayerScore(self, player):
        #Conection to player object, updates the info on that object

        player.savePlayerInfo(self.userName, self.score, self.round)

    def getCurrentRound(self):
        #Return current round

        return self.round

    def getCurrentQuestion(self):
        #Returns current loaded question

        return self.newQuestion

    def updateRound(self):
        #Updates round, only advances by one level

        self.round += 1

    def getScore(self):
        #Returns current score

        return self.score

