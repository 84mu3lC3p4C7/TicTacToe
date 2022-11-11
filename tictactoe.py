Board = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]"]
Player = "X"
GameRunning = True
Winner = None
SpaceLeft = 9

Player1 = input("Enter Player1 name: ")
Player2 = input("Enter Player2 name: ")

def PrintBoard(Board):
    print(Board[0] + "│" + Board[1] + "│" + Board[2] + "\n-----------\n" + Board[3] + "│" + Board[4] + "│" + Board[5] + "\n-----------\n" + Board[6] + "│" + Board[7] + "│" + Board[8])

def PTurn():
    global SpaceLeft
    inp = int(input("Position 1-9: "))
    if inp >= 1 and inp <= 9 and Board[inp - 1] == "[1]" or "[2]" or "[3]" or "[4]" or "[5]" or "[6]" or "[7]" or "[8]" or "[9]":
        if Player == "X":
            Board[inp - 1] = "["+"\u001b[35m"+Player+"\u001b[37m"+"]"
        else:
            Board[inp - 1] = "["+"\u001b[32m"+Player+"\u001b[37m"+"]"
        SpaceLeft -= 1

    else:
        print("Position already taken.")

def HCheck(Board):
    global Winner
    if Board[0] == Board[1] == Board[2]:
        Winner = Player
        return True
    elif Board[3] == Board[4] == Board[5]:
        Winner = Player
        return True
    elif Board[6] == Board[7] == Board[8]:
        Winner = Player
        return True

def RCheck(Board):
    global Winner
    if Board[0] == Board[3] == Board[6]:
        Winner = Player
        return True
    elif Board[1] == Board[4] == Board[7]:
        Winner == Player
        return True
    elif Board[2] == Board[5] == Board[8]:
        Winner = Board[2]
        return True

def DCheck(Board):
    global Winner
    if Board[0] == Board[4] == Board[8]:
        Winner = Player
        return True
    elif Board[2] == Board[4] == Board[6]:
        Winner = Player
        return True

def GameT(Board):
    global GameRunning
    if SpaceLeft == 0:
        print(PrintBoard(Board))
        print("Tie!")
        GameRunning = False

def GameW():
    global GameRunning, Player1, Player2
    if HCheck(Board) or RCheck(Board) or DCheck(Board):
        print(PrintBoard(Board))
        if Winner == "O":
            print("The Winner is "+ "\u001b[33m" + Player2 + "\u001b[37m" + ".")
        else:
            print("The Winner is "+ "\u001b[33m" + Player1 + "\u001b[37m" + ".")
        GameRunning = False

def PSwitch():
    global Player
    if Player == "X":
        Player = "O"
    else:
        Player = "X"

while GameRunning:
    PrintBoard(Board)
    PTurn()
    GameW()
    PSwitch()
    GameT(Board)