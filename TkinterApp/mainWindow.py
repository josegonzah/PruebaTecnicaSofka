from random import shuffle
from tkinter import *
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from player import Player
from game import Game
from Questions import Questions


questions = Questions()
player = Player()
startGame = False
dimension = "1000x350"
currentQuestion = []

def callGameWindow1():
	inicio.destroy()
	gameWindow()

def selectTypeofPlayer():
    typeOfPlayer = typeOfPlayerVar.get()

def validateUserName():
    playerStatus = typeOfPlayerVar.get()
    playerName = inputUserName.get()
    if(playerStatus == 1):
        isNew = player.setNewPlayer(playerName)
        if(isNew):
            player.saveNewPlayer(playerName)
            callGameWindow1()
        else:
            print("Error userNameNew")
            typeOfError = 1
            displayErrorMessage(typeOfError)
    else:
        isOld = player.loadOldPlayer(playerName)
        if(isOld):
            callGameWindow1()
        else:
            print("Error userName Old")
            typeOfError = 2
            displayErrorMessage(typeOfError)
    
def displayErrorMessage(typeOfError):
    error = Toplevel(inicio)
    error.configure(background='black')
    error.geometry("750x250")
    error.title("Error Message")
    if(typeOfError == 1):
        Label(error, text= "Your username is already in the database \n check it (case sensitive)", font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=80)
    else:
        Label(error, text= "Your username is not in the database \n check it (case sensitive)", font=('Windows Sans Serif', 20),bg='black', fg="#F80332" ).place(x=150,y=80)



inicio = Tk()
inicio.title("Welcome to 25 Questions")
inicio.configure(background='black')
inicio.geometry("1000x550")
inicio.grid_rowconfigure(7, weight=1)
inicio.grid_columnconfigure(2, weight=1)

pageTitle = Label(inicio,text="Welcome to 25 Questions Game", font=("Microsoft Sans Serif", 45),bg='black', fg="#1DB954")
pageTitle.grid(column=2, row=0, padx=10, pady=10)
typeOfGameMessage = Label(inicio,text="Are you new to the game? ", font=("Microsoft Sans Serif", 25),bg='black', fg="white")
typeOfGameMessage.grid(column=2, row=2, padx=10, pady=10)
typeOfPlayerVar = IntVar()
gameOptionNew = Radiobutton(inicio, text="New Player", variable=typeOfPlayerVar, value=1,command=selectTypeofPlayer, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 10)).grid(column=2, row=3)
gameOptionOld = Radiobutton(inicio, text="Saved Game", variable=typeOfPlayerVar, value=2,command=selectTypeofPlayer, bg='black', fg='#1DB954', font=("Microsoft Sans Serif", 10)).grid(column=2, row=4)
putYourUserName = Label(inicio,text="Please give us your name", font=("Microsoft Sans Serif", 25),bg='black', fg="white")
putYourUserName.grid(column=2, row=5, padx=10, pady=10)
inputUserName = Entry(inicio, bg='#1DB954', fg='white', font=("Microsoft Sans Serif", 15), )
inputUserName.grid(column=2, row=6, padx=10, pady=10)
btn_0 = Button(inicio, text="Begin Game", command=validateUserName,width=10,height=1, bg='#F80332', fg='white', font=("Microsoft Sans Serif", 15)) #  width, height en pixeles
btn_0.grid(row=7, column=2, padx=20, pady=20) # ,sticky="S"
# inicio.attributes('-fullscreen', True)

