class PoeItemType:
    def __init__(self, type, xSize, ySize):
        self.type = type
        self.xSize = xSize
        self.ySize = ySize

class PoeDetailedItem:
    def __init__(self, xSize, ySize, itemIdentifiedInfo, itemName, itemLevel):
        self.xSize = xSize
        self.ySize = ySize
        self.itemIdentifiedInfo = itemIdentifiedInfo
        self.itemName = itemName
        self.itemLevel = itemLevel
class PoeItemDB:

    def __init__(self):
        self.CurrencyTextIds = ""
        self.itemMap = dict()

    def initDB(self):
        f=open("./data/currency.txt", "r")
        self.CurrencyTextIds = f.read().splitlines()

        armourTypes = [["Amulet",1,1],
                        ["Belt",2,1],
                        ["Body_Armour",2,3],
                        ["Boots",2,2],
                        ["Bow",2,4],
                        ["Card",1,1],
                        ["Claw",2,2],
                        ["Currency",1,1],
                        ["Dagger",1,3],
                        ["Essence",1,1],
                        ["Flask",1,2],
                        ["Gem",1,1],
                        ["Gloves",2,2],
                        ["Helmet",2,2],
                        ["Jewel",1,1],
                        ["Map",1,1],
                        ["One-Handed_Axe",2,3],
                        ["One-Handed_Mace",2,3],
                        ["One-Handed_Sword",2,3],
                        ["Quiver",2,3],
                        ["Rapier",1,4],
                        ["Ring",1,1],
                        ["Sceptre",2,3],
                        ["Shield",2,4],
                        ["Staff",2,4],
                        ["Two-Handed_Axe",2,4],
                        ["Two-Handed_Mace",2,4],
                        ["Two-Handed_Sword",2,4],
                        ["Unique",-1,-1],
                        ["Wand",1,3]]

        for itemType in armourTypes:
            f = open("./data/items/"+itemType[0]+".txt", "r")

            itemTypeNames = f.read().splitlines()
            itemTypeClass =  PoeItemType(itemType[0],itemType[1],itemType[2])
            for itemName in itemTypeNames:
                self.itemMap[itemName] = itemTypeClass
            print("loaded file: "+itemType[0])
        return self.CurrencyTextIds

    def parseItemClipboard(self, itemInfo):
        itemInfo = itemInfo.splitlines()
        rarity = itemInfo[0]
        itemIdentifiedInfo = itemInfo[1]
        itemTypeName = itemInfo[2]
        if "-----" in itemInfo[2]:
            itemTypeName = itemInfo[1]
        itemIdentifiedInfo = ""

        itemLevel = -1
        i = 3
        while i < len(itemInfo):
            if "Item Level:" in itemInfo[i]:
                itemLevel = 1
            i += 1

        xSize = self.itemMap[itemTypeName].xSize
        ySize = self.itemMap[itemTypeName].ySize

        return PoeDetailedItem(xSize, ySize, itemIdentifiedInfo, itemTypeName, itemLevel)