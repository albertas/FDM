#! coding: utf-8
from random import seed, choice
from sys import version, argv

vardas_pavarde = ' '.join(argv[1:3])
if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if not vardas_pavarde:
    print('Naudojimo pavyzdys:')
    print('$ python3 uzduotys.py Albertas Gimbutas')
    exit()

seed(vardas_pavarde)
print(vardas_pavarde, 'užduotys:')
print('Pirma:', choice(range(1, 21)))
print('Antra:', choice(range(1, 30)))
print('Trečia:', choice(range(1, 37)))
print('Ketvirta:', choice(range(1, 30)))
print('Penkta:', choice(range(1, 38)))