def gameWindow():

    def updateRound():
        newGame.updateRound()
        currentRound = newGame.getCurrentRound()
        newGame.updateScore(currentRound)
        roundTitle.config(text="Round: " + str(currentRound))

    def updateQuestion():
        newGame.setNewQuestion()
        currentQuestion = newGame.getCurrentQuestion()
        questionStatement = currentQuestion[0]
        options = currentQuestion[1:]
        shuffle(options)
        questionStamentLabel.config(text=questionStatement)
        realAnswer = newGame.MapQuestions(currentQuestion[1:], options)
        option1.config(text=options[0])
        option2.config(text=options[1])
        option3.config(text=options[2])
        option4.config(text=options[3])
        # print(realAnswer)
        


    def validateUserAns():
        if(userAnswer.get()== realAnswer):
            print("es correcto")
            updateRound()
            updateQuestion()
        else:
            print("equivocado wey")
    

    newGame = Game(player, questions)
    newGame.playGame()
    currentRound = newGame.getCurrentRound()
    currentQuestion = newGame.getCurrentQuestion()
    

    gameWindow = Tk()
    gameWindow.title("Round: "+str(currentRound))
    gameWindow.geometry("1000x550")
    gameWindow.grid_rowconfigure(7, weight=1)
    gameWindow.grid_columnconfigure(2, weight=1)
    gameWindow.configure(background='black')

    roundTitle = Label(gameWindow,text="Round: "+str(currentRound), font=("Microsoft Sans Serif", 25),bg='black', fg="#EFC518")
    roundTitle.grid(column=2, row=0, padx=10, pady=10)


    questionStatement = currentQuestion[0]
    options = currentQuestion[1:]
    shuffle(options)

    questionStamentLabel = Label(gameWindow,text=questionStatement, font=("Microsoft Sans Serif", 25),bg='black', fg="white")
    questionStamentLabel.grid(column=2, row=1, padx=10, pady=10)
    userAnswer = IntVar()
    realAnswer = newGame.MapQuestions(currentQuestion[1:], options)
    option1 = Radiobutton(gameWindow, text=options[0], variable=userAnswer, value=0)
    option1.grid(column=2, row=2)
    option2 = Radiobutton(gameWindow, text=options[1], variable=userAnswer, value=1)
    option2.grid(column=2, row=3)
    option3 = Radiobutton(gameWindow, text=options[2], variable=userAnswer, value=2)
    option3.grid(column=2, row=4)
    option4 = Radiobutton(gameWindow, text=options[3], variable=userAnswer, value=3)
    option4.grid(column=2, row=5)
    validateAns = Button(gameWindow, text="Submit", command=validateUserAns,width=10,height=1, bg='#F80332', fg='white', font=("Microsoft Sans Serif", 15))
    validateAns.grid(row=7, column=2, padx=20, pady=20)

    # answer = currentQuestion[2]
    # option1 = currentQuestion[3]
    # option2 = currentQuestion[4]

#     nom = Frame(window, width=0, height=0)
#     nom.grid(column=0, row=0, pady=10)
    
#     lbl_1 = Label(nom,text="Evento: ", font=("Arial Bold", 9))
#     lbl_1.grid(column=0, row=0)



#     txt_0 = Entry(nom, width=15)
#     txt_0.grid(column=1, row=0)

#     def borrar_click(event):
#         txt_0.delete(0, END) 
#     txt_0.bind("<Button-1>", borrar_click) 
#     txt_0.insert(0,' Nombre evento')

#     prob = LabelFrame(window, text="Probabilidad", width=0, height=0)
#     prob.grid(column=0, row=1, pady=10)
    
#     Pre_1 = Frame(prob, width=0, height=0)
#     Pre_1.grid(column=0, row=0)
#     lbl_2 = Label(Pre_1,text="Primer parámetro:", font=("Arial Bold", 9))
#     lbl_2.grid(column=0, row=0)
#     var_1 = IntVar()
#     GR1 = Radiobutton(Pre_1, text="Opción 1", variable=var_1, value=1,command=sel_1).grid(column=0, row=1)
#     GR1 = Radiobutton(Pre_1, text="Opción 2", variable=var_1, value=2,command=sel_1).grid(column=0, row=2)
#     GR1 = Radiobutton(Pre_1, text="Opción 3", variable=var_1, value=3,command=sel_1).grid(column=0, row=3)
#     GR1 = Radiobutton(Pre_1, text="Opción 4", variable=var_1, value=4,command=sel_1).grid(column=0, row=4)

