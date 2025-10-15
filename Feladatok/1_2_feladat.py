"""1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! 
Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg! """


szinek = ["zöld","zöld","kék","fekete", "piros", "kék", "sárga"]
valasztott_szin = (str(input("Adj meg egy színt. ")))

darabszam = szinek.count(valasztott_szin)

if darabszam > 0:
    print(f'A(z) {valasztott_szin} már benne van a listában {darabszam}-szor/szer.')
    print(szinek)

elif valasztott_szin not in szinek:
    print('Nincsen benne a színed a listában.')
    print(szinek)