#Define a function contains_blue that accepts any number of arguments.
# It should return True if any of the arguments are "blue" (all lowercase).
# Otherwise, it should return False . For example:
def contains_blue(arg):
        return True if "blue" in arg else False

def main():
        arg = input("Enter the arguments with comma separated:")
        print("Is blue word present :", contains_blue(arg))

main()