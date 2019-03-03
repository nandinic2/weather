def expand(n):
    count = 0
    x = list(map(int,str(n)))
    stop = len(x) -1
    for num in x:
        count += 1
        num = x*10**count
        return num

#        arr = [num + x[count-1]*10**(count-1), "+" , x[count-2]*10**(count-2)

print(expand(591))
