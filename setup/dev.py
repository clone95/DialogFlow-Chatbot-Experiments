import os

cities = []

with open("setup/cities.csv") as file:
    for el in file.readlines():
        cities.append(el[:-2])

print(cities)