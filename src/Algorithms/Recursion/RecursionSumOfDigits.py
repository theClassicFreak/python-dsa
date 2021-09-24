# Print sum of digits of a number
def sumOfDigits(n):
    assert n>=0 and int(n) == n , 'Number must be integer and +ve' 
    if (n<10):
        return n
    return (n%10) + sumOfDigits(int(n/10))

print(sumOfDigits(19834))