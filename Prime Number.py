# To input a number and check whether it is a prime number or not.

n = int(input("Enter number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("It is not prime.")
            break
    else:
        print("It is prime.")
else:
    print("It is not prime.")