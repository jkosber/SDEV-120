#SDEV 120 Project
#Team Dont Care


import pandas as pd


# MODULE 1: EMPLOYEE DATA MANAGEMENT
# -----------------------------------

# Hourly rate "database" (using Employee ID)
pay_rate_database = {
    "101": 18.50, "102": 21.75, "103": 16.25, "104": 22.00, "105": 19.00,
    "106": 25.00, "107": 17.75, "108": 23.50, "109": 15.85, "110": 24.40
}

# Function to enter employee information
def get_employee_data():
    employee = {}

    employee["first_name"] = input("Enter First Name: ")
    employee["last_name"] = input("Enter Last Name: ")

    # Loop until valid ID is entered
    valid_id = False
    while valid_id == False:
        emp_id = input("Enter Employee ID (101-110): ")
        if emp_id in pay_rate_database:
            employee["id"] = emp_id
            valid_id = True
        else:
            print("Invalid ID! Try again.")

    # Number of dependents (basic entry)
    employee["dependents"] = input("Enter Number of Dependents: ")

    return employee



# MODULE 2: TIME TRACKING
# ---------------------------


def get_hours():
    valid = False

    # Loop until hours between 0 and 80
    while valid == False:
        hours = float(input("Enter Hours Worked (0 - 80): "))
        
        if 0 <= hours <= 80:
            valid = True
        else:
            print("Hours must be between 0 and 80. Try again.")

    return hours




# MODULE 3: PAYROLL CALCULATIONS
# ---------------------------------


def calculate_pay(emp_id, hours):
    rate = pay_rate_database[emp_id]

    # Regular and overtime hours
    if hours > 40:
        reg_hours = 40
        overtime = hours - 40
    else:
        reg_hours = hours
        overtime = 0

    gross = (reg_hours * rate) + (overtime * rate * 1.5)

    # Basic tax calculations
    state_tax = gross * 0.056
    federal_tax = gross * 0.079

    net = gross - state_tax - federal_tax

    return gross, state_tax, federal_tax, net



# MAIN PROGRAM for data entry + saving and exporting to excel)
# -------------------------------------------------------------

employees = []
count = 1

print("\nPAYROLL ENTRY\n")

while count <= 10:
    print(f"\nEntering Information for Employee #{count}\n")

    emp = get_employee_data()
    emp["hours_worked"] = get_hours()

    gross, state, federal, net = calculate_pay(emp["id"], emp["hours_worked"])

    emp["gross_pay"] = gross
    emp["state_tax"] = state
    emp["federal_tax"] = federal
    emp["net_pay"] = net

    employees.append(emp)

    count = count + 1

# Save to Excel spreadsheet
df = pd.DataFrame(employees)
df.to_excel("Payroll.xlsx", index=False)

print("\nPayroll Completed Successfully! File saved as Payroll.xlsx\n")
