#! coding: utf-8
from random import seed, choice
from sys import version, argv
import unicodedata

args = [a.strip('<').strip('>') for a in argv[1:]]
if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if len(args) < 2:
    try:
        print('Naudojimo pavyzdys (nurodykite savo vardą ir pavardę vietoje Albertas Gimbutas):')
        print('$ python3 uzduotys.py Albertas Gimbutas')
    except:
        print('Naudojimo pavyzdys (nurodykite savo varda ir pavarde vietoje Albertas Gimbutas):')
        print('$ python3 uzduotys.py Albertas Gimbutas')
    exit()


vardas_pavarde = ' '.join(args).lower()
vardas_pavarde = unicodedata.normalize('NFKD', vardas_pavarde).encode('ascii','ignore').decode()

seed(vardas_pavarde)
try:
    print(f'"{" ".join(args)}" užduočių numeriai:')
except:
    print(f'"{" ".join(args)}" uzduociu numeriai:')

print('Pirma:', choice(range(1, 21)))
print('Antra:', choice(range(1, 30)))
print('Trecia:', choice(range(1, 37)))
print('Ketvirta:', choice(range(1, 30)))
print('Penkta:', choice(range(1, 38)))
