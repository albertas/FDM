# FDM Informatika I pratybos
##### Turinys

 1. [Užduotys](#užduotys)<br>
 2. [Pratybų įrašai](#pratybų_įrašai)<br>
 3. [Prisijungimas prie MIF kompiuterio](#prisijungimas_prie_mif_kompiuterio)<br>
 4. [Kodo įvykdymas](#kodo_įvykdymas)<br>
 5. [Užduočių atlikimas naudojant asmeninius kompiuterius (Windows)](#užduočių_atlikimas_naudojant_asmeninius_kompiuterius_(windows))<br>
 6. [Papildomiems įgūdžiams HackerRank.com](#papildomiems_įgūdžiams_hackerrank.com)<br>
 7. [Teorijos paskaitų puslapis](#teorijos_paskaitų_puslapis)<br>
 8. [Kontaktai](#kontaktai)<br>

<a name="užduotys"/>

### Užduotys

 - [1 užduoties variantai](https://klevas.mif.vu.lt/~tomukas/uzduotys/ruduo/uzd_1.html) (1 balas) iki 2020-10-13.
 - [2 užduoties variantai](https://klevas.mif.vu.lt/~tomukas/uzduotys/ruduo/uzd_2.html) (1 balas) iki 2020-10-27.
 - [3 užduoties variantai](https://klevas.mif.vu.lt/~tomukas/uzduotys/ruduo/uzd_3.html) (1 balas) iki 2020-11-10.
 - [4 užduoties variantai](https://klevas.mif.vu.lt/~tomukas/uzduotys/ruduo/uzd_4.html) (1 balas) iki 2020-12-01.
 - [5 užduoties variantai](https://klevas.mif.vu.lt/~tomukas/uzduotys/ruduo/uzd_5.html) (1 balas) iki 2020-12-22.

Už kiekvieną pavėluotą savaitę atsiskaityti maksimalus užduoties balas mažinamas po 10%.

Taip pat, yra galimybė gauti 1 papildomą balą iš pratybų už pratybų metu atliktą pristatymą Python
programavimo kalbos tematika. Apie būsimą pranešimą prašau el. paštu informuoti bent viena savaite
prieš pristatymą. Temą galite pasirinkti laisvai, pavyzdžiui tai gali būti pasirinktos
[Python bibliotekos](https://docs.python.org/3/library/index.html) arba asmeninio projekto pristatymas.

Jums priskirtų užduočių variantų numeriai bus atsiųsti el. paštu. Jeigu laiško negavote 
ar dar kartą norėtumėte sužinoti Jums priskirtų užduočių variantus terminale turite įvykdyti
komandas:

    git clone https://github.com/albertas/fdm
    python3 fdm/uzduotys.py Vardas Pavardė

Šias užduotis bus galima atsiskaityti [python.lt](https://python.lt) svetainėje. Svetainė sukurta
šioms pratyboms.

Taip pat, užduotis galite ištestuoti savo lokalioje aplinkoje, terminale įvykdydami tokias komandas:

    cd fdm
    git pull
    cd ..
    python3 fdm/test1.py Vardas Pavardė jusu_pirmoji_programa.py

įvykdžius šią komandą Jūsų programa bus patikrinta. Aptikus klaidų bus išvestas
pranešimas su kokia įvestimi programa veikė nekorektiškai. Sėkmės atveju bus atspausdintas 
pranešimas, kiek Jums skirta balų už šią užduotį. Atspausdintąjį pranešimą ir progarmos kodą
pranšau atsiųsti man el. paštu . Taip pat, jeigu kyla kokių nors
klausimų ar kėblumų, mielai į juos atsakysiu el. paštu **albertas.gimbutas@mif.vu.lt**.

Norėdami patikrinti kitas užduotis įvykdykite aukščiau nurodytą komandą, tik
atitinkamai pakeisdami `test1.py` į `test2.py`, `test3.py`, `test4.py` ir `test5.py`. Pavyzdžiui,

    python3 fdm/test2.py Vardas Pavardė jusu_antroji_programa.py
    python3 fdm/test3.py Vardas Pavardė jusu_trecioji_programa.py
    python3 fdm/test4.py Vardas Pavardė jusu_ketvirtoji_programa.py
    python3 fdm/test5.py Vardas Pavardė jusu_penktoji_programa.py

<a name="pratybų_įrašai"/>

### Pratybų įrašai
[2020-09-22 12:00](https://python.lt/static/videos/FDM_2020-09-22_1200.mp4)<br>
[2020-09-22 14:00](https://python.lt/static/videos/FDM_2020-09-22_1400.mp4)

[2020-09-29 14:00](https://python.lt/static/videos/FDM_2020-09-29_1400.mp4)

[2020-10-06 12:00](https://python.lt/static/videos/FDM_2020-10-06_1200.mp4)<br>
[2020-10-06 14:00](https://python.lt/static/videos/FDM_2020-10-06_1400.mp4)

[2020-10-13 12:00](https://python.lt/static/videos/FDM_2020-10-13_1200.mp4)<br>
[2020-10-13 14:00](https://python.lt/static/videos/FDM_2020-10-13_1400.mp4)

[2020-10-20 12:00](https://python.lt/static/videos/FDM_2020-10-20_1200.mp4)<br>
[2020-10-20 14:00](https://python.lt/static/videos/FDM_2020-10-20_1400.mp4)

[2020-10-27 12:00](https://python.lt/static/videos/FDM_2020-10-27_1200.mp4)<br>
[2020-10-27 14:00](https://python.lt/static/videos/FDM_2020-10-27_1400.mp4)

<a name="prisijungimas_prie_mif_kompiuterio"/>

### Prisijungimas prie MIF kompiuterio
1. Turite sužinoti savo studento pažymėjimo numerį lsp.lt svetainėje, jis taip pat pateiktas ant LSP pažymėjimo.
2. Susikurti savo VU paskyrą: [id.vu.lt](https://id.vu.lt) puslapyje
3. Turite susikurti savo MIF paskyrą: [https://radius.mif.vu.lt/passwd2](https://radius.mif.vu.lt/passwd2) puslapyje.
4. Naudodami MIF paskyrą galite prisijungti prie:  **linux (vnc)**

<a name="kodo_įvykdymas"/>

### Kodo įvykdymas
Programas galite redaguoti su Gedit arba Notepad:
1. Terminale (ar Git Bash'e) parašykite: `gedit failo_vardas.py`
2. Parašykite programą, pavyzdžiui `print('Labas')`.
3. Išsaugokite failą paspausdami **Ctrl+s**.
4. Atidarykite kitą terminalo langą ir parašykite: `python3 failo_vardas.py`
Bus įvykdyta Jūsų programa.
5. Gedit nustatymuose pasikeiskite, kad tabuliacijos simboliai būtų pakeičiami į 4 tarpus.

Python veikimą galite išbandyti ir su interaktyviu Python interpretatoriumi:
1. Atidarykite Terminalo langą.
2. Parašykite **python3**. Atsidarys interaktyvus interpretatorius, kuris
iš karto įvykdo Jūsų įvestas komandas.

Programos kodą taip pat galite rašyti ir įvykdyti svetainėse:
* [python.lt](https://python.lt)
* [repl.it](https://repl.it/languages/Python3)


<a name="užduočių_atlikimas_naudojant_asmeninius_kompiuterius_(windows)"/>

### Užduočių atlikimas naudojant asmeninius kompiuterius (Windows)
1. Įsidiekite [Python](https://www.python.org/downloads/). Įsitikinkite, kad
   diegiant yra pasirinkta *Add Python to environement variables*.
2. Įsidiekite [Git bash](https://gitforwindows.org/).
    Git bash yra Terminalo atitikmuo.
3. Git bash (Terminale) vietoje `python3` naudokite tiesiog `python`, nes
   `python3` komanda bus nerasta.
4. Įrašykite `export PYTHONIOENCODING=utf-8` eilutę į `~/.bashrc` failą
   (sukurti jeigu neegzistuoja), kad būtų tinkamai spausdinami lietuviški simboliai.
   Arba Terminale įvykdykite `export PYTHONIOENCODING=utf-8` komandą prieš
   vykdydami Python komandas.

<a name="papildomiems_įgūdžiams_hackerrank.com"/>

### Papildomiems įgūdžiams HackerRank.com
Programavimo pradmenims įgauti ir žinioms gilinti egzistuoja puikus
https://HackerRank.com tinklapis. Jame galima programuoti ir testuoti užduočių
sprendimus. Programavimo užduotys sugrupuotos pagal tematiką, sudėtingumą.
Python programavimo kalbos galima išmokti atlikus užduotis:
https://HackerRank.com/domains/python

<a name="teorijos_paskaitų_puslapis"/>

### Teorijos paskaitų puslapis:
https://klevas.mif.vu.lt/~tomukas/paskaitos/Informatika1.html

<a name="kontaktai"/>

### Kontaktai
El. paštas:  **albertas.gimbutas@mif.vu.lt**


