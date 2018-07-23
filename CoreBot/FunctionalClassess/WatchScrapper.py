import sys
sys.path.append("..")
from CoreBot.DTOs.WatchCasioBgDTO import WatchCasioBgDTO
from .CasioWebsiteLogicalExtractor import CasioWebsiteLogicalExtractor
import urllib.request
import http
from bs4 import BeautifulSoup
import time

class WatchScrapper:

    def __init__(self, watchLinks, baseurl):
        self.watchLinks = watchLinks
        self.watchCasioDtoList = []
        self.baseurl = baseurl
        self.fullWatchLinksList = []
        for watchLink in self.watchLinks:
            self.fullWatchLinksList.append(baseurl+watchLink)

    def returnWatchCasioDtoList(self):
        self._populateCasioDtoList()
      #  print(len(self.watchCasioDtoList))
      #  for printdto in self.watchCasioDtoList:
       #     printdto.printAllProperties()
        return self.watchCasioDtoList
    
    def _populateCasioDtoList(self):
        for wathcLink in self.fullWatchLinksList:
            time.sleep(0.5)
            soup = self._extractWatchHtml(wathcLink)
            image = self._extractWatchImage(soup)    
            description = self._extractWatchDescription(soup)
            price = self._extractWatchPrice(soup)
            name = self._extractWatchName(soup)
            #For Now will return image link (think of storage strategy later)
            watchDTO = WatchCasioBgDTO(name, image, price , description)
            self.watchCasioDtoList.append(watchDTO)
        

    def _extractWatchHtml(self , url):
        try:
            dom = urllib.request.urlopen(url).read()
        except (http.client.IncompleteRead) as e:
            dom = e.partial
        soup = BeautifulSoup(dom, "html.parser")
        return soup
        
    def _extractWatchImage(self, soup):
        images = soup.find_all("a", {"id": "product"})
        for imagelink in images:
            linktag =imagelink.find('img')
            linkimage = linktag.get("src")
            return self.baseurl+"/"+linkimage.strip()
                    
    
    def _extractWatchDescription(self, soup):
        listDescription = []
        rightsideWithDescription = soup.find("div", {"id": "rightside"})
        innerdiv = rightsideWithDescription.find("div", {"class": "inner_wrap"})
        ultopDescription = innerdiv.find("ul")
        listsDescription = ultopDescription.find_all("li")
        for list in listsDescription:
            listDescription.append(list.get_text())
        return listDescription
        
    
    def _extractWatchPrice(self, soup):
        spantag = soup.find("span", {"id": "pprice"})
        strongprice = spantag.find("strong")
        return strongprice.get_text()
    
    def _extractWatchName(self, soup):
        namediv = soup.find("div", {"id": "rightside"})
        heading = namediv.find("h1")
        return heading.get_text()    
        


