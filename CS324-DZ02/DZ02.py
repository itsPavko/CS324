def daLiJeProst(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prostiBrojevi(pocetak, kraj):
    prosti = []
    for num in range(pocetak, kraj + 1):
        if daLiJeProst(num):
            prosti.append(num)
    return prosti


pocetak = int(input("Početak intervala: "))
kraj = int(input("Kraj intervala: "))


prosti = prostiBrojevi(pocetak, kraj)
print(f"Prosti brojevi u intervalu od {pocetak} do {kraj} su: {prosti}")
