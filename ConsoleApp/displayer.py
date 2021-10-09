from random import shuffle

class Displayer:

    def displayQuestion(Question):
        print(str(Question[0])+"\n")
        options = Question[1:]
        shuffle(options)
        for i in options:
            print(i + "\n")
        userInput = input("Write the option you want: ")

        return userInput

    def congratulations():
        print("Congratulations you won")

    def displayCorrectMessage():
        print("You picked the correct answer you can advance a round \n")
    
    def displayGameOver():
        print("You didn't pick the correct answer Game Over")
    
    def requestPlayerStatus(self):
        playerStatus = input("Are you new to the game?: ")
        return playerStatus

    def requestUserName(self):
        username = input("Give us your username: ")
        return username

    def oldPlayerError(self):
        print("Your username is not in the data base (is case sensitive)")
    
    def newPlayerError(self):
        print("Your username is already in the database, please check (is case sensitive)")

