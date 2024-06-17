import Array2D

class Matrix:
    def __init__(self, l, c):
        self.nRows = l
        self.nCols = c
        self.values = Array2D.Array2D(l, c)

    def nRows(self):
        return self.nRows
    
    def nCols(self):
        return self.nCols

    def print(self):
        self.values.print()
        
    def __getitem__(self,keys):
        row = keys[0]
        col = keys[1]
        assert row >= 0 and row < self.nRows and col >= 0 and col <= self.nCols , "Nombre d'indices du tableau non valide."
        return self.values[keys]

    def __setitem__(self,keys, val):
        row = keys[0]
        col = keys[1]
        assert row >= 0 and row < self.nRows and col >= 0 and col <= self.nCols , "Nombre d'indices du tableau non valide."
        self.values[keys]=val

    def __init__(self, filename=None,l=None, c=None,):
        if filename:
            with open(filename) as file:
                line = int(file.readline())
                col = int(file.readline())
                # Attribut de la classe
                self.nRows = line
                self.nCols = col
               
                self.values = Array2D.Array2D(line, col)
                # Extract the values from the remaining lines.
                i = 0
                for line in file:
                    values = line.split()
                    for j in range(col):
                        self.values[i,j] = int(values[j])
                    i+=1
                file.close()
        else:
                self.nRows = l
                self.nCols = c
                self.values = Array2D.Array2D(l, c)
    
    def nRows(self):
        return self.nRows
    
    def nCols(self):
        return self.nCols


    def add(self, m):
         #assert (m.nRows != self.nRows) and (m.nCols != self.nCols) , "Les matrices sont incompatible pour une operation d'addition"
         for row in range(self.nRows):
             for col in range(self.nCols):
                 self[row, col] += m[row, col] 
    def sud(self, m):
         #assert (m.nRows != self.nRows) and (m.nCols != self.nCols) , "Les matrices sont incompatible pour une operation d'addition"
         for row in range(self.nRows):
             for col in range(self.nCols):
                 self[row, col] -= m[row, col] 

    def scaleBy(self,m):
         for row in range(self.nRows):
             for col in range(self.nCols):
                 self[row, col] *= m

    def tras(self):
        transposed_data = [[self.values[j][i] for j in range(self.nRows)] for i in range(self.nCols)]
        self.data = transposed_data
        self.nRows, self.nCols = self.nCols, self.nRows