import math
import PoeStash
import PoeInputMacro
import PoeDepositAll

def sortStashTab(tabId, itemDB):
    tabSetup = PoeStash.getTabs()
    if tabId == -1:
        tabId = getDefaultQuad(tabSetup)

    items = PoeStash.getStash(tabId)
    PoeInputMacro.changeTab(tabId)

    isQuadTab = tabSetup.isQuad(tabId)
    sortTab(tabSetup.mapTab, tabId, items, itemDB, tabSetup, 'isMap')
    sortTab(tabSetup.currencyTab, tabId, items, itemDB, tabSetup, 'isCurrency')
    sortTab(tabSetup.essenceTab, tabId, items, itemDB, tabSetup, 'isEssence')
    sortTab(tabSetup.fragmentTab, tabId, items, itemDB, tabSetup, 'isFragment')
    sortTab(findStashTabId('div', tabSetup), tabId, items, itemDB, tabSetup, 'isDivination')
    sortTab(findStashTabId('flasks', tabSetup), tabId, items, itemDB, tabSetup, 'isFlask')
    sortTab(findStashTabId('jewels', tabSetup), tabId, items, itemDB, tabSetup, 'isJewel')
    sortTab(findStashTabId('jewels', tabSetup), tabId, items, itemDB, tabSetup, 'isMetamorph')

def findStashTabId(tabName, tabSetup):
    for tabInfo in tabSetup.tabInfoList:
        if tabInfo.name in tabName:
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