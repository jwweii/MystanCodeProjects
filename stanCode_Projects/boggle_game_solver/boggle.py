"""
File: boggle.py
Name:Chein-Wei Peng
----------------------------------------
TODO: Leetcode LC212
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: This is the main function executing boggle game.
	"""
	start = time.time()
	####################
	dictionary = read_dictionary()
	boggle_dic = {}
	check = False
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		check = check_ch(row)
		if check is True:
			ch_coordination(i, row, boggle_dic)
		else:
			print('Illegal input')
			break
	if check is True:
		find_word(boggle_dic, dictionary)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split()
			dictionary.append(word[0])
	return dictionary


def check_ch(row: str) -> bool:
	"""
	This function will check if the input is legal or illegal.
	"""
	row_lst = row.lower().split()
	ans = True
	if len(row_lst) == 4:
		for i in range(4):
			if row_lst[i].isalpha() is False or len(row_lst[i]) != 1:
				ans = False
	else:
		ans = False
	return ans


def ch_coordination(i: int, row: str, boggle_dic: dict):
	"""
	This function will build the row list for boggle game.
	"""
	row_lst = row.lower().split()
	for j in range(4):
		# each character will be presented by an x and y coordinate.
		boggle_dic[(i+1, j+1)] = row_lst[j]


def find_word(boggle_dic: dict, dictionary: list):
	"""
	The function will the preliminary process for finding words in boggle game.
	"""
	word = ''
	word_lst = []
	xy_lst = []
	for xy in boggle_dic:
		xy_lst.append(xy)
		word += boggle_dic[xy]
		find_word_helper(xy, xy_lst, boggle_dic, word, word_lst, dictionary)
		if len(xy_lst) > 0:  # clean the xy list to zero after a series of search from a coordinate.
			xy_lst = []
			word = ''
	if len(word_lst) > 1:  # present the number in correct grammar.
		print(f'There are {len(word_lst)} words in total.')
	else:
		print(f'There is {len(word_lst)} word.')


def find_word_helper(xy: tuple, xy_lst: list, boggle_dic: dict, word: str, word_lst: list, dictionary: list):
	"""
	This function will find all possible arrangements of the word using recursion algorithm.
	"""
	# Chose the next coordinate (present in x and y axis).
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			if 0 < xy[0]+i <= 4 and 0 < xy[1]+j <= 4:
				next_xy = (xy[0]+i, xy[1]+j)
				if next_xy not in xy_lst:
					xy_lst.append(next_xy)
					word += boggle_dic[next_xy]
					# check if the word is in dictionary if the word length > 4.
					if len(word) >= 4:
						if word in dictionary and word not in word_lst:
							print(f'Found {word}')
							word_lst.append(word)
					# Explore
					if has_prefix(word, dictionary) is True:
						find_word_helper(next_xy, xy_lst, boggle_dic, word, word_lst, dictionary)
					# Un-chose
					xy_lst.pop()
					word = word[:len(word) - 1]


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary (list)
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	prefix_in_word = False
	for word in dictionary:
		if word.startswith(sub_s) is True:
			prefix_in_word = True
			break
	return prefix_in_word


if __name__ == '__main__':
	main()
