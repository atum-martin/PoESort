#import re
import regex as re
import PoeInputMacro
import time
import PoeStash

class ClientState:
    tradeReqs = dict()
    state = 0
    currentTradePartner = ""
    tabSetup = PoeStash.getTabs()
    itemDB = 0

class TradeReq:
    def __init__(self, itemName, price, tab, leftIdx, downIdx):
        self.price = price
        self.itemName = itemName
        self.tab = tab
        self.leftIdx = leftIdx
        self.downIdx = downIdx
        self.timestamp = time.time()

def listenToFile(itemDB):
    ClientState.itemDB = itemDB
    print("starting to listen to POE logfile")
    from filetail import FileTail
    tail = FileTail("C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client.txt")
    for line in tail:
        regexWhisper(line)


def regexWhisper(input):
    #Hangul = korean characters
    #2020/01/04 18:00:10 15393796 ac9 [INFO Client 2240] : The_WalkingDead has joined the area.
    regex = "([0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*\\[INFO Client [0-9]*] @(To|From) (?:<(.+)> )?([\p{Hangul}a-zA-Z0-9_, ]+): (.+)"
    joinTheAreaRegex = "([0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*\\[INFO Client [0-9]*] : ([\p{Hangul}a-zA-Z0-9_, ]+) has joined the area."
    leaveTheAreaRegex = "([0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*\\[INFO Client [0-9]*] : ([\p{Hangul}a-zA-Z0-9_, ]+) has left the area."
    tradeRegex = "I would like to buy your ([a-zA-Z0-9, _()]*) listed for ([a-zA-Z0-9, _~]*) in ([a-zA-Z0-9, _~]*) \(stash tab \"([a-zA-Z0-9, _~]*)\"; position: left ([0-9]*), top ([0-9]*)"
    tradeAcceptedRegex = "([0-9]{4}\/[0-9]{2}\/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*\\[INFO Client [0-9]*] : Trade accepted."
    m = re.match(regex, input)
    if m:
        #print(str(m.group(1))+" "+str(m.group(2))+" "+str(m.group(3))+" "+str(m.group(4))+" "+str(m.group(5)))
        whisper = m.group(5)
        #print(whisper)
        timestamp = m.group(1)
        whisperDirection = m.group(2)
        clan = m.group(3)
        player = m.group(4)
        if "From" in whisperDirection and "I would like to buy your" in whisper:
            #open stash
            print("whisper: "+ whisper)
            tradeWhisper = re.search(tradeRegex, whisper)
            print("tradeWhisper: " + tradeWhisper.group(1) + " " + tradeWhisper.group(
                2) + " " + tradeWhisper.group(3) + " " + tradeWhisper.group(4) + " " + tradeWhisper.group(5) + " " + tradeWhisper.group(6))
            itemName = tradeWhisper.group(1)
            price = tradeWhisper.group(2)
            league = tradeWhisper.group(3)

            tab = tradeWhisper.group(4)
            leftIdx = tradeWhisper.group(5)
            downIdx = tradeWhisper.group(6)
            tradeReq = TradeReq(itemName, price, tab, leftIdx, downIdx)
            ClientState.tradeReqs[player] = tradeReq
            removeOldTrades()
            invitePlayer(player)

    m = re.match(joinTheAreaRegex, input)
    if m:
        # joined the area
        player = m.group(2)
        print("joined area "+player)
        if ClientState.tradeReqs[player]:
            refreshTimeout(player)
            getItemsFromStash(ClientState.tradeReqs[player])
            print("items from stash " + player)
            tradePlayer(player)
            spawnTradeThread()
    m = re.match(tradeAcceptedRegex, input)
    if m:
        time.sleep(1)
        kickPlayer(ClientState.currentTradePartner)
    m = re.match(leaveTheAreaRegex, input)
    if m:
        # left the area
        player = m.group(2)

def getItemsFromStash(trade):
    PoeInputMacro.openStash()
    tabId = findStashTabId(trade.tab)
    isQuadTab = ClientState.tabSetup.isQuad(tabId)
    PoeInputMacro.changeTab(tabId)
    PoeInputMacro.clickStashItem(trade.leftIdx, trade.downIdx, isQuadTab)
    PoeInputMacro.closeStash()

def findStashTabId(tabName):
    for tabInfo in ClientState.tabSetup.tabInfoList:
        if tabInfo.name in tabName:
            return tabInfo.id
    return -1

def refreshTimeout(player):
    if ClientState.tradeReqs[player]:
        ClientState.tradeReqs[player].timestamp = time.time()

def removeOldTrades():
    for playerName, trade in ClientState.tradeReqs.items():
        if trade.timestamp < time.time()-60:
            print("removing old trade: "+playerName)
            del ClientState.tradeReqs[playerName]

def invitePlayer(playerName):
    inviteStr = "/invite "+playerName
    PoeInputMacro.typeOutChat(inviteStr)

def tradePlayer(playerName):
    tradeStr = "/tradewith " + playerName
    ClientState.currentTradePartner = playerName
    PoeInputMacro.typeOutChat(tradeStr)
    spawnTradeThread()

def spawnTradeThread():
    waitTimer = 30
    print("spawnTradeThread")
    while waitTimer > 0:
        time.sleep(1)
        if PoeInputMacro.countItemsOnMyTradeScreen() <= 10 and ClientState.state == 0:
            print("spawnTradeThread opened trade screen ")
            ClientState.state = 1
            #trade screen opened
            addRequestedItems()
            waitTimer = 30
        if ClientState.state == 1:
            print("spawnTradeThread opened trade screen ")
            screenshot = checkThereItems()
            #PoeInputMacro.hitTradeAccept()
        waitTimer -= 1

def checkThereItems():
   return True

def addRequestedItems():
    player = ClientState.currentTradePartner
    trade = ClientState.tradeReqs[player]
    addRequestedItem(trade)

def addRequestedItem(trade):
    x = 0
    y = 0
    screenshot = PoeInputMacro.screenInv()
    while x < 12:
        while y < 5:
            # check is an item in slot
            if PoeInputMacro.checkInvSlot(x, y, screenshot):
                # whitelisted spot at the end of inv for scrolls
                if not (x == 11 and y == 3) and not (x == 11 and y == 4):
                    itemInfo = PoeInputMacro.getItemStatusInv(x, y)
                    detailedItemInfo = ClientState.itemDB.parseItemClipboard(itemInfo)
                    print("addRequestedItem ")
                    if detailedItemInfo.itemIdentifiedInfo in trade.itemName:
                        PoeInputMacro.clickInvItem(x, y)
                    print("addRequestedItem "+ detailedItemInfo.itemIdentifiedInfo+" "+trade.itemName)
            y += 1
        y = 0
        x += 1
