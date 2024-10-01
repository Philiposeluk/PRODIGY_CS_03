# Password Complixity Checker 

This tool assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters.

## Features
- Checks password length (minimum of 8 characters)
- Verifies presence of uppercase letters
- Verifies presence of lowercase letters
- Checks for numbers
- Checks for special characters

## Requirements
- Python 3.x

## Usage

1. Clone the repository:

       git clone https://github.com/Philiposeluk/password_complixity_checker.git

       cd password complixity checker

2.  Run the script:
    
        python3 password_strength.py
    
3.  Enter a password when prompted.

   
## Code
    import re

    def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@#$%^&+=]', password))

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        number_criteria, special_char_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = []
    feedback.append(f"Length (≥8): {'✔️' if length_criteria else '❌'}")
    feedback.append(f"Uppercase letters: {'✔️' if uppercase_criteria else '❌'}")
    feedback.append(f"Lowercase letters: {'✔️' if lowercase_criteria else '❌'}")
    feedback.append(f"Numbers: {'✔️' if number_criteria else '❌'}")
    feedback.append(f"Special characters: {'✔️' if special_char_criteria else '❌'}")

    return strength, feedback

    if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    strength, feedback = assess_password_strength(password)
    print(f"\nPassword strength: {strength}")
    print("Feedback:")
    for line in feedback:
        print(line)

## License

   This project is licensed under the MIT License.       

