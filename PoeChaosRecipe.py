import PoeStash
import PoeInputMacro
import time

class PoeChaosRecipe:
    tabResults = []
    tabResultsTimestamp = 0.0
    tabs = [0]
    tabSetup = None

def getTabContents():

    #return cached results if less than 5 minutes old
    if len(PoeChaosRecipe.tabResults) > 0 and time.time() - PoeChaosRecipe.tabResultsTimestamp < 300:
        return PoeChaosRecipe.tabResults
    for tab in PoeChaosRecipe.tabs:
        items = PoeStash.getStash(tab)
        PoeChaosRecipe.tabResults.append(items)
    PoeChaosRecipe.tabResultsTimestamp = time.time()
    return PoeChaosRecipe.tabResults

def printChaosAmounts(tabResults):
    print("helmets: "+str(countChaosItem(tabResults, 'isHelmet')))
    print("gloves: " + str(countChaosItem(tabResults, 'isGloves')))
    print("boots: " + str(countChaosItem(tabResults, 'isBoots')))
    print("rings: " + str(countChaosItem(tabResults, 'isRing')))
    print("amulets: " + str(countChaosItem(tabResults, 'isAmulet')))
    print("belts: " + str(countChaosItem(tabResults, 'isBelt')))
    print("weapons: " + str(countChaosItem(tabResults, 'isChaosWeapon')))
    print("body: " + str(countChaosItem(tabResults, 'isBodyArmour')))

def getChaosRecipe(itemDB):
    tabResults = getTabContents()
    withdrawItems = []
    printChaosAmounts(tabResults)
    withdrawItems.append(findChaosItem(tabResults, 'isHelmet', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isGloves', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isBoots', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isRing', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isRing', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isAmulet', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isBelt', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isChaosWeapon', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isChaosWeapon', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isBodyArmour', withdrawItems))

    removeItems(tabResults, withdrawItems)

    if PoeChaosRecipe.tabSetup is None:
        PoeChaosRecipe.tabSetup = PoeStash.getTabs()

    for tab in PoeChaosRecipe.tabs:
        if tabHasItems(tab, withdrawItems):
            PoeInputMacro.changeTab(tab)
            for item in withdrawItems:
                if item.tabId == tab:
                    print("withdraw: "+str(item.x)+" "+str(item.y)+" "+item.typeLine)
                    PoeInputMacro.clickStashItem(item.x, item.y, PoeChaosRecipe.tabSetup.isQuad(tab))

def removeItems(tabResults, withdrawItems):
    for tab in tabResults:
        for item in withdrawItems:
            if item in tab:
                tab.remove(item)

def tabHasItems(tabId, withdrawItems):
    for item in withdrawItems:
        if item.tabId == tabId:
            return True
    return False

def findChaosItem(tabs, func, withdrawItems):
    for tab in tabs:
        for item in tab:
            #item level 65+, rare only, unid,
            if getattr(item, func)() and not alreadyReserved(item, withdrawItems) and not item.identified and item.ilvl >= 65 and item.frameType == 2:
                return item
    raise Exception("no item found for slot: "+func)

def countChaosItem(tabs, func):
    count = 0
    for tab in tabs:
        for item in tab:
            #item level 65+, rare only, unid,
            if getattr(item, func)() and not item.identified and item.ilvl >= 65 and item.frameType == 2:
                count += 1
    return count

def alreadyReserved(item, withdrawItems):
    return item in withdrawItems
