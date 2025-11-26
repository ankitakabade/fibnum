# Program to calculate the sum of first n Fibonacci numbers

n = 10  # <-- You can change this value

a, b = 0, 1
fib_sum = 0

for _ in range(n):
    fib_sum += a
    a, b = b, a + b

print("Sum of first", n, "Fibonacci numbers is:", fib_sum)