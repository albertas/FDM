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
    $ python3 test1.py Vardas Pavardė jusu_programa.py

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
  * [`dict` (žodynas)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
  * `set` (aibė)
  * `tuple` (kortedžas arba sąrašas konstanta)

Immutable ir Mutable kintamųjų apibrėžimai.



### Būsimos pratybos

[Funkcijos apibrėžimas](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

Klaidų ieškojimas naudojant `import pdb; pdb.set_trace()`, debugerio veiksmai: `n`, `s`, `c`, `q`.

Papildytas Python interaktyvus interpretatorius: `ipython`.
