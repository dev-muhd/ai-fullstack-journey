name = input("What is your name? ")
age = int(input("What is your age? "))
height = float(input("What is your height? "))

is_student = input("Are you a student? (True/False) ") == "True"
city = input("Where are you from? ")


try:
    if age < 0:
        raise ValueError("Age cannot be negative")
    age_in_months = age * 12
except ValueError as e:
    print ("Error:", e)
    age = None
    age_in_months = None
finally:
    print("Execution finished!")



try:
    if height <= 0:
        raise ValueError("Height must be positive")
    height_in_cm = height * 100
except ValueError as e:
    print("Error:", e)
    height = None
    height_in_cm = None
finally:
    print("Execution finished!")



print(f"Hello {name}! Here is your info:")
print(f"Age: {age} (int)")
print(f"Height: {height} (float)")
print(f"Student: {is_student} (bool)")
print(f"City: {city} (str)")
print(f"Age in months: {age_in_months}")
print (f"Height in cm: {height_in_cm}")


print("Hello {0}! Age: {1} years ({2} months), Height: {3} m ({4} cm), Student: {5}, City: {6}".format(name, age, age_in_months, height, height_in_cm, is_student, city))
print(f"Hello {name}! Age: {age} years ({age_in_months} months), Height: {height} m ({height_in_cm} cm), Student: {is_student}, City: {city}")
