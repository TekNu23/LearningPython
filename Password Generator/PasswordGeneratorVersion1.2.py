import string
import secrets

def banner():
    print("=" * 60)

def password_gen():

    length = int(input("Enter password length: "))
    num_passwords = int(input("How many passwords do you wanna make: "))

    banner()
    print("Choose character set for password from these :")
    print("1. Digits")
    print("2. Letters")
    print("3. Special characters")
    print("4. Submit")
    print("5. Exit")
    banner()

    characterlist = ""

    while True:
        choice = int(input("Pick a number, for strong passwords pick 1 to 3, then 4 \n: "))
        if choice == 1:

            characterlist += string.ascii_letters
        elif choice == 2:

            characterlist += string.digits
        elif choice == 3:

            characterlist += string.punctuation
        elif choice == 4:
            break
        elif choice == 5:
            exit()
        else:
            banner()
            print("Please pick a valid option!")

    banner()

    print("Generated Passwords: ")
    for i in range(num_passwords):

        password = "".join(secrets.choice(characterlist) for i in range(length))

        print(password)

    banner()

if __name__ == "__main__":
    password_gen()