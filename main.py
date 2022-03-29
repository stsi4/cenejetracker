import requests
from bs4 import BeautifulSoup
import csv
from product import Product

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
    #defines product info
    name = input("Kateri izdelek hočeš? ")
    link_name = "+".join(name.split())
    max_price = float(input("Vaša maximalna cena? "))
    product_page = 1
    products = []

    #you should add an option to only get info from the first page

    #loops through every page

    with open("products.csv", "w") as csv_file:
        fieldnames = ["price", "link", "name"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        while True:
            #soup
            url = f"https://www.ceneje.si/Iskanje/Izdelki?page={product_page}&q={link_name}"
            source = requests.get(url).text
            soup = BeautifulSoup(source, "lxml")

            #checks if the page contains 0 products
            if not soup.find("div", class_="content"):
                print("end")
                break
            
            #checks each product if it is within the price range
            for div in soup.find_all("div", class_ = "content"):
                
                product = Product(name, div.p.a["href"], get_price(div))

                if product.check_page(max_price):
                    products.append(product)
                
            product_page += 1
        
        products.sort(key= lambda x: x.price)
        for prod in products:
            csv_writer.writerow({"price": prod.price, "link": prod.link, "name": prod.name})
            print(prod)
        
if __name__ == "__main__":
    main()