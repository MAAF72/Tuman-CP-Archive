n = int(input())
for i in range(n):
    x = int(input())
    print("Case #{}: {} triangle(s) with {} edges.".format(i+1, x-2, x+(x-3)))
