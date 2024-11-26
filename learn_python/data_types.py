age = 25
print(type(age))
height = 5.9
print(type(height))
name = "John Doe"
print(type(name))  # Prints the type of 'name'
is_student = True
print(type(is_student))
hobbies = ["reading", "swimming", "coding"]
print(type(hobbies))
print(hobbies[0])
coordinates = (40.7128, -74.0060)
print(type(coordinates))
print(coordinates[1])
skills = {"Python", "Java", "C++"}
print(type(skills))
print(skills)
person_profile = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student,
    "hobbies": hobbies,
    "coordinates": coordinates,
    "skills": skills
}
print(person_profile)
print(f"Name: {person_profile['name']}")
print(f"Age: {person_profile['age']}")
print(f"Height: {person_profile['height']}")
print(f"Is student: {person_profile['is_student']}")
print(f"Hobbies: {person_profile['hobbies']}")
# Retrieves the value for the 'coordinates' key.
print(f"Coordinates: {person_profile['coordinates']}")
# Retrieves the value for the 'skills' key ({"Python", "Java", "C++"}).
print(f"Skills: {person_profile['skills']}")
