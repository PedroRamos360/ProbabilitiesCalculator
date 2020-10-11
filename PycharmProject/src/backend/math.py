from src.backend.factorial import factorial


def arrangements(n, p):
	if n < 0 or p < 0:
		raise ValueError("N or P can't be lower than zero")
	if n < p:
		raise ValueError("N can't be lower than P")
	return int(factorial(n)/factorial(n-p))


def combinations(n, p):
	if n < 0 or p < 0:
		raise ValueError("N or P can't be lower than zero")
	if n < p:
		raise ValueError("N can't be lower than P")
	return int(factorial(n)/(factorial(p) * factorial(n-p)))


def permutations(n, p):
	p = p.split('\n')
	if n < 0:
		raise ValueError("Total elements can't be lower than zero")
	total = factorial(n)
	if p:
		for number in p:
			if int(number) < 0:
				raise ValueError("The number of repetitions can't be lower than zero")
			if n < int(number):
				raise ValueError("Total elements can't be lower than the repetitions of one element")
			total /= int(number)

	return int(total)
