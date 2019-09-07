Inp = int(input())

Result = 14000605
while Inp != -1 :
	Result -= Inp
	Inp = int(input())

if Result == 0 :
	print("Time to attack Then-Oz!")
elif Result > 0 :
	print(Result, "possibilities more!")
else :
	print("Hey Set-Range, enough travelling! This is too much!")