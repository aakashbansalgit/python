arr = [1,2,3,4,5,6,7,8,9,10]
arr3 = []
for i in range (len(arr)):
        arr2 = []
        for j in range (i, len(arr)):
                arr2.append(arr[j])
                print(arr2)
                arr3.append(arr2[:])
arr3.sort()
print(arr3)