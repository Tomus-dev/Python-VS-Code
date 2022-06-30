
# Fibonacci

# def fib(n):
#     if (n <= 2):
#         return 1   
#     return fib(n - 1) + fib(n -2)
# print(fib(5))

# def dib(n):
#     if (n<=1):
#         return
#     dib(n-1)
#     dib(n-1)

# print(dib(5))

# memoization

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)

print(fib(40))



# https://www.youtube.com/watch?v=oBt53YbR9Kk