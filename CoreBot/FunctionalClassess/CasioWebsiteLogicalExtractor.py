import urllib.request
import http
from bs4 import BeautifulSoup

class CasioWebsiteLogicalExtractor:

    watchesLinks = []
    verifyAllModelsLinkGotMen = 0
    verifyAllModelsLinkGotWomen = 0
    
    #helperForDebugging = {"page": 0, "links" : 0}
    #addPageDict = []
    def __init__(self, baseUrl):
        self.urlMen = baseUrl + "/men-watches"
        self.urlWomen = baseUrl + "/ladie-watches"

    def returnAllWatchLinks(self):
        self._setCountWatchersChecker()
        self._getAllWatchLinks()
        #for i in self.watchesLinks:
            #print(i)
        print(len(self.watchesLinks))
        print("Compare Links Top Bottom")
        print(str(self.verifyAllModelsLinkGotMen + self.verifyAllModelsLinkGotWomen))
        
        #for i in self.addPageDict:
         #   print("page:"+str(i["page"]) + "links:"+ str(i["links"]))
        
        return self.watchesLinks
    
    def _getAllWatchLinks(self):
        pageindex = 1
        while(True):
            soup = self._pageNavigatorChecker(self.urlMen + "/page/" + str(pageindex))
            if not soup:
                break
            self._extractLinksFromPage(soup)
         #   self.helperForDebugging["page"] = pageindex
          #  self.addPageDict.append(self.helperForDebugging.copy())
            pageindex = pageindex+1     
        
        pageindex = 1
        while(True):
            soup = self._pageNavigatorChecker(self.urlWomen + "/page/" + str(pageindex))
            if not soup:
                break
            self._extractLinksFromPage(soup)
         #   self.helperForDebugging["page"] = pageindex
          #  self.addPageDict.append(self.helperForDebugging.copy())
            pageindex = pageindex+1     

    def _pageNavigatorChecker(self, url):
        try:
            dom = urllib.request.urlopen(url).read()
        except (http.client.IncompleteRead) as e:
            dom = e.partial
        soup = BeautifulSoup(dom, "html.parser")
        pageContent = soup.find("div", {"id": "results"})
        if "Няма резултати" in pageContent.get_text():
            return False
        else:
            return soup   

    def _extractLinksFromPage(self, soup):
        watchDivs = soup.findAll("div", {"class": "product_box"})      
        linkcountnumberpage = 0
        for t in watchDivs:
            links = t.findAll('a')
            for href in links:
                if ("Casio" in href.get_text()) or ("CASIO" in href.get_text()):
                    self.watchesLinks.append(href.get('href'))
                    linkcountnumberpage = linkcountnumberpage + 1
     #   self.helperForDebugging["links"] = linkcountnumberpage
     
    def _setCountWatchersChecker(self):
        soup = self._pageNavigatorChecker(self.urlMen + "/page/" + "1")
        if soup:
            menWatchLinks = soup.find("b", {"id": "rescount"})
            self.verifyAllModelsLinkGotMen = int(menWatchLinks.get_text())
        soup = self._pageNavigatorChecker(self.urlWomen + "/page/" + "1")
        if soup:
            menWatchLinks = soup.find("b", {"id": "rescount"})
            self.verifyAllModelsLinkGotWomen = int(menWatchLinks.get_text())   



#s = CasioWebsiteLogicalExtractor("https://casioshop.bg")

#s.returnAllWatchLinks()
