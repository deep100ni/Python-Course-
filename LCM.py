# To input two numbers and find their LCM

n1 = eval(input("Enter first number: "))
n2 = eval(input("Enter second number: "))
n1 = abs(int(n1))
n2 = abs(int(n2))
i = 1
while((n1*i)%n2 != 0): 
  i += 1
  LCM = n1*i
print("LCM of",n1,"and",n2,"=",LCM)
    