import string
import random

def banner():
    print("=" * 60)

def password_gen():

    length = int(input("Enter password length: "))
    num_passwords = int(input("How many passwords do you wanna make: "))
    special_character = int(input("How many special characters per password: "))

    #special character cannot exceed password length
    if special_character > length:
        print(f"Special characters [{special_character}] cannot exceed password length [{length}], please try again")
        banner()
        password_gen()

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
        choice = int(input("Pick a number "))
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

        special_chars = [random.choice(string.punctuation) for i in range(special_character)]
        non_special_pool = characterlist.translate(str.maketrans('', '', string.punctuation))
        remaining_chars = [random.choice(non_special_pool) for i in range(length - special_character)]

        password_chars = special_chars + remaining_chars
        random.shuffle(password_chars)
        password = "".join(password_chars)

        print(password)

    banner()

    password_gen()

if __name__ == "__main__":
    password_gen()