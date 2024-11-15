class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa, smer):
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa
        self.smer = smer
        self.polozeni_ispiti = {}

    def dodaj_polozeni_ispit(self, sifra_predmeta, ocena):
        if ocena == 5:
            print(f"Student nije položio ispit {sifra_predmeta}.")
        else:
            self.polozeni_ispiti[sifra_predmeta] = ocena

# Instanciranje dva studenta
student1 = Student("Nikola", "Randjelovic", "5033", "Informacione Tehnologije")
student2 = Student("Milos", "Ivanovic", "5032", "Softversko inzenjerstvo")

# Dodavanje položenih ispita
student1.dodaj_polozeni_ispit("MA101", 9)
student1.dodaj_polozeni_ispit("SE201", 8)
student1.dodaj_polozeni_ispit("NT110", 7)

student2.dodaj_polozeni_ispit("CS101", 7)
student2.dodaj_polozeni_ispit("IT350", 5)
student2.dodaj_polozeni_ispit("MA201", 9)

# Provera da li su studenti na istom smeru
if student1.smer == student2.smer:
    print(f"{student1.ime} i {student2.ime} su na istom smeru.")
else:
    print(f"{student1.ime} i {student2.ime} nisu na istom smeru.")

# Broj položenih ispita po studentu
print(f"{student1.ime} je položio {len(student1.polozeni_ispiti)} ispita.")
print(f"{student2.ime} je položio {len(student2.polozeni_ispiti)} ispita.")

# Ispiti koje su oba studenta položili
zajednicki_ispiti = set(student1.polozeni_ispiti.keys()) & set(student2.polozeni_ispiti.keys())
if zajednicki_ispiti:
    print(f"Ovi studenti imaju sledeće zajedničke ispite: {', '.join(zajednicki_ispiti)}.")
else:
    print("Ovi studenti nemaju zajedničkih položenih ispita.")