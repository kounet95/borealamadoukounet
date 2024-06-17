import Matrix as m

m1 = m.Matrix("matrice1.txt")
m2 = m.Matrix("matrice2.txt")
m1.print()
print("\n")
m2.print()
print("\n")
m2.add(m1)
m2.print()
print("\n")
m2.sud(m1)
m2.print()
m1.scaleBy(5)
m1.print()
m1.tras()
m1.tras
