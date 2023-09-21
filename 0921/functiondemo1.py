student = {} #딕셔너리                               #1

def myinput(man) :                                  #3                   
    name = input("Enter your name : ")              #4
    age = input("Enter your age : ")                #4
    man["name"] = name                              #4
    man["age"] = age                                #5

myinput(student)                                    #2 #5
print(student)                                         #6
