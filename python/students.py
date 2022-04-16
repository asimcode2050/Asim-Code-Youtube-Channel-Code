"""
Python program to calculate the sum of the number of male and female students
https://youtu.be/I-OLMz8JLTs
Please Subscribe to Asim Code
"""
male = 0
female = 0
total_students = 0
male_percent = 0.0
female_percent = 0.0

male = int(input("Please enter the number of male students: "))
female = int(input("Please enter the number of female students: "))

total_students = male + female
male_percent = male / total_students
female_percent = female / total_students

print("Male :", format(male_percent,'.2f'), "%")
print("Female :", format(female_percent,'.2f'), "%")

