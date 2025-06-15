#Create a decorator to log function execution time
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'''{func.__name__} 
              took {(end_time - start_time)} seconds
                to execute.''')
        return result
    return wrapper

@timeit
def calculate_average(n):
    return sum(range(n))/len(range(n))

@timeit
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(calculate_average(500))
print(factorial(40))