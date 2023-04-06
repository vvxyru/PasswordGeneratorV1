import random

again = ""
password = ""
passwordChars = ""

print("Welcome to Vincent's random password generator.")

while True:
    again = ""
    password = ""
    passwordChars = ""

    while True:
        try:
            length = int(input("Please enter the length of your desired password: "))
        except ValueError:
            print("Integers only!")
        else:
            break

    useUpper = input("Include uppercase characters? (Y/N): ").upper() == "Y"
    useLower = input("Include lowercase characters? (Y/N): ").upper() == "Y"
    useNumber = input("Use numbers? (Y/N): ").upper() == "Y"
    useSpecial = input("Use special characters? (Y/N): ").upper() == "Y"


    upperCharacters = "ABCDEFGHIJKLMNOPQRSTUVQWXYZ"
    lowerCharacters = "abcdefghijklmnopqrstuvwxyz"
    digitCharacters = "1234567890"
    specialCharacters = "!@#$%^&*()_+-={}|[]\:\";'<>?,./`~'"

    if useUpper:
        passwordChars += upperCharacters
    if useLower:
        passwordChars += lowerCharacters
    if useNumber:
        passwordChars += digitCharacters
    if useSpecial:
        passwordChars += specialCharacters

    try:
        for i in range(length):
            password += random.choice(passwordChars)
    except OverflowError:
        print("Password too large!")
        exit()

    print("Your generated password is: " + password)

    while again != "Y" or "N":
        again = input("Would you like to generate another? (Y/N): ").upper() == "Y"
        if again:
            break
        else:
            print("Goodbye!")
            exit()
