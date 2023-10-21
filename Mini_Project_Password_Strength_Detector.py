def check_password_strength(password):
    length=len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in  password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(not char.isalnum() for char in password)

    #Determining the strength of the password given by the user.
    if length > 8 and has_uppercase and has_lowercase and has_lowercase and has_digit and has_special_char:
        return "Strong"
    elif 6 < length <= 8:
        return "Medium"
    else:
        return "Weak"


if __name__ == "__main__":
    password = input("Enter your password:")
    strength = check_password_strength(password)
    print(f"Password strength:{strength}")



