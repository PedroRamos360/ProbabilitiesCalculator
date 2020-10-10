from src.backend.factorial import factorial


def arrengements(n, p):
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


def permutations(n, *p):
	if n < 0:
		raise ValueError("Total elements can't be lower than zero")
	total = factorial(n)
	if p:
		for number in p:
			if number < 0:
				raise ValueError("The number of repetitions can't be lower than zero")
			if n < number:
				raise ValueError("Total elements can't be lower than the repetions of one element")
			total /= number

	return int(total)
