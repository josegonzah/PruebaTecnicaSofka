from random import shuffle
from tkinter import *
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from player import Player
from game import Game
from Questions import Questions


class window():
    # Window object that has all the work related to displaying information and controlling the flow of the 
    # application

    def __init__(self):
        # Instantiate a space to draw, a set of questions that is loaded once and only a user per session

        self.root = Tk()
        self.questions = Questions()
        self.player = Player()
        self.configureMainWindow()
        self.root.mainloop()

    def configureMainWindow(self):
        #Tkinter intiation of objects, widgets and actions asociated to events
        # that will be in the validation window

        self.root.title("25 Questions")
        self.root.configure(background='black')
        self.root.geometry("1200x900")
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        pageTitle = Label(self.root,text="Welcome to 25 Questions Game", font=("Microsoft Sans Serif", 45),bg='black', fg="#1DB954")
        pageTitle.grid(column=2, row=0, padx=10, pady=10)
        typeOfGameMessage = Label(self.root,text="Are you new to the game? ", font=("Microsoft Sans Serif", 25),bg='black', fg="white")
        typeOfGameMessage.grid(column=2, row=2, padx=10, pady=10)
        typeOfPlayerVar = IntVar()
        Radiobutton(self.root, text="New Player", variable=typeOfPlayerVar, value=1, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 10)).grid(column=2, row=3)
        Radiobutton(self.root, text="Saved Game", variable=typeOfPlayerVar, value=2, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 10)).grid(column=2, row=4)
        putYourUserName = Label(self.root,text="Please give us your name", font=("Microsoft Sans Serif", 25),bg='black', fg="white")
        putYourUserName.grid(column=2, row=5, padx=10, pady=10)
        inputUserName = Entry(self.root, bg='#1DB954', fg='white', font=("Microsoft Sans Serif", 15), )
        inputUserName.grid(column=2, row=6, padx=10, pady=10)
        submitButton = Button(self.root, text="Begin Game", command=lambda:self.validateUserName(inputUserName.get(),typeOfPlayerVar.get()),width=10,height=1, bg='#F80332', fg='white', font=("Microsoft Sans Serif", 15)) #  width, height en pixeles
        submitButton.grid(row=7, column=2, padx=20, pady=20)

    def validateUserName(self, userName, typeOfGame):
        #Validation of user checking in the players database via the player object
        #to begin a game based on the data given by the database

        playerStatus = typeOfGame
        playerName = userName
        validUsername = self.checkValidUsername(userName) 
        if(playerStatus == 1):
            isNew = self.player.setNewPlayer(playerName)
            if(isNew and validUsername):
                self.player.saveNewPlayer(playerName)
                self.startGame()
            else:
                typeOfError = 1
                self.displayErrorMessage(typeOfError)
        else:
            isOld = self.player.loadOldPlayer(playerName)
            if(isOld and validUsername):
                self.startGame()
            else:
                typeOfError = 2
                self.displayErrorMessage(typeOfError)

    def checkValidUsername(self, userName):
        if(',' in userName):
            error = Toplevel(self.root)
            error.configure(background='black')
            error.geometry("750x250")
            error.title("Error Message")
            Label(error, text= "Do not put a , (comma) inside your username", font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=80)
            return False
        else:
            return True

    def displayErrorMessage(self, typeOfError):
        #Handles errors asociated to the users, poping a window up

        error = Toplevel(self.root)
        error.configure(background='black')
        error.geometry("750x250")
        error.title("Error Message")
        if(typeOfError == 1):
            Label(error, text= "Your username is already in the database \n check it (case sensitive)", font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=80)
        else:
            Label(error, text= "Your username is not in the database \n check it (case sensitive)", font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=80)

    def startGame(self):
        #Clears window and calls a function to setup the new content and the game object

        for widgets in self.root.winfo_children():
            widgets.destroy()
        self.configureQuestionsWindow()
    
    def configureQuestionsWindow(self):
        #Sets up a new game object with the objects player that was previously validated and the bank of questions

        game = Game(self.player, self.questions)
        self.setQuestionsWindow(game)

    def setQuestionsWindow(self, game):
        #Check if the game was already completed and gets significant data to build the window with
        #the questionaire. Gets a random question from the pack, reorders the options in a random order
        #and has the information about the location of the correct answer in the shuffled order of options

        if(self.isCleared(game)):
            self.gameCleared(game)
        else:
            game.setNewQuestion()
            currentRound = game.getCurrentRound()
            currentQuestion = game.getCurrentQuestion()
            options = currentQuestion[1:]
            questionStatement = currentQuestion[0]
            currentScore = game.getScore()
            shuffle(options)
            realAnswer = game.MapQuestions(currentQuestion[1:], options)
            self.buildQuestionsWindow(questionStatement, currentRound, options, realAnswer, currentScore, game)

    def buildQuestionsWindow(self, questionStatement, currentRound, options, realAnswer, currentScore, game):
        #Builds the window and has the actions asociated to events in the window
        
        roundTitle = Label(self.root,text="Round: "+str(currentRound), font=("Microsoft Sans Serif", 25),bg='black', fg="#EFC518")
        roundTitle.grid(column=2, row=0, padx=10, pady=10)
        questionStamentLabel = Label(self.root,text=questionStatement, font=("Microsoft Sans Serif", 25),bg='black', fg="white")
        questionStamentLabel.grid(column=2, row=1, padx=10, pady=10)
        scoreLabel = Label(self.root,text="SCORE: " + str(currentScore), font=("Microsoft Sans Serif", 15),bg='black', fg="#1DB954")
        scoreLabel.grid(column=3, row=0, padx=10, pady=10)
        userAnswer = IntVar()
        Radiobutton(self.root, text=options[0], variable=userAnswer, value=0, bg='black', fg='#1DB954').grid(column=2, row=2)
        Radiobutton(self.root, text=options[1], variable=userAnswer, value=1, bg='black', fg='#1DB954').grid(column=2, row=3)
        Radiobutton(self.root, text=options[2], variable=userAnswer, value=2, bg='black', fg='#1DB954').grid(column=2, row=4)
        Radiobutton(self.root, text=options[3], variable=userAnswer, value=3, bg='black', fg='#1DB954').grid(column=2, row=5)
        validateAns = Button(self.root, text="Submit", command=lambda:self.validateUserAns(realAnswer, userAnswer.get(), game),width=10,height=1, bg='#F80332', fg='white', font=("Microsoft Sans Serif", 15))
        validateAns.grid(row=7, column=2, padx=20, pady=20)

    def validateUserAns(self, realAnswer, userAnswer, game):
        #checks if the answer given by the user is the correct one and updates the object game according to the 
        #action

        if(userAnswer == realAnswer):
            for widgets in self.root.winfo_children():
                widgets.destroy()
            self.updateGame(game)
        else:
            for widgets in self.root.winfo_children():
                widgets.destroy()
            self.gameOver(game)
            
    def updateGame(self, game):
        #updates values of the object game and rebuilds the window

        game.updateScore()
        self.setQuestionsWindow(game)

    def gameOver(self, game):
        #Clears window and shows message of game over

        game.resetScore()
        self.showGameOver()

    def showGameOver(self):
        #Builds game over window

        error = Toplevel(self.root)
        error.configure(background='black')
        error.geometry("750x250")
        error.title("GAME OVER")
        Label(error, text= "Game Over: You Loose", font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=80)

    def gameCleared(self, game):
        #Builds game cleared window

        cleared = Toplevel(self.root)
        cleared.configure(background='black')
        cleared.geometry("750x250")
        cleared.title("You win")
        Label(cleared, text= "You WON", font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=80)
        Label(cleared, text= "Score: "+str(game.getScore()), font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=160)
    
    def isCleared(self, game):
        #Checks if the game is already completed to decide which content to render

        if(game.getCurrentRound() == 6):
            return True
        else:
            return False
