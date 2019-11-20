import sys


def projection(a, b, c):
    '''
    a, b - taškai ant tiesės
    c - taškas, kurį reikia suprojektuoti į a, b taškų tiesę
    grąžinama c taško projekcija į a, b taškų tiesę
    Remtasi: https://stackoverflow.com/a/12499474
    '''
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    x3 = c[0]
    y3 = c[1]
    px = x2 - x1
    py = y2 - y1
    dAB = px * px + py * py
    u = ((x3 - x1) * px + (y3 - y1) * py) / dAB
    x = x1 + u * px
    y = y1 + u * py
    return [x, y]

def test_projection():
    # if projection([0,0],[1,1],[0,1]) != [0.5, 0.5]:
    #     print('projection funkcija nekorektiškai veikia')
    #     exit()

    assert projection([0,0],[1,1],[0,1]) == [0.5, 0.5]
    assert projection([0,0],[1,2],[0,1]) == [0.4, 0.8]

    print('Visi testai įvykdyti sėkmingai!')


if __name__ == '__main__':




    zodynas = {}

    for title in ['a', 'b', 'c']:
        x = int(input('Įveskite '+title+' taško x koordinatę: '))
        y = int(input('Įveskite '+title+' taško y koordinatę: '))
        zodynas[title] = [x, y]

    print(zodynas)      # {'a': [0, 0], 'b': [0, 1], 'c': [1, 1]}

    zodynas['a'][0]  # 0
    zodynas['a'][1]  # 0

    bx, by = zodynas['b']
    print(bx)
    print(by)

    print('Projekcijas:', projection(zodynas['a'], zodynas['b'], zodynas['c']))
