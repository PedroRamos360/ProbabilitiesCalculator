def factorial(n):
	if n < 0:
		raise ValueError("It is not possible to do factorial of negative numbers")
	if n == 0:
		return 1
	total = n
	while n > 1:
		n -= 1
		total *= n

	return total
