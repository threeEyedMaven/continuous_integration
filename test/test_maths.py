#! /usr/bin/env python3

from src import maths
import pytest

class TestMath(object):
    def test_sum(self):
        assert maths.sum(3, 4) == 7
        
    def test_sum_type(self):
        with pytest.raises(TypeError):
            maths.sum("dharma", 10)