#! /usr/bin/env python3
def integerSum(n):
	if not isinstance(n, int):
		raise TypeError
	sum = 0
	for i in range(1, n+1):
		sum = sum + i
	return sum

def sum(value1, value2):
	if not isinstance(value1, int) or not isinstance(value2, int):
		raise TypeError
	else:
        	return value1 + value2
