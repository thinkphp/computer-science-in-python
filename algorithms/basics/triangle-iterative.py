# Se citeste un numar natural nenul n. Sa se construiasca un triunghi isoscel ce contine caracterul * in felul urmator:

# - pe primul rand (cel mai de sus) se va pune caracterul *
# - pe fiecare rand se va pune cu doua caractere * mai mult
# decat pe randul superior si cu doua mai putin decat pe randul inferior.

def main():
	# solved iteratively
	n = 10
	line = 1
	space = n - 1
	c = 1
	while line <= n:
		for i in range(1,space+1):
			print(" ", end = "")
		for i in range(1, c + 1):
		    print("*", end = "")	
		print("")    
		line = line + 1
		space = space - 1
		c += 2
main()	
