#task 1

details = {'Dipika':80,'Bhushan':99,'Ira':83,'Radha':100,'krishna':99.5}

name = input("Enter student name: ")
marks = details.get(name, None)

print(f"{name}'s marks obtained: {marks}"if marks is not None  else "Student not found")


#task2

list = [1,2,3,4,5,6,7,8,9,10]

print('Extracted first five elements :',list[0:5])
print('reverse extracted elements :', list[0:5][::-1])
