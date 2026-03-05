from eligibility import check_eligibility
from utils import get_int_input

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
        age = get_int_input("Enter age (or type 'exit'): ", min_value=0, max_value=60)

        grade = get_int_input(  "Enter grade (or type 'exit'): ", min_value=0,  max_value=100)

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