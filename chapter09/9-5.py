class User():
    def __init__(self, first_name, last_name, gender, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("The user's name is " + self.last_name.title() + " " + self.first_name.title() + ".")
        print("The user's gender is " + self.gender + ".")
        print("The user is " + str(self.age) + ".")
        print("The user's email address is " + self.email + ".")

    def greet_user(self):
        print("Hello, " + self.last_name.title() + " " + self.first_name.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('bin', 'huang', 'male', '27', 'xxxx@ssssss.com')
# print(user_1.login_attempts)
for i in range(1, 5):
    user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
