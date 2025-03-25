class getEmployeeData:
    salary= 30000
    role = 'employee'
    language = 'python'

data = getEmployeeData()
data.salary = 40000 # instance variable it will print this if instance variable is not present then it will print class variable
salary = data.salary
role  = data.role
lang = data.language
print(salary, role, lang) # here you get all the data for employee