"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        #                #
        #      TODO:     #
        #                #
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find_all('tbody')
        for item in items:
            text = item.text
            text_new = text.split()
            boy_number = 0
            girl_number = 0
            for i in range(4, 1004, 5):
                boy_string_number = text_new[i - 2].split(',')
                boy_integer_number = int(boy_string_number[0]) * 1000 + int(boy_string_number[1])
                boy_number += boy_integer_number
                girl_string_number = text_new[i].split(',')
                girl_integer_number = int(girl_string_number[0]) * 1000 + int(girl_string_number[1])
                girl_number += girl_integer_number
            print('Male number:', boy_number)
            print('Girl number:', girl_number)


if __name__ == '__main__':
    main()
