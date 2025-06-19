# Build a temperature converter CLI tool
import argparse
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9
def main():
    parser = argparse.ArgumentParser(description="Temperature Converter CLI Tool")
    parser.add_argument("temperature", type=float, help="Temperature value to convert")
    parser.add_argument("--to-fahrenheit", action="store_true", help="Convert Celsius to Fahrenheit")
    parser.add_argument("--to-celsius", action="store_true", help="Convert Fahrenheit to Celsius")

    args = parser.parse_args()

    if args.to_fahrenheit:
        result = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature}°C is {result:.2f}°F")
    elif args.to_celsius:
        result = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature}°F is {result:.2f}°C")
    else:
        print("Please specify a conversion direction: --to-fahrenheit or --to-celsius")   

if __name__ == "__main__":
    main()  