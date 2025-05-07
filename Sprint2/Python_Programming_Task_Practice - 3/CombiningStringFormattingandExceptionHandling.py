def validate_password(password):
    if len(password) < 8:
        raise ValueError(f"Error: The password {password} is too short. It must be at least 8 characters long.")
    
    hasletter=any(char.isalpha() for char in password)
    hasdigit=any(char.isdigit() for char in password)
    
    if not (hasdigit and hasletter):
        raise ValueError("Password must contain both letters and numbers.")

    return True


validate_password("abcd")
validate_password("abcdefgh")
validate_password("445453644")