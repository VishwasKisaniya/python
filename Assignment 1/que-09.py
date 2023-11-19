def is_valid_password(password):
    #checking the validity
    if len(password) < 5:
        return False

    # Check if the password contains the symbol "&"
    if '&' not in password:
        return False

    has_lowercase = False
    has_uppercase = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True

    return has_lowercase and has_uppercase

def main():
    password = input("Enter your password: ")

    if is_valid_password(password):
        print("Password is valid!")
    else:
        print("Password does not meet the requirements.")

if __name__ == "__main__":
    main()
