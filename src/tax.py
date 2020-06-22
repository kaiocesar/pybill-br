from abc import abstractmethod

DEPENDENTS_VALUE = 189.59


class Tax(object):
    @abstractmethod
    def calculate(self, paybill):
        pass


class INSS(Tax):
    def calculate(self, paybill):
        salary = paybill.salary
        descount = 0
        if salary <= 1751.81:
            descount = salary * 0.08
        elif salary >= 1751.82 and salary <= 2919.72:
            descount = salary * 0.09
        elif salary >= 2919.73 and salary <= 5839.45:
            descount = salary * 0.11
        else:
            descount = 642.34
        return round(descount, 4)


class FGTS(Tax):
    def calculate(self, paybill):
        return paybill.salary * 0.08


class IRRF(Tax):
    # inss > dependents > irrf
    def calculate(self, paybill):
        salary = paybill.salary
        # dependents = paybill.dependents
        # base_salary = salary - 
        descount = 0
        if salary <= 1903.98:
            descount = 0
        elif salary >= 1903.99 and salary <= 2826.65:
            descount = salary * 0.09
        elif salary >= 2826.66 and salary <= 3751.05:
            descount = salary * 0.11
        elif salary >= 3751.06 and salary <= 4664.68:
            descount = salary * 0.11
        else:
            descount = 642.34
        return round(descount, 4)
