# int
# return the nth fib number
# recursion
memo = {

}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f

print(fib(121))

#iternative way

#def fib_i(n):
#    a,b = 0, 1
#    for i in range(0,n):
#        a, b = b, a+b
#    return a

#print(fib_i(4))
