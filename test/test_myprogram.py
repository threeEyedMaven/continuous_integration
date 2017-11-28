import src.myprogram as myprogram
import pytest

def test_doubleit():
	assert myprogram.doubleit(10) == 20
	assert myprogram.doubleit(50) == 100

def test_division():
	with pytest.raises(ZeroDivisionError):
		myprogram.division(5, 0)
	assert myprogram.division(10, 5) == 2
