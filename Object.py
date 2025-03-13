class Animal:
    def __init__(self, animalID, animalName, imageName, imageEx):
        self.animalID = animalID
        self.animalName = animalName
        self.imageName = imageName
        self.imageEx = imageEx

class Goods:
    def __init__(self, goodsID, goodsPrice, goodsStock, AnimalID, imageName, goodsEx):
        self.goodsID = goodsID
        self.goodsPrice = goodsPrice
        self.goodsStock = goodsStock
        self.AnimalID = AnimalID
        self.imageName = imageName
        self.goodsEx = goodsEx
