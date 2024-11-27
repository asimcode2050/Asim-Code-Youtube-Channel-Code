import json
person = {
    "name": "Alice",
    "age": 25,
    "city": "London",
    "isStudent": False
}
json_string = json.dumps(person)
print("JSON String:", json_string)
python_object = json.loads(json_string)
print("Python Object:", python_object)
with open('person.json', 'w') as file:
    json.dump(person, file)
with open('person.json', 'r') as file:
    data_from_file = json.load(file)
print("Data Read from File:", data_from_file)
