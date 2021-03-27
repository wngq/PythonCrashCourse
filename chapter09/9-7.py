class User():
    def __init__(self, first_name, last_name, gender, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.email = email

    def describe_user(self):
        print("The user's name is " + self.last_name.title() + " " + self.first_name.title() + ".")
        print("The user's gender is " + self.gender + ".")
        print("The user is " + str(self.age) + ".")
        print("The user's email address is " + self.email + ".")

    def greet_user(self):
        print("Hello, " + self.last_name.title() + " " + self.first_name.title() + ".")


class Admin(User):
    def __init__(self, first_name, last_name, gender, age, email):
        super().__init__(first_name, last_name, gender, age, email)
        self.privileges = []

    def show_privileges(self):
        print("\n The Admin have privileges of ")
        for privilege in self.privileges:
            print("- " + privilege)


admin_1 = Admin('bin', 'huang', 'male', '27', 'xxxx@ssssss.com')
admin_1.privileges = ['can add post', 'can delete post', 'can ban user']
admin_1.describe_user()
admin_1.show_privileges()
