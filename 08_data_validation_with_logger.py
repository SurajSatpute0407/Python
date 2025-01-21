from datetime import datetime
import re
import logging
import sys


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger = args[0].logger if args and hasattr(args[0], 'logger') else None
        if logger:
            logger.debug(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        if logger:
            logger.debug(f"{func.__name__} Completed.")
        return result
    return wrapper


# Base Validator Class
class Validator:
    def __init__(self, takeinput, logger=None, optional=False):
        self.takeinput = takeinput
        self.optional = optional
        self.logger = logger

    def validate(self):
        raise NotImplementedError("Subclasses must override validate method")

# Derived Validators
class NameValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value = input(error + self.takeinput)
            if self.optional and value=='':
                return value
            else:
                try:
                    name_function = lambda x: x.isalpha() and len(x) >= 2 and len(x) <= 20
                    if name_function(value):
                        a = value.capitalize()
                        if self.logger:
                            self.logger.info(f"Valid input for name: {a}")  
                        return a
                    else:
                        error = 'Name should contain letters only and characters are between 2 and 20. '
                        if self.logger:
                            self.logger.error(f"Validation failed for name: {value}. Reason: {error}")
                        raise Exception(error)      
                except:
                    print(sys.exc_info()[1])




class MobileValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value = input(error + self.takeinput)
            try:
                mobno_function = lambda x: x.isdigit() and len(x) == 10
                if mobno_function(value):
                    if self.logger:
                        self.logger.info(f"Valid input for Mobile No: {value}")
                    return int(value)
                else:
                    error = 'Mobile No should contain digits only and length should be 10. '
                    if self.logger:
                        self.logger.error(f"Validation failed for Mobile no: {value}. Reason: {error}")
                    raise Exception(error)     
            except:
                print(sys.exc_info()[1])



class GenderValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value=input(error + self.takeinput)
            try:
                gender_function = lambda x: x.lower() in ["male", "female", "other", "m", "f", "o"]
                if gender_function(value):
                    if value.lower() == "m" or value.lower() == "male":
                        if self.logger:
                            self.logger.info(f"Valid gender: Male")
                        return "Male"
                    elif value.lower() == "f" or value.lower() == "female":
                        if self.logger:
                            self.logger.info(f"Valid gender: Female")
                        return "Female"
                    elif value.lower() == "o" or value.lower() == "other":
                        if self.logger:
                            self.logger .info(f"Valid gender: Other")
                        return "Other"
                    else:
                        error = """Gender should be "male", "female", "other". """
                        if self.logger:
                            self.logger.error(f"Validation failed for Gender: {value}. Reason: {error}")
                        raise Exception(error)      
            except:
                print(sys.exc_info()[1])


class EmailValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value=input(error + self.takeinput)
            try:
                email_function = lambda x: re.match(r"^[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,3}$", x)
                if email_function(value):
                    if self.logger:
                        self.logger.info(f"Valid input for Email: {value}")
                    return value
                else:
                    error = "Enter a valid email address. "
                    if self.logger:
                        self.logger.critical(f"Validation failed for Email: {value}. Reason: {error}")
                    raise Exception(error)      
            except:
                print(sys.exc_info()[1])


class PancardValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value=input(error + self.takeinput)
            try:
                pancard_function = lambda x: re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$", x) and len(x)==10
                if pancard_function(value):
                    if self.logger:
                        self.logger.info(f"Valid input for Pancard: {value}")
                    return value
                else:
                    error = "PAN card should be in XXXXX0000X format. "
                    if self.logger:
                        self.logger.error(f"Validation failed for Pancard: {value}. Reason: {error}")
                    raise Exception(error)      
            except:
                print(sys.exc_info()[1])


class DOBValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value=input(error + self.takeinput)
            try:
                current_date = datetime.now()
                date=datetime.strptime(value, '%Y-%m-%d')
                if date >= current_date:
                    error = 'Date of birth cannot be in the future. '
                    if self.logger:
                        self.logger.error(f"Validation failed for Date of Birth: {date}. Reason: {error}")
                    raise Exception(error)
                else:
                    dobdate = date.strftime('%Y-%b-%d')
                    if self.logger:
                        self.logger.info(f"Valid input for Date of Birth: {dobdate}")
                    return dobdate      
            except:
                print(sys.exc_info()[1])


class AddressValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value=input(error + self.takeinput)
            try:
                address_function = lambda x: re.match(r"^[A-z0-9_\s%+-]+, [\w\s.-]+- \d{6}$", x)
                if address_function(value):
                    if self.logger:
                        self.logger.info(f"Valid input for Address: {value}")
                    return value
                else:
                    error = "Please follow the format: (City, State - 123456)\n "
                    if self.logger:
                        self.logger.warning(f"Validation failed for Address: {value}. Reason: {error}")
                    raise Exception(error)      
            except:
                print(sys.exc_info()[1])


class PasswordValidator(Validator):
    @log_decorator
    def validate(self):
        error = ''
        while True:
            value=input(error + self.takeinput)
            try:
                password_function = lambda x: re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", x) and len(x)>=8
                if password_function(value):
                    con_password = input("Confirm your password: ")
                    try:
                        if value == con_password:
                            if self.logger:
                                self.logger.info(f"Valid input for Password: {value}")
                            return value
                        else:
                            error = "Passwords do not match. "
                            if self.logger:
                                self.logger.critical(f"Validation failed for Password: {value}. Reason: {error}")
                            raise Exception(error)
                    except:
                        print(sys.exc_info()[1])   
                else:
                        error = "Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (e.g., @, #, !). "
                        if self.logger:
                            self.logger.error(f"Validation failed for Password: {value}. Reason: {error}")
                        raise Exception(error)      
            except:
                print(sys.exc_info()[1])



class Registration:
    def __init__(self):
        self.details = {}
        self.logger = None

    def setup_logger(self, user_identifier):
        self.logger = logging.getLogger(user_identifier)
        self.logger.setLevel(logging.DEBUG)

        log_filename = f"{user_identifier}_log.log"
        file_handler = logging.FileHandler(log_filename)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s --> %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)

        self.logger.info(f"Log file created for user: {user_identifier}")


    @log_decorator
    def register(self):

        firstname = NameValidator("Enter your first name: ", self.logger).validate()
        middlename = NameValidator("Enter your middle name: ", self.logger, optional=True).validate()
        lastname = NameValidator("Enter your last name: ", self.logger).validate()
        self.details['Fullname'] = f'{firstname} {middlename} {lastname}'

        user_identifier = f"{firstname}_{lastname}".lower()
        self.setup_logger(user_identifier)

        self.details['First'] = firstname
        self.details['Last'] = lastname

        self.logger.info(f'Validated Full Name: {self.details['Fullname']}')

        self.details['Mobile No'] = MobileValidator("Enter your mobile number: ", self.logger).validate()
        self.details['Gender'] = GenderValidator("Enter your gender: ", self.logger).validate()
        self.details['Email'] = EmailValidator("Enter your email address: ", self.logger).validate()
        self.details['Pancard'] = PancardValidator("Enter your PAN card number: ", self.logger).validate()
        self.details['DOB'] = DOBValidator("Enter your date of birth (YYYY-MM-DD): ", self.logger).validate()
        self.details['Address'] = AddressValidator("Enter your address (City, State - 123456): ", self.logger).validate()
        self.details['Password'] = PasswordValidator("Enter your password: ", self.logger).validate()
        self.calculate_age()

         
        self.logger.info("User registration completed.")



    @log_decorator
    def calculate_age(self):
        dob = datetime.strptime(self.details['DOB'], '%Y-%b-%d')
        age = datetime.now().year - dob.year
        if (datetime.now().month, datetime.now().day) < (dob.month, dob.day):
            age -= 1
        self.details['Age'] = age
        self.logger.info(f"Calculated age: {age}")


    @log_decorator
    def display(self):
        print("\nCustomer Details:")
        for key, value in self.details.items():
            print(f"{key}: {value}")


