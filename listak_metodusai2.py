honapok = ['január', 'február','március', 'április','május','június']
honapok = [1, 3, 5, 2]

#sorbarendezés
sorted_honapok = (sorted(honapok))
print(honapok)
print(sorted_honapok)
# print(honapok.sort())
# print(honapok)

reversed_honapok = sorted(honapok, reverse=True)
print(reversed_honapok)

#az adot elem első elofordulasanak
print(honapok.index("március"))
print("április" in honapok)