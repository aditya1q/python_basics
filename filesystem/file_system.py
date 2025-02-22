#🐍🐍🐍🐍 read file: 

# f = open('aadi.txt') # takes two parameter one is file name second is file mode(means you want to read or write by defaut it is read mode so don't need to write the mode)
# f = open('aadi.txt', "r") # read mode(by default or you can add that mode) 
# data = f.read()
# print(data)
# f.close() # make sure to close the file (good practice)


#🐍🐍🐍🐍 write file: 

# data = "hlw aadi"
# w = open("kanha.txt", "w")
# w.write(data)
# print(data)
# w.close() # make sure to close the file (good practice)


#🐍🐍🐍🐍 append data in file: 

# data = ' hlw kanha'
# u = open("kanha.txt", "a")
# u.write(data)
# u.close() # make sure to close the file (good practice)

#🐍🐍🐍🐍 with statement in file system : 

# f = open("aadi.txt")
# print(f.read())
# f.close()

# # The same can be written using with statement like this
# with open("aadi.txt") as f:
#     print(f.read())
# here you don't have to explicitly close the file 