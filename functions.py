from random import shuffle
def displayQuestion(Question):
    print(str(Question[0])+"\n")
    options = Question[1:]
    options = shuffle(options)
    for i in options:
        print(i + "\n")
    userInput = input("Write the option you want")

    return userInput
    
