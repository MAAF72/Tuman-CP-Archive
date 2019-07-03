n = int(input())
huruf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(n):
    x = int(input()) - 1
    letters = ''
    while x > 25:
        s = (x % 26)
        x = x // 26 - 1
        letters = huruf[s] + letters
    letters = huruf[x] + letters
    print("Case #{}: {}".format(i+1, letters))