"""2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában,
a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, 
és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
"""

import random

szamok = [random.randint(1,3) for _ in range(10)]
print(szamok)

ujszam = int(input('Adj meg egy számot [1;3] intervallumon.'))


if ujszam in szamok:
    for i in range(szamok.count(ujszam)):
        szamok.remove(ujszam)
    print(szamok)

elif ujszam not in szamok:
    print('Nincs benne a szám.')

