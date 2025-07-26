n = int(input("Enter a number : "))
def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(n)
print(f"The factorial of {n} is: {result}")