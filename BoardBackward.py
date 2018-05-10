from Board import Board

class BoardBackward(Board):
    MNOOZNIK_WYGRANEJ = 5
    moves = []

    def __init(self, size, player1=0,player2=0,board=None):
        super.__init__(size, player1, player2,board)

    def moveBackward(self, row, columm, color):
        points, warunek = self.move(row, columm, color)
        if points == 0:
            myRow = self.getRowZeroPoints(row, self.board)
            myColumn = self.getColumnZeroPoints(columm, self.board)
            list1, diagonalFirst = self.getDiagonalFirst(self.board, row, columm)
            list2, diagonalSecond = self.getDiagonalSecond(self.board, row, columm)
            if len(myRow) % 2 == 0 and len(myRow) != 0:
                points += (self.board[row] == color).sum()
            if len(myColumn) % 2 == 0 and len(myColumn) != 0:
                points += (self.board[:, columm] == color).sum()
            if len(diagonalFirst) % 2 == 0 and len(diagonalFirst) != 0:
                 points += list(list1).count(color)
            if len(diagonalSecond)%2 == 0 and len(diagonalSecond) != 0:
                points += list(list2).count(color)
        else:
            points = points**3
        if warunek:
            self.moves.append((row, columm, color, points))

    def getMoves(self):
        _, positions = self.getAllDiagonals(self.board)
        columnRows = self.getRowsColumnsPoints(self.board)
        filtr = list(filter(lambda p: len(p) % 2 == 1, positions + columnRows))
        procenty = [round(i*0.025,2) for i in range(1,101)]
        for i in procenty:
            filtr2 = list(filter(lambda p: len(p) <= self.size * i, filtr))
            filtr2 = [i[0] for i in filtr2]
            mySet = set(filtr2)
            lista2 = list(mySet)
            if len(lista2) != 0:
                return lista2
        filtr = [i[0] for i in filtr]
        mySet = set(filtr)
        lista = list(mySet)
        return lista

    def back(self):
        if len(self.moves) > 0:
            move = self.moves.pop()
            self.board[move[0],move[1]] = 0
            if self.player1Color == move[2]:
                self.player1 -= move[3]
            else:
                self.player2 -= move[3]