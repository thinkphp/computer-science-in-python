def func( n ):
	
    def bin( n ):
	
	    if n != 0 :
	    	
	    	bin( n // 2 )
	    	
	    print( n % 2, end = "" )
	    
    bin( n )
    
func(8)	    
