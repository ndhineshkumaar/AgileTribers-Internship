class AgeError(Exception):
    def _init_(self,message="You must be at least 18 years old."):
        super().__init__(self.message)

def get_user_age():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise AgeError("You must be at least 18 years old.")
        print("Access granted.")
    except AgeError as e:
        print(e)
    except ValueError:
        print("Please enter a valid integer for age.")



get_user_age()