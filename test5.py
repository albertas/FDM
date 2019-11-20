#! coding: utf-8
import sys
import os
from sys import version, argv, path
from random import seed, choice, shuffle, randint, random
from unittest.mock import patch, MagicMock
import importlib
from io import StringIO
from datetime import datetime
from os import getcwd


if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if len(argv) < 4:
    print('Paleisdami nurodykite savo vardą, pavardę bei failą, kuriame yra Jūsų kodas, pvz:')
    print('python3 test5.py Vardas Pavardė failas.py')
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
        [
'''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
''',
         '24'],
    ],
    2: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         '69'],
    ],
    3: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         '68']
    ],
    4: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt\n',
        'meroL muspi rolod tis ,tema rutetcesnoc gnicsipida ,tile des od domsuie ropmet tnudidicni'],
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est LABORUM.\n',
        'meroL muspi rolod tis tema rutetcesnoc gnicsipida tile des od domsuie ropmet tnudidicni tu erobal te erolod angam auqila tU mine da minim mainev siuq durtson noitaticrexe ocmallu sirobal isin tu piuqila xe ae odommoc tauqesnoc siuD etua eruri rolod ni tiredneherper ni etatpulov tilev esse mullic erolod ue taiguf allun rutairap ruetpecxE tnis taceacco tatadipuc non tnediorp tnus ni apluc iuq aiciffo tnuresed tillom mina di tse'],
    ],
    5: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
        'reprehenderit'],
    ],
    6: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
        'Lorem ipsum dolor magna minim irure dolor velit nulla culpa'],
    ],
    7: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt\n',
        'do'],
    ],
    8: [
        ['lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         'lprfm jpsvm dplpr sjt bmft, cpnsfctftvr bdjpjscjng fljt, sfd dp fjvsmpd tfmppr jncjdjdvnt vt lbbprf ft dplprf mbgnb bljqvb. ut fnjm bd mjnjm vfnjbm, qvjs npstrvd fxfrcjtbtjpn vllbmcp lbbprjs njsj vt bljqvjp fx fb cpmmpdp cpnsfqvbt. dvjs bvtf jrvrf dplpr jn rfprfhfndfrjt jn vplvptbtf vfljt fssf cjllvm dplprf fv fvgjbt nvllb pbrjbtvr. excfptfvr sjnt pccbfcbt cvpjdbtbt npn prpjdfnt, svnt jn cvlpb qvj pffjcjb dfsfrvnt mplljt bnjm jd fst lbbprvm.']
    ],
    9: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         'Lorem ipsum dolor sit amet, conse6tetur adipiscing elit, sed do eiusmod tempo6 incididunt ut labore et dolore magna aliqua. Ut enim ad minim venia6, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo conse6uat. Duis aute irure dolor in repre6ender6t in voluptate velit esse cillum dolor6 eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'],
    ],
    10: [
        ['Lor1m ipsum dolor sit am1t, consect1tur adipiscing el2t, sed do eiusmod tempor incid2dunt ut labore et dol2re magna aliqua. Ut 3nim ad minim veniam, q3is nostrud exercitation 3llamco lab3ris nisi ut aliquip ex ea c1mm2do c3ns1qu2t Duis aute irure dolor in reprehenderit in voluptate v1lit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         'LorAm ipsum dolor sit amAt, consectAtur adipiscing elBt, sed do eiusmod tempor incidBdunt ut labore et dolBre magna aliqua. Ut Cnim ad minim veniam, qCis nostrud exercitation Cllamco labCris nisi ut aliquip ex ea odBmmAc tBuqAsnCc Duis aute irure dolor in reprehenderit in voluptate vAlit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.']
    ],
    11: [
        ['Lorem ipsum doaor sit amet, consectetur adapiscing elit, sed do eiasmod tempor incididunt ut laaore et dolore magna aliqua. Ut enim ad miaim veniam, quis noatrud exercitation ullamco laaoris nisi ut aliquip ex ea coaaodo consequat. Duis auae irure dolor in reprehenaerit in voluptate velit esae cillum doaore eu fugiat nulla pariatur. Exaepteur sint occaecat cupidatat non proident, sunt in culpa qui ofaicia deserunt moalit anim id est laborum.\n',
         'doaoradapiscing eiasmodlaaore miaimnoatrud laaoriscoaaodo auaeesae doaoreExaepteur ofaiciamoalit']
    ],
    12: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
        'meroL muspi rolod tema rutetcesnoc gnicsipida tile domsuie ropmet tnudidicni erobal erolod angam auqila minim mainev durtson noitaticrexe ocmallu sirobal piuqila odommoc tauqesnoc rolod tiredneherper etatpulov tilev mullic erolod taiguf allun rutairap ruetpecxE tnis taceacco tatadipuc tnediorp tnus apluc aiciffo tnuresed tillom murobal']
    ],
    13: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
        'aliqua minim esse non'],
    ],
    14: [
        ['Lorem ipsum dolllllllllllllor sit amet, connnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnsectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolllllllllore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ulllllllllllllllllllllamco laboris nisi ut aliquip ex ea commmmmmodo consequat. Duis aute irure dolllllllllllllor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Exxxxxxxxcepteur sint occaecat cuuuuupidatat non proident, sunt in culpa qui offffficia deserunt mollit anim id est laborum.\n',
         'Lorem ipsum dol$12or sit amet, con$36sectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dol$8ore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ul$20amco laboris nisi ut aliquip ex ea com$5odo consequat. Duis aute irure dol$12or in reprehenderit in voluptate velit es$1e cil$1um dolore eu fugiat nul$1a pariatur. Ex$7cepteur sint oc$1aecat cu$4pidatat non proident, sunt in culpa qui of$4icia deserunt mol$1it anim id est laborum' ],
    ],
    15: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         'amet, adipiscing elit, do tempor incididunt ut labore et dolore aliqua. Ut enim ad veniam, quis exercitation nisi ut ex ea. Duis aute in in esse cillum dolore eu fugiat pariatur. sint occaecat proident, sunt in deserunt mollit anim id.']
    ],
    16: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         'Lorem ipsum dolor sit, consectetur, sed eiusmod magna. minim, nostrud ullamco laboris aliquip commodo consequat. irure dolor reprehenderit voluptate velit nulla. Excepteur cupidatat non, culpa qui officia est laborum.']
    ],
    17: [
        ['Lorem ipsum dolor sit amet, consectetur (adipiscing elit), sed do eiusmod tempor incididunt ut labore (et dolore magna aliqua). Ut enim ad minim veniam, quis (nostrud exercitation) ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         'Lorem ipsum dolor sit amet, consectetur (), sed do eiusmod tempor incididunt ut labore (). Ut enim ad minim veniam, quis () ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.']
    ],
    18: [
        ['Lorem ipsum dolor sit amet, consectetur (adipiscing elit), sed do eiusmod tempor incididunt ut labore (et dolore magna aliqua). Ut enim ad minim veniam, quis (nostrud exercitation) ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
         'meroL muspi rolod tis tema, rutetcesnoc gnicsipida tile, des od domsuie ropmet tnudidicni tu erobal te erolod angam auqila. tU mine da minim mainev, siuq durtson noitaticrexe ocmallu sirobal isin tu piuqila xe ae odommoc tauqesnoc. siuD etua eruri rolod ni tiredneherper ni etatpulov tilev esse mullic erolod ue taiguf allun rutairap. ruetpecxE tnis taceacco tatadipuc non tnediorp, tnus ni apluc iuq aiciffo tnuresed tillom mina di tse murobal.']
    ],
    19: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserundt mollit anim id est laborulm.\n',
         'do ut et Ut ad ut ex ea in in eu in deserundt id laborulm']
    ],
    20: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserundt mollit anim id est laborulm.\n',
         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed eiusmod tempor incididunt labore dolore magna aliqua. enim minim veniam, quis nostrud exercitation ullamco laboris nisi aliquip commodo consequat. Duis aute irure dolor reprehenderit voluptate velit esse cillum dolore fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt culpa qui officia deserunt mollit anim est laborum.']
    ],
    21: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n',
        '30 consectetur adipiscing eiusmod tempor incididunt labore dolore aliqua veniam nostrud exercitation ullamco laboris aliquip commodo consequat reprehenderit voluptate cillum dolore fugiat pariatur Excepteur occaecat cupidatat proident officia deserunt mollit laborum']
    ],
    22: [
        [
'''Lorem ipsum dolor: sit amet
consectetur adipiscing: elit
sed do eiusmod tempor incididunt ut labore: et dolore magna aliqua
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia: deserunt mollit anim id est laborum
''',
'''Lorem ipsum dolor:
consectetur adipiscing:
sed do eiusmod tempor incididunt ut labore:
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia:
''']
    ],
    23: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temporincididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quisnostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eufugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui officia deserunt mollit anim id est laborum.\n',
         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, seddo eiusmod temporincididunt ut laboreet dolore magnaaliqua. Ut enim ad minim veniam, quisnostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum doloreeufugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui officia deserunt mollit anim id est laborum.']
    ],
    24: [
        ['Lorem ipsum dolor sit amet, conse- ctetur adipiscing elit, sed do eiusmod tempori- ncididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quisn- ostrud exerci- tation ullamco laboris nisi ut aliquip ex ea commo- do consequat. Duis aute irure dolor in repreh- enderit in voluptate velit esse cillum dolore eufugiat nulla pariatur. Excepteur sint occaecat cupid- atat non proident, sunt inculpa qui officia dese- runt mollit anim id est laborum.\n',
         'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temporincididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quisnostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eufugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui officia deserunt mollit anim id est laborum.']
    ],
    25: [
        ['Lor1m ipsum d2lor sit amet, cons3ct4tur adipiscing el5t, sed do eiu6mod temporin7ididunt ut lab8re et dol9re m0gna aliqua. Ut enim ad min1m veniam, quisn22strud exerc3itation ull4mco laboris ni5si ut al6iquip ex ea commodo con7sequat. D8uis aute iru1re dolor in repre3henderit in voluptate velit esse ci6llum dolore eufugiat nulla pariat8ur. Except9eur sint occa0ecat cupidat1at non pro3ident, sunt inculpa qui of5ficia des3erunt mollit a6nim id est la00borum.\n',
         'LorLm ipsum ddlor sit amet, conscctctur adipiscing elet, sed do eiuemod temporintididunt ut lablre et doldre mmgna aliqua. Ut enim ad minmm veniam, quisnqqstrud exerceitation ullumco laboris ninsi ut alaiquip ex ea commodo concsequat. DDuis aute iruire dolor in reprerhenderit in voluptate velit esse cicllum dolore eufugiat nulla pariatpur. ExceptEeur sint occaoecat cupidatcat non propident, sunt inculpa qui ofoficia desderunt mollit aanim id est lallborum.']
    ],
    26: [
        ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temporincididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quisnostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eufugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui officia deserunt mollit anim id est laborum.\n',
         'minim esse non']
    ],
    27: [
        ['Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod temporincididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quisnostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eufugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt inculpa qui officia deserunt mollit anim id est laborum\n',
         'laborum est id anim mollit deserunt officia qui inculpa sunt proident non cupidatat occaecat sint Excepteur pariatur nulla eufugiat dolore cillum esse velit voluptate in reprehenderit in dolor irure aute Duis consequat commodo ea ex aliquip ut nisi laboris ullamco exercitation quisnostrud veniam minim ad enim Ut aliqua magna dolore et labore ut temporincididunt eiusmod do sed elit adipiscing consectetur amet sit dolor ipsum Lorem']
    ],
    28: [
        ['Lorem 1psum dolor sit 2met consectetur adipiscing 3lit sed do eiusmod 4emporincididunt ut labore 5t dolore magna 6liqua Ut enim ad 7inim veniam 8uisnostrud exercitation 9llamco laboris nisi ut aliquip ex ea 10ommodo 0consequat Duis aute 1irure dolor in 2reprehenderit 3in voluptate velit 4esse cillum dolore 5eufugiat nulla 6pariatur Excepteur sint 7occaecat cupidatat 8non proident 9sunt inculpa 0qui officia 1deserunt mollit 2anim id 3est laborum\n',
         'Lorem dolor sit consectetur adipiscing sed do eiusmod ut labore dolore magna Ut enim ad veniam exercitation laboris nisi ut aliquip ex ea Duis aute dolor in voluptate velit cillum dolore nulla Excepteur sint cupidatat proident inculpa officia mollit id laborum']
    ],
    29: [
        ['Lorem 1psum dolor sit 2met consectetur adipiscing 3lit sed do eiusmod 4emporincididunt ut labore 5t dolore magna 6liqua Ut enim ad 7inim veniam 8uisnostrud exercitation 9llamco laboris nisi ut aliquip ex ea 10ommodo 0consequat Duis aute 1irure dolor in 2reprehenderit 3in voluptate velit 4esse cillum dolore 5eufugiat nulla 6pariatur Excepteur sint 7occaecat cupidatat 8non proident 9sunt inculpa 0qui officia 1deserunt mollit 2anim id 3est laborum\n',
         'Lorem musp1 dolor sit tem2 consectetur adipiscing til3 sed do eiusmod tnudidicniropme4 ut labore t5 dolore magna auqil6 Ut enim ad mini7 veniam durtsonsiu8 exercitation ocmall9 laboris nisi ut aliquip ex ea odommo01 tauqesnoc0 Duis aute eruri1 dolor in tiredneherper2 ni3 voluptate velit esse4 cillum dolore taigufue5 nulla rutairap6 Excepteur sint taceacco7 cupidatat non8 proident tnus9 inculpa iuq0 officia tnuresed1 mollit mina2 id tse3 laborum']
    ],
    30: [
        ['Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod temporincididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quisnostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eufugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt inculpa qui officia deserunt mollit anim id est laborum\n',
         'amet elit dolore enim nisi commodo Duis aute esse dolore sint occaecat sunt anim']
    ],
    31: [
        ['Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniamve quis nostrudno exercitation ullamco laboris nisni ut aliquip ex ea commodco consequat Duis aute irureir dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborumla\n',
         'do ut et Ut ad veniamve nostrudno nisni ut ex ea commodco irureir in in eu in id laborumla']
    ],
    32: [
        ['Lorem ipsum dolor msit amet, consectetur adipiscing elit, msed do eiusmod mtempor incididunt ut labore et dolore magna maliqua. Ut enim ad minim veniam, quis mnostrud exercitation mullamco laboris nisi ut aliquip ex ea mcommodo consequat. Duis aute irure dolor in reprehenderit in voluptate mvelit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa mqui officia deserunt mollit manim id est laborum.\n',
         '13']
    ],
    33: [
        ['Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum\n',
         'dolor consectetur adipiscing incididunt dolore magna aliqua minim exercitation ullamco nisi aliquip commodo irure dolor reprehenderit voluptate esse cillum dolore nulla pariatur Excepteur occaecat cupidatat non officia deserunt mollit']
    ],
    34: [
         ['Lorem musp1 dolor sit tem2 consectetur adipiscing til3 sed do eiusmod tnudidicniropme4 ut 1labore t5 dolore mag0na auqil6 Ut enim ad mini7 veniam durtsonsiu8 exercitation ocmall9 labor1is nisi ut aliquip ex ea odommo01 tauqesnoc0 Duis aute eruri1 dolor in tiredneherper2 ni3 voluptate velit esse4 cillum dolore taigufue5 nulla rutairap6 Excepteur sint taceacco7 cupidatat non8 proident tnus9 inculpa iuq0 officia tnuresed1 mollit mina2 id tse3 laborum\n',
          'musp1 tem2 til3 tnudidicniropme4 1labore t5 mag0na auqil6 mini7 durtsonsiu8 ocmall9 labor1is odommo01 tauqesnoc0 eruri1 tiredneherper2 ni3 esse4 taigufue5 rutairap6 taceacco7 non8 tnus9 iuq0 tnuresed1 mina2 tse3']
    ],
    35: [
         ['Lorem musp1 dolor sit tem2 consectetur adipiscing til3 sed do eiusmod tnudidicniropme4 ut 1labore t5 dolore mag0na auqil6 Ut enim ad mini7 veniam durtsonsiu8 exercitation ocmall9 labor1is nisi ut aliquip ex ea odommo01 tauqesnoc0 Duis aute eruri1 dolor in tiredneherper2 ni3 voluptate velit esse4 cillum dolore taigufue5 nulla rutairap6 Excepteur sint taceacco7 cupidatat non8 proident tnus9 inculpa iuq0 officia tnuresed1 mollit mina2 id tse3 laborum\n',
          'Lorem dolor sit consectetur adipiscing sed do eiusmod ut dolore Ut enim ad veniam exercitation nisi ut aliquip ex ea Duis aute dolor in voluptate velit cillum dolore nulla Excepteur sint cupidatat proident inculpa officia mollit id laborum']
    ],
    36: [
         ['Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum\n',
          'Lorem ipsum dolor sit consectetur sed eiusmod magna minim nostrud ullamco laboris aliquip commodo consequat irure dolor reprehenderit voluptate velit nulla Excepteur cupidatat non culpa qui officia est laborum 29']
    ],
    37: [
         ['Lorem ipsum dolor sit amet consectetur Adipiscing elit sed Do eiusmod temPor incididunt ut laBore et DOLORE magna aLiqua Ut enim ad minim veniam quis Nostrud exerciTation ullamco laBoris nisI ut Aliquip ex ea commodo consequat Duis aute irure dolor IN reprehenderit in voluptatE velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum\n',
          'Lorem Adipiscing Do temPor laBore DOLORE aLiqua Ut Nostrud exerciTation laBoris nisI Aliquip Duis IN voluptatE Excepteur 17']
    ]
}
test_data = data[u5]
shuffle(test_data)
path.append(getcwd())

