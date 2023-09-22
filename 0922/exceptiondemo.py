first = int(input("Enter a first number : "))
second = int(input("Enter a second number : "))

try :
    print(f"{first} / {second} = {first / second}")
except Exception as err:
    print(err)
finally :
    
    print("Program is over..")
# else : 
#     print("Program is over")