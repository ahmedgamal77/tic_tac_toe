from graphics import *
import random 
import time

win = GraphWin("TIC TAC TOE", 800,700 )
win.setBackground("white")

def getname():
    
  
    message = Text(Point(400,250), "Please Enter Your Name")
    message.setSize(30)

    message.draw(win)
    
    textEntry = Entry(Point(400,300),15)
    textEntry.setSize(25)
    textEntry.setFill("white")
   
    textEntry.draw(win)


    message1 = Text(Point(400,400), "ENTER")
    message1.setSize(30)

    message1.draw(win)
    
    ok = Rectangle(Point(325,375), Point(475, 425))
    message1.setFill("red")
   
    ok.draw(win)
    win.getMouse()
    playerName = textEntry.getText()

    


    ll = ok.getP1()  # assume p1 is ll (lower left)
    ur = ok.getP2()  # assume p2 is ur (upper right)

    while True :
        point = win.getMouse()

        if(ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()):
            message.undraw()
            textEntry.undraw()
            ok.undraw()
            message1.undraw()
            break 

    return playerName 

def playerLetter():
    message = Text(Point(400,250), "Choose your Letter")
    message.setSize(30)

    message.draw(win)
    
    

    messagex = Text(Point(250,400), "X")
    messagex.setSize(35)

    messagex.draw(win)
    
    x = Rectangle(Point(200,350), Point(300, 450))
    messagex.setFill("red")
   
    x.draw(win)

    messageo = Text(Point(550,400), "O")
    messageo.setSize(35)
    messageo.draw(win)
    
    o = Rectangle(Point(500,350), Point(600, 450))
    messageo.setFill("blue")
   
    o.draw(win)
    llo = o.getP1()  # assume p1 is ll (lower left)
    uro = o.getP2()  # assume p2 is ur (upper right)
    llx = x.getP1()  # assume p1 is ll (lower left)
    urx = x.getP2()  # assume p2 is ur (upper right)

    
    while True :
        point = win.getMouse()

        if(llo.getX() < point.getX() < uro.getX() and llo.getY() < point.getY() < uro.getY()):
            
            message.undraw()
            messageo.undraw()
            messagex.undraw()
            o.undraw()
            x.undraw()
            return ['O', 'X']
             
        elif(llx.getX() < point.getX() < urx.getX() and llx.getY() < point.getY() < urx.getY()):
            
            message.undraw()
            messageo.undraw()
            messagex.undraw()
            o.undraw()
            x.undraw()
            return ['X', 'O']
             

    
    
def scores(name,nscore,cscore,le):
    color1="black"
    color2="black"
    if le=="X":
        color1="red"
        color2="blue"
    elif le=="O":
        color1="blue"
        color2="red"
    
    message1=Text(Point(700,100),name+" :")
    message2=Text(Point(700,200),nscore)
    message3=Text(Point(700,400),"Computer :")
    message4=Text(Point (700,500),cscore)
    message1.setSize(30)
    message2.setSize(30)
    message3.setSize(30)
    message4.setSize(30)
    message1.setFill(color1)
    message2.setFill(color1)
    message3.setFill(color2)
    message4.setFill(color2)
    message1.draw(win)
    message2.draw(win)
    message3.draw(win)
    message4.draw(win)






    


def boardready(name):
    
    pointc=Point(25,300)
    pointd=Point(575,300)
    pointe=Point(25,500)
    pointf=Point(575,500)
    lineb=Line(pointc,pointd)
    linec=Line(pointe,pointf)
    pointf=Point(200,100)
    pointg=Point(200,675)
    pointh=Point(400,100)
    Pointi=Point(400,675)
    linee=Line(pointf,pointg)
    linef=Line(pointh,Pointi)

    

    lineb.setWidth(3)
    linec.setWidth(3)
    linee.setWidth(3)
    linef.setWidth(3)
    lineb.setFill("orange")
    linec.setFill("orange")
    linee.setFill("orange")
    linef.setFill("orange")
    


    lineb.draw(win)
    linec.draw(win)
    linee.draw(win)
    linef.draw(win)
    message = Text(Point(300,50), "Hello "+name)
    message.setSize(30)
    message.setFill("orange")

    message.draw(win)


