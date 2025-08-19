# 1. Iterables and Iterators
print("1. Iterables and Iterators")

my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

# 2. Generator using yield
print("\n2. Generator using yield")

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num, end=' ')  # 5 4 3 2 1

# 3. List, Dictionary, and Set Comprehensions
print("\n\n3. Comprehensions")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print("Square dict:", square_dict)

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}
print("Even numbers set:", even_set)

# 4. Custom Iterator
print("\n4. Custom Iterator")

class CountdownIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

cd = CountdownIterator(5)
for num in cd:
    print(num, end=' ')  # 5 4 3 2 1

# 5. Custom Generator
print("\n\n5. Custom Generator")

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Print first 10 Fibonacci numbers
fib = fibonacci_generator()
for _ in range(10):
    print(next(fib), end=' ')  # 0 1 1 2 3 5 8 13 21 34

# 6. Infinite Prime Number Generator
print("\n\n6. Infinite Prime Number Generator")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Print first 20 prime numbers
primes = prime_generator()
for _ in range(20):
    print(next(primes), end=' ')  # 2 3 5 7 11 13 ...

