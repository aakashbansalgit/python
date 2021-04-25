from math import *
def func1(a):
    div1=[]
    for i in range (1,a+1):
        if n%i==0:
            div1.append(i)
    return div1
def func2(a):
    div2 = set()
    for i in range (1,int(sqrt(a))+1):
        if n%i==0:
            div2.add(i)
            div2.add(n//i)
    return list(div2)
    

t= int(input())
while t:
    n=int(input())
    div1=func1(n)
    print (*div1)
    div2=func2(n)
    print(*div2)
    t=t-1
    