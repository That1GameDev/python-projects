import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [random.choice(characters) for _ in range(length)]
    return ''.join(password)

def main():
    print("=== Password Generator ===")
    while True:
        print("\n1. Generate password")
        print("2. Generate custom length password")
        print("3. Quit")
        choice = input("Choose option: ")

        if choice == "1":
            password = generate_password()
            print(f"Generated password: {password}")
        elif choice == "2":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print(f"Generated password: {password}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

main()