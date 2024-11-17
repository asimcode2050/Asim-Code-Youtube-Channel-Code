try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file does not exist!")
except IOError:
    print("Error: An input/output error occurred.")
else:
    print("File was read successfully!")
finally:
    print("Execution finished.")
