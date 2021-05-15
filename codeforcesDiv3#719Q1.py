
def suspecion(n,st):
    for i in range (n-1):
        m = 0
        for j in range (i+1,n):
            if st[i] != st[j]:
                m = 1
            if (st[i] == st[j]) and m == 1:
                return "NO"
    return "YES"


if __name__ == '__main__':
    output = ""
    tests = int(input())
    for tests_itr in range(tests):
        n = int(input())
        st = input()
        output = output + suspecion(n, st) +"\n"
    print (output)            
            
                
            