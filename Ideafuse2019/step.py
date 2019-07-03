n = int(input())
for a in range(n):
    t = int(input())
    x = str(input())
    i = -1
    jum = 0
    while i < t:
        if i+1 == t:
            i += 1
        elif i+2 == t:
            i += 2
        else:
            if x[i+1] == '1':
                i += 1
            elif x[i+2] == '1':
                i += 2
            else:
                jum += 1
                i += 2
        # print(i)
    print("Case #{}: {}".format(a+1, jum))