# 1. Colors
class Color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

# 2. imports
from conversions import to_decimal, from_decimal
from operations import add, subtract, multiply, divide
from validators import is_valid_for_base

# 3. main function
def main():

    while True:

        print(Color.BLUE + "\n=== MULTI BASE CALCULATOR ===" + Color.RESET)
        print(Color.YELLOW + "1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit" + Color.RESET)

        choice = int(input("Choose option: "))

        if choice not in range(1,6):
            print(Color.RED + "❌ Invalid input! Please try again." + Color.RESET)
            continue


        if choice == 5:
            print("Goodbye 👋")
            break

        num1 = input("Enter first number: ")
        base1 = int(input("Base of first number (2,8,10,16): "))

        num2 = input("Enter second number: ")
        base2 = int(input("Base of second number (2,8,10,16): "))

        output_base = int(input("Output base (2,8,10,16): "))

        # Validation
        if not is_valid_for_base(num1, base1) or not is_valid_for_base(num2, base2):
            print(Color.RED + "❌ Invalid input! Please try again." + Color.RESET)
            continue

        dec1 = to_decimal(num1, base1)
        dec2 = to_decimal(num2, base2)

        if choice == 1:
            result = add(dec1, dec2)
        elif choice == 2:
            result = subtract(dec1, dec2)
        elif choice == 3:
            result = multiply(dec1, dec2)
        elif choice == 4:
            result = divide(dec1, dec2)

        final = from_decimal(result, output_base)
        print(Color.GREEN + f"✅ Result: {final}" + Color.RESET)

# Execute Program
main()