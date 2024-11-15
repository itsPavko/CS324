import random
imenik = {}

m = 5033//3

for i in range(m):
    imenik[i] = random.uniform(50, 33)

n = 5033 % 3 
print(f'n = {n}')

for i in range (n):
    kluc, value = random.choice(list(imenik.items()))
    print(f'kljuc: {kljuc}, sifra : {value}')