def main():
	fin = open('algsort.in','r')	
	fout = open('algsort.out','w')
	N = int(fin.readline().strip())
	arr = fin.readline().strip().split(" ")
	#arr = list(map(int, arr)) 
	arr = [int(i) for i in arr]	
	#arr.sort()
	#for i in arr:
	#	fout.write(str(i) + " ")
	print(arr)
	finished = False
	size = N
	while not finished == True:
		swapped = 0
		i = 0
		while i < size - 1:
			if arr[i] > arr[i+1]:
				aux = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = aux
				swapped = 1
			i += 1
		if swapped == 1:
		   size -= 1
		else:
		   finished = True
	for i in arr:
		fout.write(str(i) + ' ')

main()	
