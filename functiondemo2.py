# original = 5
# target = original
# print("original = %d, target = %d" % (original, target))
# original = 100
# print("original = %d, target = %d" % (original, target))

def change(target) : 
    target = 100
    print("In the change : targer = %d" % target)

original = 5
print("Befor Call change : original = %d" % original)
change(original)
print("After Call change : original = %d" % original)