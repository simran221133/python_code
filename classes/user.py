class User:
    """Class for user information"""

    def __init__(self, first_name, last_name, relation, login_attempts):
        """Initilize attributes for a User Class"""
        self.first_name = first_name
        self.last_name = last_name
        self.relation = relation
        self.login_attempts = login_attempts

    def describe_user(self):
        """Print user information"""
        print(f"User's first name: {self.first_name} & last name: {self.last_name}")
        
    def greet_user(self):
        """Print user information"""
        print(f"Hello {self.first_name} {self.last_name}! Welcome On-Board...")
        print(f"Relation to the User: {self.relation}")
        print(f"")

    def increment_login_attempts(self):
        """To increment login attempts"""
        self.login_attempts += 1
        print(f"User just tried Logging In! Login attempts incremented:{self.login_attempts}")

    def reset_login_attempts(self):
        """To reset login attempts"""
        self.login_attempts = 0
        print(f"Login attempts have been Reset: {self.login_attempts}")

