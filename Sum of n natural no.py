# To find the sum of first n natural numbers 

n = eval(input("Enter the value of n : "))
sum = 0
i = 1
while i <= n: 
  sum += i
  i += 1
print("Sum of frst",n,"natural numbers =",sum)