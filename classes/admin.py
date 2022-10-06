from user import User

class Admin(User):
    """SubClass of user class"""

    """Initialize attributes of  the parent class"""
    def __init__(self, first_name, last_name, relation, login_attempts):
        super().__init__(first_name, last_name, relation, login_attempts)