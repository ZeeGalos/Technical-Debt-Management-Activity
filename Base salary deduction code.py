def compute_deductions(salary):
    sss_cost = float(salary * 0.045)
    philhealth_cost = float((salary * 0.05))

    if salary <= 1500.0:
        pagibig_cost = float(salary * 0.01)
    else:
        pagibig_cost = float(salary * 0.02)

    tax_value = 1875.0

    deductions = sss_cost + philhealth_cost + pagibig_cost + tax_value
    net_salary = salary - deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_cost)
    print("PhilHealth Deduction:", philhealth_cost)
    print("Pag-IBIG Deduction:", pagibig_cost)
    print("Tax Deduction:", tax_value)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary with decimals: "))

while True:
    try:
        salary = float(input("Enter your monthly salary with decimals: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for your salary. ")

compute_deductions(salary)