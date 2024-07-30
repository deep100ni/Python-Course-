# To display even natural numbers from 2 to n

n = eval(input("Enter the value of n: "))
n = abs(int(n))
for num in range(2,n+1,2): 
  print(num)