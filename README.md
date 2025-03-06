# Technical-Debt-Management-Activity

Poor naming conventions changes:

sss -> sss_cost

philhealth -> philhealth_cost

pagibig -> pagibig_cost

tax -> tax_value

Lack of modular functions:
# Added calculations based on input salary

 sss_cost = float(salary * 0.045)
    philhealth_cost = float((salary * 0.05))

    if salary <= 1500.0:
        pagibig_cost = float(salary * 0.01)
    else:
        pagibig_cost = float(salary * 0.02)

Hardcoded values instead of dynamic inputs:
# Added float input for SSS, Philhealth, and Pagibig

sss: 1200 -> sss_cost = float(salary * 0.045)
philhealth: (salary * 0.05) / 2 -> philhealth_cost = float((salary * 0.05))
pagibig: 100 -> pagibig_cost = float(salary * 0.01) or pagibig_cost = float(salary * 0.02)

No error handling:

input validation

Code duplication:
