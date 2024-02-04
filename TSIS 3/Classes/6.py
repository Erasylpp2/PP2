numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False, numbers))
print(prime_numbers)
