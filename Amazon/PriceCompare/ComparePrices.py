import urllib.request
import http
from bs4 import BeautifulSoup
import time
import collections
from PriceConverter.PriceConverter import PriceConverter
from decimal import *

class PriceChecker:

    def __init__(self, productDTO):
        self.productDTO = productDTO
        self.url = "https://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="

    def comparePrice(self):
        time.sleep(10)
        try:
            AmzonPoundPriceGBN = self._loadProductSearchResult()
        except:
            time.sleep(60)
            try:
                AmzonPoundPriceGBN = self._loadProductSearchResult()
            except:
                AmzonPoundPriceGBN = None
        try:
            ProductPriseBGN = Decimal(self.productDTO.price)
        except:
            print(str(self.productDTO.price))
            ProductPriseBGN = 0
        if AmzonPoundPriceGBN is None:
            return ProductPriseBGN
        AmazonPriceBGN = PriceConverter.convertFromPoundsToBGN(AmzonPoundPriceGBN)
        if AmazonPriceBGN < Decimal(ProductPriseBGN):
            if AmazonPriceBGN > Decimal(ProductPriseBGN * Decimal(0.9)):
                return Decimal(ProductPriseBGN * Decimal(0.9))
            return None
        if AmazonPriceBGN > Decimal(ProductPriseBGN):
            return ProductPriseBGN
        return None
        



    def _loadProductSearchResult(self):
        formatedProductDTOName = self.productDTO.name.strip().replace(" ", "+")
        url = self.url+ formatedProductDTOName
        print(url)
        try:
            dom = urllib.request.urlopen(url).read()
        except (http.client.IncompleteRead) as e:
            dom = e.partial
        soup = BeautifulSoup(dom, "html.parser")
        try:
            orderedListRoot = soup.find("ul", {"id": "s-results-list-atf"})
            resultsListElement = orderedListRoot.find("li", {"id": "result_0"})
            priceElement = resultsListElement.find("span", {"class": "a-size-base a-color-price s-price a-text-bold"})     
            price = priceElement.get_text()
            return float(price.strip().replace("£",""))
        except:
            return None



