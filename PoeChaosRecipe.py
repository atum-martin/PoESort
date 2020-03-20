import PoeStash
import PoeInputMacro
import time

class PoeChaosRecipe:
    tabResults = []
    tabResultsTimestamp = 0.0
    tabs = [4]

def getTabContents():

    #return cached results if less than 5 minutes old
    if len(PoeChaosRecipe.tabResults) > 0 and time.time() - PoeChaosRecipe.tabResultsTimestamp < 300:
        return PoeChaosRecipe.tabResults
    for tab in PoeChaosRecipe.tabs:
        items = PoeStash.getStash(tab)
        PoeChaosRecipe.tabResults.append(items)
    PoeChaosRecipe.tabResultsTimestamp = time.time()
    return PoeChaosRecipe.tabResults

def getChaosRecipe(itemDB):
    tabResults = getTabContents()
    withdrawItems = []
    withdrawItems.append(findChaosItem(tabResults, 'isHelmet', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isGloves', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isBoots', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isRing', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isRing', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isAmulet', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isBelt', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isWeapon', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isWeapon', withdrawItems))
    withdrawItems.append(findChaosItem(tabResults, 'isBodyArmour', withdrawItems))

    removeItems(tabResults, withdrawItems)
    tabSetup = PoeStash.getTabs()

    for tab in PoeChaosRecipe.tabs:
        if tabHasItems(tab, withdrawItems):
            PoeInputMacro.changeTab(tab)
            for item in withdrawItems:
                if item.tabId == tab:
                    print("withdraw: "+str(item.x)+" "+str(item.y))
                    PoeInputMacro.clickStashItem(item.x, item.y, tabSetup.isQuad(tab))

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

def alreadyReserved(item, withdrawItems):
    return item in withdrawItems
