from dotenv import load_dotenv
import os
from utils import add, subtract, multiply, divide, power, square


load_dotenv()

debug_mode = os.getenv("DEBUG")


def main():
    print(f"[DEBUG] Mode: {debug_mode}")
    print(f"Result (1 + 2) = {add(1, 2)}")
    print(f"Result (5 - 3) = {subtract(5, 3)}")
    print(f"Result (10 * 2) = {multiply(10, 2)}")
    print(f"Result (2 ^ 3) = {power(2, 3)}")
    print(f"Result (4^2) = {square(4)}")


if __name__ == "__main__":
    main()
