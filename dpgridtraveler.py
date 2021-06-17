def grid(n,m):
    if (n==1 and m==1):
        return 1
    if n==0:
        return 0
    if m ==0:
        return 0
    return grid(n-1,m)+grid(n,m-1)    
    
def grid2(n,m, memo = {}):
    key = str(m)+','+str(n)
    key2= str(n)+','+str(m)
    if (key in memo):
        return memo[key]
        if (key2 in memo):
        return memo[key2]
    if (n==1 and m==1):
        return 1
    if n==0:
        return 0
    if m ==0:
        return 0    
    memo[key] = grid2(n-1,m, memo)+grid2(n,m-1, memo)
    memo[key2] = memo[key]
    return memo[key]
        
if __name__ == '__main__':
    print (grid2(2,3))
    print (grid2(3,5))
    print (grid2(18,18))
    