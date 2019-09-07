def Josephus(N, K) :
	if N == 1 :
		return 0
	elif K == 1 :
		return N - 1
	else :
		Count = 1
		if K <= N :
			Count = N // K
		
		First = (K - 1) % N
		
		Last = First + (K * (Count - 1))
		
		Next = Last + 1
		
		Result = Josephus(N - Count, K)
		
		if (Next + Result) < N :
			return Next + Result
		else :
			Result -= (N - Next)
			Block = Result // (K - 1)
			IndexBlock = Result % (K - 1)
			return (Block * K) + IndexBlock

Inp = input().split()

print(Josephus(int(Inp[0]), int(Inp[1]) + int(Inp[2])) + 1)