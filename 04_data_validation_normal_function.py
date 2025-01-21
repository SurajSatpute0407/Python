from datetime import datetime, date, time
import re


def validate(takeinput, check, optional=False):
    error = ""
    while True:
        value = input(error + takeinput)
        if optional and value == "":
            return value

        elif check == "name":
            if value.isalpha() and len(value) >= 2 and len(value) <= 20:
                a = value.capitalize()
                return a
            else:
                error = "Error: Name should contain letters only and characters are between 2 and 20. "

        elif check == "phoneno":
            if value.isdigit() and len(value) == 10:
                return int(value)
            else:
                error = "Error: Mobile No should contain digits only and length should be 10. "

        elif check == "gender":
            if value.lower() in ["male", "female", "other"]:
                a = value.capitalize()
                return a
            else:
                error = """Error: Gender should be "male", "female", "other". """

        elif check == "email":
            if re.match(r"^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,3}$", value):
                return value
            else:
                error = "Error: Enter a valid email address. "

        elif check == "pancard":
            if re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]$", value) and len(value) == 10:
                return value
            else:
                error = "Error: PAN card should contain only alphanumeric characters and length should be 11. "

        elif check == "dob":
            try:
                current_date = datetime.now()
                date = datetime.strptime(value, "%Y-%m-%d")
                if date >= current_date:
                    error = "Date of birth cannot be in the future."
                else:
                    dobdate = date.strftime("%Y-%b-%d")
                    return dobdate
            except:
                error = "Wrong date format! "

        elif check == "address":
            if re.match(
                r"^[A-z0-9_\s%+-]+, [A-z0-9_\s%+-]+, [\w\s.-]+, [\w\s.-]+- \d{6}$",
                value,
            ):
                return value
            else:
                error = "Error: Please follow the format: Flat No 123, XYZ Tower, Main Street, Mumbai - 123456.\n "

        elif check == "pancard":
            if re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]$", value) and len(value) == 10:
                return value
            else:
                error = "Error: PAN card should contain only alphanumeric characters and length should be 11. "

        elif check == "password":
            if (
                re.match(
                    r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                    value,
                )
                and len(value) >= 8
            ):
                con_password = input("Confirm your password: ")

                if value == con_password:
                    return value
                else:
                    error = "Error: Passwords do not match. "

            else:
                error = "Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (e.g., @, #, !). "


print("Customer Details are:\n")
firstname = validate("Enter your firstname:", "name")
print("First name: ", firstname)
middlename = validate("Enter your middlename (Optional):", "name", optional=True)
print("Middle name: ", middlename)
lastname = validate("Enter your lastname:", "name")
print("Last name: ", lastname)
mobno = validate("Enter your Mobile no:", "phoneno")
print("Mobile No: ", mobno)
gender = validate("Enter your Gender:", "gender")
print("Gender: ", gender)
email = validate("Enter your email:", "email")
print("Email: ", email)
pancard = validate("Enter your Pancard:", "pancard")
print("Pancard No: ", pancard)
dob = validate("Enter your DOB:", "dob")
print("Date of Birth (DOB): ", dob)

dob1 = datetime.strptime(dob, "%Y-%b-%d")
age = dob1
age = datetime.now().year - dob1.year
if datetime.now().month < dob1.month or (
    datetime.now().month == dob1.month and datetime.now().day < dob1.day
):
    age -= 1
print("Age: ", age)

address = validate("Enter your address:", "address")
print("Address: ", address)

password = validate("Enter your password:", "password")
print("Password: ", password)

print("\nCustomer Registered sucessfully!:")
