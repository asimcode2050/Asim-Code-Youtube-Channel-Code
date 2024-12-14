''' 
my_tuple = (1, 2, 3)

"John" (a string)
16 (an integer)
92 (an integer)
'''
student_info = ("John", 16, 92)
student_name = student_info[0]  # 'John' is at index 0 in the tuple
student_age = student_info[1]   # 16 is at index 1 in the tuple
student_grade = student_info[2]  # 92 is at index 2 in the tuple
print("Student Name:", student_name)   # Expected output: John
print("Student Age:", student_age)     # Expected output: 16
print("Student Grade:", student_grade)  # Expected output: 92
students = [
    ("John", 16, 92),  # First students info
    ("Sarah", 17, 85),  # Second students info
    ("Alice", 15, 88)  # Third students info
]
for student in students:
    name, age, grade = student
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
