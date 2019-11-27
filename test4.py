#! coding: utf-8
import importlib
import os
import sys
from datetime import datetime
from io import StringIO
from os import getcwd
from random import seed, choice, shuffle, randint, random
from sys import version, argv, path
from unittest.mock import patch


if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if len(argv) < 4:
    print('Paleisdami nurodykite savo vardą, pavardę bei failą, kuriame yra Jūsų kodas, pvz:')
    print('python3 test4.py Vardas Pavardė failas.py')
    exit()

os.environ['PYTHONIOENCODING'] = "utf-8"

def set_seed(name, surname):
    seed(name + ' ' + surname)

vardas = argv[1]
pavarde = argv[2]
filename = argv[-1]

package = filename[:-3] if filename.endswith('.py') else filename
set_seed(vardas, pavarde)

u1 = choice(range(1, 21))
u2 = choice(range(1, 30))
u3 = choice(range(1, 37))
u4 = choice(range(1, 30))
u5 = choice(range(1, 38))


data = {
    1: [
        [[0, 0, 1, 1], [1.4142135623730951, 1.0]],
        [[0, 1, 2, 1], [2.0, 0.0]],
        [[1, 0, 3, 1], [2.23606797749979, 0.5]],
        [[-1, 0, 3, -1], [4.123105625617661, -0.25]],
    ],
    2: [
        [[0,0, 0,1, 1,1], True],
        [[0,0, 0,1, 0,2], False],
        [[0,0, 0,1, 1,0], True],
        [[1,0, 0,1, 1,1], True],
        [[0,0, 1,0, 2,0], False],
    ],
    3: [
        [[0,0, 0,1, 1,1], True],
        [[0,0, 0,1, 0,2], False],
        [[0,0, 0,1, 1,0], True],
        [[1,0, 0,1, 1,1], True],
        [[0,0, 1,0, 2,1], False],
    ],
    4: [
        [[0,0, 0,1, 1,1], [0.5]],
        [[2,0, 0,2, 2,2], [2.0]],
        [[0,0, 0,2, 1,2], [1.0]],
        [[0,0, 4,0, 5,1], [2.0]],
    ],
    5: [
        [[0, 0, 0, 1, 1, 1], [1.0, 1.4142135623730951, 1.0]],
        [[0, 1, 2, 1, 2, 0], [2.0, 2.23606797749979, 1.0]],
        [[1, -1, 3, 1, 1, 3], [2.8284271247461903, 4.0, 2.8284271247461903]],
        [[2, 1, 0, -1, 1, 3], [2.8284271247461903, 2.23606797749979, 4.123105625617661]],
    ],
    6: [
        [[0,0, 0,1, 1,1], [0.5]],
        [[2,0, 0,2, 2,2], [2.0]],
        [[0,0, 0,2, 1,2], [1.0]],
        [[0,0, 4,0, 5,1], [2.0]],
    ],
    7: [
        [[0,0, 0,1, 1], [0, 0.5]],
        [[0,0, 1,0, 1], [0.5, 0]],
        [[0,2, 2,0, 2], [2., 2]],
        [[1,3, 3,1, 2], [3., 3]],
    ],
    8: [
        [[0,0, 0,1, 1,1], [1.0]],
        [[0,0, 1,0, 2,2], [2.0]],
        [[1,0, 1,1, 2,1], [1.0]],
        [[1,1, 2,2, -1,1], [1.41421356]],
    ],
    9: [
        [[0,0, 0,1, 1,1], False],
        [[0,0, 0,1, 0,2], True],
        [[0,0, 0,1, 1,0], False],
        [[1,0, 0,1, 1,1], False],
        [[0,0, 1,0, 2,0], True],
    ],
    10: [
        [[0,0, 0,1, 1,1], True],
        [[0,0, 0,1, 0,2], True],
        [[0,0, 0,1, 1,0], True],
        [[1,0, 0,1, 1,1], True],
        [[0,0, 1,0, 2,1], True],
        [[0,0, 1,0, 3,1], False],
    ],
    11: [
        [[0,0, 0,1, 1,1], 'status'],
        [[0,0, 0,1.2, 1.,1], 'smailus'],
        [[0,0, 0,1, 3,3], 'bukas'],
        [[0,0, 1,0, 2,1], 'bukas'],
        [[0,0, 0,1, 1,0], 'status'],
        [[1,0, 0,1, 1,1], 'status'],
        [[0,0, 0,2, 0.5,1.0], 'bukas'],
    ],
    12: [
        [[0,0, 0,1, 1,1], False],
        [[0,0, 0,1, 1,2], True],
        [[0,0, 0,1, 0.3,0.5], True],
        [[0,0, 0,1, 2.0,0.5], False],
        [[0,0, 0,2, 0.5,1.0], True],
    ],
    13: [
        [[0,0, 0,1, 1,1], False],
        [[0,0, 0,1, 1,2], False],
        [[0,0, 0,1, 0.3,0.5], False],
        [[0,0, 0,1, 2.0,0.5], True],
        [[0,0, 0,2, 0.5,1.0], False],
    ],
    14: [
        [[0,0, 0,1, 1,1, 1,0], True],
        [[0,0, 0,2, 2,2, 2,0], True],
        [[0,0, 0,1, 2,2, 2,0], False],
        [[0,-2, -1,0, 0,2, 1,0], True],
    ],
    15: [
        [[0,0, 0,1], [0, -1]],
        [[1,1, 2,2], [0, 0]],
        [[1,1, 0.5,0.75], [1.5, 1.25]],
        [[0,0, 1,1], [-1, -1]],
        [[0,0, 1,2], [-1, -2]],
    ],
    16: [
        [[0,0, 0,1, 1,1], [-1,1]],
        [[0,0, 0,1, 1,2], [-1,2]],
        [[0,0, 1,1, 0,1], [1,0]],
        [[0,0, 1,1, 0,2], [2,0]],
    ],
    17: [
        [[0,0, 0,1, 1,1, 1,2], True],
        [[0,0, 0,1, 1,1, 2,1], False],
        [[0,0, 1,0, 0,0, 1,1], False],
        [[0,0, 1,0, 0,1, 1,1], True],
    ],
    18: [
        [[0,0, 0,1, 1,1], True],
        [[0,0, 0,1, 1,2], False],
        [[0,0, 0,1, 1,0], True],
        [[1,0, 0,1, 1,1], True],
        [[0,0, 2,0, 1,1], True],
        [[0,0, 2,0, 1.2,1], False],
    ],
    19: [
        [[0,0, 0,1, 1,1], False],
        [[0,0, 0,1, 1,2], False],
        [[0,0, 0,1, 1,0], False],
        [[1,0, 0,1, 1,1], False],
        [[0,0, 2,0, 1,1], False],
        [[0,0, 2,0, 1.2,1], False],
        [[0,0, 2,0, 1.2,1], False],
        [[0,0, 6,0, 3,5.196152422706632], True],
    ],
    20: [
        [[0,0, 0,1], [0,-1]],
        [[0,0, 1,0], [-1,0]],
        [[0,0, 1,1], [-1,-1]],
        [[1,1, 2,1], [0,1]],
        [[1,1, 2,2], [0,0]],
    ],
    21: [
        [[0,0, 0,1, 1,1, 1,0], True],
        [[0,0, 1,1, 0,1, 1,0], True],
        [[0,0, 2,2, 0,1, 1,0], False],
        [[0,0, 2,1, 0,1, 1,0], False],
        [[0,0, 2,2, 0,2, 2,0], True],
        [[0,0, 0,2, 2,2, 2,0], True],
        [[0,0, 2,0, 2,2, 0,2], True],
    ],
    22: [
        [[0,0, 0,1, 1,1, 1,0], True],
        [[0,0, 2,2, 0,1, 1,0], False],
        [[0,0, 2,1, 0,1, 1,0], False],
        [[-1,0, 2,0, 1,1, -2,1], True],
    ],
    23: [
        [[0,0, 0,1, 1,1, 1,0], True],
        [[0,0, 1,1, 0,1, 1,0], True],
        [[0,0, 2,2, 0,1, 1,0], False],
        [[0,0, 2,1, 0,1, 1,0], False],
        [[0,0, 2,2, 0,2, 2,0], True],
        [[0,0, 0,2, 2,2, 2,0], True],
        [[0,0, 2,0, 2,2, 0,2], True],
        [[0,0, 1,0, 1,2, 0,2], True],
        [[0,0, 1,0, 2,2, 0,2], False],
    ],
    24: [
        [[0,0, 0,1, 1,1, 1,0], True],
        [[0,0, 1,1, 0,1, 1,0], True],
        [[0,0, 2,2, 0,1, 1,0], True],
        [[0,0, 2,1, 0,1, 1,0], True],
        [[0,0, 2,2, 0,2, 2,0], True],
        [[0,0, 0,2, 2,2, 2,0], True],
        [[0,0, 2,0, 2,2, 0,2], True],
        [[0,0, 1,0, 1,2, 0,2], True],
        [[-1,0, 2,0, 1,1, 0,2], False],
    ],
    25: [
        [[0,0, 0,1, 1,1, 1,0], False],
        [[0,0, 1,1, 0,1, 1,0], False],
        [[0,0, 2,2, 0,1, 1,0], True],
        [[-1,0, 2,0, 1,1, 1,0], True],
    ],
    26: [
        [[0,0, 0,1, 1,1, 1,0], False],
        [[0,0, 1,1, 0,1, 1,0], False],
        [[0,0, 3,3, 0,1, 1,0], True],
        [[-1,0, 2,0, 1,1, 1,0], False],
    ],
    27: [
        [[0,0, 0,1, 1,1, 0,0], False],
        [[0,0, 0,1, 1,2, 0,0], False],
        [[0,0, 0,1, 1,0, 0,0], False],
        [[1,0, 0,1, 1,1, 1,0], False],
        [[0,0, 2,0, 1,1, 0,0], False],
        [[0,0, 2,0, 1.2,1, 0,0], False],
        [[0,0, 2,0, 1.2,1, 0,0], False],
        [[0,0, 6,0, 3,5.196152422706632, 0,0], True],

    ],
    28: [
        [[0, 0, 0, 1, 1, 1], [1.0, 1.4142135623730951, 1.0]],
        [[0, 1, 2, 1, 2, 0], [2.0, 2.23606797749979, 1.0]],
        [[1, -1, 3, 1, 1, 3], [2.8284271247461903, 4.0, 2.8284271247461903]],
        [[2, 1, 0, -1, 1, 3], [2.8284271247461903, 2.23606797749979, 4.123105625617661]],
    ],
    29: [
        [[0, 0, 0, 1, 1, 1], [1.4142135623730951]],
        [[0, 1, 2, 1, 2, 0], [2.23606797749979]],
        [[1, -1, 3, 1, 1, 3], [4.0]],
        [[2, 1, 0, -1, 1, 3], [4.123105625617661]],
    ]
}
test_data = data[u4]
shuffle(test_data)
path.append(getcwd())

