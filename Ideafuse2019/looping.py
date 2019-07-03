import time

st = time.time()
x = 0
for i in range(10000000):
    if i % 2 == 0:
        x += i*i
    else:
        x -= 1
end = time.time()
print(end-st,"ms")