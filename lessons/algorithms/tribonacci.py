memo = {

}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        f = fib(n-1) + fib(n-2) + fib(n-3)
        # adds last three numbers together
    memo[n] = f
    # adds it to the hash
    return f

print(fib(100))
