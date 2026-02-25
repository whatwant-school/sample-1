from dotenv import load_dotenv
import os
from utils import add, subtract, multiply, divide


load_dotenv()


def main():
    print(f"Debug Mode: {debug_mode}")
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"10 * 2 = {multiply(10, 2)}")


if __name__ == "__main__":
    main()
