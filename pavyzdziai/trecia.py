N = int(input('Įveskite N: '))
a_list = []
for i in range(N):
    a_list.append(int(input(f'Įveskite {i+1}`tąjį a')))
b = int(input('Įveskite b: '))

a_modified_list = []
for e in a_list:
    if e > b:
        a_modified_list.append(b)
    else:
        a_modified_list.append(e)

for e in a_modified_list:
    print(e)
