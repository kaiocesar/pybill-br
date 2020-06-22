import pytest
from src.calculate_bill import CalculateBill
from src.pybill import PyBill
from src.tax import INSS, FGTS, IRRF


class TestCalcBill:

    def test_calc_inss_range_1(self):
        paybill = PyBill(salary=1751.81)
        assert CalculateBill().calculate(paybill, INSS()) == 140.1448

    def test_calc_inss_range_2(self):
        paybill = PyBill(salary=1751.83)
        assert CalculateBill().calculate(paybill, INSS()) == 157.6647

    def test_calc_inss_range_3(self):
        paybill = PyBill(salary=2919.73)
        assert CalculateBill().calculate(paybill, INSS()) == 321.1703

    def test_calc_inss_range_4(self):
        paybill = PyBill(salary=5839.46)
        assert CalculateBill().calculate(paybill, INSS()) == 642.34

    def test_calc_inss_with_zero_salary(self):
        paybill = PyBill(salary=0)
        assert CalculateBill().calculate(paybill, INSS()) == 0

    def test_calc_ftgs_with_valid_salary(self):
        paybill = PyBill(salary=2000)
        assert CalculateBill().calculate(paybill, FGTS()) == 160

    def test_calc_irrf_range_1(self):
        paybill = PyBill(salary=1903.98)
        assert CalculateBill().calculate(paybill, IRRF()) == 0

    def test_calc_irrf_range_2(self):
        paybill = PyBill(salary=2826.66)
        assert CalculateBill().calculate(paybill, IRRF()) == 0
