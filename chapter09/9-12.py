from admin import Admin

admin_1 = Admin('bin', 'huang', 'male', '27', 'xxxx@ssssss.com')
admin_1.privileges.show_privileges()
# 要在Privileges()类里赋值
admin_1.privileges.privileges = ['can add post', 'can delete post', 'can ban user']
admin_1.privileges.show_privileges()