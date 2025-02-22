# #🐍🐍🐍🐍 first example :

# class Employee: # class (Employee is class) name always start from capital letter
#     language = "Python" # this is call attribute
#     salary = 30000   # we don't need comma for next key value

#     # we can create a function inside class
#     def getInfo(self): # it will take one argument always because we need something from an object
#         print(f"My name is {self.name} and i'm proficient in {self.language}. My current salary is {self.salary}")

#     @staticmethod # it is a decorator(if we don't need any property from an object then we mark that function as a staticmethod)
#     def greet(): # here we don't need anything from an object so we can add the @staticmethod here
#         print('good morning')

# aadi_info = Employee()
# aadi_info.name = "Aditya Tiwari" # also you can pass the additonal property which are not present in class also you can modify these also
# aadi_info.language = "javascript" # now it will update the language
# aadi_info.getInfo()
# # Employee.getInfo(aadi_info) # also we can write that above line like this





# 🐍🐍🐍🐍 second example :

# class Identity:

#     # here we create mulitple fields for info we also can do like that

#     # we don't have a name field in my class pass name explicitely rather then we have dundor method
#     def __init__(self, name, salary, language): # dundor method which is called automatically when we call the class (if we call class more then one time it will also called that much time)
#         print('called automatically')
#         self.name = name
#         self.salary = salary
#         self.language = language

# info = Identity("Harry", 120000, "javascript")
# print(info.name, info.salary, info.language)




# 🐍🐍🐍🐍 third example : create a class for programmer who are working for microsoft


# class Programmer:
#     company = "Microsoft"

#     def __init__(self, salary, position):
#         self.salary = salary
#         self.position = position
#         print(f'i am working in {self.company} as a {self.position} and my salary is {self.salary}')

# employee = Programmer(120000, "Frontend Developer")





# 🐍🐍🐍🐍 fourth example : need sqaure root of the number


# class Calculater:
#     def __init__(self, n):
#         self.n = n
#     def square_root(self):
#         print(f"The square root of {self.n} is {self.n * self.n}")
#     def cube(self):
#         print(f"Cube of {self.n} is {int(self.n ** 3)}")
#     def root(self):
#         print(f"Root of {self.n} is {self.n ** 1/2}")
# num = int(input("Enter the Number: "))
# output = Calculater(num)
# output.square_root()
# output.cube()
# output.root()

