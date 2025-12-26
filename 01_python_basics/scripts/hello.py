"""
A Simple script to practice Python Basics:
- Variables
- Input and Output
- String formatting
"""
def main():
    name = input("Enter your name:")
    birth_year = int(input("Enter your birth year:"))
    current_year = 2025
    age = current_year - birth_year

    print(f"\nHello, {name}!)")
    print(f"You are approximately {age} years old.")
    print(f"Your name has {len(name)} characters.")

if __name__ == "__main__":
    main()


