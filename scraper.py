import requests
from bs4 import BeautifulSoup

product_code = input("Podaj kod produktu: ")
#url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons = requests.get(url)
if respons.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    print(type(opinions))
    if len(opinions) > 0:
        opinions_all = []
        for opinion in opinions:
            single_opinion = {
                ""
            }
else:
    print("Nie ma opinii")
    
