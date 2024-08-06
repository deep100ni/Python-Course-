n = int(input("Enter number :"))
a,b = 0,1
print(a,end="")
for i in range (2,n+1):
  print(b,end="")
  a,b=b,a+b