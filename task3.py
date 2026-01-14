import secrets
import string

def get_valid_length():
    """Prompts user for length and ensures it is a positive integer."""
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length >= 4:
                return length
            print("For security, please choose a length of at least 4.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def generate_password():
    print("--- Secure Password Generator ---")
    
    # 1. Get Length
    length = get_valid_length()

    # 2. Define Character Sets
    char_sets = {
        'letters': string.ascii_letters,
        'numbers': string.digits,
        'symbols': string.punctuation
    }
    
    # 3. Get User Preferences
    pool = ""
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if include_letters: pool += char_sets['letters']
    if include_numbers: pool += char_sets['numbers']
    if include_symbols: pool += char_sets['symbols']

    # Validation: Ensure at least one set is selected
    if not pool:
        print("Error: You must select at least one character type! Defaulting to letters.")
        pool = char_sets['letters']

    # 4. Generate Random String
    # Use secrets.choice for cryptographic security
    password = "".join(secrets.choice(pool) for _ in range(length))
    
    print(f"\nYour generated password: {password}")
    print("---------------------------------")

if __name__ == "__main__":
    generate_password()