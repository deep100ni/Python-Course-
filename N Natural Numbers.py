# To display n natural numbers

n = eval(input("Enter a number : "))
for i in range(1,n+1): 
  if n<0 or n == 0: 
    break 
  else: 
    print (i)
print("Done")