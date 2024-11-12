import json  # Import the json module to handle JSON data
with open('data.json', 'r') as file:
    data = json.load(file)
if 'name' in data:
    data['name'] = 'John Doe'
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
