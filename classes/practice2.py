class getEmployeeData:
    # these are class object 
    salary = 30000
    role = 'employee'
    language = 'python'

    def getInfo(self):  # it will take one argument
        print(
            f'my role is {self.role}, my lang is {self.language} and my salary is {self.salary}')

    # here you can see i don't need any of the property of that object but still i need to pass that self object in that function
    def greetWithSelf(self):
        print('giving error if we do not pass self argument')

    # solution: if we don't need any object property so don't need to pass self
    @staticmethod
    def greetWithoutSelf():
        print('Not giving error here of self argument')


data = getEmployeeData()
data.getInfo()
data.greetWithSelf()
data.greetWithoutSelf()
# or we can do this
# getEmployeeData.getInfo(data)
