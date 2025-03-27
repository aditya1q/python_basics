# learn how to use classMethod(if you want to use class variable instead of instance variable)

class Employee:
    a = 1
    @classmethod # if we don't use this it will print 11 but now it will print 1 because i've used classMethod
    def showClass(cls):
        print(f'this is class variable value {cls.a}')

e = Employee()
e.a = 11
e.showClass()