def canConstruct(string, arr):
    if string == '':
        return True
    for word in arr:
        if string.count(word)>0:
            m= string.index(word)
            if m == 0:
                newstring = string[len(word):]
                canConstruct(newstring, arr)
    return False

if __name__ == '__main__':
    print (canConstruct('abcdefg', ['abc','def','defg']))
        