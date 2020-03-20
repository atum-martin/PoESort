import math
import PoeStash
import PoeInputMacro
import PoeDepositAll

def sortStashTab(tabId, itemDB):
    items = PoeStash.getStash(tabId)
    PoeInputMacro.changeTab(tabId)
    tabSetup = PoeStash.getTabs()
    isQuadTab = tabSetup.isQuad(tabId)
    sortTab(tabSetup.mapTab, tabId, items, itemDB, 'isMap')
    sortTab(tabSetup.currencyTab, tabId, items, itemDB, 'isCurrency')
    sortTab(tabSetup.essenceTab, tabId, items, itemDB, 'isEssence')
    sortTab(tabSetup.fragmentTab, tabId, items, itemDB, 'isFragment')
    sortTab(21, tabId, items, itemDB, 'isDivination')
    sortTab(20, tabId, items, itemDB, 'isFlask')
    sortTab(19, tabId, items, itemDB, 'isJewel')
    sortTab(18, tabId, items, itemDB, 'isMetamorph')

def sortTab(targetTab, originTab, items, itemDB, func):
    filteredItems = []
    tabSetup = PoeStash.getTabs()
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