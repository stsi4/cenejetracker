import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import csv

def get_price(div):
    price = list(div.b.text.split()[0])
    try:
        price.remove(".")
    except Exception as e:
        pass
    price[price.index(",")] = "."
    price = "".join(price)
    return float(price)

def main():
    product_name = input("Kateri izdelek hočeš? ")
    product_price = float(input("Vaša maximalna cena? "))
    product_url = "+".join(product_name.split())

    url = f"https://www.ceneje.si/Iskanje/Izdelki?q={product_url}"
    source = requests.get(url).text
    #print(source)
    soup = BeautifulSoup(source, "lxml")

    price_sort = []

    #finds cheap products
    for div in soup.find_all("div", class_ = "content"):
        
        name = div.h3.a.text
        link = div.p.a["href"]
        #checks if products match
        if product_name.lower() in name.lower():
            link = div.p.a["href"]
            buy_product_price = get_price(div)
            
            if float(buy_product_price) < product_price:
                price_sort.append([buy_product_price, link])

    price_sort.sort(key= lambda x: x[0])
    with open("products.csv", "w") as csv_file:
        fieldnames = ["price", "link", "name"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in price_sort:
            item.append(product_name)
            csv_writer.writerow({"price": item[0], "link": item[1], "name": item[2]})
            print(f"{Fore.GREEN}{product_name}{Style.RESET_ALL}, {Fore.MAGENTA}{item[0]}{Style.RESET_ALL}, {Fore.RED}{item[1]}{Style.RESET_ALL}")
        
if __name__ == "__main__":
    main()