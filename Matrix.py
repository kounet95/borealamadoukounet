import Array2D

class Matrix:
    def __init__(self, l=0, c=0):
        self.nRows = l
        self.nCols = c
        self.values = Array2D.Array2D(l, c)
    def nRows(self):
        nombredeLigne = self.nRows
        return nombredeLigne
    def nCols(sel):
        nombredeColone = sel.nCols
        return nombredeColone
    
    def print(self):
        self.values.print()

m = Matrix(4, 3)
m.print()
print("********************")
print("le nombre de ligne est:", m.nRows)  
print("********************")
print("le nombre de colone est:", m.nCols)  