class User(Registration):
    
    def __init__(self, **dict1):
        self.user = dict1
        self.id = dict1["Mobile No"]
        self.email = dict1["Email"]
        self.__passw = dict1["Password"]
        self.lg_status = False
        self.file_name = dict1['First']+"_"+dict1["Last"]
        self.logger = None
        self.setup_logger(self.file_name)

    @log_decorator
    def login(self):
        id = input("Enter mobile no or email: ")
        if id.isdigit():
            self.logger.info(f'Valid input entered: {id}')
            id = int(id)
        else:
            id = str(id)
            self.logger.info(f'Valid input entered: {id}')
        passw = input("Enter password:")
        if id == self.id or id == self.email:
            if passw == self.__passw:
                print("Successfully logged-in\n")
                self.logger.info(f'Successfully Logged-In: {id}')
                self.lg_status = True
            else:
                print("wrong password")
                self.logger.error(f'Wrong Password: {id}')
        else:
            print("wrong username")
            self.logger.error(f'Wrong Username: {id}')
            
    @log_decorator
    
    def bookTicket(self):
        self.from1 = input("Enter source destination: ")
        self.to = input("Enter destination location:")
        try:
            if self.lg_status:
                print(f"\nTicket confirmed from {self.from1.title()} to {self.to.title()}\n")
                self.logger.info(f"Ticket booked: {self.from1.title()} to {self.to.title()}")
            else:
                error = "not loggedin"
                if self.logger:
                    self.logger.error(f"Validation failed Reason: {error}")
                raise Exception(error)
        except:
            print(sys.exc_info())

    @log_decorator
    def logout(self):
        if self.lg_status == True:
            self.logger.info(f"{self.email} log out successfully!")
            self.lg_status=False
            print(f'\n{self.email} log out successfully!\n')
        else:
            self.logger.critical(f"Please login first...n")
            print('User not active right now! Please login first...')



# Using the Class
if __name__ == "__main__":
    # while True:
        reg = Registration()
        reg.register()
        reg.display()
        
        print("\nCustomer Registered Successfully!\n")

        d1=reg.details
        a = User(**d1)
        a.login()
        a.bookTicket()
        a.logout()
        
        

        # more_users = input("Register another user? (yes/no): ").strip().lower()
        # if more_users != "yes":
        #     break