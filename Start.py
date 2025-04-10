import numpy as np
import random
import Move

# funzione che restituisce la matrice
def getMatrice():
    # stringa che contiene i caratteri per creazione matrice -: strada normale 5: ostacolo
    str = "-5" 
    # peso dei caratteri per la generazione matrice
    pesi = [0.85, 0.15]
    # creazione matrice pesta con caratteri dati
    matrice = random.choices(str, pesi, k=100)
    # reshape per prendere l'array creato randomicamente per poi renderlo una matrice vera e propria
    matrice = np.reshape(matrice, (10,10))
    return matrice

# funzione che restituisce coordinate iniziali del rover nella mappa
def getX_Y(matrice):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    while matrice[y][x] == "5":
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    matrice[y][x] = "1"
    return x, y

# funzione che restituisce orientamento iniziale
def getOrient():
    # richiesta input di orientamento
    orientation = " "
    while orientation != "N" and orientation != "W" and orientation != "E" and orientation != "S":
        orientation = input("dammi L'orintamento (N, S, E, W): ").upper()
    return orientation    

# funzione che restituisce i comandi di movimento
def getCommands():     
    comandi = input("dammi una stringa di comandi comandi(f, b, l, r): ").lower()
    # join usato in maniera tale come filtro per prendere dalla sringa data in input solo i caratteri che mi interessano
    comandi = "".join(s for s in comandi if s in 'fblr')
    print(comandi)
    return comandi

orientation = getOrient()
matrice = getMatrice()
commands = getCommands()
x, y = getX_Y(matrice)
lenCom = len(commands)

# faccio partire il programma creando l'oggetto Move
start = Move.Movement(matrice, orientation, x, y, commands, lenCom)
start.Run()                 
