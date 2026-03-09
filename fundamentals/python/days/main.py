from loan_system.eligibility import check_eligibility
from loan_system.validation import get_int_input, get_valid_employment, validate_age, validate_credit_score, validate_income

def main():
    while True:
        
        
        try:
            age = get_int_input("Enter age (or type 'exit'): ")

            if age is None:
                break
            validate_age(age)

            credit_score = get_int_input("Enter credit score (or type 'exit'): ")

            if credit_score is None:
                break
            validate_credit_score(credit_score)

            income = get_int_input("How much is your income (or type 'exit'): ")

            if income is None:
                break
            validate_income(income)

            employed = get_valid_employment()
            if employed is None:
                break
            
            eligible = check_eligibility(age, credit_score, income, employed)

            print("Eligible" if eligible else "Not Eligible")

        except ValueError as e:
            print("Validation error:", e)
            continue

        while True:
            again = input("Check another applicant? (y/n or 'exit'): ").strip().lower()

            if again in ("y", "yes"):
                break
            elif again in ("n", "no", "exit"):
                return
            else:
                print("Please answer yes(y) or no(n).")

if __name__ == "__main__":
    main()