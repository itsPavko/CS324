import random
import array

n = 4442
indeksi = []
for x in range(n):
    number = random.randint(1000,9999)
    indeksi.append(number)

indeksi.sort()
indeksi.reverse()
print(indeksi)