def gcd(n,m):
    if n == 0:
        return m
    return gcd(m%n,n)

def lcm(n,m):
    return n*m/gcd(n,m)


t=int(input())
while t:
    a,c = [int(a) for a in input().split()]
    print ("gcd = {} lcm = {}".format(gcd(a,c),lcm(a,c)))
    t=t-1
    