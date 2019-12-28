def createextendedmatrix(board):
    '''create matrix of same row size but column size of (old column + 2*row size)
    and place the board in the middle of new matrix '''

    oldcolumnlength = len(board[0].returnlist())
    oldrowlength = len(board)

    newrowsize = oldrowlength + 2 * oldcolumnlength

    boardinlistoflistform = []

    for column in range(oldrowlength):
        boardinlistoflistform.append(board[column].returnlist()) #create the board in list of list form
                                                                 #because board is a list of stack form

    columnofnulls = ["null" for x in range(oldcolumnlength)]   #the empty columns surrounding the board

    listoflist = []
    for column in range(newrowsize):
        listoflist.append(columnofnulls)
    extendedmatrix = np.array(listoflist)

    extendedmatrix[oldcolumnlength:oldcolumnlength+oldrowlength] = boardinlistoflistform #place the old matrix at the centre

    return extendedmatrix


def createnewboardandcheckdiagonal(board): #check multiple diagonals
    '''create an longer version of the board and place the old board at the middle of the board
    '''

    extendedmatrix = createextendedmatrix(board)
    won, winner, winningposition = checkdiagonaltotheright(extendedmatrix)
    if won == False: #check diagonal in reverse direction
        won, winner, winningposition = checkdiagnoaltotheleft(extendedmatrix)
    #check the diagonals starting from 0,0 of new board to oldboard row + column
    #do this again but reverse direction

def checkdiagonaltotheright(extendedmatrix): #check 1 diagonal
    '''checkdiagonals starting from down left to top right'''

    winningposition = ["none"]

    previousmarker = extendedmatrix[0][0] #marker at left most end
    rowcolumn = len(extendedmatrix)-len(extendedmatrix[0])-1 #row and collumn have same index
    runlength = 1


    for shift in range(rowcolumn): #shift the diagonal check by this much
        for i in range(0,len(extendedmatrix[0])):

            if previousmarker == extendedmatrix[i+shift][i] and previousmarker != "null" and previousmarker != "0":
                runlength += 1
                print("diagonally + 1", previousmarker, runlength)

            else:            #not matching
                previousmarker = extendedmatrix[i+shift][i]
                runlength = 1 #reset counter


            if runlength >= 4:
                print("won diagonally to the right")
                winner = previousmarker
                winningposition = ["torightdiagonal", i, shift-len(extendedmatrix[0])]
                return True, winner, winningposition
    return False, "nobody", winningposition
