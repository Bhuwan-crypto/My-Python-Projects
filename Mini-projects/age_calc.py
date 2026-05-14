import datetime

dob = int(input("Enter your year of birth\n"))
current_year = datetime.datetime.now().year

# checking invalid values
if dob > current_year:
    print("You are not born yet")
else:
    age = current_year - dob

    if 13 <= age < 18:
        print(f"Your age is {age} and you are a teen")
    elif age < 13:
        print(f"Your age is {age} and you are a child")
    elif 18 <= age < 60:
        print(f"Your age is {age} and you are an adult")
    elif 60 <= age < 100:
        print(f"Your age is {age} and you are old")
    else:
        print(f"Your age is {age} and you are dead")
