#1. Create a function that takes a number num and returns its length.
#Examples
#number_length(10) ➞ 2
#number_length(5000) ➞ 4
#number_length(0) ➞ 1

def number_length(num):
    return len(str(num))

def main():
    num=int(input("Enter number:"))
    print(number_length(num))

main()


