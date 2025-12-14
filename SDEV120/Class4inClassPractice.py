# Simple Sequence

name = input("input your first name: ")
age = int(input("input your age: "))

print("your name is: ", name)
print("your age is: ", age)



#selection
score = int(input("Enter your score: "))
if score > 50:
    print("you passed")
else:
    print("you failed")





#list to store employee details
employees = []

while True:
    name = input("Enter name: ")
    emp_id = input("Enter id: ")
    employees.append({"name": name, "id": emp_id})
    another = input("input another employee: yes/no ")
    if another != "yes":
        break

print("\nEmployee List:")
for employee in employees:
    print("Name:", employee["name"], "- ID:", employee["id"])
