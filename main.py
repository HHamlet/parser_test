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


def parse_site(link):
    url = 'https://www.coingecko.com'
    coin_list = []
    res = requests.get(link, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    class_for_rank = ("tw-text-gray-900 dark:tw-text-moon-50 tw-px-1 "
                      "tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-sticky tw-left-[24px]")

    class_for_name = "tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5"

    class_for_coin = "tw-text-gray-900 dark:tw-text-moon-50 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-end"

    coins = soup.find('tbody').find_all('tr')
    for coin in coins:
        rank = coin.find(class_=class_for_rank).text.strip()
        coin_name_tk = coin.find(class_=class_for_name).text.strip().split()

        coin_link = url + coin.find(class_="tw-flex tw-items-center tw-w-full").get("href")

        coin_img = coin.find(class_="tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill").get("src")

        coin_price = coin.find(
            class_=class_for_coin).text.strip()
        temp = "".join(re.findall(r"\d+\.\d+", coin_price.replace(",", "")))
        decimal_price = Decimal(temp)

        coin_volume24h = coin.findChildren(
            class_=class_for_coin)[-2].text.strip()
        temp = "".join(re.findall(r"\d+", coin_volume24h.replace(",", "")))
        decimal_value24h = Decimal(temp)

        coin_market_cap = coin.findChildren(
            class_=class_for_coin)[-1].text.strip()
        temp = "".join(re.findall(r"\d+", coin_market_cap.replace(",", "")))
        decimal_market_cap = Decimal(temp)

        coin_data = [rank, coin_name_tk[0], coin_name_tk[1], coin_link, coin_img, decimal_price, decimal_value24h, decimal_market_cap]
        coin_list.append(coin_data)

    return coin_list


def main():
    for i in range(1, 3):

        url_ = f'https://www.coingecko.com/?page={i}'
        coin_list = parse_site(link=url_)
        write_csv("coin_pars.csv", coin_list)


if __name__ == "__main__":
    main()
