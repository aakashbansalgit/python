import math

def func(xa,xb,A,B):
    return (math.ceil(A/xa)+math.ceil(B/xb))
    
    
if __name__ == '__main__':
    k = int(input())
    for i in range (k):
        arr = input()
        arr = list(map(int,arr.split(' ')))
        m = func(arr[0],arr[1],arr[2],arr[3])
        print (m)
        