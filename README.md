# Technical-Debt-Management-Activity

Poor naming conventions changes:
sss -> sss_cost
philhealth -> philhealth_cost
pagibig -> pagibig_cost
tax -> tax_value

Lack of modular functions:
# Added calculations based on input salary and net salary in one line

 sss_cost = float(salary * 0.045)
    philhealth_cost = float((salary * 0.05))

    if salary <= 1500.0:
        pagibig_cost = float(salary * 0.01)
    else:
        pagibig_cost = float(salary * 0.02)

net_salary = salary - (sss_cost + philhealth_cost + pagibig_cost + tax_value)


Hardcoded values instead of dynamic inputs:
# Added float input for SSS, Philhealth, and Pagibig

sss: 1200 -> sss_cost = float(salary * 0.045)
philhealth: (salary * 0.05) / 2 -> philhealth_cost = float((salary * 0.05))
pagibig: 100 -> pagibig_cost = float(salary * 0.01) or pagibig_cost = float(salary * 0.02)

No error handling:
# Added a check to make sure the input is a valid number
while True:
    try:
        salary = float(input("Enter your monthly salary: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for your salary.")

Code duplication:
N/A