#     Pre_2 = Frame(prob, width=0, height=0)
#     Pre_2.grid(column=0, row=2)
#     lbl_3 = Label(Pre_2,text="Segundo parámetro:", font=("Arial Bold", 9))
#     lbl_3.grid(column=0, row=0)
#     var_2 = IntVar()
#     GR2 = Radiobutton(Pre_2, text="Opción 1", variable=var_2, value=1,command=sel_2).grid(column=0, row=1) 
#     GR2 = Radiobutton(Pre_2, text="Opción 2", variable=var_2, value=2,command=sel_2).grid(column=0, row=2)
#     GR2 = Radiobutton(Pre_2, text="Opción 3", variable=var_2, value=3,command=sel_2).grid(column=0, row=3)
#     GR2 = Radiobutton(Pre_2, text="Opción 4", variable=var_2, value=4,command=sel_2).grid(column=0, row=4)

    
#     Pre_3 = Frame(prob, width=0, height=0)
#     Pre_3.grid(column=0, row=3)
#     lbl_4 = Label(Pre_3,text="Tercer parámetro:", font=("Arial Bold", 9))
#     lbl_4.grid(column=0, row=0)
#     var_3 = IntVar()
#     GR3 = Radiobutton(Pre_3, text="Opción 1", variable=var_3, value=1,command=sel_3).grid(column=0, row=1)
#     GR3 = Radiobutton(Pre_3, text="Opción 2", variable=var_3, value=2,command=sel_3).grid(column=0, row=2)
#     GR3 = Radiobutton(Pre_3, text="Opción 3", variable=var_3, value=3,command=sel_3).grid(column=0, row=3)
#     GR3 = Radiobutton(Pre_3, text="Opción 4", variable=var_3, value=4,command=sel_3).grid(column=0, row=4)

#     Pre_4 = Frame(prob, width=0, height=0)
#     Pre_4.grid(column=0, row=4)
#     lbl_11 = Label(Pre_4,text="Cuarto parámetro:", font=("Arial Bold", 9))
#     lbl_11.grid(column=0, row=0)
#     var_7 = IntVar()
#     GR7 = Radiobutton(Pre_4, text="Opción 1", variable=var_7, value=1,command=sel_7).grid(column=0, row=1)
#     GR7 = Radiobutton(Pre_4, text="Opción 2", variable=var_7, value=2,command=sel_7).grid(column=0, row=2)
#     GR7 = Radiobutton(Pre_4, text="Opción 3", variable=var_7, value=3,command=sel_7).grid(column=0, row=3)
#     GR7 = Radiobutton(Pre_4, text="Opción 4", variable=var_7, value=4,command=sel_7).grid(column=0, row=4)


    
#     grav = LabelFrame(window, text="Gravedad", width=0, height=0)
#     grav.grid(column=1, row=1, pady=10)
    
#     Pre_4 = Frame(grav, width=0, height=0)
#     Pre_4.grid(column=0, row=0)
#     lbl_5 = Label(Pre_4,text="Primer parámetro:", font=("Arial Bold", 9))
#     lbl_5.grid(column=0, row=0)
#     var_4 = IntVar()
#     GR4 = Radiobutton(Pre_4, text="Opción 1", variable=var_4, value=1,command=sel_4).grid(column=0, row=1)
#     GR4 = Radiobutton(Pre_4, text="Opción 2", variable=var_4, value=2,command=sel_4).grid(column=0, row=2)
#     GR4 = Radiobutton(Pre_4, text="Opción 3", variable=var_4, value=3,command=sel_4).grid(column=0, row=3)
#     GR4 = Radiobutton(Pre_4, text="Opción 4", variable=var_4, value=4,command=sel_4).grid(column=0, row=4)


