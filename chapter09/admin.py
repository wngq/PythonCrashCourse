from user_for_912 import User


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("\n The Admin have privileges of ")
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("This user have no privileges.")


class Admin(User):
    def __init__(self, first_name, last_name, gender, age, email):
        super().__init__(first_name, last_name, gender, age, email)
        self.privileges = Privileges()
