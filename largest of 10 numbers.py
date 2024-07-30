# To the largest of 10 numbers entered

n = eval(input("Enter a number : "))
max = n
for i in range (1,10): 
  n = eval(input("Enter a number : "))
  if n>max: 
    max = n
print(max,"is the largest number entered")