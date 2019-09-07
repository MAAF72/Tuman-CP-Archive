import re
n = int(input())
vocal = ['a', 'e', 'i','o','u',]
conso = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ng']
for a in range(n):
    new = ''
    newold = []
    old = str(input())
    old = re.split('(ng)', old)
    for i in old:
        if i != 'ng': newold.extend(list(i))
        else: newold.append(i)
    i = 0
    while i < len(newold) - 1:
        if (newold[i] in conso) and (newold[i+1] in conso):
            new = new + newold[i].upper() + newold[i+1].upper()
            i += 2
        elif (newold[i] in vocal) and (newold[i+1] in vocal):
            new = new + newold[i].upper() + newold[i+1].upper()
            i += 2
        else:
            new += newold[i]
            i += 1
    if i == len(newold) - 1:
        new += newold[i]
                
    print("Case #{}: {}".format(a+1, new))
