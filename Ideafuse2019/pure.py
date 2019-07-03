MAX = 1000001; 

factor = [0]*(MAX + 1); 

def generatePrimeFactors(): 
    factor[1] = 1; 

    for i in range(2,MAX): 
        factor[i] = i; 

    for i in range(4,MAX,2): 
        factor[i] = 2; 

    i = 3; 
    while(i * i < MAX):
        if (factor[i] == i):
            j = i * i; 
            while(j < MAX):
                if (factor[j] == j): 
                    factor[j] = i; 
                j += i; 
        i+=1; 

def calculateNoOFactors(n): 
    if (n == 1): 
        return 1; 
    ans = 1; 

    dup = factor[n]; 

    c = 1; 

    j = int(n / factor[n]); 

    while (j > 1):
        if (factor[j] == dup): 
            c += 1; 

        else: 
            dup = factor[j]; 
            ans = ans * (c + 1); 
            c = 1; 

        j = int(j / factor[j]); 

    ans = ans * (c + 1); 

    return ans; 

if __name__ == "__main__": 

    generatePrimeFactors()
    print(factor)

    # n = int(input())
    # for a in range(n):
    #     l, r, k = map(int, input().split())
    #     jumlah = 0
        # for i in range(l,r+1):
        #     x = calculateNoOFactors(i)-1
        #     if x == k:
        #         jumlah += 1
        #         print(i)
        # print("Case #{}: {}".format(a+1, jumlah))

