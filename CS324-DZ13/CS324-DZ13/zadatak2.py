def prikazi_pozicije(niz_modela):
    for pozicija, model in enumerate(niz_modela, start=1):
        print(f"Pozicija {pozicija}: {model}")

# Primer niza modela automobila sa minimum 20 elemenata
niz_modela = [
    "Civic", "Accord", "Corolla", "Camaro", "Mustang",
    "Cherokee", "Wrangler", "911", "Cayenne", "Tiguan",
    "Aventador", "Huracan", "Fiesta", "Focus", "Mondeo",
    "Clio", "Megane", "Polo", "Golf", "Passat"
]

# Pozivanje funkcije sa zadatim nizom modela automobila
prikazi_pozicije(niz_modela)