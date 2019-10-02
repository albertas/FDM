#! coding: utf-8
import sys
from sys import version, argv, path
from random import seed, choice, shuffle, randint, random
from unittest.mock import patch
import importlib
from io import StringIO
from datetime import datetime
from os import getcwd


if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if len(argv) < 4:
    print('Paleisdami nurodykite savo vardą, pavardę bei failą, kuriame yra Jūsų kodas, pvz:')
    print('python3 test1.py Vardas Pavardė failas.py')
    exit()

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
    1: [[[1,2,3], [3,3,3]], [[2,2,3], [3,3,3]], [[3,3,3], [3,3,3]], [[3,2,1], [3,2,1]], [[3,2,3], [9,4,9]], [[2,3,1], [4,9,1]]],
    2: [[[-1, -2, -3], [1, 2, 3]], [[-3, -2, -3], [3, 2, 3]], [[3, -2, 3], [3, 10, 3]], [[-3, -2, 3], [-30, -20, 30]], [[3, -2, -3], [30, -20, -30]]],
    3: [[[1,2,3], [abs(1-3)]], [[3,4,1], [abs(1-4)]], [[6,4,2], [abs(2-6)]], [[-6,4,2], [abs(-6-4)]], [[-6,-4,-2], [abs(-6+2)]]],
    4: [[[10, 2, 5], [10]], [[2,4,8], [8]], [[10,20,2], [20]], [[2,6,3], [6]]],
    5: [[[1,2,3], [1,2,3]], [[4,2,3], [4,4,3]], [[5,4,3], [5,4,9]], [[6,8,2], [6,8,4]], [[8,-3,2], [8,9,2]]],
    6: [[[1,2,3], [3]], [[8,2,3], [8]], [[3,7,3], [7]], [[9,3,2], [9]], [[-1,0,-2], [0]], [[10,6,3], [10]]],
    7: [[[1,2,3], False], [[2,2,3], True], [[-2,2,1], False], [[0, 100, 100], True], [[9,4,9], True]],
    8: [[[1,2,3], [1,2,3]], [[4,5,11], [4, 5, 11]], [[4,2,9], [9]], [[6,1,5], [6]], [[8,4,2], [8, 4, 2]]],
    9: [[[0,1,2], 'nekvadratine'], [[2,4,2], [1]], [[1,2,3], [0]]],
    10: [[[0,1,0], [0,1,0]], [[0,0,1], [0,0,1]], [[0,-1,1], [0,1]], [[9,1,0], [1,0]]],
    11: [[[1,2,3], [1]], [[6,3,3], [3]], [[10,3,2], [2]], [[3,2,2], [2]], [[3,3,2], [1]], [[3,8,2], [4]]],
    12: [[[1,2,3], [0]], [[5,10,3],[2]], [[5,6,7],[3]], [[8,4,5],[2]], [[7,3,2],[1]], [[5,9,10],[3]]],
    13: [[[1,2,3], [0, 3, 0]], [[-1,2,-3], [2, 1, 0]], [[-1,0,-3], [2, 0, 1]], [[0,0,0], [0, 0, 3]], [[-1,2,0], [1, 1, 1]]],
    14: [[[1,2,3], [3,2,1]], [[3,1,3], [3,3,1]], [[9,-2,3], [9,3,-2]], [[-1,2,3], [3,2,-1]]],
    15: [[[3,2,1], []], [[1,2,3], [3]], [[0,2,1], [0]], [[3,2,9], [9]]],
    16: [[[1,2,3], [1]], [[-1,2,3], [-1]], [[10,2,3], [2]], [[10,0,9], [0]]],
    17: [[[1,2,3], [6]], [[1,2,-10], [7]], [[1,-2,-10], [9]], [[-1,-2,-10], [7]]],
    18: [[[2,4,8], [1,2,4]], [[3,6,9], [1,2,3]], [[12,6,18], [2,1,3]], [[12,6,1], [12,6,1]]],
    19: [[[1,2,3], [1]], [[-1,2,3], [1]], [[1,0,0], [2]], [[-1,-2,-1], [2]], [[3,3,3], [3]]],
    20: [[[1,2,3], [2]], [[1,1,3], [1]], [[1,-2,3], [-2]], [[1,-2,-3], [-3]], [[4,4,3], [3]]]
}
test_data = data[u1]
shuffle(test_data)
path.append(getcwd())

print('Testuojama: ', end='')
for inputs, expected_result in test_data:
    def input_mock(prompt=None):
        for i in inputs:
            yield str(i)

    result = None
    with patch('builtins.input', side_effect=input_mock()) as input_mock, \
         patch('sys.stdout', new=StringIO()) as output_mock:

        i = importlib.import_module(package)
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
            result = [v.strip(':",;!.\'`') for v in value.split()]
            result = [int(v) for v in result if v.strip('-').isdigit()]; randint(1, 100)

    if expected_result != result:
        print('\nPrograma veikia nekorektiškai su įvestimis:', ', '.join([str(i) for i in inputs]))
        print(expected_result, ',', result)
        exit()
    else:
        print('+', end='')
        sys.stdout.flush()

print(f'\nSveikinu! {" ".join(argv[1:-1])} atsiskaitė 1`ąja užduotį ({filename} {u1}-{randint(100,999)}).')
score = 10
if datetime.now().isocalendar()[1] > 40:
    score -= datetime.now().isocalendar()[1] - 40
print(f'Jums už šią užduotį skirtas {score/10:g} balas.')