#name=getname()
#Letter=playerLetter()
#boardready(name)


def whoGoesFirst():

      # Randomly choose the player who goes first.

    if random.randint(0, 1) == 0:

        return 'computer'

    else:

        return 'player'

def playAgain():

      # This function returns True if the player wants to play again, otherwise it returns False.

    

    
    message = Text(Point(400,250), "Do you want to play again ??")
    message.setSize(30)

    message.draw(win)
    
    

    messagex = Text(Point(250,400), "YES")
    messagex.setSize(30)

    messagex.draw(win)
    
    x = Rectangle(Point(175,350), Point(325, 450))
    messagex.setFill("Green")
   
    x.draw(win)

    messageo = Text(Point(550,400), "NO")
    messageo.setSize(30)
    messageo.draw(win)
    
    o = Rectangle(Point(475,350), Point(625, 450))
    messageo.setFill("Red")
   
    o.draw(win)
    llo = o.getP1()  # assume p1 is ll (lower left)
    uro = o.getP2()  # assume p2 is ur (upper right)
    llx = x.getP1()  # assume p1 is ll (lower left)
    urx = x.getP2()  # assume p2 is ur (upper right)

    
    while True :
        point = win.getMouse()

        if(llo.getX() < point.getX() < uro.getX() and llo.getY() < point.getY() < uro.getY()):
            
            message.undraw()
            messageo.undraw()
            messagex.undraw()
            o.undraw()
            x.undraw()
            return False
             
        elif(llx.getX() < point.getX() < urx.getX() and llx.getY() < point.getY() < urx.getY()):
            
            message.undraw()
            messageo.undraw()
            messagex.undraw()
            o.undraw()
            x.undraw()
            return True


def makeMove(board, letter, move):

    board[move] = letter

def changecolor(bo,le):
    color="black"
    if le=="X":
        color="red"
    elif le=="O":
        color="blue"
    if bo[7] == le and bo[8] == le and bo[9] == le :
        pos1=7
        pos2=8
        pos3=9
    elif bo[4] == le and bo[5] == le and bo[6] == le :
        pos1=4
        pos2=5
        pos3=6
    elif bo[1] == le and bo[2] == le and bo[3] == le :
        pos1=1
        pos2=2
        pos3=3
        
    elif bo[7] == le and bo[4] == le and bo[1] == le :
        pos1=7
        pos2=4
        pos3=1
        

    elif bo[8] == le and bo[5] == le and bo[2] == le :
        pos1=8
        pos2=5
        pos3=2
        

    elif bo[9] == le and bo[6] == le and bo[3] == le : 
        pos1=9
        pos2=6
        pos3=3
        
    elif bo[7] == le and bo[5] == le and bo[3] == le :
        pos1=7
        pos2=5
        pos3=3
        

    elif bo[9] == le and bo[5] == le and bo[1] == le : 
        pos1=9
        pos2=5
        pos3=1



    place1=Point(100,600)
    place2=Point(300,600)
    place3=Point(500,600)
    place4=Point(100,400)
    place5=Point(300,400)
    place6=Point(500,400)
    place7=Point(100,200)
    place8=Point(300,200)
    place9=Point(500,200)
    places={1:place1,2:place2,3:place3,4:place4,5:place5,6:place6,7:place7,8:place8,9:place9}
    message1 = Text(places[pos1],le)
    message1.setSize(30)
    message2 = Text(places[pos2],le)
    message2.setSize(30)
    message3 = Text(places[pos3],le)
    message3.setSize(30)
    message1.setFill("black")
    message2.setFill("black")
    message3.setFill("black")
    
    message1.draw(win)
    message2.draw(win)
    message3.draw(win)
    time.sleep(1)
    message1.setFill(color)
    message2.setFill(color)
    message3.setFill(color)
    time.sleep(1)
    message1.setFill("black")
    message2.setFill("black")
    message3.setFill("black")
    
    time.sleep(1)
    message1.setFill(color)
    message2.setFill(color)
    message3.setFill(color)
    
    time.sleep(1)
    message1.setFill("black")
    message2.setFill("black")
    message3.setFill("black")
    
    time.sleep(1)
    message1.setFill(color)
    message2.setFill(color)
    message3.setFill(color)
    


