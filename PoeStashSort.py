import math
import PoeStash
import PoeInputMacro
import PoeDepositAll
import PoePlayerConfig

def sortStashTab(tabId, itemDB):
    tabSetup = PoeStash.getTabs()
    if tabId == -1:
        tabId = getDefaultQuad(tabSetup)

    items = PoeStash.getStash(tabId)
    PoeInputMacro.changeTab(tabId)

    isQuadTab = tabSetup.isQuad(tabId)
    if getTabId(tabSetup, tabSetup.mapTab, PoePlayerConfig.PlayerConfig.sorting_override_maps) >= 0:
        sortTab(getTabId(tabSetup, tabSetup.mapTab, PoePlayerConfig.PlayerConfig.sorting_override_maps), tabId, items, itemDB, tabSetup, 'isMap')

    if getTabId(tabSetup, tabSetup.currencyTab, PoePlayerConfig.PlayerConfig.sorting_override_currency) >= 0:
        sortTab(getTabId(tabSetup, tabSetup.currencyTab, PoePlayerConfig.PlayerConfig.sorting_override_currency), tabId, items, itemDB, tabSetup, 'isCurrency')

    if getTabId(tabSetup, tabSetup.essenceTab, PoePlayerConfig.PlayerConfig.sorting_override_essence) >= 0:
        sortTab(getTabId(tabSetup, tabSetup.essenceTab, PoePlayerConfig.PlayerConfig.sorting_override_essence), tabId, items, itemDB, tabSetup, 'isEssence')

    if getTabId(tabSetup, tabSetup.fragmentTab, PoePlayerConfig.PlayerConfig.sorting_override_fragments) >= 0:
        sortTab(getTabId(tabSetup, tabSetup.fragmentTab, PoePlayerConfig.PlayerConfig.sorting_override_fragments), tabId, items, itemDB, tabSetup, 'isFragment')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_override_div) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_override_div), tabId, items, itemDB, tabSetup, 'isDivination')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_override_delve) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_override_delve), tabId, items, itemDB, tabSetup, 'isDelveItem')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_flask) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_flask), tabId, items, itemDB, tabSetup, 'isFlask')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_jewel) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_jewel), tabId, items, itemDB, tabSetup, 'isJewel')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_prophecy) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_prophecy), tabId, items, itemDB, tabSetup, 'isProphecy')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_incubator) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_incubator), tabId, items, itemDB, tabSetup, 'isIncubator')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_oil) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_oil), tabId, items, itemDB, tabSetup, 'isOil')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_catalyst) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_catalyst), tabId, items, itemDB, tabSetup, 'isCatalyst')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_metamorph) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_metamorph), tabId, items, itemDB, tabSetup, 'isMetamorph')

    if getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_gem) >= 0:
        sortTab(getTabId(tabSetup, -1, PoePlayerConfig.PlayerConfig.sorting_gem), tabId, items, itemDB, tabSetup, 'isGem')

def getTabId(tabSetup, autoSetupTabId, overrideTabId):
    if isinstance(overrideTabId, int):
        #user has given an id and not a tabname.
        if overrideTabId == -1 and autoSetupTabId == -1:
            return -1
        if overrideTabId >= 0:
            return overrideTabId
        if autoSetupTabId >= 0:
            return autoSetupTabId
    else:
        #overrideTabId is a string (lookup by tabname)
        if overrideTabId == "-1" and autoSetupTabId == -1:
            return -1
        if overrideTabId == "-1":
            return autoSetupTabId
        return findStashTabId(overrideTabId, tabSetup)

def shouldSort(autoSetupTabId, overrideTabId):
    if isinstance(overrideTabId, int):
        if overrideTabId == -1 and autoSetupTabId == -1:
            return False
        if overrideTabId >= 0:
            return True
        if autoSetupTabId >= 0:
            return True
    else:
        if overrideTabId == "-1" and autoSetupTabId == -1:
            return False
        if overrideTabId != "-1":
            return True
        if autoSetupTabId >= 0:
            return True


def findStashTabId(tabName, tabSetup):
    for tabInfo in tabSetup.tabInfoList:
        if tabName == tabInfo.name:
            print("found stash tab for: "+tabName+" "+tabInfo.name+" "+str(tabInfo.id))
            return (tabInfo.id+1)
    return -1

def getDefaultQuad(tabSetup):
    for tabInfo in tabSetup.tabInfoList:
        if tabSetup.isQuad(tabInfo.id):
            print("default quad: "+tabInfo.name+" Id: "+str(tabInfo.id))
            return tabInfo.id
    if len(tabSetup.tabInfoList) >= 1:
        return tabSetup.tabInfoList[len(tabSetup.tabInfoList)-1].id
    return -1

def sortTab(targetTab, originTab, items, itemDB, tabSetup, func):
    if targetTab == -1:
        return
    filteredItems = []
    for item in items:
        if getattr(item, func)(itemDB):
            print(item.typeLine + " : " +func+" : "+ str(getattr(item, func)(itemDB)))
            PoeInputMacro.clickStashItem(item.x, item.y, tabSetup.isQuad(originTab))
            filteredItems.append(item)
    if len(filteredItems) > 0:
        #clickTheseItemsInInv(targetTab, filteredItems)
        PoeInputMacro.changeTab(targetTab)
        PoeDepositAll.despositAllInv()
        PoeInputMacro.changeTab(originTab)

def clickTheseItemsInInv(targetTab, items):
    PoeInputMacro.changeTab(targetTab)
    i = 0
    while i < len(items):
        x = math.floor((i / 5))
        y = i % 5
        PoeInputMacro.clickInvItem(x, y)
        i += 1