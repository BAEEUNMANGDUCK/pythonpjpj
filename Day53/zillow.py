import selenium
from bs4 import BeautifulSoup
import requests
import lxml

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSemcmUGUahTi_C9JtLZgiQu4SiXiDz7d37PtyBauFjKd7b2DQ/viewform?usp=sf_link"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}





class Zillow:
    def __init__(self,url):
        response = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(response.text, 'html.parser')


    def get_links(self):
        links = self.soup.select(selector="li div div article div div a")
        links_list = []
        for link in links:
            url = link.get("href")
            if url not in "https://www.zillow.com/":
                url = "https://www.zillow.com" + url
            url = url.replace("https://www.zillow.comhttps:", "https:")
            if url not in links_list:
                links_list.append(url)

        return links_list

    def get_prices(self):
        prices = self.soup.select(selector='.PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1')

        prices_list = [price.getText().split(' ')[0] for price in prices]

        return prices_list


    def get_addresses(self):
        addresses = self.soup.select(selector='.property-card-data > a > address')
        address_list = []
        for address in addresses:
            each_address = f"{address.getText()}"
            if each_address.find('|') != -1:
                each_address = each_address.split(' | ')[1]
            address_list.append(each_address)

        return address_list




