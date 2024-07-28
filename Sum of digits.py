# To input a number and display the sum of its digits.

n = int(input("Enter an number :"))
sum = 0
while n != 0: 
  digit = n%10
  sum += digit 
  n //= 10
print(sum)