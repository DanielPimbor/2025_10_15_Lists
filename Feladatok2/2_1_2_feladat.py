szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

t_szavak = []

for elem in szavak:
    if elem.startswith("t") or elem.startswith("T"):
        print(elem)
        t_szavak.append(elem)

print(t_szavak)
