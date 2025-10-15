"""1.3 Feladat
Egészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó által megadott szín kerüljön felvételre a listába,
és csak ezután történjen meg a lista tartalmának kiírása! """

szinek = ["zöld","zöld","kék","fekete", "piros", "kék", "sárga"]
valasztott_szin = (str(input("Adj meg egy színt. ")))

darabszam = szinek.count(valasztott_szin)

if darabszam > 0:
    print(f'A(z) {valasztott_szin} már benne van a listában {darabszam}-szor/szer.')
    print(szinek)

elif valasztott_szin not in szinek:
    print('Nincsen benne a színed a listában.')
    szinek.append(valasztott_szin)
    print(szinek)