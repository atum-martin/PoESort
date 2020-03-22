import PoeStash
import PoeInputMacro
import PoeItemDB
import PoeStashSort
import PoeChaosRecipe
import PoeDepositAll
import PoeTradeMacros
import PoeLogListener
import time
import threading
import math
import json


with open('data/config/1080p_config.json') as json_data_file:
    config = json.load(json_data_file)

PoeInputMacro.setupMacro(config)
itemDB = PoeItemDB.PoeItemDB()
itemDB.initDB()

#PoeLogListener.regexWhisper("2019/12/28 19:41:02 12140169 ac9 [INFO Client 3304] @From WishItsMylast: Hi, I would like to buy your Tabula Rasa Simple Robe listed for 11 chaos in Metamorph (stash tab \"~price 5 chaos\"; position: left 23, top 2)")
#PoeLogListener.regexWhisper("2020/01/03 17:56:59 364642828 ac9 [INFO Client 3128] @To 요하네스벅포: ty")
#PoeLogListener.regexWhisper("2020/01/03 17:56:11 364594421 ac9 [INFO Client 3128] @To 요하네스벅포: 안녕하세요, 변형(보관함 탭 \"판매\", 위치: 왼쪽 11, 상단 3)에 1 fuse(으)로 올려놓은 창살 지도(Cage Map)(T3)을(를) 구매하고 싶습니다")

t = threading.Thread(target=PoeLogListener.listenToFile, args=(itemDB,))
t.start()

def checkIsPoeInForeground():
    foregroundText = PoeInputMacro.getForegroundWindowName()
    if "Path of Exile" in foregroundText:
        return True
    return False

from pynput import keyboard

def on_release(key):
    if format(key) == '<97>':
        print("martin chaos test: " + format(key)+" "+PoeInputMacro.getForegroundWindowName())
        #PoeChaosRecipe.getTabContents()
        if checkIsPoeInForeground():
            #PoeInputMacro.getItemStatusStash(0,0,True)
            PoeStashSort.sortStashTab(-1, itemDB)
            #PoeStashSort.sortStashTab(5, itemDB)
        else:
            print("action: "+format(key)+" aborted, window not in focus")
    if format(key) == '<98>':
        print("martin test: " + format(key)+" "+PoeInputMacro.getForegroundWindowName())
        try:
            if checkIsPoeInForeground():
                PoeChaosRecipe.getChaosRecipe(itemDB)
                #PoeTradeMacros.listTradeItemsThem(itemDB)
            else:
                print("action: " + format(key) + " aborted, window not in focus")
        except Exception as e:
            print("out of chaos recipe: "+str(e))
    if format(key) == '<99>':
        print("martin test: " + format(key)+" "+PoeInputMacro.getForegroundWindowName())
        if checkIsPoeInForeground():
            PoeDepositAll.despositAllInv()
        else:
            print("action: "+format(key)+" aborted, window not in focus")

with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()





