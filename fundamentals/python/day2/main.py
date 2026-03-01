try:
    age = int(input("What is your age? "))
    income = float(input("How much do you earn? "))
    is_student = input("Are you a student? (True/False) ") == "True"
    credit_score = int(input("What is your credit score? "))
    citizen = input("Are you a citizen? (True/False) ") == "True"

    if age < 18 or not citizen:
        print("Not Eligible")
    elif is_student:
        if credit_score >= 600:
            print("Eligible")
        else:
            print("Not Eligible")
    else: 
        if income>= 30000 and credit_score >= 700:
            print("Eligible")
        else:
            print("Not Eligible")
except ValueError as e:
    print("Invalid input! Please enter numbers where required.")
        
