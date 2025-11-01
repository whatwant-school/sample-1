from dotenv import load_dotenv
import os


load_dotenv()

debug_mode = os.getenv("DEBUG")


def main():
    print(f"Debug Mode: {debug_mode}")


if __name__ == "__main__":
    main()
