# learn how to use dunder

class GetEmployeeData:
    # dunder method which is called automatically when we create an object
    def __init__(self, role, language, salary):
        self.role = role
        self.language = language
        self.salary = salary
        print('Run imediatly')
        print(
            f'my role is {role}, my lang is {language} and my salary is {salary}')

    def getInfo(self):  # it will take one argument
        print(
            f'my role is {self.role}, my lang is {self.language} and my salary is {self.salary}')


# we can pass the data from here which called instance variable
data = GetEmployeeData('employee', 30000, 'python')
data.getInfo()
# or we can do this
# getEmployeeData.getInfo(data)
