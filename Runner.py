from CoreBot.CasioScrapper import CasioScrapper
from Storage.StoreCasioDTO import StoreCasioDTO
from CoreBot.DTOs.WatchCasioBgDTO import WatchCasioBgDTO
from Amazon.PriceCompare.ComparePrices import PriceChecker
import collections


#casioScrapper = CasioScrapper()
#print("Started To scrape all Wathces")
#allCasioDTOS = casioScrapper.ScrapeAllWatchesAndGetDtos()
#print("All Watches Dtos Got")
#print("Started Atempt To Save Them To DB")
#storage = StoreCasioDTO()
#storage.storeWathesDTOS(allCasioDTOS)

stor = StoreCasioDTO()
watches = stor.readAllWathcDTOFromCasioWatchInMemory()

listOFWatchesForOffer = []

for watc in watches:
    watc.price = watc.price.replace(" ","")
    watc.price = watc.price.replace("лв.","")
    watc.price = watc.price.replace(",",".")
    p = PriceChecker(watc)
    price = p.comparePrice()

    if price is not None:
        listOFWatchesForOffer.append(price)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(str(len(listOFWatchesForOffer)))

#for p in a:
#    print(p)




#p = PriceChecker(productDTOMock)

#price = p.comparePrice()

#print(productDTOMock.price)
#print(price)
