def is_prime(n):
 if n > 1:
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    else:
        return True

def count_primes(numbers):
    prime_count = 0
    for num in numbers:
        if is_prime(num):
            prime_count += 1
    return prime_count


numbers = list(map(int, input("Enter numbers separated by space: ").split()))


prime_count = count_primes(numbers)

print(f"Number of prime numbers: {prime_count}")