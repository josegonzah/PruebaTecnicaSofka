# PruebaTecnicaSofka 25 Questions
<h2>By Jose David Gonzalez Henao</h2>
<h3>Instructions:</h3>
<p>25 Questions is a game that will test your knowledge in differnt areas. The game has two modes of play:
Console and Tkinter app, in the console app you will have to run it and it will request your mode of play. If you 
already have a created user you should provide the exact name that you saved your previous game otherwise the game will
not run. Whereas if you use the new player option you the username provided should not be already on the database otherwise
the game will not run. When you start the game the game throws you a random related to your level question with 4 options to get
the correct option you should write exactly the same line that you think is correct. If you fail you restart the test,
if you get the correct answer you advance. This process is repeated until you loose or until you answer 5 consecutive questions.
The other mode of play is in a Tkinter app. When you run it it will prompt a window requesting you the same info as in the console app
this app has the added filter that it requires the username to not have a comma so it doesn't interfere with the csv file. Then after
the user is loged in succesfully the program prompts a question with 4 options, the user should select the option by clicking it and then confirm
the selection by pushing the button "Submit", if the answer is correct you advence if it is not the game will show a game over
window and you loose all the progress. The game finishes when you answer 5 questions in a row. In both cases the game automathicly saves
if you get an answer right so if you close the window it will pick up right where you left. Meanwhile if you fail all your score is lost and
you have to restart the game<br></p>

<h3>Instructions to run the game</h3>
<p>The game was designe in python3 so to run the console app you just need to open the file main.py using python like this: python main.py
in the console app directory.
To run the tkinter app you also need the tkinter library, to install it you can use pip like this:
python python -m pip install --upgrade pip python -m pip install Pillow python -m pip install tk. To install python 3 you can install it directly from the python.org website.
To run the desktop app just type python main.py inside the directory TKinterApp

