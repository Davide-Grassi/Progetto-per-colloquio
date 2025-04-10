class Movement:

    # inizializzazione delle variabili
    def __init__(self, matrice, orientation, x, y, comandi, lenCom):
        self.matrice = matrice
        self.orientation = orientation
        self.x = x
        self.y = y
        self.comandi = comandi
        self.lenCom = lenCom
    
    # Funzione di stampa self.matrice
    def Stamp(self):
        for row in self.matrice:
            for column in row:
                if column == "1":
                    match self.orientation:
                        case "E": 
                            print(chr(16), end = ' ')
                        case "W": 
                            print(chr(17), end = ' ')
                        case "S": 
                            print(chr(31), end = ' ')
                        case "N": 
                            print(chr(30), end = ' ')
                elif column == "5":
                    print(chr(216), end = ' ')
                else:
                    print(column, end = ' ')    
            print("")
        print("")

    #  Movimento con orientamento a Sud  
    def SudMov(self):

        self.Stamp()
        
        while self.lenCom > 0:
            # controllo indicazione
            if self.comandi[-self.lenCom] == "f":
                # controllo per wrap shape per contare 1: colonne 0: righe
                if self.matrice.shape[0] == self.y+1:
                    if self.matrice[0][self.x] == "5":
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[0][self.x] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.y = 0
                else:
                    if self.matrice[self.y+1][self.x] == "5":
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[self.y+1][self.x] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.y += 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "b":
                if self.matrice[self.y-1][self.x] == "5":
                    self.lenCom = 0
                    print("è stato incontrato un ostacolo")
                    break
                else:
                    self.matrice[self.y-1][self.x] = self.matrice[self.y][self.x]
                    self.matrice[self.y][self.x] = "-"
                    self.Stamp()
                    self.y -= 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "l":
                self.orientation = "E"
                self.lenCom -= 1
                return
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "r":
                self.orientation = "W"
                self.lenCom -= 1
                return
            self.lenCom -= 1

    #  Movimento con orientamento a Est 
    def EstMov(self):

        self.Stamp()
        
        while self.lenCom > 0:
            if self.comandi[-self.lenCom] == "f":
                # controllo per wrap shape 1 colonne 0 righe
                if self.matrice.shape[1] == self.x+1:
                    if self.matrice[self.y][0] == "5":
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[self.y][0] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.x = 0
                else:
                    if self.matrice[self.y][self.x+1] == "5":
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[self.y][self.x+1] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.x += 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "b":
                if self.matrice[self.y][self.x-1] == "5":
                    self.lenCom = 0
                    print("è stato incontrato un ostacolo")
                    break
                else:
                    self.matrice[self.y][self.x-1] = self.matrice[self.y][self.x]
                    self.matrice[self.y][self.x] = "-"
                    self.Stamp()
                    self.x -= 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "l":
                self.orientation = "N"
                self.lenCom -= 1
                return
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "r":
                self.orientation = "S"
                self.lenCom -= 1
                return
            self.lenCom -= 1

    #  Movimento con orientamento a Nord             
    def NordMov(self):

        self.Stamp()
        
        while self.lenCom > 0:
            # controllo indicazione
            if self.comandi[-self.lenCom] == "f":
                if self.matrice[self.y-1][self.x] == "5":
                    self.lenCom = 0
                    print("è stato incontrato un ostacolo")
                    break
                else:
                    self.matrice[self.y-1][self.x] = self.matrice[self.y][self.x]
                    self.matrice[self.y][self.x] = "-"
                    self.Stamp()
                    self.y -= 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "b":
                # controllo per wrap shape 1 colonne 0 righe
                if self.matrice.shape[0] == self.y+1:
                    if self.matrice[0][self.x] == "5":
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[0][self.x] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.y = 0
                else:
                    if self.matrice[self.y+1][self.x] == "5": 
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[self.y+1][self.x] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.y += 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "l":
                self.orientation = "W"
                self.lenCom -= 1
                return
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "r":
                self.orientation = "E"
                self.lenCom -= 1
                return
            self.lenCom -= 1
    
    #  Movimento con orientamento a West       
    def WestMov(self):
        
        self.Stamp()
        
        while self.lenCom > 0:
            # controllo indicazione
            if self.comandi[-self.lenCom] == "f":
                if self.matrice[self.y][self.x-1] == "5":
                    self.lenCom = 0
                    print("è stato incontrato un ostacolo")
                    break
                else:
                    self.matrice[self.y][self.x-1] = self.matrice[self.y][self.x]
                    self.matrice[self.y][self.x] = "-"
                    self.Stamp()
                    self.x -= 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "b":
                # controllo per wrap shape 1 colonne 0 righe
                if self.matrice.shape[1] == self.x+1:
                    if self.matrice[self.y][0] == "5":
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[self.y][0] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.x = 0
                else:
                    if self.matrice[self.y][self.x+1] == "5":
                        self.lenCom = 0
                        print("è stato incontrato un ostacolo")
                        break
                    else:
                        self.matrice[self.y][self.x+1] = self.matrice[self.y][self.x]
                        self.matrice[self.y][self.x] = "-"
                        self.Stamp()
                        self.x += 1
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "l":
                self.orientation = "S"
                self.lenCom -= 1
                return
            # controllo indicazione
            elif self.comandi[-self.lenCom] == "r":
                self.orientation = "N"
                self.lenCom -= 1
                return
            self.lenCom -= 1    

    # funzione di Partenza           
    def Run(self):
        while self.lenCom > 0:
            if self.orientation == "S":
                self.SudMov()
            elif self.orientation == "E":
                self.EstMov()
            elif self.orientation == "N":
                self.NordMov()
            elif self.orientation == "W":
                self.WestMov()
        print("Serie di comandi finita")