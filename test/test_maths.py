#! /usr/bin/env python3
from src import maths
import pytest

class TestMath(object):
    def test_fibonacci(self):
        assert maths.fibonacci(1) == 0
        assert maths.fibonacci(2) == 1
        assert maths.fibonacci(5) == 3
        assert maths.fibonacci(10) == 34

    def test_sum(self):
        assert maths.sum(3, 4) == 7
        
    def test_sum_type(self):
        with pytest.raises(TypeError):
            maths.sum("dharma", 10)
    def test_integer_sum(self):
        assert maths.integerSum(10) == 55
        assert maths.integerSum(9) == 45
