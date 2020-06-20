def calc_inss(base_salary):
    if base_salary < 0:
        return 0
    elif base_salary <= 1751.81:
        return base_salary * (8/100)
    elif base_salary >= 1751.82 and base_salary <= 2919.72:
        return base_salary * (9/100)
    elif base_salary >= 2919.73 and base_salary <= 5839.45:
        return base_salary * (11/100)
    else:
        return 642.34

