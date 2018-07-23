import sys
import time
sys.path.append("..")
from CoreBot.DTOs.WatchCasioBgDTO import WatchCasioBgDTO
import psycopg2
import urllib.request
from decimal import Decimal

class StoreCasioDTO:

    def __init__(self):
        pass


    def storeWathesDTOS(self, casioDTOList):
        self.casioDTOList = casioDTOList
        for wathcDto in self.casioDTOList:
            try:
                time.sleep(0.5)
                self._storeWatch(wathcDto)
            except Exception as e:
                print("type error: " + str(e))

    def readAllWathcDTOFromCasioWatchInMemory(self):
        casioDTOLIST = []
        conn = psycopg2.connect(database = "CasioBot", user = "postgres", password = "MortalKombat3", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT * FROM casiowatch")
        row = cur.fetchone()
        while row is not None:
            name, description, price, image =row
            casioDTOLIST.append(WatchCasioBgDTO(name, image, price, description))
            row = cur.fetchone()
        conn.close()
        return casioDTOLIST
    

    def _storeWatch(self, wathcDTO):
        conn = psycopg2.connect(database = "CasioBot", user = "postgres", password = "MortalKombat3", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        price = Decimal(wathcDTO.price)
        name = str(wathcDTO.name).replace("'", '')
        try:
            imageurl = wathcDTO.image.strip()
            imageurl = str(imageurl).replace(" ", '')
            response = urllib.request.urlopen(imageurl)
            image = response.read()
        except Exception as e:
            image = b''
            print(wathcDTO.image + "Possible unable to open this image and download it")
        description = ",".join(wathcDTO.description)
        description = str(description).replace("'", '')
        description = str(description).replace('"', '')
        cur.execute("INSERT INTO casiowatch (name,description,price,image) \
                    VALUES ('%s', '%s', %d, %s)" % (name, description, price, psycopg2.Binary(image)))

        conn.commit()
        #print("Records created successfully")
        conn.close()
        #print("Opened database successfully")

    def storeWatchesAmazonReadyTable(self, casioDTOList):
        self.casioDTOList = casioDTOList
        for wathcDto in self.casioDTOList:
            try:
                self.storeWatch(wathcDto)
            except Exception as e:
                print("type error: " + str(e))

    def storeWatchAmazonReadyTable(self, wathcDto):
        conn = psycopg2.connect(database = "CasioBot", user = "postgres", password = "MortalKombat3", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        price = Decimal(wathcDTO.price)
        name = str(wathcDTO.name).replace("'", '')
        image = wathcDto.image

        # check the format
        description = ",".join(wathcDTO.description)
        description = str(description).replace("'", '')
        description = str(description).replace('"', '')
        cur.execute("INSERT INTO amazonwatch (name,description,price,image) \
                    VALUES ('%s', '%s', %d, %s)" % (name, description, price, psycopg2.Binary(image)))

        conn.commit()
        #print("Records created successfully")
        conn.close()
        #print("Opened database successfully")

    def updateWatchAmazonReadyTable(self):
        pass

    def removeAllDataFromCasioWatchesTable(self):
        pass

    def readAllWathcDTOFromAmazonWatchInMemory(self):
        pass


