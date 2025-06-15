#Calculate factorial recursively
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Enter a number to find the factorial: ")) 
print(f"The factorial of {n} is", factorial(n))   