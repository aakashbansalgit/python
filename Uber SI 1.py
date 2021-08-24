def func(base2):
    number = 0
    m = 1
    for el in base2:
        if el == True:
            number += m
        m=m*2
    out = []
    while number >0:
        k = number%6
        out.append(k)
        number = number//6
    return out
        
        


