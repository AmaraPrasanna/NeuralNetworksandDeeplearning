def inchToCent(value):
    return value*2.54

heights = [] 
maxLengthList =int(input("enter no of persons : ")) 
heights = []

# Adding elements to the list in a loop
for i in range(maxLengthList):
    item = int(input("Enter the height of a person: "))
    heights.append(item)
new_list = []

for x in heights:
    value = int(x)
    new_list.append(inchToCent(value))
    
print("show list : ",new_list)
