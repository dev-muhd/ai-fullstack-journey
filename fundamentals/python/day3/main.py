def check_eligibility(age, grade, employed):
    return age >= 18 and (grade >= 70 or employed)
    
def get_valid_age():
    while True:
        user_input = input("Enter age(or type 'exit'): ").strip().lower()
        if user_input == "exit":
            return None
        
        try:
            age = int(user_input)
            if age < 0:
                print("Age can't be negative")
                continue
            return age
        except ValueError:
            print("Inavlid input. Please enter a numeric value")

def get_valid_grade():
    while True:
        user_input = input("Enter grade(or type 'exit'): ").strip().lower()
        if user_input == "exit":
            return None
        
        try:
            grade = int(user_input)
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100.")
                continue
            return grade
        except ValueError:
            print("Invalid input. Please enter a whole number.")

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

def main():
    while True:
        age = get_valid_age()
        if age is None:
            break

        grade = get_valid_grade()
        if grade is None:
            break

        employed = get_valid_employment()
        if employed is None:
            break

        eligible = check_eligibility(age, grade, employed)
        if eligible:
            print("Eligible")
        else:
            print("Not Eligible")

        while True:
            again = input("Check another student? (y/n or 'exit'): ").strip().lower()

            if again in ("y", "yes"):
                break
            elif again in ("n", "no", "exit"):
                return
            else:
                print("Please answer yes(y) or no(n).")

main()