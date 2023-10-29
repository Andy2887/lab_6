def encode(raw_password):
    encoded_password = ""
    for c in raw_password:
        i = int(c) + 3
        encoded_password += str(i)
    return encoded_password

def main():
    flag = True

    stored_password = ""
    while flag:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit\n''')
        user_choice = int(input("Please enter an option: "))
        if user_choice == 1:
            raw_password = input("Please enter your password to encode: ")
            stored_password = encode(raw_password)
            print("Your password has been encoded and stored!\n")
        if user_choice == 2:
            print("The partner completes this part")
        if user_choice == 3:
            flag = False


if __name__ == "__main__":
    main()