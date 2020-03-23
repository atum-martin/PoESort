import PoeInputMacro

def despositAllInv():
    x = 0
    y = 0
    screenshot = PoeInputMacro.screenInv()
    while x < 12:
        while y < 5:
            #check is an item in slot
            if PoeInputMacro.checkInvSlot(x, y, screenshot):
                #whitelisted spot at the end of inv for scrolls
                if not (x == 11 and y == 3) and not (x == 11 and y == 4):
                    #print("pixel "+str(x)+" "+str(y)+ " "+str(PoeInputMacro.checkInvSlot(x, y, screenshot)))
                    PoeInputMacro.clickInvItem(x,y)
                    screenshot = PoeInputMacro.screenInv()
            y += 1
        y = 0
        x += 1