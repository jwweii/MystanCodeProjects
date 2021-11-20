"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return: the largest digit.
	"""
	if n < 0:
		n *= -1
	n_mode = n % 10
	return find_largest_digit_help(n, n_mode)


def find_largest_digit_help(n, n_max):
	"""
	The function will return the largest digit.
	"""
	# Set the stopping rule of the recursion algorithm.
	if n < 10:
		return n_max
	n = n // 10
	if n > 0:
		# Explore
		n_mode = n % 10
		if n_mode > n_max:
			n_max = n_mode
		# Explore
		max_ = find_largest_digit_help(n, n_max)
		return max_


if __name__ == '__main__':
	main()
