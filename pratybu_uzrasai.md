### Pirmosios pratybos
Algoritmas - veiksmų seka, kurią reikia atlikti norint gauti rezultatą.

Programa - konkrečių komandų 

Kintamasis - vieta atmintyje, kurioje galima išsaugoti reikšmę.

Python programavimo kalbos savybės:
 - interpretuojama - programos žingsniai vykdomi iš eilės.
 - dinamiškai tipizuojama - tas pats kintamasis gali turėti skirtingo tipo reikšmes.

Python programavimo standartas PEP8

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

Git commandos: `clone`, `pull`, `commit`, `push`, `status`, `log`. Versijavimo
sistemos naudojimo nauda: prieinamos senesnės kodo versijos, nors dirbama tik su
aktualia versija. Leidžia bendradarbiauti rašant kodą. [Git dokumentacija](https://git-scm.com/). Nemokamas Git repozitorijų talpinimas [GitLab](https://gitlab.com), [GitHub](https://github.com).

Duomenų struktūros: [`list` (sąrašas)](https://docs.python.org/3/tutorial/introduction.html#lists) ir [jo metodai](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists),
[`dict` (žodynas)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

[Funkcijos apibrėžimas](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

[`for` ir `while` ciklai](https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools).

Klaidų ieškojimas naudojant `import pdb; pdb.set_trace()`, veiksmai: `n`, `s`, `c`, `q`.

Papildytas Python interaktyvus interpretatorius: `ipython`.



