import random
import csv
class Questions:
    ##Questions object is basically a dictionary which keys are the rounds asociated to the bank of questions
    #and the values are arrays that contains arrays, those inner arrays have, in order, the statement, the answer
    #and the other 3 options. This object was created with the purpose of only loading once this file as it is
    #the file that has the potential to be the largest and to handle the data more eaisily

    def __init__(self):
        #Declares the questions dictionary

        self.bankOfQuestions = {}
        self.nameOfQuestionDB = 'questionDB.csv'
        ##The bank of questions will be populated next
        self.populateBankOfQuestions(self.nameOfQuestionDB)
    
    def getRandomQuestion(self, round):
        #Returns a random questionn from the dictionary given a level of difficulty

        numberOfQuestions = len(self.bankOfQuestions[round])
        randomQuestion = random.randint(0, numberOfQuestions-1)
        return self.bankOfQuestions[round][randomQuestion]
    
    def addNewQuestion(self, round, statement, answer, option1, option2, option3):
        #Method designed for future developers to add a question via code and not access directly 
        #the csv file

        if(round > 0 and round <= len(self.bankOfQuestions)+1):
            newQuestion = [statement, answer, option1, option2, option3]
            self.bankOfQuestions[round].append(newQuestion)
            newQuestionDB = [str(round), statement, answer, option1, option2, option3]
            with open(self.nameOfQuestionDB, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(newQuestionDB)
                csv_file.close()
        else:
            print("Can´t add question check difficulty level")
    
    def populateBankOfQuestions(self, nameOfDataBase):
        #Method to populate the dictionary inside this object by loading the data of the csv
        #file to the dictionary

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
                    option3 = row[5]
                    currentQuestion = [statement, answer ,option1 , option2, option3]
                    if difficulty in self.bankOfQuestions:
                        self.bankOfQuestions[difficulty].append(currentQuestion)
                    else:
                        level = []
                        level.append(currentQuestion)
                        self.bankOfQuestions[difficulty] = level
                    line_count += 1
