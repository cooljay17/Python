# Problem 1: Write a function that takes in an integer, minutes, and converts it into seconds
# Problem 2: Write a function that takes two numbers as arguments and returns their sum.
# Problem 3: Create a function that takes a string and returns the number (count)
# of vowels contained within it
#Bonus-Print Fizz if number divisible by 3,Print Buzz if divisible by 5.Print FizzBuzz if divisible by
#both 3 and 5. Print string not divisible by 3 and 5
def convertminstosecs(mins):
    return mins * 60


def sumof2nums(firstnum, secondnum):
    return firstnum + secondnum


def countofvowels(word):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for idx, w in enumerate(word):
        if (w in vowels):
            count = count + 1
    return count


def printfizzbuzz(num):
    return "FizzBuzz" if (num % 3 == 0 and num % 5 == 0) else (
        "Fizz" if num % 3 == 0 else
        ("Buzz" if num % 5 == 0 else "Not divisible by 3 or 5"
         )
    )


def main():
    mins = int(input("Enter the minutes to be converted:"))
    print("Seconds :", convertminstosecs(mins))
    firstnum = int(input("Enter first number:"))
    secondnum = int(input("Enter second number:"))
    print("Sum :", sumof2nums(firstnum, secondnum))
    word = input("Enter a word:")
    print("Count of vowels :", countofvowels(word))
    num = int(input("Enter a number :"))
    print(printfizzbuzz(num))


main()
