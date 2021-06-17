def howSum(sum, arr):
    if sum <0:
        return None
    if sum ==0:
        return []
    for num in arr:
        k = sum-num
        j = howSum(k,arr)
        if (j != None):
            j.append(num)
            return j
        
#time -> n^m *m
#space -> m

def howSum2(sum, arr, memo = {}):
    if sum in memo:
        return memo[sum]
    if sum <0:
        return None
    if sum ==0:
        return []
    for num in arr:
        k = sum-num
        j = howSum2(k,arr,memo)
        if (j != None):
            j.append(num)
            return j
        else:
            memo[k] = None
            
#time -> n *m *m
#space -> m*m

if __name__ == '__main__':
    print (howSum(3000, [7,2]))