print(f'Testuojama ({u5}): ', end='')
for inputs, expected_result in test_data:
    def input_mock(prompt=None):
        for i in inputs:
            yield str(i)

    def file_content(type_=str):
        lines = [l + '\n' for l in inputs.split('\n') if l]
        if type_ == list:
            yield lines
        elif type_ == iter:
            yield iter(lines)
        else:
            yield inputs

    write_file = StringIO()
    def do_nothing():
        pass
    write_file.close = do_nothing
    def open_method(file, mode='r', *args, **kwargs):
        if mode == 'r':
            m = MagicMock()
            m.read.side_effect = file_content()
            m.__enter__().read.side_effect = file_content()
            m.readlines.side_effect = file_content(list)
            m.__iter__.side_effect = file_content(iter)
            m.close.side_effect = do_nothing
            return m
        return write_file

        # print(args)
        # print(kwargs)
        # pass

    result = None
    with patch('builtins.open') as open_mock, patch('sys.stdout', new=StringIO()) as output_mock:
        open_mock.side_effect = open_method

        i = importlib.import_module(package)
        package_file = i.__file__
        del sys.modules[package]

        result = write_file.getvalue()

    with open(i.__file__) as code_file:
        code = code_file.read()
        if 'def' not in code:
            print('\n\nPrograma netenkina reikalavimų, nes nėra panaudota funkcija.\n')
            exit()
        elif 'open' not in code:
            print('\n\nPrograma netenkina reikalavimų, nes žodžius turite nuskaityti iš failo ir rezultatą įrašyti į failą.\n')
            exit()

    def not_empty_words(text):
        return [w.strip('.,?!') for w in text.split() if w]

    if not_empty_words(expected_result) != not_empty_words(result):
        print('\nPrograma veikia nekorektiškai, kai nuskaitomo failo turinys yra:\n', ''.join([str(i) for i in inputs]))
        print('\n\nTikėtąsi:\n', expected_result, '\n\n, o gauta:\n', result)
        exit()
    else:
        print('+', end='')
        sys.stdout.flush()

print(f'\nSveikinu! {" ".join(argv[1:-1])} atsiskaitė 5`ąją užduotį ({filename} {u5}-{randint(100,999)}).')
score = 10
if datetime.now().isocalendar()[1] > 51:
    score -= datetime.now().isocalendar()[1] - 51
print(f'Jums už šią užduotį skirtas {score/10:g} balas.')
