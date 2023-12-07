import requests
from bs4 import BeautifulSoup
import csv
import re
from decimal import Decimal


url = 'https://www.coingecko.com'

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}


def write_csv(f_name, coin_list):
    with open(f_name, "a") as f:
        writer = csv.writer(f)
        for coin in coin_list:
            writer.writerow(coin)


def parse_site(link):
    coin_list = []
    res = requests.get(link, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")

    coins = soup.find('tbody').find_all('tr')
    for coin in coins:
        rank = coin.find(
            class_="tw-text-gray-900 dark:tw-text-moon-50 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-sticky "
                   "tw-left-[24px]").text.strip()
        coin_name_tk = coin.find(
            class_="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5").text.strip().split()

        coin_link = url + coin.find(class_="tw-flex tw-items-center tw-w-full").get("href")

        coin_img = coin.find(class_="tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill").get("src")

        coin_price = coin.find(
            class_="tw-text-gray-900 dark:tw-text-moon-50 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit "
                   "tw-text-end").text.strip()
        temp = "".join(re.findall(r"\d.", coin_price.replace(",", "")))
        decimal_price = Decimal(temp)

        volume24h = coin.findChildren(
            class_="tw-text-gray-900 dark:tw-text-moon-50 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit "
                   "tw-text-end")[-2].text.strip()
        temp = "".join(re.findall(r"\d.", volume24h.replace(",", "")))
        decimal_value24h = Decimal(temp)

        coin_data = [rank, coin_name_tk[0], coin_name_tk[1], coin_link, coin_img, decimal_price, decimal_value24h]
        coin_list.append(coin_data)

    return coin_list


def main():
    for i in range(1, 3):

        url_ = f'https://www.coingecko.com/?page={i}'
        coin_list = parse_site(link=url_)
        write_csv("coin_pars.csv", coin_list)


if __name__ == "__main__":
    main()
