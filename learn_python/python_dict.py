'''
my_dict = {'name': 'Alice', 'age': 25}
'''
student_info = {
    "name": "John Doe",
    "age": 16,  # The key 'age' has the value 16. This is an integer.
    "grade": "10th"
}
print("The students name is:", student_info["name"])
print("The students age is:", student_info["age"])
print("The students grade is:", student_info["grade"])
student_info["grade"] = "11th"
print("Updated grade:", student_info["grade"])  # Prints: Updated grade: 11th
student_info["phone"] = "123-456-7890"
print("The student's phone number is:", student_info["phone"])
del student_info["phone"]
print("Updated student info:", student_info)
