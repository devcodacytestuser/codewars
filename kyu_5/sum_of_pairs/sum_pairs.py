#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def sum_pairs(ints: list, s: int):
	"""
	Given a list of integers and a single sum value,
	returns the first two values (parse from the left please)
	in order of appearance that add up to form the sum.

	:param ints: a list of integers
	:param s: a single sum value
	:return: the first two values = s
	"""

	results = dict()
	short_ints = simplify(ints)

	for indx_a, a in enumerate(short_ints):
		for indx_b, b in enumerate(short_ints):
			if indx_a != indx_b:
				if a + b == s:
					dif = abs(indx_a - indx_b)

					if dif == 1:
						return [a, b]

					if dif not in results:
						results[dif] = [a, b]

	return results[min(results)] if len(results) > 0 else None


def simplify(ints: list) -> list:
	result = list()
	temp = -1

	for i in ints:
		if temp != i:
			temp = i
			result.append(i)

	return result
