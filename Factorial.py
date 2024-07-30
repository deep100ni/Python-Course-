# To input an integer and find its factorial

n = eval(input("Enter the value of n: "))
n = abs(int(n))
factorial = 1
for num in range(2,n+1): 
  factorial *= num
print(factorial)