def isWinner(bo, le):

      # Given a board and a player’s letter, this function returns True if that player has won.

      # We use bo instead of board and le instead of letter so we don’t have to type as much.

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top

    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle

    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom

    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side

    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle

    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side

    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal

    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def getBoardCopy(board):

      # Make a duplicate of the board list and return it the duplicate.

    dupeBoard = []

 

    for i in board:

        dupeBoard.append(i)

 

    return dupeBoard


def isSpaceFree(board, move):

      # Return true if the passed move is free on the passed board.

    return board[move] == ' '




def getPlayerMove(board):

    # Let the player type in their move.


    point1l=Point(0,700)
    point1u=Point(200,500)
    point2l=Point(200,700)
    point2u=Point(400,500)
    point3l=Point(400,700)
    point3u=Point(600,500)
    point4l=Point(0,500)
    point4u=Point(200,300)
    point5l=Point(200,500)
    point5u=Point(400,300)
    point6l=Point(400,500)
    point6u=Point(600,300)
    point7l=Point(0,300)
    point7u=Point(200,100)
    point8l=Point(200,300)
    point8u=Point(400,100)
    point9l=Point(400,300)
    point9u=Point(600,100)


    while True :
        point = win.getMouse()
        
        

        if(point1l.getX() < point.getX() < point1u.getX() and point1u.getY() < point.getY() < point1l.getY()):
            
           if isSpaceFree(board, 1):
               
               return 1 

             
        elif(point2l.getX() < point.getX() < point2u.getX() and point2u.getY() < point.getY() < point2l.getY()):
            
           if isSpaceFree(board, 2):
               
               return 2
        elif(point3l.getX() < point.getX() < point3u.getX() and point3u.getY() < point.getY() < point3l.getY()):
            
           if isSpaceFree(board, 3):
               return 3         
        elif(point4l.getX() < point.getX() < point4u.getX() and point4u.getY() < point.getY() < point4l.getY()):
            
           if isSpaceFree(board, 4):
               return 4 
        elif(point5l.getX() < point.getX() < point5u.getX() and point5u.getY() < point.getY() < point5l.getY()):
            
           if isSpaceFree(board, 5):
               return 5 
        elif(point6l.getX() < point.getX() < point6u.getX() and point6u.getY() < point.getY() < point6l.getY()):
            
           if isSpaceFree(board, 6):
               return 6 
        elif(point7l.getX() < point.getX() < point7u.getX() and point7u.getY() < point.getY() < point7l.getY()):
            
           if isSpaceFree(board, 7):
               return 7 
        elif(point8l.getX() < point.getX() < point8u.getX() and point8u.getY() < point.getY() < point8l.getY()):
            
           if isSpaceFree(board, 8):
               return 8 
        elif(point9l.getX() < point.getX() < point9u.getX() and point9u.getY() < point.getY() < point9l.getY()):
            
           if isSpaceFree(board, 9):
               return 9               
           



def chooseRandomMoveFromList(board, movesList):

      # Returns a valid move from the passed list on the passed board.

      # Returns None if there is no valid move.

    possibleMoves = []

    for i in movesList:

        if isSpaceFree(board, i):

            possibleMoves.append(i)

 

    if len(possibleMoves) != 0:

        return random.choice(possibleMoves)

    else:

        return None






def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.

    for i in range(1, 10):

        if isSpaceFree(board, i):

            return False

    return True

def drawBoard(board):

    index=0
    for let in board:
        
        if let !=' ':
            drawletter(let,index)
        index=index+1    
    
   
    
def drawletter(let,index):
    color="black"
    if let=="X":
        color="red"
    elif let=="O":
        color="blue"    
    place1=Point(100,600)
    place2=Point(300,600)
    place3=Point(500,600)
    place4=Point(100,400)
    place5=Point(300,400)
    place6=Point(500,400)
    place7=Point(100,200)
    place8=Point(300,200)
    place9=Point(500,200)
    places={1:place1,2:place2,3:place3,4:place4,5:place5,6:place6,7:place7,8:place8,9:place9}
    message = Text(places[index],let)
    message.setSize(30)
    message.setFill(color)

    message.draw(win)

