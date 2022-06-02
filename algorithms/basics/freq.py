#
#
# Insertion Sort Technique
#
#

def sort( arr ):

	n = len(arr)

	for i in range(1, n):

		aux = arr[ i ]

		j = i - 1

		while j >= 0 and arr[ j ] >= aux:

			arr[ j + 1 ] = arr[ j ]

			j -= 1

		arr[ j + 1 ] = aux	

#
# Show Freq function
#		

def show_freq( arr ):

	n = len(arr)

	k = 0

	freq = [0] * (n+1)

	vec = [0] * (n+1)

	vec[k] = arr[k]

	freq[k] = 1

	for i in range( n - 1 ):

		if arr[ i ] == arr[ i + 1 ]:			

			freq[k] += 1
		else:

		    k += 1

		    vec[ k ] = arr[ i + 1 ]

		    freq[ k ] = 1

	for i in range( k + 1 ):

		if freq[ i ] == 1:

			print("Element %d apare o singura data"%(vec[i]))
		else:
			print("Element %d apare de %d ori"%(vec[i], freq[i]))

#
#
# Main Function
#
#
			
def main():

	arr = [5,4,3,2,1,2,13,41,5,6,41,17,8,19,0,-1,2,5,1]

	sort( arr )

	print( arr )

	show_freq( arr )

main()	
