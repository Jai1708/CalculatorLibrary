"""
Unit tests for calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(2, 2) == 4

    def test_subtraction(self):
        assert calculator.subtract(2, 2) == 0
