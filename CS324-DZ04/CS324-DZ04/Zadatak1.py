import random

def generate_and_sort_array(ime, br_indeks):
    if len(ime) % 2 == 0:
        array = [random.randint(0, br_indeks) for _ in range(br_indeks)]
    else:
        array = [random.uniform(-int(str(br_indeks)[:2]), int(str(br_indeks)[2:])) for _ in range(br_indeks)]
   
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


ime = input("Unesite ime: ")
br_indeks = int(input("Unesite cetvorocifreni broj za br_indeks: "))

sorted_array = generate_and_sort_array(ime, br_indeks)
print("Sortirani niz:", sorted_array)
