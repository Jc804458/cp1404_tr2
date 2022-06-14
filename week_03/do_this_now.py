valid_age = False
age = 0
while not valid_age:
    try:
        age = int(input("age: "))
        if age < 0 or age > 150:
            print("Age must be between 0 and 150:")
        else:
            valid_age = True
    except ValueError:
        print("Invalid(not an integer)")

if age % 2 == 0:
    print(f"{age} is even")
else:
    print(f"{age} is odd")
