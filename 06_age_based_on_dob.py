from datetime import datetime, date, time


def validate(takeinput):
    error = ""
    while True:
        value = input(error + takeinput)
        try:
            current_date = datetime.now()
            date = datetime.strptime(value, "%Y-%m-%d")
            if date >= current_date:
                print("Date of birth cannot be in the future. ")
                error = "Please enter a valid date in the format YYYY-MM-DD. "
            else:
                dobdate = date.strftime("%Y-%b-%d")
                return dobdate
        except ValueError:
            print("Date format should be valid (YYYY-MM-DD).")
        except:
            print("Please enter a valid date in the format YYYY-MM-DD.")


dob = validate("Enter your DOB (YYYY-MM-DD):")
print("DOB:", dob)


dob1 = datetime.strptime(dob, "%Y-%b-%d")
age = dob1
age = datetime.now().year - dob1.year
if datetime.now().month < dob1.month or (
    datetime.now().month == dob1.month and datetime.now().day < dob1.day
):
    age -= 1
print(f"Age: {age}")
