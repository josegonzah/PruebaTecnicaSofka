import random
class Questions:
    def __init__(self):
        self.bankOfQuestions = {
            1: [["enunciado", "correcto", "opcion1", "opcion2"], ["enunciado", "correcto", "opcion1", "opcion2"], ["enunciado", "correcto", "opcion1", "opcion2"], ["enunciado", "correcto", "opcion1", "opcion2"], ["enunciado", "correcto", "opcion1", "opcion2"]]
            # 2:{

            # }
            # 3:{

            # }
            # 4:{

            # }
            # 5:{

            # }
        }
    
    def getRandomQuestion(self, round):
        numberOfQuestions = len(self.bankOfQuestions[round])
        randomQuestion = random.randint(0, numberOfQuestions-1)
        return self.bankOfQuestions[round][randomQuestion]
    
    def setNewQuestion(self, round, statement, answer, option1, option2):
        newQuestion = [statement, answer, option1, option2]
        self.bankOfQuestions[round].append(newQuestion)