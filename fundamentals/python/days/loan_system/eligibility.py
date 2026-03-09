def check_eligibility(age, credit_score, income, employed):
    return (age >= 18 
            and income >= 3000 
            and (credit_score >= 350 or employed)
    )
    