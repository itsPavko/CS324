def srednja_vrednost(niz):
    try:
        tmp = 0
        for elem in niz:
            if isinstance(elem, (int, float)):
                tmp += elem
            else:
                raise TypeError(f"Element {elem} nije podržan tip podatka.")
        
        return tmp / len(niz)
    
    except ZeroDivisionError:
        return "Niz ne sme biti prazan."
    except TypeError as e:
        return str(e)


niz1 = [10, 20, 30, 40, 50]
niz2 = [2.5, 5.0, 7.5, 10.0]
niz3 = [1, "jedan", 3, 4, 5]  # Izazvaće izuzetak
niz4 = [0.5, "tri", 2.5, "pet", 4.5]  # Izazvaće izuzetak
niz5 = [1, "jedan", 3, 4, 5]

rezultat1 = srednja_vrednost(niz1)
rezultat2 = srednja_vrednost(niz2)
rezultat3 = srednja_vrednost(niz3)
rezultat4 = srednja_vrednost(niz4)
rezultat5 = srednja_vrednost(niz5)

print(f"Srednja vrednost niza 1: {rezultat1}")
print(f"Srednja vrednost niza 2: {rezultat2}")
print(f"Srednja vrednost niza 3: {rezultat3}")
print(f"Srednja vrednost niza 4: {rezultat4}")
print(f"Srednja vrednost niza 5: {rezultat5}")