class GetProgrammer:  # Parent class
    def __init__(self, role, salary, language):  # Parameters reordered for clarity
        self.role = role
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f'My role is {self.role}, my language is {self.language} and my salary is {self.salary}')


class GetEmployee(GetProgrammer):  # Child class inheriting from GetProgrammer
    def __init__(self, role, salary, language):
        super().__init__(role, salary, language)  # Call parent class constructor
        self.language = 'Javascript'  # Override the language for this class

    def newLanguage(self):
        print(f'My role is {self.role}, my language is {self.language} and my salary is {self.salary}')


# Creating instances
programmer = GetProgrammer('programmer', 30000, 'python')
programmer.getInfo()  # Output: My role is programmer, my language is python and my salary is 30000

employee = GetEmployee('employee', 40000, 'python')  # 'python' will be overridden by 'Javascript'
employee.newLanguage()  # Output: My role is employee, my language is Javascript and my salary is 40000
employee.getInfo()      # Output: My role is employee, my language is Javascript and my salary is 40000