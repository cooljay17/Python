#1. Write a function called number_compare. This function takes in two parameters (both numbers).
# If the first is greater than the second, this function returns "First is greater"
# If the second number is greater than the first, the function returns "Second is greater"
# Otherwise the function returns "Numbers are equal"

def number_compare(first,second):
    return "First is greater" if first > second else ("Second is greater" if second > first else "Numbers are equal")

def main():
    first = int(input("Enter first number:"))
    second = int(input("Enter second number:"))
    print(number_compare(first, second))

main()