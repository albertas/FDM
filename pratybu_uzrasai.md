### Pirmosios pratybos
Algoritmas - baigtinė veiksmų seka, kurią reikia atlikti norint gauti rezultatą.

Programa - algoritmas užrašytas konkrečia porgramavimo kalba.

Kintamasis - vieta atmintyje, kurioje galima išsaugoti reikšmę.

Python programavimo kalbos savybės:
 - interpretuojama - programos žingsniai vykdomi iš eilės.
 - dinamiškai tipizuojama - tas pats kintamasis gali turėti skirtingo tipo reikšmes.

Python kodo stiliaus standartas: [PEP8](https://pep8.org/) - nusako taisykles
kaip turėtų būti formatuotas kodas.

Python paketų archyvas: [pypi.org](https://pypi.org)

Naudosime Python3. [Interpretatoriaus paleidimo instrukcijos](https://docs.python.org/3/tutorial/interpreter.html).

Funkcijos kurias išmokome: `print()`, `help()`, `dir()`, `input()`.


### Antrosios pratybos
Priskyrimo operatorius: `=`

[Sąlygos sakinio (`if`)](https://docs.python.org/3/tutorial/controlflow.html#if-statements) struktūra:

    if <sąlyga1>:
        print('<sąlyga1> teisinga')
    elif <sąlyga2>;
        print('<sąlyga2> teisinga, <sąlyga1> neteisinga')
    else:
        print('visos sąlygos neteisingos')

Skaičių palyginimo operatoriai:  `>` `<` `>=` `<=` `!=` `==`
Palyginimo operacijos reikšmė yra loginė.

Loginio tipo operatoriai: `and` `or` `not`

Visų tipų kintamieji gali būti paversti į loginį tipą.
Jeigu kintamasis yra tuščias, jis verčiamas į `False`, kitu atveju jis verčiamas
į `True`. Naturaliųjų skaičių atveju nulis yra laikomas tuščia reikšme.

Tipų konvertavimo funkcijos: `int()`, `bool()`, `str()`, `float()`
Funkcijos: `max()`, `min()`



### Trečiosios pratybos
Linux terminalo komandos skirtos navigavimui po failinę sistemą:  `pwd`, `cd`, `ls`, `mkdir`, `mv`, `cp`, `scp`, `rm`.

Git commandos: `clone`, `pull`, `add`, `commit`, `push`, `status`, `log`. Versijavimo
sistemos naudojimo nauda: prieinamos senesnės kodo versijos, nors dirbama tik su
aktualia versija. Leidžia bendradarbiauti rašant kodą. [Git dokumentacija](https://git-scm.com/). Nemokamas Git repozitorijų talpinimas [GitLab](https://gitlab.com), [GitHub](https://github.com).

Norint atsiskaityti pirmąją užduotį įvykdykite ir pakvieskite mane:

    $ cd FDM
    $ git pull
    $ cd ..
    $ python3 FDM/test1.py Vardas Pavardė jusu_programa.py

### Ketvirtosios pratybos

  * Duomenų struktūra [`list` (sąrašas)](https://docs.python.org/3/tutorial/introduction.html#lists) ir [jo metodai `append`, `pop`, `index`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), [slicing (elementų ištraukimas iš sąrašo [from,to,step] ](https://docs.python.org/3/tutorial/introduction.html#strings).
  * Ciklai [`while`](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming) ir  [`for`](https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools) ciklai. Jų eigos valdymas naudojant [`break` ir `continue`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) sąkinius.
  * Skaičių operatoriai:
    * `%` - grąžina sveikųjų skaičių dalybos liekaną
    * `//` - grąžina sveikųjų skaičių dalybos sveikąją dalį
    * `**` - pakelia skaičių kvadratu
  * Realiųjų skaičių apvalinimas naudojant: `int()`, `round()`
  * Pagalbinės funkcijos:
    * [`range()`](https://docs.python.org/3/library/stdtypes.html#range) -
      sugeneruoja skaičių seką.
    * [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) - sunumeruoja skaičių seką.
  * Simbolių eilučių formatavimas naudojant `f"{}"` išraišką.

### Penktosios pratybos
Duomenų struktūros:
  * [`tuple()` (kortedžas, dar vadinamas sąrašu konstanta)](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) 
  * [`dict()` (žodynas)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
  * [`set()` (aibė)](https://docs.python.org/3/tutorial/datastructures.html#sets)

Pagalbinė funkcija: [`len()`](https://docs.python.org/3.7/library/functions.html#len) - grąžina elementų skaičių sąraše, aibėje ar žodyne.

[**Immutable**](https://docs.python.org/3/glossary.html#term-immutable) ir [**Mutable**](https://docs.python.org/3/glossary.html#term-mutable) kintamųjų apibrėžimai:
  * [**Immutable**](https://docs.python.org/3/glossary.html#term-immutable) - kintamieji konstantos (jų negalima keisti), pvz.: `int()`,
    `str()`, `bool()`, `float()`, `tuple()`. Atlikus veiksmą su **Immutable** kintamuoju yra sukuriama nauja reikšmė, o
    ne modifikuojama jau egzistuojanti.
  * [**Mutable**](https://docs.python.org/3/glossary.html#term-mutable) - po sukūrimo kintamojo reikšmė gali būti redaguojama, pvz.:
    `list()`, `set()`, `dict()`.

**Mutable** kintamojo priskyrimas priskiria nuorodą, o ne reikšmę:

```
>>> a = [1]
>>> b = a
>>> c = a[:]  # Sukuria naują sąrašą su tokiais pačiais elementais
>>> b.append(2)
>>> print(a)
... [1, 2]
>>> print(b)
... [1, 2]
>>> print(c)
... [1]
```


### Šeštosios pratybos
Kintamųjų vardų sudarymo taisyklės: 
 * turi prasidėti raide (a-zA-Z_).
 * varde gali būti raidės ir skaičiai (a-zA-Z_0-9).
 * nenaudoti rezervuotų vardų kintamiesiams
 * kintamieji, kurių vardai prasideda _ turi specialią reikšmę.

Paklaidos, kurio atsiranda dirbant su realiosiomis reikšmėmis. `round(<reikšmė>, <tikslumas>)` funkcijos naudojimas reikšmių palyginimams.

[Funkcijos](https://docs.python.org/3/tutorial/controlflow.html#defining-functions):
 * funkcijos struktūra, raktiniai žodžiai `def`, `return`:
    
```
def kvadratas(a):
    return a*a
```

 * parametras - reikšmės, kurių tikisi funkcija (pvz., `a`).
  * parametrų nustatytosios reikšmės (pvz.: `atspausdinti`):

```
def kvadratas(a, atspausdinti=False):
    if atspausdinti:
        print(a*a)
    return a*a
```

 * argumentas - reikšmės su kuriomis funkcija iškviečiama (pvz.: `2`; `3, True`):

```
kvadratas(2)
kvadratas(3, True)
kvadratas(3, atspausdinti=True)
```

 * funkcijos grąžinamos reikšmės.


Žodynų ir sąrašų elementų panaudojimas.

```
zodynas = {}

for title in ['a', 'b', 'c', 'd']:
    x = int(input('Įveskite '+title+' taško x koordinatę'))
    y = int(input('Įveskite '+title+' taško y koordinatę'))
    zodynas[title] = [x, y]

print(zodynas)      # {'a': [0, 0], 'b': [0, 1], 'c': [1, 1], 'd': [2, 2]}

zodynas['a'][0]  # 0
zodynas['a'][1]  # 0

bx, by = zodynas['b']
```


### Septintosios pratybos
Failai ir jų metodai:
  * open() 
  * close()
  * read()
  * write()

```
In [46]: f = open('laikinas.txt', 'r')

In [47]: content = f.read()

In [48]: content
Out[48]: 'Labas pasauli,\nHello world!\nBandau įrašyti\n'

In [49]: content.split()
Out[49]: ['Labas', 'pasauli,', 'Hello', 'world!', 'Bandau', 'įrašyti']

In [50]: for zodis in content.split():
    ...:     zodis = zodis.strip('.,!?')
    ...:     print(zodis)

```


Konteksto valdytojas (context manager), pvz.: `with open('filname') as f:`

```
In [38]: with open('laikinas.txt', 'r') as f:
    ...:     print(f.read())
```

Simbolių eilučių metodai:
 * split()

 * strip()
```

In []: zodis = 'Labas,'                                                       
In []: zodis.strip('.,!?')
Out[]: 'Labas'                                                       
```

 * replace()

```
In []: zodis.replace('t', 'T')                                               
Out[]: 'Turinys'

In []: zodis.replace('t', '')                                                
Out[]: 'urinys'
```

 * lower()

```
In []: zodis = 'Labas'                                                       

In []: zodis.lower()                                                         
Out[]: 'labas'

In []: yra_didziuju = (zodis.lower() != zodis)                               

In []: yra_didziuju                                                          
Out[]: True
```

 * upper()

```
In []: zodis.upper()                                                         
Out[]: 'LABAS'
```

Simbolių eilučių formatavimas naudojant `f'{}'`.

### Aštuntosios pratybos
-

### Devintosios pratybos
Importavimo sakinys `import`

```
import math     # Standard library packages are available by default
print(math.pi)

from math import pi
print(pi)

from math import pi, sqrt, sin, cos
```

Paketu laikomi ir python failai einamajame kataloge. Importuojant
nereikia nurodyti failo plėtinio.

Paketu laikomi ir katalogai, esantys einamajame kataloge, jeigu juose yra
`__init__.py` failas.

Importuojant failą yra įvykdomas visas failo turinys išskyrus kodas po bloko:

```if __name__ == '__main__':```


Standartinės bibliotekos paketai `sys`, `os`, `math`:
  * `sys`
    * `argv` - argumentų sąrašas kuris buvo perduotas iškviečiant programą
    * `path` - vietos, kuriose ieškoma Python paketų
    * `version` - Python versija

  * `os` 
    * dir()
    * exists()
    * isfile()
    * join()
    * cwd()

  * `math` 
    * pi
    * cos()
    * sqrt()

Paketų įsidiegimas naudojant `pip`, pvz terminale įvykdant `pip install -u matplotlib`:

```
from matplotlib import pyplot as plt

xs = [0, 1, 0.5]
ys = [0, 0, 0.5]
plt.plot(xs, ys)
plt.show()
```



Jeigu parašote tą patį pasikartojantį kodą, tik su kitais kintamaisiais - tą kodą reikia
iškelti į funkciją. Funkcijų panaudojimo pavyzdžiai:

```
def dist(a, b):
    retrun math.sqrt(a**2 + b**2)
```

Jeigu kodas yra suskaidytas į funkcijas, funkcijoms gali būti rašomi automatiniai testai, pavyzdžiui:

```
def dist(a, b):
    retrun math.sqrt(a**2 + b**2)

def test_dist():
    assert dist([0,0], [1,0]) == 1
    assert dist([0,0], [3,4]) == 5

if `test` in sys.argv:
    test_dist()
```

Visos funkcijos prasidedančios `test_` gali būti surinktos ir įvykdytos
naudojant `pytest` paketą, kurį galima įsidiegti su `pip3 install pytest`.


### Dešimtosios pratybos
Klaidų (exception) sugavimas:

```
try:
    sarasas[100]
except IndexError as exc:
    print('Toks indeksas neegzistuoja')
```

Klaidų (exception) sukėlimas:

```
raise ValueException('Nekorektiški taškai')
```

Klaidos pakartotinis sukėlimas:

```
try:
    sarasas[100]
except IndexError:
    print('Toks indeksas neegzistuoja')
    raise
```



### Būsimos pratybos

Klaidų ieškojimas naudojant `import pdb; pdb.set_trace()`, debugerio veiksmai: `n`, `s`, `c`, `q`.

Papildytas Python interaktyvus interpretatorius: `ipython`.
