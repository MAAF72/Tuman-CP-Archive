N = int(input())

for t in range(N) :
	K = int(input())
	B = int(input())
	
	Section1 = [0] * 26

	Section2 = [0] * 26

	Section3 = [0] * 26

	Section4 = [0] * 26
	
	Matrix = []
	
	for i in range(B) :	
		Line = input().split()
		Matrix.append(Line)
		
		#Upper
		if i < (B // 2) :
			#Left
			for j in range(0, K // 2) :
				Section1[ord(Line[j]) - ord('a')] += 1
			
			#Right
			for j in range(K // 2, K) :
				Section2[ord(Line[j]) - ord('a')] += 1
		else : #Lower
			#Left
			for j in range(0, K // 2) :
				Section3[ord(Line[j]) - ord('a')] += 1
			
			#Right
			for j in range(K // 2, K) :
				Section4[ord(Line[j]) - ord('a')] += 1
	
	SectionIndex = [-1] * 26
	
	for j in range(26) :
		Max = Section1[j]
		MaxIndex = 1
		
		if Section2[j] > Max :
			Max = Section2[j]
			MaxIndex = 2
		
		if Section3[j] > Max :
			Max = Section3[j]
			MaxIndex = 3
		
		if Section4[j] > Max :
			Max = Section4[j]
			MaxIndex = 4
			
		SectionIndex[j] = MaxIndex
		
		
	print(t + 1)
	for j in range(B) :
		for k in Matrix[j] :
			print("{}{} ".format(k, SectionIndex[ord(k) - ord('a')]), end='')
		print()