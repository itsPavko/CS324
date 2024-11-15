import random


n = int(input("Unesite broj indeksa (n): "))


random_brojevi = [random.randint(1, 100) for _ in range(n)]

print("Generisani brojevi:")
print(random_brojevi)

# Sortiramo listu u padajućem redosledu
random_brojevi.sort(reverse=True)

print("Sortirani brojevi u padajućem redosledu:")
print(random_brojevi)