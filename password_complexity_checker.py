import re

def assess_password_strength(password):
    # Criteria for assessing strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@#$%^&+=]', password))

    # Count how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        number_criteria, special_char_criteria])

    # Determine strength level
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

    # Prepare feedback message
       
    feedback = []
    feedback.append(f"Length (≥8): {'✔️' if length_criteria else '❌'}")
    feedback.append(f"Uppercase letters: {'✔️' if uppercase_criteria else '❌'}")
    feedback.append(f"Lowercase letters: {'✔️' if lowercase_criteria else '❌'}")
    feedback.append(f"Numbers: {'✔️' if number_criteria else '❌'}")
    feedback.append(f"Special characters: {'✔️' if special_char_criteria else '❌'}")

    return strength, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    strength, feedback = assess_password_strength(password)
    print(f"\nPassword strength: {strength}")
    print("Feedback:")
    for line in feedback:
        print(line)
