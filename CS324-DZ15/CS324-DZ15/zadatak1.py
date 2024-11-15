def je_prost_broj(broj):
    if broj < 2:
        return False
    for i in range(2, int(broj**0.5) + 1):
        if broj % i == 0:
            return False
    return True

def prosti_brojevi_interval(a, b):
    prosti_brojevi_lista = [broj for broj in range(a, b+1) if je_prost_broj(broj)]
    return prosti_brojevi_lista

def kvadrat(broj):
    return broj**2

def kvadrati_prostih_brojeva(prosti_brojevi_lista):
    kvadrati_prostih_brojeva_lista = list(map(kvadrat, prosti_brojevi_lista))
    return kvadrati_prostih_brojeva_lista

# Primer 
a = 10
b = 50
prosti_brojevi_lista = prosti_brojevi_interval(a, b)
kvadrati_prostih_brojeva_lista = kvadrati_prostih_brojeva(prosti_brojevi_lista)

print(f"Prosti brojevi u intervalu [{a},{b}]: {prosti_brojevi_lista}")
print(f"Kvadrati prostih brojeva: {kvadrati_prostih_brojeva_lista}")