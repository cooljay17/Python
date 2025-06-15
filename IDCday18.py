# Enforce a naming convention with a metaclass

class NamingConventionMeta(type):
    def __new__(cls, name, bases, dct):
        if not name.startswith("My"):
            raise TypeError("Class names must start with 'My'")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=NamingConventionMeta):
    pass

# This will raise a TypeError because it doesn't start with "My"
class BadClass(metaclass=NamingConventionMeta):
    pass

def main():
 if __name__ == "__main__":
    try:
        obj = MyClass()
    except TypeError as e:
        print(f"Error: {e}")

    try:
        bad_obj = BadClass()        
    except TypeError as e:
        print(f"Error: {e}")

main()        