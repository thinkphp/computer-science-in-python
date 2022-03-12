# Se citeste un numar natural nenul n. Sa se construiasca un triunghi isoscel ce contine caracterul * in felul urmator:

# - pe primul rand (cel mai de sus) se va pune caracterul *
# - pe fiecare rand se va pune cu doua caractere * mai mult
# decat pe randul superior si cu doua mai putin decat pe randul inferior.

# solved recursively
def triangle(line, s, c):    
    if line <= n:
    	for i in range(1, s + 1):
    		print(" ", end ="")
    	for j in range(1, c + 1):
    	    print("*", end = "")
    	print("")     
    	triangle(line + 1, s - 1, c + 2)

def main():

	global n
	n = 10
	triangle(1, n - 1, 1) 

main()    