print(f'Testuojama ({u4}): ', end='')
for inputs, expected_result in test_data:
    def input_mock(prompt=None):
        for i in inputs:
            yield str(i)

    result = None
    with patch('builtins.input', side_effect=input_mock()) as input_mock, \
         patch('sys.stdout', new=StringIO()) as output_mock:

        i = importlib.import_module(package)
        package_file = i.__file__
        del sys.modules[package]

        value = output_mock.getvalue()
        if type(expected_result) == bool:
            if value.strip().lower() in ['taip', 'true']:
                result = True
            elif value.strip().lower() in ['ne', 'false']:
                result = False
        elif type(expected_result) == str:
            result = value.strip().lower().replace('ė', 'e')
        else:
            result = [v.strip(':",;!.\'`[]()') for v in value.split()]
            result = [float(v) for v in result if v.strip('-').replace('.', '').isdigit()]; randint(1, 100)

    with open(i.__file__) as code_file:
        code = code_file.read()
        if 'def' not in code:
            print('\n\nPrograma netenkina reikalavimų, nes nėra panaudota funkcija.')
            exit()
        if 'dict(' not in code and '{' not in code:
            print('\n\nPrograma netenkina reikalavimų, nes taškų koordinates turite talpinti žodyne.')
            print("Pavyzdžiui:  taškai = {'a': [0, 0], 'b': [0, 1], 'c': [1, 1]}.")
            exit()

    def approx(l):
        if type(l) == list or type(l) == tuple:
            return set([round(v, 5) for v in l])
        return l

    if approx(expected_result) != approx(result):
        print('\nPrograma veikia nekorektiškai su įvestimis:', ', '.join([str(i) for i in inputs]))
        print('Tikėtąsi', expected_result, ', o gauta', result)
        exit()
    else:
        print('+', end='')
        sys.stdout.flush()

print(f'\nSveikinu! {" ".join(argv[1:-1])} atsiskaitė 4`ąją užduotį ({filename} {u4}-{randint(100,999)}).')
score = 10
if datetime.now().isocalendar()[1] > 48:
    score -= datetime.now().isocalendar()[1] - 48
print(f'Jums už šią užduotį skirtas {score/10:g} balas.')
