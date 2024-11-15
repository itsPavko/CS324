import csv
import os
from collections import Counter
#pip install matplotlib
import matplotlib.pyplot as plt

class University:
    def __init__(self, id, name, program, field, duration):
        self.id = id
        self.name = name
        self.program = program
        self.field = field
        self.duration = duration

trajanja = {}
univerziteti = []
dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dir, 'data.csv')
with open(path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        univerzitet = University(*row)
        univerziteti.append(univerzitet)




#prosecno trajanje
n = 0
m = 0
for univerzitet in univerziteti:
    n += int(univerzitet.duration)
    m += 1
p = n/m
print (f'Prosecno trajanje strudija na svim programima je: {p}')

#pojedinacno prosecno trajanje
nbas = 0
nmas = 0
ndas = 0
mbas = 0
mmas = 0
mdas = 0
for univerzitet in univerziteti:
    if univerzitet.program == ' BAS':
        nbas += int(univerzitet.duration)
        mbas += 1
    if univerzitet.program == ' MAS':
        nmas += int(univerzitet.duration)
        mmas += 1
    if univerzitet.program == ' DAS':
        ndas += int(univerzitet.duration)
        mdas += 1
pbas = nbas/mbas
pmas = nmas/mmas
pdas = ndas/mdas
print (f'Prosecno trajanje strudija na BAS programima je: {pbas}')
print (f'Prosecno trajanje strudija na MAS programima je: {pmas}')
print (f'Prosecno trajanje strudija na DAS programima je: {pdas}')

#najcesce trajanje programa
for univerzitet in univerziteti:
    program = univerzitet.program
    duration = univerzitet.duration

    if program in trajanja:
        trajanja[program].append(duration)
    else:
        trajanja[program] = [duration]

najcesca_trajanja = {}

for program, durations in trajanja.items():
    counter = Counter(durations)
    najcesce, frequency = counter.most_common(1)[0]
    najcesca_trajanja[program] = najcesce

for program, duration in najcesca_trajanja.items():
    print(f"Program {program} ima najcesce trajanje od: {duration}")

#broj studenata po univerzitetu
univerzitet_brojac = Counter([university.name for university in univerziteti])
univerziteti_n = list(univerzitet_brojac.keys())
counts = list(univerzitet_brojac.values())
plt.bar(univerziteti_n, counts, color='blue')
plt.xlabel('Univerzitet')
plt.ylabel('Broj studenta')
plt.title('Histogram broja studenata po univerzitetu')
plt.show()

#pie chart
program_brojac = Counter([(university.name, university.program) for university in univerziteti])

labels = [f"{university_name}\n{program}" for university_name, program in program_brojac.keys()]
counts = list(program_brojac.values())

plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Pie grafikon raspodele studenata')
plt.show()