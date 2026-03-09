def get_int_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == "exit":
            return None
        try:
            value = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if value < 0:
            print("value must be positive")
        
        return value
    
def get_valid_employment():
    while True:
        user_input = input("Are you employed? (y/n) ").strip().lower()
        if user_input in ("y", "yes"):
            return True
        elif user_input in ("n", "no"):
            return False
        elif user_input == "exit":
            return None
        else:
            print("Answer yes(y) or no(n)")

def validate_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")


    if age < 18 :
        raise ValueError("Applicant must be at least 18")

    if age > 60:
        raise ValueError("Age value unrealistic")

def validate_credit_score(score):

    if score < 300 or score > 850:
        raise ValueError("Credit score must be between 300 and 850")

def validate_income(income):

    if income < 0:
        raise ValueError("Income cannot be negative")