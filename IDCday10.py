#Read numbers from a file and handle errors gracefully
def read_numbers(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Warning: Could not convert '{line.strip()}' to a number.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    
    return numbers

file_path = input("Enter the file name with extension: ")
number_list = read_numbers(file_path)
if number_list:
    print("Numbers read from the file:", number_list)