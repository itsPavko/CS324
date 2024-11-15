import numpy as np

# Kreiranje jedinične matrice dimenzija 3x3
matrica1 = np.eye(3)

# Ispis rezultujuće matrice
print("Prva matrica je: ")
print(matrica1)

# Kreiranje matrice dimenzija 4x4 popunjene nulama
matrica2 = np.zeros((4, 4))

# Postavljanje vrednosti na 10 u određenim redovima i kolonama
matrica2[1:3, 1:3] = 10

# Ispis rezultujuće matrice
print("Druga matrica je: ")
print(matrica2)

# inicijalizovanje treceg niza
niz3 = np.ones((5,5), dtype='int32')
# pomocni, unutrasni niz
pomocni_niz = np.zeros((3,3), dtype='int32')
pomocni_niz[1,1] = 1
# ubacivanje jednog niza u drugi
niz3[1:-1, 1:-1] = pomocni_niz
print("treci niz je: ")
print(niz3)