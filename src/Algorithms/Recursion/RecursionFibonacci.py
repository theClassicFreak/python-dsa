# Print nth Fibonacci number
def fibonacci(n):
    assert n>=0 and int(n) == n , 'Fibonacci number index must be integer and +ve' 
    if n in [0,1]:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(20))