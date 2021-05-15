def fib(n):
    a = 1
    b = 1
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return a

def fib2(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

def fib3(n, memo = {}):
    if n<=2:
        return 1
    else:
        if (n in memo):
            return momo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1)+fib(n-2);
    return memo[n] 
    

if __name__ == '__main__':
    print (fib(7))
    print (fib(1))
    print (fib(2))
    print (fib(10))
    print (fib(8))
    print (fib(6))
    print (fib2(7))
    print (fib2(1))
    print (fib2(2))
    print (fib2(10))
    print (fib2(8))
    print (fib2(6))
    print (fib3(7))
    print (fib3(1))
    print (fib3(2))
    print (fib3(10))
    print (fib3(8))
    print (fib3(50))