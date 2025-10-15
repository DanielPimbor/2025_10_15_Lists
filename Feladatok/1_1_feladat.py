"""1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót,
és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket! """

szinek = ["zöld", "piros", "kék", "sárga"]
valasztott_szin = (str(input("Adj meg egy színt. ")))

if valasztott_szin in szinek:
    print('A színed már benne van a listában.')
    print(szinek)

elif valasztott_szin not in szinek:
    print('Nincsen benne a színed a listában.')
    print(szinek)

