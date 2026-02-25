from dotenv import load_dotenv
import os
from utils import add, subtract, multiply, divide, power, square


load_dotenv()

debug_mode = os.getenv("DEBUG")


def main():
    print(f"Debug Mode: {debug_mode}")
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"10 * 2 = {multiply(10, 2)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"4^2 = {square(4)}")


if __name__ == "__main__":
    main()
