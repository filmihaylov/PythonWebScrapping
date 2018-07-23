import sys
sys.path.append("..")
from CoreBot.FunctionalClassess.CasioWebsiteLogicalExtractor import CasioWebsiteLogicalExtractor
from CoreBot.FunctionalClassess.WatchScrapper import WatchScrapper
from CoreBot.DTOs.WatchCasioBgDTO import WatchCasioBgDTO

class CasioScrapper:

    baseUrl = "https://casioshop.bg"

    def ScrapeAllWatchesAndGetDtos(self):
        extractor = CasioWebsiteLogicalExtractor(self.baseUrl)
        watchLinks = extractor.returnAllWatchLinks()
        watchScrapp = WatchScrapper(watchLinks, self.baseUrl)
        watchDtoList = watchScrapp.returnWatchCasioDtoList()
        print("-------------len-------of DTOs to be Send To DB")
        print(len(watchDtoList))
        return watchDtoList




#s = CasioScrapper()

#v = s.ScrapeAllWatchesAndGetDtos()
