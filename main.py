import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.coingecko.com'

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}


def write_csv(f_name, coin_list):
    with open(f_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow(coin_list)


def parse_site(link):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    tag = soup.find('tbody')
    coins = tag.find_all('tr')
    for coin in coins:
        rank = coin.find(
            class_="tw-text-gray-900 dark:tw-text-moon-50 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-sticky "
                   "tw-left-[24px]").text.strip()
        coin_name_tk = coin.find(
            class_="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5").text.strip().split()
        coin_link = url + coin.find(class_="tw-flex tw-items-center tw-w-full").get("href")
        coin_img = coin.find(class_="tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill").get("src")
        coin_price = coin.find(
            class_="tw-text-gray-900 dark:tw-text-moon-50 tw-px-1 tw-py-2.5 2lg:tw-p-2.5 tw-bg-inherit tw-text-end").text.strip().split()[
            0]

        # print(f"{rank}-{coin_name_tk[0]}-{coin_name_tk[1]}-{coin_link} - {coin_price} --{coin_img}")
        coin_list = [rank, coin_name_tk[0], coin_name_tk[1], coin_link, coin_img, coin_price]
        write_csv("coin_pars.csv", coin_list)


def main():
    parse_site(link=url)


if __name__ == "__main__":
    main()
