#Check if a user-entered number is prime
import math
n=int(input("*****PRIME NUMBER CHECK**** Enter the number: "))
if n <= 1:
    print("WRONG ENTRY!!!Enter numbers greater than or equal to 1")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")    