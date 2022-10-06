class Employee:
    '''Class for employee info'''

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def employee_info(self):
        print(f"Employee information: {self.first_name} {self.last_name} \n Annual Salary: {self.annual_salary}")

    def give_raise(self, new_raise=5000):
        '''method to give raise to the employee's'''

        self.new_raise = new_raise
        self.new_salary = int(self.annual_salary) + int(self.new_raise)
        print(f"Raised Salary: {self.new_salary}")



        