#! coding: utf-8
from sys import version, argv


if not version.startswith('3'):
    print('Naudokite python3')
    exit()


if len(argv) < 3:
    try:
        print('Naudojimo pavyzdys (nurodykite savo vardą ir pavardę vietoje Albertas Gimbutas):')
        print('$ python3 uzduotys.py Albertas Gimbutas')
    except:
        print('Naudojimo pavyzdys (nurodykite savo varda ir pavarde vietoje Albertas Gimbutas):')
        print('$ python3 uzduotys.py Albertas Gimbutas')
    exit()


def set_seed(all_args):
    import unicodedata
    from random import seed
    args = [a.strip('<').strip('>') for a in all_args if not a.endswith('.py')]
    vardas_pavarde = ' '.join(args).lower()
    vardas_pavarde = unicodedata.normalize('NFKD', vardas_pavarde).encode('ascii','ignore').decode()
    seed(vardas_pavarde)


def get_task_variants():
    from sys import argv
    from random import choice
    set_seed(argv[1:])
    return [
        choice(range(1, 21)),
        choice(range(1, 30)),
        choice(range(1, 37)),
        choice(range(1, 30)),
        choice(range(1, 38)),
    ]


try:
    print(f'"{" ".join(argv[1:])}" užduočių numeriai:')
except:
    print(f'"{" ".join(argv[1:])}" uzduociu numeriai:')

variants = get_task_variants()
print('Pirma:', variants[0])
print('Antra:', variants[1])
print('Trecia:', variants[2])
print('Ketvirta:', variants[3])
print('Penkta:', variants[4])
