classmates = ["rohan" , "umer" , "mustafa","ayyan","hadi"]
print('names of classmates', classmates)

number_of_students = ('names of students:', len(classmates))
print("first pos:" , classmates[1])
print("second pos:" , classmates[2])
print('third pos:', classmates[3])
print('failed student:' , classmates[-1])

classmates.append("mahad")
print('new student mahad is added:', classmates)
classmates.remove('hadi')
print('hadi has been removed from the class', classmates)
classmates.sort()
print('sorted classmates:',classmates)
classmates.reverse()
print('class list hass been reversed new class list:' , classmates)

