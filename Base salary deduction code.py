def compute_deductions(salary):
    sss_cost = float(input("Enter SSS deduction value with decimals: "))
    philhealth_cost = float((salary * 0.05) / 2.0)
    pagibig_cost = float(input("Enter Pagibig deduction value with decimals: "))
    tax_value = float(input("Enter tax deduction value with decimals: "))

    deductions = sss_cost + philhealth_cost + pagibig_cost + tax_value
    net_salary = salary - deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_cost)
    print("PhilHealth Deduction:", philhealth_cost)
    print("Pag-IBIG Deduction:", pagibig_cost)
    print("Tax Deduction:", tax_value)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)