s = int(input("Enter the Time in second : "))
print(s," second =",end=' ')
h = s//3600
m = s%3600
s = m%60
m = m//60
print(h,"hr",m,"min",s,"second")

