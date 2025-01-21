from datetime import datetime, date, time
import re
import sys


def validate(takeinput, check, optional=False):
    error = ""
    while True:

        value = input(error + takeinput)
        if optional and value == "":
            return value

        elif check == "name":
            name_function = lambda x: x.isalpha() and len(x) >= 2 and len(x) <= 20
            if name_function(value):
                a = value.capitalize()
                return a
            else:
                error = "Name should contain letters only and characters are between 2 and 20. "

        elif check == "phoneno":
            mobno_function = lambda x: x.isdigit() and len(x) == 10
            if mobno_function(value):
                return int(value)
            else:
                error = "Mobile No should contain digits only and length should be 10. "

        elif check == "gender":
            gender_function = lambda x: x.lower() in [
                "male",
                "female",
                "other",
                "m",
                "f",
                "o",
            ]
            if gender_function(value):
                if value.lower() == "m" or value.lower() == "male":
                    return "Male"
                elif value.lower() == "f" or value.lower() == "female":
                    return "Female"
                elif value.lower() == "o" or value.lower() == "other":
                    return "Other"
            else:
                error = """Gender should be "male", "female", "other". """

        elif check == "email":
            email_function = lambda x: re.match(
                r"^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,3}$", x
            )
            if email_function(value):
                return value
            else:
                error = "Enter a valid email address. "

        elif check == "pancard":
            pancard_function = (
                lambda x: re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$", x) and len(x) == 10
            )
            if pancard_function(value):
                return value
            else:
                error = "PAN card should contain only alphanumeric characters and length should be 11. "

        elif check == "dob":
            try:
                current_date = datetime.now()
                date = datetime.strptime(value, "%Y-%m-%d")
                if date >= current_date:
                    print("Date of birth cannot be in the future. ")
                    error = "Please enter a valid date in the format YYYY-MM-DD. "
                else:
                    dobdate = date.strftime("%Y-%b-%d")
                    return dobdate
            except:
                error = "Please enter a valid date in the format YYYY-MM-DD."

        elif check == "address":
            address_function = lambda x: re.match(
                r"^[A-z0-9_\s%+-]+, [\w\s.-]+- \d{6}$", x
            )
            if address_function(value):
                return value.title()
            else:
                error = "Please follow the format: City, State - 123456.\n "

        elif check == "pancard":
            pancard_function = (
                lambda x: re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$", x) and len(x) == 10
            )
            if pancard_function(value):
                return value
            else:
                error = "PAN card should contain only alphanumeric characters and length should be 11. "

        elif check == "password":
            password_function = (
                lambda x: re.match(
                    r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                    x,
                )
                and len(x) >= 8
            )
            if password_function(value):
                con_password = input("Confirm your password: ")
                if value == con_password:
                    return value
                else:
                    error = "Passwords do not match. "
            else:
                error = "Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (e.g., @, #, !). "


print("Customer Details are:\n")
firstname = validate("Enter your firstname:", "name")
middlename = validate("Enter your middlename (Optional):", "name", optional=True)
lastname = validate("Enter your lastname:", "name")
mobno = validate("Enter your Mobile no:", "phoneno")
gender = validate("Enter your Gender:", "gender")
email = validate("Enter your email:", "email")
pancard = validate("Enter your Pancard:", "pancard")
dob = validate("Enter your DOB:", "dob")
address = validate("Enter your address (City, State - 123456):", "address")
password = validate("Enter your password:", "password")


dob1 = datetime.strptime(dob, "%Y-%b-%d")
age = dob1
age = datetime.now().year - dob1.year
if datetime.now().month < dob1.month or (
    datetime.now().month == dob1.month and datetime.now().day < dob1.day
):
    age -= 1
# print('Age: ',age)

fullname = f"{firstname} {middlename} {lastname}"

print("\nCustomer Registered sucessfully!")


print("\nCustomer Details:\n")

dict1 = {
    "name": fullname,
    "Mobile No": mobno,
    "Gender": gender,
    "Email:": email,
    "Pancard": pancard,
    "DOB": dob,
    "Age": age,
    "Address": address,
    "Password": password,
}

for i in dict1:
    print(f"{i} : {dict1[i]}")
