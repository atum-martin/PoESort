import requests
import PoePlayerConfig

class PoeTab:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def isQuad(self):
        if 'QuadStash' in self.type:
            return True
        return False

class PoeItem:
    def __init__(self, x, y, w, h, identified, typeLine, iconPath, tabId, ilvl, frameType):
        self.typeLine = ''
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tabId = tabId
        self.iconPath = iconPath
        self.identified = identified
        self.typeLine = typeLine
        self.ilvl = ilvl
        self.frameType = frameType

    def __str__(self):
        return self.typeLine + " "+ str(self.x) + " " + str(self.y) + " " + str(self.w) + " " + str(self.h) + " " + str(self.identified)

    def isBoots(self):
        if "2DItems/Armours/Boots" in self.iconPath:
            return True
        return False

    def isBelt(self):
        if "2DItems/Belts" in self.iconPath:
            return True
        return False

    def isJewel(self, itemDB):
        if "2DItems/Jewels" in self.iconPath:
            return True
        return False

    def isWeapon(self):
        if "2DItems/Weapons/OneHandWeapons" in self.iconPath:
            return True
        return False

    def isChaosWeapon(self):
        if "2DItems/Weapons/OneHandWeapons" in self.iconPath:
            return True
        if "2DItems/Armours/Shields" in self.iconPath:
            return True
        return False

    def isAmulet(self):
        if "2DItems/Amulets" in self.iconPath:
            return True
        return False

    def isGloves(self):
        if "2DItems/Armours/Glove" in self.iconPath:
            return True
        return False

    def isGem(self):
        if "2DItems/Gem" in self.iconPath:
            return True
        return False

    def isBodyArmour(self):
        if "2DItems/Armours/BodyArmours" in self.iconPath:
            return True
        return False

    def isHelmet(self):
        if "2DItems/Armours/Helmet" in self.iconPath:
            return True
        return False

    def isRing(self):
        if "2DItems/Rings" in self.iconPath:
            return True
        return False

    def isMap(self, itemDB):
        if " map" in self.typeLine.lower():
            return True
        return False

    def isEssence(self, itemDB):
        #if " essence of " in self.typeLine.lower():
        if "Currency/Essence" in self.iconPath:
            return True

        return False

    def isProphecy(self, itemDB):
        if "Currency/ProphecyOrbRed" in self.iconPath:
            return True
        return False

    def isFlask(self, itemDB):
        if " flask" in self.typeLine.lower():
            return True
        return False

    def isMetamorph(self, itemDB):
        if "Currency/Metamorph" in self.iconPath:
            return True
        return False

    def isIncubator(self, itemDB):
        if "Currency/Incubation" in self.iconPath:
            return True
        return False

    def isOil(self, itemDB):
        if "Currency/Oils" in self.iconPath:
            return True
        return False

    def isCatalyst(self, itemDB):
        if "Currency/Catalysts" in self.iconPath:
            return True
        return False

    def isGem(self, itemDB):
        if "2DItems/Gems" in self.iconPath:
            return True
        return False

    def isDelveItem(self, itemDB):
        if "Currency/Delve" in self.iconPath:
            return True
        return False


    def isDivination(self, itemDB):
        if "2DItems/Divination/InventoryIcon.png" in self.iconPath:
            return True
        return False

    def isFragment(self, itemDB):
        if "splinter" in self.typeLine.lower():
            return True
        if "sacrifice at" in self.typeLine.lower():
            return True
        if "fragment of" in self.typeLine.lower():
            return True
        if " scarab" in self.typeLine.lower():
            return True
        if "divine vessel" in self.typeLine.lower():
            return True
        if "offering to the godess" in self.typeLine.lower():
            return True
        if "2DItems/Maps" in self.iconPath:
            return True
        return False

    def isCurrency(self, itemDB):
        for currencyName in itemDB.CurrencyTextIds:
            if currencyName in self.typeLine:
                return True
        return False

class StashSetup:
    def __init__(self, currencyTab, essenceTab, fragmentTab, mapTab, tabInfoList):
        self.currencyTab = currencyTab
        self.essenceTab = essenceTab
        self.fragmentTab = fragmentTab
        self.mapTab = mapTab
        self.tabInfoList = tabInfoList
    def __str__(self):
        return str(self.currencyTab) + " " + str(self.essenceTab) + " " + str(self.fragmentTab) + " " + str(self.mapTab)

    def isQuad(self, id):
        return self.tabInfoList[id].isQuad()
def getTabs():
    URL = "https://www.pathofexile.com/character-window/get-stash-items?accountName="+PoePlayerConfig.PlayerConfig.account_name+"&realm=pc&league="+PoePlayerConfig.PlayerConfig.league+"&tabs=1&tabIndex=0&public=false"

    headers = {'cookie': "POESESSID="+PoePlayerConfig.PlayerConfig.poe_session_id,
              'x-requested-with': 'XMLHttpRequest',
              'referer': 'https://www.pathofexile.com/',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'accept': 'application/json, text/javascript, */*; q=0.01',
              'accept-language': 'en-US,en;q=0.9',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

    r = requests.get(url=URL, headers=headers)

    data = r.json()
    print(data)
    currencyTab = -1
    essenceTab = -1
    fragmentTab = -1
    mapTab = -1
    tabInfoList = []

    for tab in data['tabs']:
        i = tab['i']
        name = tab['n']
        type = tab['type']
        if 'CurrencyStash' in type and currencyTab == -1:
            currencyTab = i;
        if 'MapStash' in type and mapTab == -1:
            mapTab = i;
        if 'FragmentStash' in type and fragmentTab == -1:
            fragmentTab = i;
        if 'EssenceStash' in type and essenceTab == -1:
            essenceTab = i;
        tabInfo = PoeTab(i, name, type)
        tabInfoList.append(tabInfo)
    return StashSetup(currencyTab, essenceTab, fragmentTab, mapTab, tabInfoList)


def getStash(tabId):
    URL = "https://www.pathofexile.com/character-window/get-stash-items?accountName="+PoePlayerConfig.PlayerConfig.account_name+"&realm=pc&league="+PoePlayerConfig.PlayerConfig.league+"&tabs=0&tabIndex="+str(tabId)+"&public=false"

    headers = {'cookie': "POESESSID="+PoePlayerConfig.PlayerConfig.poe_session_id,
              'x-requested-with': 'XMLHttpRequest',
              'referer': 'https://www.pathofexile.com/',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'accept': 'application/json, text/javascript, */*; q=0.01',
              'accept-language': 'en-US,en;q=0.9',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

    r = requests.get(url=URL, headers=headers)

    data = r.json()
    print(data)
    poeItems = []
    for item in data['items']:
       x = item['x']
       y = item['y']
       w = item['w']
       h = item['h']
       ilvl = item['ilvl']
       iconPath = item['icon']
       typeLine = item['typeLine']
       identified = item['identified']
       frameType = item['frameType']
       #print(typeLine+" "+iconPath+" "+str(frameType))
       itemIn = PoeItem(x, y, w, h, identified, typeLine, iconPath, tabId, ilvl, frameType)
       poeItems.append(itemIn)
    return poeItems