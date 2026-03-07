from loan_system.eligibility import check_eligibility

def run_tests():
    test_cases = [
        (17, 90, False, False),
        (18, 70, False, True),
        (18, 60, True, True),
        (18, 60, False, False),
        (25, 95, False, True),
    ]

    for age, grade, employed, expected in test_cases:
        result = check_eligibility(age, grade, employed)
        assert result == expected, (
            f"Failed for age={age}, grade={grade}, employed={employed}"
        )

    print("All tests passed.")

if __name__ == "__main__":
    run_tests()