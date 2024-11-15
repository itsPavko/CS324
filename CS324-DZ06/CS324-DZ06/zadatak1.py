import csv

def kreiraj_raspored():
    raspored = []

    
    raspored.append(["Dan", "Predmet", "Pocetak", "Kraj", "Ucionica"])
    raspored.append(["Ponedeljak", "CS225-Operativni Sistemi", "9:45", "12:15", "RU1-2"])
    raspored.append(["Utorak", "IT335-Administracija mreza", "9:00", "10:30", "U3"])
    raspored.append(["Sreda", "IT255 - Veb sistemi 1", "11:30", "19:00", "RU4-2"])
    raspored.append(["Cetvrtak", "CS225-Operativni sistemi", "11:30", "14:00", "RU1"])
    raspored.append(["Petak", "CS324-Skripting jezici", "13:15", "15:45", "RU3-2"])
    

    return raspored

def sacuvaj_kao_csv(raspored, zadatak1):
    with open(zadatak1, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(raspored)

if __name__ == "__main__":
    zadatak1 = "raspored_casova.csv"
    raspored = kreiraj_raspored()
    sacuvaj_kao_csv(raspored, zadatak1)
    print(f"Raspored časova je uspešno sačuvan kao '{zadatak1}'.")