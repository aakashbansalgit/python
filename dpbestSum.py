def bestSum(sum, arr):
    if sum <0:
        return None
    if sum ==0:
        return []
    result = None
    for num in arr:
        k = sum-num        
        j = bestSum(k,arr)
        if (j != None):
            j.append(num)
            d = j
            if (result == None or len(d)<len(result)):
                result = d
    return result

#time -> n^m *m
#space -> m*m

def bestSum2(sum, arr, memo={}):
    if sum in memo:
        return memo[sum]
    if sum <0:
        return None
    if sum ==0:
        return []
    result = None
    for num in arr:
        k = sum-num        
        j = bestSum2(k,arr,memo)
        if (j != None):
            d = j[:]
            d.append(num)
            if (result == None or len(d)<len(result)):
                result = d[:]
    memo[sum] = result
    return result

#time -> n^m *m
#space -> m

if __name__ == '__main__':
    # memo = {}
    # print (bestSum2(100,[1,3,2,25]))
    # memo = {}
    # print (bestSum2(100,[1,3,2,4,7]))
    # memo = {}
    # print (bestSum2(100,[1,3,2,4,5,25]))
    # memo = {}
    print (bestSum2(100,[1,3,2,4,50]))
