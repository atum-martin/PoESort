import PoeInputMacro

def listTradeItemsThem(itemDB):
    x = 0
    y = 0
    screenshot = PoeInputMacro.screenTradeThem()
    itemSlots = [[]]
    while x < 12:
        while y < 5:
            #check is an item in slot
            if PoeInputMacro.checkTradeSlotThem(x, y, screenshot) and not itemSlots[x][y]:
                #whitelisted spot at the end of inv for scrolls
                #print("pixel "+str(x)+" "+str(y)+ " "+str(PoeInputMacro.checkInvSlot(x, y, screenshot)))
                item = PoeInputMacro.getItemStatusTradeThem(x,y)
                print(item)
                detailedItemInfo = itemDB.parseItemClipboard(item)
                addItemToLocalList(detailedItemInfo,x,y, itemSlots)
            y += 1
        y = 0
        x += 1
def addItemToLocalList(detailedItemInfo, x, y, itemSlots):
    itemX = 0
    itemY = 0
    while itemX < detailedItemInfo.sizeX:
        while itemY < detailedItemInfo.sizeY:
            itemSlots[x + itemX][y + itemY] = detailedItemInfo
            itemY += 1
        itemX += 1