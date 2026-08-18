student = {"grades": "A,B,C", "class": "10A", "Age": "16"}

print("----STUDENT RESULT----")
print("\nClass of student:", student["class"])
print("Age of student:", student["Age"])
student["grades"]= "B,B,U"
print("grades of student:", student["grades"])

student["name"] = "ayyan"
student.pop("Age")
print(student)
#combining list and dictionary through methods "zip" and "dict"
names = {"mustafa", "ayyan","hadi","shayan"}
roll_numbers = [1,2,3,4]

students_roll_nos = dict(zip(roll_numbers , names))
print("Students roll numbers:", students_roll_nos)

