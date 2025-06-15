# Generate the first n Fibonacci numbers with a generator
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = int(input("Enter the limit  to generate Fibonacci numbers:"))
fib_gen = fibonacci_generator(n)
for number in fib_gen:
    print(number)