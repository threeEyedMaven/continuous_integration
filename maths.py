#! /usr/bin/env python3
def sum(value1, value2):
	if not isinstance(value1, int) or not isinstance(value2, int):
		raise TypeError
	else:
        	return value1 + value2
