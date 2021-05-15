def countfunc(n,arr):
    count = 0
    for i in range (n-1):
        for j in range (i+1,n):
            if arr[j]-arr[i] == j-i:
                count = count+1
    return count
    
if __name__ == '__main__':
    output = ""
    tests = int(input())
    for i in range (tests):
        n = int(input())
        arr = input()
        arr = list(map(int,arr.split(' ')))
        count = countfunc(n,arr)
        output = output + str(count) + "\n"
    print (output)