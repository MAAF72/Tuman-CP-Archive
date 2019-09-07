import re

Inp = input()

X = re.findall("([0-9]*[0-9])", Inp)

#X = [[int(X[i]), int(X[i+1])] for i in range(0, len(X), 2)]

Sequence = []
#Overlap = []
OverlapIndex = -1
MaxOverlap = -1


for i in range(0, len(X), 2) :
	A = int(X[i])
	B = int(X[i + 1])

	if A > B :
		if i > 0 :
			if Sequence[-1][0] <= A <= Sequence[-1][1] :
				if B > Sequence[-1][1] :
					Sequence[-1][1] = B
			else :
				if OverlapIndex == -1 :
					OverlapIndex = len(Sequence)
					Sequence.append([A, 50])
		else :
			Sequence.append([A, B])
			
		#Overlap.append([0, B])
		MaxOverlap = max(MaxOverlap, B)
		
	else :
		if i > 0 :
			if Sequence[-1][0] <= A <= Sequence[-1][1] :
				if B > Sequence[-1][1] :
					Sequence[-1][1] = B
			else :
				Sequence.append([A, B])
		else :
			Sequence.append([A, B])

#print(Sequence)

i = 0
while True and MaxOverlap != -1 :
	if Sequence[i][1] < MaxOverlap :
		Sequence.pop(0)
	else :
		if Sequence[i][0] <= MaxOverlap :
			Sequence[-1][1] = Sequence[i][1]
			Sequence.pop(0)
		else :
			Sequence[-1][1] = MaxOverlap
		break

if len(Sequence) == 0 :
	print("[(0, 50)]")
else :
	print('[', end='')
	for i in range(len(Sequence) - 1) :
		print('({}, {}), '.format(Sequence[i][0], Sequence[i][1]), end='')
	print('({}, {})'.format(Sequence[len(Sequence) - 1][0], Sequence[len(Sequence) - 1][1]), end='')
	print(']')