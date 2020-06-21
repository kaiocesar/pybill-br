class PyBill(object):
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
