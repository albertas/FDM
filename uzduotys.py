#! coding: utf-8
from random import seed, choice
from sys import version, argv

args = [a.strip('<').strip('>') for a in argv[1:3]]
vardas_pavarde = ' '.join(args)
if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if not vardas_pavarde:
    print('Naudojimo pavyzdys:')
    print('$ python3 uzduotys.py Albertas Gimbutas')
    exit()

seed(vardas_pavarde)
print(vardas_pavarde, 'uzduotys:')
print('Pirma:', choice(range(1, 21)))
print('Antra:', choice(range(1, 30)))
print('Trecia:', choice(range(1, 37)))
print('Ketvirta:', choice(range(1, 30)))
print('Penkta:', choice(range(1, 38)))
