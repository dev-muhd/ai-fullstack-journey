from loan_system.eligibility import check_eligibility
from loan_system.validation import get_int_input, get_valid_employment

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

if __name__ == "__main__":
    main()