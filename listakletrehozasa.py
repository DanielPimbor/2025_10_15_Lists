honapok = ['január', 'február','március', 'április','május','június']

print('---------------------------')
print(type(honapok))

print('---------------------------')
print(len(honapok))

print('---------------------------')
print(honapok[0])
print(honapok[1])
print(honapok[2])
print(honapok[3])

print('---------------------------')
print(f'Utolsó elem a listába:{honapok[-1]}')

print('---------------------------')
# az 1-es és 2-es indexű elemek kiíratása
print(honapok[1:3])

print('---------------------------')
# az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

print('---------------------------')
# az 1-es és 2-es indexű elemek kiíratása
print(honapok[2:])

print('---------------------------')
print(','.join(honapok))

print('---------------------------')
#lista bejárása , i = növekvő szám, for in range ciklussal
for i in range(len(honapok)):
    print(honapok[i])

print("----------Honapok-----------")

#itemsel
for honap in honapok:
    print(honap)





