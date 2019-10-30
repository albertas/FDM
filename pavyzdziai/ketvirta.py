
zodynas = {}

for title in ['a', 'b', 'c', 'd']:
    x = int(input('Įveskite '+title+' taško x koordinatę'))
    y = int(input('Įveskite '+title+' taško y koordinatę'))
    zodynas[title] = [x, y]

print(zodynas)      # {'a': [0, 0], 'b': [0, 1], 'c': [1, 1], 'd': [2, 2]}

zodynas['a'][0]  # 0
zodynas['a'][1]  # 0

bx, by = zodynas['b']
print(bx)
print(by)
