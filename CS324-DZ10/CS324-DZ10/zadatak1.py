import pandas as pd
import matplotlib.pyplot as plt

# Pravljenje praznog rečnika za čuvanje podataka o ispitima
ispit = {}

# Unos položenih ispita od strane studenta
while True:
    sifra_predmeta = input("Unesite šifru predmeta (ili 'kraj' za završetak unosa): ")
    if sifra_predmeta.lower() == 'kraj':
        break
    ocena = int(input("Unesite ocenu: "))

    if sifra_predmeta in ispit:
        ispit[sifra_predmeta].append(ocena)
    else:
        ispit[sifra_predmeta] = [ocena]

# Kreiranje DataFrame-a koristeći Pandas
df = pd.DataFrame([(predmet, ocena) for predmet, ocene in ispit.items() for ocena in ocene], columns=['Predmet', 'Ocena'])

# Računanje broja ocena
broj_ocena = df['Ocena'].value_counts().sort_index()

# Računanje broja položenih ispita
broj_polozenih_po_predmetu = df['Predmet'].value_counts()

# Računanje promene prosečne ocene
prosecna_ocena_po_predmetu = df.groupby('Predmet')['Ocena'].mean().diff()

# Prikaz podataka
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

#raspored ocena
axs[0].pie(broj_ocena, labels=broj_ocena.index, autopct='%1.1f%%')
axs[0].set_title('Raspored ocena')

#broj položenih predmeta po šifri predmeta
broj_polozenih_po_predmetu.plot(kind='barh', ax=axs[1])
axs[1].set_title('Broj položenih predmeta po šifri predmeta')

# Line plot - promena prosečne ocene
prosecna_ocena_po_predmetu.plot(ax=axs[2])
axs[2].set_title('Promena prosečne ocene po položenom predmetu')

# Snimanje grafa i CSV datoteke
plt.tight_layout()
fig.savefig('Student_izvestaj.png')
df.to_csv('Student_izvestaj.csv', index=False)

plt.show()
