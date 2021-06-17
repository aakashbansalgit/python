def canSum(sum, arr):
    if sum <0:
        return False
    if sum ==0:
        return True
    for num in arr:
        if canSum(sum-num,arr):
            return True
    return False        
    
def canSum2(sum, arr, memo = {}):
    if sum in memo:
        return memo[sum]
    if sum <0:
        return False
    if sum ==0:
        return True
    for num in arr:
        k = sum-num
        if canSum2(k,arr, memo):
            return True
        else:
            memo[k]= False
    return False          

if __name__ == '__main__':
    print (canSum2(900,[17,7]))