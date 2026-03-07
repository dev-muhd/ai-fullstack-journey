def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        user_input = input(prompt).strip().lower()

        if user_input == "exit":
            return None
        try:
            value = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        
        if min_value is not None and value < min_value:
            print(f"Value must not exceed {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Value must not exceed {max_value}.")
            continue
        
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