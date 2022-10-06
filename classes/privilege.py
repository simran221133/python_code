class Privilege:

    def __init__(self, part):
        self.part = part

    def show_privileges(self):
        """Print all the flavors"""
        print(f"Admin has the following privileges {self.part}")
        print(f"")