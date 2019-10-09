a = int(input('Įveskite skaičių a: '))
b = int(input('Įveskite skaičių b: '))
c = int(input('Įveskite skaičių c: '))

if (a <= b) and (b <= c):
    didziausias = max(a, b, c)
    a = didziausias
    b = didziausias
    c = didziausias
elif (a > b) and (b > c):
    pass
else:
    a = a * a
    b = b * b
    c = c * c
# print(a, b, c)

print(a)
print(b)
print(c)

# 1 2 3
# > < >= <= != ==
#
# bool()
# and or not






