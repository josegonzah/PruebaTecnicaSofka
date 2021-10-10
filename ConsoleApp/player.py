import csv
class Player:
    def __init__(self):
        #Player object that has relevant info on player and handles conection to csv file
        #Note that this is not an efficient, scalable way if the users database is a large file
        #it consumes resources in the connection. Is better to explore other options

        self.name = ""
        self.score = 0
        self.round = 1
        self.playerDB = 'playersDB.csv'

    def setNewPlayer(self, userName):
        ##Sets new player with the info that is validated, returns True if is a valid
        #userName and False if it is not

        self.name = userName
        return self.checkNewPlayer(userName)

    def checkNewPlayer(self, userName):
        #Checks if the userName is available to the user, it has to be unique

        with open(self.playerDB) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    print(row)
                    if(row[0] == userName):
                        csv_file.close()
                        return False
                    line_count += 1
            csv_file.close()
            return True
    
    def saveNewPlayer(self, userName):
        #Stores data of a newly created user as a row in the csv file

        newUserData = [userName, '0', '1']
        with open(self.playerDB, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(newUserData)
            csv_file.close()
    
    def savePlayerInfo(self, usernaName, score, round):
        #Updates the user csv file with the new information

        newData = [usernaName, score, round]
        with open(self.playerDB) as inf:
            reader = csv.reader(inf.readlines())
        with open(self.playerDB, 'w', newline='') as outf:
            writer = csv.writer(outf)
            for line in reader:
                if(line[0] == usernaName):
                    writer.writerow(newData)
                    break
                else:
                    writer.writerow(line)
            writer.writerows(reader)

    def loadOldPlayer(self, userName):
        #Checks if a registeredd player is in fact there and loads the data into the player 
        #object to be handled

        with open(self.playerDB) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    if(row[0] == userName):
                        self.name = userName
                        self.score = int(row[1])
                        self.round = int(row[2])
                        csv_file.close()
                        return True
                    line_count += 1
            csv_file.close()
            if(self.name == ''):
                return False
                    
                        



            

    

