'''
TicTactoe:

    Board
    N
    -> printBoard()
    -> input(i,j, value)
    -> calulateEndState()

Player:
    side:
    - play()
'''

import random

class TicTacToe:

    def __init__(self, N):
        self.N = N
        self.board = []
        self._constructboard(N)

    def _constructboard(self, N):
        for i in range(N):
            temp = []
            for j in range(N):
                temp.append([])
            self.board.append(temp)

    def input(self, i, j ,value):
        if (value != '0' and value != 'x') or (i < 0 or i >= self.N) or (j < 0 or j >= self.N) or self.board[i][j] != []:
            print("Invalid Input Choice")
            return False

        self.board[i][j] = value

    def printBoard(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.board[i][j], end= "\t")
                if j  < self.N - 1:
                    print(" | ", end= "\t")
            print("")

    def _checkDiagonals(self):
        # Checking the first diagonal
        value = self.board[0][0]
        firstDiagonalCheck = True
        for i in range(1, self.N):
            if self.board[i][i] != value or value == []:
                firstDiagonalCheck = False

        secondDiagonalCheck = True
        value = self.board[0][self.N - 1]
        for i in range(0, self.N):
            if self.board[i][self.N - i - 1] != value or value == []:
                secondDiagonalCheck = False

        return firstDiagonalCheck or secondDiagonalCheck

    def _checkRows(self):
        rowCheck = True
        for i in range(0, self.N):
            value = self.board[i][0]
            for j in range(1,  self.N):
                if self.board[i][j] != value or value == []:
                    rowCheck = False
            if rowCheck == True:
                return True
            elif i < self.N - 1:
                rowCheck = True
        return rowCheck

    def _checkColumns(self):
        colCheck = True
        for j in range(0, self.N):
            value = self.board[0][j]
            for i in range(1, self.N):
                if self.board[i][j] != value or value == []:
                    colCheck = False
            if colCheck == True:
                return True
            elif j < self.N - 1:
                colCheck = True
        return colCheck

    def isWin(self):
        return self._checkRows() or self._checkColumns() or self._checkDiagonals()

    def endTurn(self):
        self.printBoard()
        return self.isWin()

class Player:

    def __init__(self, sign):
        self.sign = sign

    def getSign(self):
        return self.sign


print("Enter Board Size")
N = int(input())

board = TicTacToe(N)

turnCount = 0

p1 = Player('x')
p2 = Player('0')

turn = random.choice([True, False])

isWon = False

while turnCount < N * N:
    if turn == True:
        player = 'p1'
        sign = p1.getSign()
    else:
        player = 'p2'
        sign = p2.getSign()
    print("Player: ", player, " turn")
    position = input().split()
    i, j = int(position[0]), int(position[1])
    board.input(i, j, sign)
    isWon = board.endTurn()
    if isWon:
        print("Player: ", player, " has won")
        break
    turn = not turn
    turnCount += 1

if not isWon:
    print("It'a Draw!!!")