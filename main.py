import requests
from bs4 import BeautifulSoup
import csv
import re
from decimal import Decimal


headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}


def write_csv(f_name, coin_list):
    with open(f_name, "a") as f:
        writer = csv.writer(f)
        for coin in coin_list:
            writer.writerow(coin)


def refine_price(text):
    return text.strip(' \n$').replace(",", "")


def parse_site(link):
    url = 'https://www.coingecko.com'
    coin_list = []
    res = requests.get(link, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    coins = soup.find('tbody').find_all('tr')

    for coin in coins:
        teg_td = coin.find_all('td', class_=lambda x: x and 'tw-hidden' not in x.split())
        coin_rank = teg_td[1].text.strip()
        coin_name_tk = teg_td[2].div.text.split()
        coin_link = url + teg_td[2].a.get('href')
        coin_img = teg_td[2].img.get('src')
        decimal_price = Decimal(refine_price(teg_td[4].text))
        decimal_volume24h = Decimal(refine_price(teg_td[9].text))
        decimal_market_cap = Decimal(refine_price(teg_td[10].text))

        coin_data = [coin_rank, coin_name_tk[0], coin_name_tk[1], coin_link, coin_img, decimal_price, decimal_volume24h, decimal_market_cap]
        coin_list.append(coin_data)

    return coin_list


def main():
    for i in range(1, 3):

        url_ = f'https://www.coingecko.com/?page={i}'
        coin_list = parse_site(link=url_)
        write_csv("coin_pars.csv", coin_list)


if __name__ == "__main__":
    main()
