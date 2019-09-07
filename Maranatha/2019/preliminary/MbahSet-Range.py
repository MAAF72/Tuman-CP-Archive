def Head() :
	print(" .--. ", end='')
	
def Body(N) :
	if N % 2 == 0 :
		print("|oo  |", end='')
	else :
		print("|  oo|", end='')
		
def Foot() :
	print("|/\/\|", end='')
	
N = int(input())

for i in range(N) :
	for j in range(N) :
		Head()
		#print(" ", end='')
	print()	
	for j in range(N) :
		Body(i + 1)
		#print(" ", end='')
	print()
	for j in range(N) :
		Foot()
		#print(" ", end='')
	print()
		