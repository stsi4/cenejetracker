from colorama import Fore, Style

class Product():
    def __init__(self, name, link, price):
        self.name = name
        self.link = link
        self.price = price
    
    def check_page(self, max_price):
        #link = div.p.a["href"]
        if self.price <= max_price:
            return self
            #price_sort.append([buy_product_price, link])
        return None

    def __repr__(self):
        pass

    def __str__(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL}, {Fore.MAGENTA}{self.price}{Style.RESET_ALL}, {Fore.RED}{self.link}{Style.RESET_ALL}"
    