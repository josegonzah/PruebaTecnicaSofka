import random
import csv
class Questions:
    def __init__(self):
        self.bankOfQuestions = {}
        self.nameOfQuestionDB = 'questionDB.csv'
        ##The bank of questions will be populated next
        self.populateBankOfQuestions(self.nameOfQuestionDB)
    
    def getRandomQuestion(self, round):
        numberOfQuestions = len(self.bankOfQuestions[round])
        randomQuestion = random.randint(0, numberOfQuestions-1)
        return self.bankOfQuestions[round][randomQuestion]
    
    def addNewQuestion(self, round, statement, answer, option1, option2):
        if(round > 0 and round <= len(self.bankOfQuestions)+1):
            newQuestion = [statement, answer, option1, option2]
            self.bankOfQuestions[round].append(newQuestion)
            newQuestionDB = [str(round), statement, answer, option1, option2]
            with open(self.nameOfQuestionDB, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(newQuestionDB)
                csv_file.close()
        else:
            print("Can´t add question check difficulty level")
    
    def populateBankOfQuestions(self, nameOfDataBase):
        with open(nameOfDataBase) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    difficulty = int(row[0])
                    statement = row[1]
                    answer = row[2]
                    option1 = row[3]
                    option2 = row[4]
                    currentQuestion = [statement, answer ,option1 , option2]
                    if difficulty in self.bankOfQuestions:
                        self.bankOfQuestions[difficulty].append(currentQuestion)
                    else:
                        level = []
                        level.append(currentQuestion)
                        self.bankOfQuestions[difficulty] = level
                    line_count += 1
