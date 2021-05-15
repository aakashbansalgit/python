import math
 
def printSubsequences(arr, n) :
    opsize = math.pow(2, n)

    for counter in range( 1, (int)(opsize)) :
        for j in range(0, n) :
            if (counter & (1<<j)) :
                print( arr[j], end =" ")
         
        print()
 
arr = [1, 2, 3, 4]
n = len(arr)
print( "All Non-empty Subsequences")
 
printSubsequences(arr, n)