# To the smallest of 10 numbers entered

n = eval(input("Enter a number : "))
min = n
for i in range (1,10): 
  n = eval(input("Enter a number : "))
  if n<min: 
    min = n
print(min,"is the Smallest number entered")