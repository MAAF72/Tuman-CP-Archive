import heapq

T = int(input())

for i in range(T) :
	N, K = map(int, input().split())
	
	A = [int(X) for X in input().split()]
	
	C = [0] * K
	
	heapq.heapify(C) 
	
	for j in A :
		heapq.heappush(C, heapq.heappop(C) + j) 
	
	Max = heapq.nlargest(1, C)
	
	print("Case #{}: {}".format(i + 1, Max[0]))
	