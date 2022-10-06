from user import User
from admin import Admin
from privilege import Privilege

priv1 = Privilege(["Can read", "Can write", "Can edit"])
priv1.show_privileges()

"""Creating instance one(admin1) of subclass Admin"""
admin1 = Admin("Simran", "Kaur", "Smart_Kid", "several")

admin2 = Admin("Sam", "Kaur", "Smart_Kid", "several")

"""Creating instance one(user1) of class User"""
user1 = User("Ashish", "Yadav", "Boy", 4)
user1.describe_user()
user1.increment_login_attempts()
user1.greet_user()

"""Creating instance two(user2) of class User"""
user2 = User("Gurleen", "Kaur", "Best Friend", 10)
user2.describe_user()
user2.increment_login_attempts()
user2.greet_user()

"""Creating instance three(user3) of class User"""
user3 = User("Divya", "JayaKumar", "Friend", 2)
user3.describe_user()
user3.increment_login_attempts()
user3.greet_user()

"""Creating instance four(user4) of class User"""
user4 = User("Charan", "Singh", "Friend", 8)
user4.describe_user()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.reset_login_attempts()
user4.greet_user()
print(f"Number of login attempts: {user4.login_attempts}")