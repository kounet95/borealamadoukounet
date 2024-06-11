import Array2D

class Matrix:
    def __init__(self, l, c):
        self.nRows = l
        self.nCols = c
        self.values = Array2D.Array2D[l,c]
    def nRows(self):
        nombredeLigne = self.nRows
        return nombredeLigne
    def nCols(sel):
        nombredeColone = sel.nCols
        return nombredeColone
    
    def setItem(self, row, col):
        if row >= self.nRows or col >= self.nCols:
            raise IndexError("Les indices de ligne et de colonne doivent être dans les limites de la matrice")
        valSet = self.values[row][col]
        return valSet
    def getItem(self,row, col, value):
        if row >= self.nRows or col >= self.nCols:
            raise IndexError("Les indices de ligne et de colonne doivent être dans les limites de la matrice")
        if 0 <= row < self.nRows and 0 <= col < self.nCols:
           newV = self.values[row][col] = value
        return newV
    def scaleBy(self,value):
         for i in range(self.nRows):
            for j in range(self.nCols):
                self.values[i][j] *= value

    #def print(self):self.values.print()
    def display(self):
        for row in self.values:
            print(row)
    def transpose(self):
        transMatrice = [[self.values[j][i] for j in range(self.nRows)] for i in range(self.nCols)]
        self.values = transMatrice
        self.nRows, self.nCols = self.nCols, self.nRows
        return transMatrice
    def add(self, other):
        if self.nRows != other.nRows or self.nCols != other.nCols:
            print("Dimensions n'est pas compatible")
            return None
        result = Matrix(self.nRows, self.nCols)
        for i in range(self.nRows):
            for j in range(self.nCols):
                result.values[i][j] = self.values[i][j] + other.values[i][j]
        return result
    def add(self, other):
        if self.nRows != other.nRows or self.nCols != other.nCols:
            print("Dimensions n'est pas compatible")
            return None
        result = Matrix(self.nRows, self.nCols)
        for i in range(self.nRows):
            for j in range(self.nCols):
                result.values[i][j] = self.values[i][j] - other.values[i][j]
        return result
    def multiply(self, other):
        if self.nCols != other.nRows:
            print("Dimensions n'est pas compatible.")
            return None

        result = Matrix(self.nRows, other.nCols)
        for i in range(self.nRows):
            for j in range(other.nCols):
                for k in range(self.nCols):
                    result.values[i][j] += self.values[i][k] * other.values[k][j]
        return result
    def __init__(self, fileName):
        with open(fileName) as file:
            line = int(file.readline())
            col = int(file.readline())
            self.nRows = line
            self.nCols = col
            self.values = Array2D.Array2D[line, col]
            i = 0
            for line in file:
                values = line.split()
                for j in range(col):
                    self.values[i,j] = int(values[j])
                i+=1
        #columns = len(lines[0].strip().split())
        #matrix = cls(line, cols)for i, line in enumerate(line):
          # values = line.strip().split()for j, value in enumerate(cols):
              # self.values[i, j]= int(values[j])i+=1
            
        file.close()

        #return matrix
m = Matrix("etudiants.txt")
#m1 = Matrix(4, 3)
m.print()
#print("********************")
#print("le nombre de ligne est:", m.nRows)  
#print("********************")
#print("le nombre de colone est:", m.nCols)
#l = (4 ,43,  1,  2)
#c = (2 ,7 , 23 , 4)
l = [1]
c =[2]
#print("l'interjection est :",m.setItem(1,2))
#print(m.transpose())
#k = m.multiply(m1)
#k.display()
#m1.display()
