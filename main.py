from dotenv import load_dotenv
import os


load_dotenv()

debug_mode = os.getenv("DEBUG")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print(f"Debug Mode: {debug_mode}")
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")


if __name__ == "__main__":
    main()
