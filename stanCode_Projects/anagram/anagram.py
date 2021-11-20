"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dic_words = []


def main():
    """
    TODO: This function will find all the anagrams of the entered word.
    """

    ####################
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    read_dictionary()
    while True:
        input_word = input('Find anagrams for: ')
        start = time.time()
        if input_word == '-1':
            break
        else:
            find_anagrams(input_word)
    ####################
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    The function will read the dictionary.
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.split()
            dic_words.append(word[0])


def find_anagrams(s):
    """
    :param s: the entered word
    """
    new_dic = {}
    trim_dictionary(s, new_dic)
    s_lst = []
    for i in range(len(s)):
        s_lst.append(i)
    anagram = ''
    anagram_lst = []
    new_s_order = []
    print('Searching...')
    find_anagrams_helper(s, new_dic, s_lst, new_s_order, anagram, anagram_lst)
    print(f'{len(anagram_lst)} anagrams: {anagram_lst}')


def trim_dictionary(s, new_dic):
    """
    This function will improve the speed of the program by trimming the original dictionary.
    After processing in the function, only the word with the same length
    and having first character in the entered word will be left in the new dictionary.
    """
    for word in dic_words:
        if len(word) == len(s):
            for ch in s:
                if word.startswith(ch) is True:
                    new_dic[word] = ch


def find_anagrams_helper(s, new_dic, s_lst, new_s_lst, anagram, anagram_lst):
    """
    The function will find all arrangements of the character in the entered word,
    and then search the arrangement in the dictionary to fit a real word.
    """
    #  Set the stooping rule of the algorithm
    if anagram in new_dic:
        if anagram not in anagram_lst:
            print(f'Found: {anagram}')
            anagram_lst.append(anagram)
            print('Searching...')
    else:
        for number in s_lst:
            if number in new_s_lst:
                pass
            else:
                # Chose
                new_s_lst.append(number)  # list all the arrangement the sting number of the input word.
                anagram += s[number]  # arrange the order of characters by the string number.
                # Explore
                if has_prefix(anagram, new_dic) is True:  # simplified the recursion algorithm.
                    find_anagrams_helper(s, new_dic, s_lst, new_s_lst, anagram, anagram_lst)
                # Un-chose
                new_s_lst.pop()
                anagram = anagram[:len(anagram)-1]


def has_prefix(sub_s, new_dic):
    """
    :param sub_s: a subunit of the entered word
    :return: if the sub_s is the prefix of any words in the dictionary or not.
    """
    prefix_in_word = False
    for word in new_dic:
        if word.startswith(sub_s) is True:
            prefix_in_word = True
            break
    return prefix_in_word


if __name__ == '__main__':
    main()
