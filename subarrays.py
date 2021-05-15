count = 0
for i in range (len(arr)+1):
    for j in range (i+1, len(arr)+1):
        arr2 = arr[i:j]
        m = 0
        for k in range len(arr2):
            m+= arr2[k]
            if k == Value:
                count +=1
            

