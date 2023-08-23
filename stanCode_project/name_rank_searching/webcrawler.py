"""
File: webcrawler.py
Name: Jessie
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        male_total = 0
        female_total = 0
        all_lst = []
        for tag in tags:
            targets = tag.tbody.text.split()
            all_lst.append(targets)
            new_all_lst = []
            for i in range(len(all_lst[0])):
                all_lst[0][i] = string_manipulation(all_lst[0][i])
                if all_lst[0][i] != '':
                    new_all_lst.append(all_lst[0][i])
            for j in range(len(new_all_lst)):
                if j % 2 == 0:
                    male_total += int(new_all_lst[j])
                else:
                    female_total += int(new_all_lst[j])
            print('Male Number:', male_total)
            print('Female Number:', female_total)


def string_manipulation(s):
    ans = ''
    for ch in s:
        if ch.isdigit() and len(s) > 5:  # deduct name, 100% and 2023
            ans += ch
    return ans


if __name__ == '__main__':
    main()
