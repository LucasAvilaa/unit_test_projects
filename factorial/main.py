from functools import reduce
from operator import mul

# Option 1
def factorial_1(n):
    if n < 0:
        return "It is impossible to calculate the factorial of a negative number."

    result = 1

    for l in range(1, n + 1): result *= l
    
    return result

# Option 2
def factorial_2(n):
    if n < 0:
        return "It is impossible to calculate the factorial of a negative number."

    result = 1

    while n > 1: 
        result *= n
        n -= 1
    return result

# Option 3
def factorial_3(n):
    if n < 0:
        return "It is impossible to calculate the factorial of a negative number."
    elif n in (0, 1):
        return 1
    else:
        return n * factorial_3(n - 1)

# Option 4
def factorial_4(n):
    if n < 0: 
        return "It is impossible to calculate the factorial of a negative number."
        
    return reduce(lambda x, y : x * y, range(1, n + 1)) if n >= 1 else 1

# Option 5
def factorial_5(n):
    if not isinstance(n, int):
        return "Enter a number equal to or greater than 0"
    if n < 0: 
        return "It is impossible to calculate the factorial of a negative number."

    return reduce(mul, range(1, n + 1)) if n >= 1 else 1

print(factorial_5(False))