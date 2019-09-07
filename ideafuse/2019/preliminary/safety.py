# def ceil(n):
#     res = int(n)
#     return res if res == n or n < 0 else res+1
import math

def dist(x1, y1, x2, y2, r):  
    return math.ceil((((((x2 - x1)** 2) + ((y2 - y1)** 2))**(0.5)) - r))

n = int(input())
for a in range(n):
    x1, y1, r = map(int, input().split())
    m = int(input())
    distance = 0
    for i in range(m):
        x2, y2 = map(int, input().split())
        if dist(x1, y1, x2, y2, r) > 0:
            distance += dist(x1, y1, x2, y2, r)
    print("Case #{}: {}".format(a+1, distance))
