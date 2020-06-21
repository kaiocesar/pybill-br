import pytest


class TestCalcBill:

    def test_one_two(self):
        assert 1 == 1

    def test_calc_inss_range_1(self):
        paybill1 = PyBill(salary=1751.82)
        assert CalculateBill.calculate(paybill1, INSS()), 140.1456

    def test_calc_inss_range_2(self):
        pybill2 = PyBill(salary=1751.83)
        assert CalculateBill.calculate(paybill2, INSS()), 140.1464

    def test_calc_inss_range_3(self):
        pybill3 = PyBill(salary=2919.73)
        assert CalculateBill.calculate(paybill3, INSS()), 321.1703

    def test_calc_inss_range_4(self):
        pybill4 = PyBill(salary=5839.46)
        assert CalculateBill.calculate(paybill4, INSS()), 642.34

    def test_calc_inss_with_zero_salary(self):
        pybill5 = PyBill(salary=0)
        assert CalculateBill.calculate(paybill5, INSS()), 0
