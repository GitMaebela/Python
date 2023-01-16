import json
import random

employees = [{"Name": "John", "Surname": "Doe", "Leave Balance": 20},
			 {"Name": "Jane", "Surname": "Smith", "Leave Balance": 15},
			 {"Name": "Bob", "Surname": "Johnson", "Leave Balance": 10},
			 {"Name": "Emily", "Surname": "Williams", "Leave Balance": 8},
			 {"Name": "Michael", "Surname": "Jones", "Leave Balance": 12}]

# Randomly assign December leave to employees
random.shuffle(employees)

working_employee = 0
for employee in employees:
	if working_employee < 2:
		employee["On December leave"] = False
		working_employee += 1
	elif employee["Leave Balance"] > 0:
		employee["Leave Balance"] -= 1
		employee["On December leave"] = True
	else:
		employee["On December leave"] = False

# print name and whether employee is on December leave or not
for employee in employees:
	if employee["On December leave"] == True:
		print(f"{employee['Name']} {employee['Surname']} is on December leave")
	else:
		print(f"{employee['Name']} {employee['Surname']} will be working during the December holidays")


# **************************
# Output
# **************************
# Emily Williams will be working during the December holidays
# Bob Johnson will be working during the December holidays
# Jane Smith is on December leave
# Michael Jones is on December leave
# John Doe is on December leave