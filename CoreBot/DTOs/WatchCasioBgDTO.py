class WatchCasioBgDTO:

    def __init__(self, name, image, price, description):
        self.name = name
        self.image = image
        self.price = price
        self.description = description
        
    def printAllProperties(self):
        print(self.name, self.image, self.price, self.description)
