import requests
import json
from decimal import *

class PriceConverter:

    # http://data.fixer.io/api/latest?access_key=3f02108c7353ff0dc1bd5d6d0469309b
    @staticmethod
    def _connectoToService():
        r = requests.get("http://data.fixer.io/api/latest?access_key=3f02108c7353ff0dc1bd5d6d0469309b&symbols=BGN,GBP")
        response = r.json()
        return response
    
    responseJson = _connectoToService.__func__()

    @classmethod
    def convertFromPoundsToBGN(cls, ammount):
        poundsToEur = Decimal(ammount) / Decimal(cls.responseJson['rates']['GBP'])
        BGN = Decimal(poundsToEur) * Decimal(cls.responseJson['rates']['BGN'])
        return Decimal(BGN)
    
    @classmethod
    def convertFromBGNToPounds(cls, ammount):
        BGNToEur = Decimal(ammount) / Decimal(cls.responseJson['rates']['BGN'])
        GBP = Decimal(BGNToEur) * Decimal(cls.responseJson['rates']['GBP'])
        return Decimal(GBP)