import os

os.rename("foo.txt", "foo1.txt")
os.rename("foo1.txt", "foo.txt")

print(os.getcwd())

# str = input("Enter your input : ")
# print(str)

# fo = open("foo.txt", "w")
# fo.write("Python is a great language.\nYeah it's great!\n")
#
# fo.close()
#
# fo = open("foo.txt", "r+")
#
# print("Name of the file: ", fo.name)
# print("Closed or not : ", fo.closed)
# print("Opening mode : ", fo.mode)
#
# print(fo.read())

