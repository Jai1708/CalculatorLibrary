"""
Unit tests for calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(2, 2) == 4

    def test_subtraction(self):
        assert calculator.subtract(2, 2) == 0

    def test_multiplication(self):
        assert calculator.multiply(10, 10) == 100
