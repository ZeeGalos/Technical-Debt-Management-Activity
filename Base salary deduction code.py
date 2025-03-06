def compute_deductions(salary):
    sss_cost = input("Enter SSS deduction value: ")
    philhealth_cost = (salary * 0.05) / 2
    pagibig_cost = 100
    tax = 1875 # Assuming fixed value for simplicity

    deductions = sss_cost + philhealth_cost + pagibig_cost + tax
    net_salary = salary - deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_cost)
    print("PhilHealth Deduction:", philhealth_cost)
    print("Pag-IBIG Deduction:", pagibig_cost)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

    salary = float(input("Enter your monthly salary: "))
    compute_deductions(salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)