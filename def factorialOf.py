def factorialOf(x): 
    factorial = 1
    for i in range(2, x + 1): 
        factorial *= i
    return factorial 

x = int(input("Enter a number: "))
print(f"The factorial of {x} is {factorialOf(x)}")