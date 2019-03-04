import random as rand

cities = []
professions = []
hours = []
days = []


with open("cities.csv") as file:
    for el in file.readlines():
        cities.append(el.split("\t")[1])

with open("medical_profession_entries.csv") as file:
    for el in file.readlines():
        professions.append(el[:-1])

for el in range(8, 19, 1):
    hours.append(el)

for el in range(1, 31, 1):
    days.append(el)

print(professions)
print(cities)
print(hours)
print(days)