def disturn(turn):
    sen='The ' + turn + ' will go first.'
    message = Text(Point(400,300),sen)
    message.setSize(30)

    message.draw(win)
    message1 = Text(Point(400,400), "START")
    message1.setSize(30)

    message1.draw(win)
    
    ok = Rectangle(Point(325,375), Point(475, 425))
    message1.setFill("red")
   
    ok.draw(win)
    
    

    


    ll = ok.getP1()  # assume p1 is ll (lower left)
    ur = ok.getP2()  # assume p2 is ur (upper right)

    while True :
        point = win.getMouse()

        if(ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()):
            message.undraw()
            
            ok.undraw()
            message1.undraw()
            break 

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def winner(name):
    message=Text(Point(400,300),name)
    message.setSize(15)
    message.draw(win)
    
    message1 = Text(Point(400,400), "OKAY")
    message1.setSize(30)

    
    
    ok = Rectangle(Point(325,375), Point(475, 425))
    message1.setFill("red")
    ok.setFill("black")
    ok.draw(win)
    
    message1.draw(win)

    


    ll = ok.getP1()  # assume p1 is ll (lower left)
    ur = ok.getP2()  # assume p2 is ur (upper right)

    while True :
        point = win.getMouse()

        if(ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()):
            message.undraw()
            
            ok.undraw()
            message1.undraw()
            break 


#===========================================
def bestmove(board,letter):
    bestscore=-99999
    for i in range (1,10):
        if board[i]==' ':
            board[i]=letter
            score =minimax(board,0,False)
            board[i]=' '
            if score > bestscore:
                bestscore= score
                move = i

    return move            


def minimax(board,depth,isMaximizing):
    
    sc={computerLetter:1,playerLetter:-1,'t':0}   
    if isWinner(board,playerLetter):
        return sc[playerLetter]
    elif isWinner(board,computerLetter):
        return sc[computerLetter] 
    elif isBoardFull(board):
        return sc['t']    

    if isMaximizing:
        bestscore=-9999999
        for i in range (1,10):
            if board[i]==' ':
                board[i]=computerLetter
                score=minimax(board,depth+1,False)
                board[i]=' '
                bestscore=max(score,bestscore)    
        return bestscore
    else:
          
        bestscore=9999999
        for i in range(1,10):
             if board[i]==' ':
                board[i]=playerLetter
                score=minimax(board,depth+1,True)
                board[i]=' '
                bestscore=min(score,bestscore)    
        return bestscore             


#================================================


    


name=getname()
playerLetter, computerLetter = playerLetter()
nscore=0
cscore=0
while True:

     # Reset the board

    theBoard = [' '] * 10
    
    
    
    turn = whoGoesFirst()

    disturn(turn)


    gameIsPlaying = True
    boardready(name)

    scores(name,nscore,cscore,playerLetter)
    while gameIsPlaying:

        if turn == 'player':

             # Player’s turn.

            drawBoard(theBoard)
            

            move = getPlayerMove(theBoard)

            makeMove(theBoard, playerLetter, move)



            if isWinner(theBoard, playerLetter):

                drawBoard(theBoard)
                changecolor(theBoard,playerLetter)
                nscore=+1
                time.sleep(2)
                clear(win)
                winner('Good job! You have won the game')
                

                gameIsPlaying = False

            else:

                if isBoardFull(theBoard):

                    drawBoard(theBoard)
                    time.sleep(2)
                    clear(win)
                    winner('The game is a tie!')
                    

                    break

                else:

                    turn = 'computer'



        else:

             # Computer’s turn.
            #the function that will change into minimax 
            move = bestmove(theBoard, computerLetter)
            #============================
            makeMove(theBoard, computerLetter, move)
            


            if isWinner(theBoard, computerLetter):

                drawBoard(theBoard)
                changecolor(theBoard,computerLetter)
                cscore=+1
                time.sleep(2)
                clear(win)
                winner('The computer has beaten you! You lose.')
                     
                

                gameIsPlaying = False

            else:

                if isBoardFull(theBoard):

                    drawBoard(theBoard)
                    time.sleep(2)
                    clear(win)
                    winner('The game is a tie!')
                    

                    break

                else:

                    turn = 'player'


    clear(win)
    if not playAgain():

        break    
    clear(win)
    


