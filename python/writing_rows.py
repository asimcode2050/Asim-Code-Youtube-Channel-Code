'''
How to write rows as lists to csv file in Python
YouTube Channel: Asim Code
Please Subscribe to Asim Code.
https://youtu.be/hjep1nS9uNA
'''
import csv
data_set = [["ID1234", "tom", "hanks"], [
    "ID4567", "mike", "tyson"], ["ID8923", "bill", "gates"]]

with open("employees.csv", 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows(data_set)

f = open("employees.csv", "r")
print(f.read())
f.close()
