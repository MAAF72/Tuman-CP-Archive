t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        somenum = list(map(int, input().split()))
        arr.append(somenum)
    ans = {"baris": 0, "kolom": 0}
    for x in range(n):
        baris = arr[x].count(1)
        kolom = [arr[k][x] for k in range(n)].count(1)
        if baris % 2 == 1: ans["baris"] += 1
        if kolom % 2 == 1: ans["kolom"] += 1
        # print("ans: ", baris, kolom)
    print("ans: ", max(ans["baris"], ans["kolom"]))