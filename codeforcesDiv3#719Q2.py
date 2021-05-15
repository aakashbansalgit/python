def countfunc(n):
    count = 0
    if n <10:
        return n
    else:
        count = 9
        while n>10:
            k = str(n)
            m = int("1"*len(k))
            count = count +int(n/m)
            n = int("9"*(len(k)-1))
    return count
        
            

if __name__ == '__main__':
    output = ""
    tests = int(input())
    for i in range (tests):
        n = int(input())
        count = countfunc(n)
        output = output + str(count) + "\n"
    print (output)
        

