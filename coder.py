def encode(raw_password):
    encoded_password = ""
    for c in raw_password:
        i = int(c) + 3
        if i == 10:
            i = 0
        elif i == 11:
            i = 1
        elif i == 12:
            i = 2
        encoded_password += str(i)
    return encoded_password

 # initialize decode() method
def decode(encoded_password):
    decoded_password = ""
    for x in encoded_password:
        e = int(x) - 3
        if e == -3:
            e = 7
        elif e == -2:
            e = 8
        elif e == -1:
            e = 9
        decoded_password += str(e)
    return decoded_password

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
            decoded_password = decode(stored_password)
            print(f'The encoded password is {stored_password}, and the original password is {decoded_password}.\n')
        if user_choice == 3:
            flag = False


if __name__ == "__main__":
    main()