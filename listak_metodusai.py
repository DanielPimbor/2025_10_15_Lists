honapok = ['január', 'február','március', 'április','május','június']
print('1---------------------------')
#listavegere rakja
honapok.append('július')

print(honapok)
print('2---------------------------')
# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
honapok.pop()

torolt_honap = honapok.pop()

print(f'Utolsó hónap:{torolt_honap}')

print(f'Utolsó hónap törölve:{honapok}')

print('3---------------------------')

#index törlés
torolt_honap = honapok.pop(0)
print(torolt_honap)
print(honapok)

print('4---------------------------')

honapok.remove("február")
print(honapok)
honapok.insert(0, "február")
print(honapok)

print('5---------------------------')

del honapok[1]
print(honapok)

print('6---------------------------')
#empty list

honapok.clear()
print(honapok)

