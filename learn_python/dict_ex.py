student = {
    "name": "John",
    "age": 20,
    "city": "New York"
}
print("Student Name:", student["name"])  # Output: John
print("Student Address:", student.get("address"))  # Output: None
print("Student Address:", student.get(
    "address", "Not Provided"))  # Output: Not Provided
student["age"] = 21  # Now the age is updated to 21
print("Updated Age:", student["age"])  # Output: 21
student["major"] = "Computer Science"
print("Student Major:", student["major"])  # Output: Computer Science
del student["city"]  # This removes the 'city' key and its associated value
print("Updated Student Info:", student)
removed_value = student.pop("age")  # Removes 'age' and returns its value (21)
print("Removed Age Value:", removed_value)  # Output: 21
print("Updated Student Info after pop:", student)
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")