#     Pre_5 = Frame(grav, width=0, height=0)
#     Pre_5.grid(column=0, row=2)
#     lbl_6 = Label(Pre_5,text="Segundo parámetro:", font=("Arial Bold", 9))
#     lbl_6.grid(column=0, row=0)
#     var_5 = IntVar()
#     GR5 = Radiobutton(Pre_5, text="Opción 1", variable=var_5, value=1,command=sel_5).grid(column=0, row=1) 
#     GR5 = Radiobutton(Pre_5, text="Opción 2", variable=var_5, value=2,command=sel_5).grid(column=0, row=2)
#     GR5 = Radiobutton(Pre_5, text="Opción 3", variable=var_5, value=3,command=sel_5).grid(column=0, row=3)
#     GR5 = Radiobutton(Pre_5, text="Opción 4", variable=var_5, value=4,command=sel_5).grid(column=0, row=4)
# #    res_2 = Label(Pre_2)
# #    res_2.pack(side='top', anchor = 'w')
    
#     Pre_6 = Frame(grav, width=0, height=0)
#     Pre_6.grid(column=0, row=3)
#     lbl_7 = Label(Pre_6,text="Tercer parámetro:", font=("Arial Bold", 9))
#     lbl_7 .grid(column=0, row=0)
#     var_6 = IntVar()
#     GR6 = Radiobutton(Pre_6, text="Opción 1", variable=var_6, value=1,command=sel_6).grid(column=0, row=1)  
#     GR6 = Radiobutton(Pre_6, text="Opción 2", variable=var_6, value=2,command=sel_6).grid(column=0, row=2)
#     GR6 = Radiobutton(Pre_6, text="Opción 3", variable=var_6, value=3,command=sel_6).grid(column=0, row=3)
#     GR6 = Radiobutton(Pre_6, text="Opción 4", variable=var_6, value=4,command=sel_6).grid(column=0, row=4)
    
#     Pre_8 = Frame(grav, width=0, height=0)
#     Pre_8.grid(column=0, row=4)
#     lbl_12 = Label(Pre_8,text="Cuarto parámetro:", font=("Arial Bold", 9))
#     lbl_12 .grid(column=0, row=0)
#     var_8 = IntVar()
#     GR8 = Radiobutton(Pre_8, text="Opción 1", variable=var_8, value=1,command=sel_8).grid(column=0, row=1)  
#     GR8 = Radiobutton(Pre_8, text="Opción 2", variable=var_8, value=2,command=sel_8).grid(column=0, row=2)
#     GR8 = Radiobutton(Pre_8, text="Opción 3", variable=var_8, value=3,command=sel_8).grid(column=0, row=3)
#     GR8 = Radiobutton(Pre_8, text="Opción 4", variable=var_8, value=4,command=sel_8).grid(column=0, row=4)
    
    
#     resultado_1 = Frame(window, width=0, height=0)
#     resultado_1.grid(column=0, row=2, pady=10)
#     lbl_8 = Label(resultado_1,text="Probabilidad:", font=("Arial Bold", 9))
#     lbl_8 .grid(column=0, row=0)
#     txt_1 = Entry(resultado_1, width=5)
#     txt_1.grid(column=1, row=0)
#     txt_1.insert(0,' N/A')
    
#     resultado_2 = Frame(window, width=0, height=0)
#     resultado_2.grid(column=1, row=2, pady=10)
#     lbl_9 = Label(resultado_2,text="Gravedad:", font=("Arial Bold", 9))
#     lbl_9 .grid(column=0, row=0)
#     txt_2 = Entry(resultado_2, width=5)
#     txt_2.grid(column=1, row=0)
#     txt_2.insert(0,' N/A')
    
#     resultado_3 = Frame(window, width=0, height=0)
#     resultado_3.grid(column=0, row=3, pady=10)
#     lbl_10 = Label(resultado_3,text="Riesgo ambiental:", font=("Arial Bold", 9))
#     lbl_10 .grid(column=0, row=0)
#     txt_3 = Entry(resultado_3, width=5)
#     txt_3.grid(column=1, row=0)
#     txt_3.insert(0,' N/A')
 
# #    botones = Frame(window)
# #    botones.grid(column=1, row=3)
    
#     btn_2 = Button(window, text="Terminar", command=terminar,width=10,height=1)
#     btn_2.grid(column=1, row=4, pady=10)
    
#     btn_3 = Button(window, text="Guardar", command=guardar,width=10,height=1)
#     btn_3.grid(column=0, row=4, pady=10)

mainloop()
 