predmeti = {}

n = int(input("Unesite broj predmeta: "))

for i in range(n):
    sifra = input(f'Unesite sifru predmeta {i + 1}: ')
    ocena = int(input(f'unesite ocenu predmeta {i + 1}: '))
    predmeti.__setitem__(sifra,ocena)

print("Polozeni predmeti: ")
for sifra, value in predmeti.items():
    if value > 5:
        print(f'Polozen je predmet sa sifrom {sifra}, i ocenom {value}') 

