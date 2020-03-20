import pyautogui
import time
import ctypes
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import win32clipboard
#1080p
#17,162 - 650,162
#17,794 - 650,793
#24 items - 26.375 pixels per item

#1273-589 1904-588
#1272-850 1904-851
class ResolutionConfig:
    inv_click_xoffset = 1
    inv_click_yoffset = 1
    stash_click_xoffset = 1
    stash_click_yoffset = 1
    item_slot_adjustment = 1
    tab_dropdown_loc_x = 1
    tab_dropdown_loc_y = 1
    first_tab_loc_x = 1
    first_tab_loc_y = 1
    tab_pixel_size = 1
    trade_click_x_them = 1
    trade_click_y_them = 1
    screenshot_inv_x = 1
    screenshot_inv_y = 1
    screenshot_inv_width = 1
    screenshot_inv_height = 1
    screenshot_trade_them_x = 1
    screenshot_trade_them_y = 1
    screenshot_trade_them_width = 1
    screenshot_trade_them_height = 1
    screenshot_trade_x = 1
    screenshot_trade_y = 1
    screenshot_trade_width = 1
    screenshot_trade_height = 1
    inv_test_offset_x = 1
    inv_test_offset_y = 1
    trade_them_test_offset_x = 1
    trade_them_test_offset_y = 1
    trade_me_test_offset_x = 1
    trade_me_test_offset_y = 1


def setupMacro(config):
    pyautogui.PAUSE = 0.1
    ResolutionConfig.inv_click_xoffset = config['inv_click_xoffset']
    ResolutionConfig.inv_click_yoffset = config['inv_click_yoffset']
    ResolutionConfig.stash_click_xoffset = config['stash_click_xoffset']
    ResolutionConfig.stash_click_yoffset = config['stash_click_yoffset']
    ResolutionConfig.item_slot_adjustment = config['item_slot_adjustment']
    ResolutionConfig.tab_dropdown_loc_x = config['tab_dropdown_loc_x']
    ResolutionConfig.tab_dropdown_loc_y = config['tab_dropdown_loc_y']
    ResolutionConfig.first_tab_loc_x = config['first_tab_loc_x']
    ResolutionConfig.first_tab_loc_y = config['first_tab_loc_y']
    ResolutionConfig.tab_pixel_size = config['tab_pixel_size']
    ResolutionConfig.trade_click_x_them = config['trade_click_x_them']
    ResolutionConfig.trade_click_y_them = config['trade_click_y_them']
    ResolutionConfig.trade_click_x_me = config['trade_click_x_them']
    ResolutionConfig.trade_click_y_me= config['trade_click_y_them']
    ResolutionConfig.screenshot_inv_x = config['screenshot_inv_x']
    ResolutionConfig.screenshot_inv_y = config['screenshot_inv_y']
    ResolutionConfig.screenshot_inv_width = config['screenshot_inv_width']
    ResolutionConfig.screenshot_inv_height = config['screenshot_inv_height']
    ResolutionConfig.screenshot_trade_them_x = config['screenshot_trade_them_x']
    ResolutionConfig.screenshot_trade_them_y = config['screenshot_trade_them_y']
    ResolutionConfig.screenshot_trade_them_width = config['screenshot_trade_them_width']
    ResolutionConfig.screenshot_trade_them_height = config['screenshot_trade_them_height']
    ResolutionConfig.screenshot_trade_x = config['screenshot_trade_x']
    ResolutionConfig.screenshot_trade_y = config['screenshot_trade_y']
    ResolutionConfig.screenshot_trade_width = config['screenshot_trade_width']
    ResolutionConfig.screenshot_trade_height = config['screenshot_trade_height']

    ResolutionConfig.inv_test_offset_x = ResolutionConfig.inv_click_xoffset - ResolutionConfig.screenshot_inv_x
    ResolutionConfig.inv_test_offset_y = ResolutionConfig.inv_click_yoffset - ResolutionConfig.screenshot_inv_y

    ResolutionConfig.trade_me_test_offset_x = ResolutionConfig.trade_click_x_me - ResolutionConfig.screenshot_trade_x
    ResolutionConfig.trade_me_test_offset_y = ResolutionConfig.trade_click_y_me - ResolutionConfig.screenshot_trade_y

    ResolutionConfig.trade_them_test_offset_x = ResolutionConfig.trade_click_x_them - ResolutionConfig.screenshot_trade_them_x
    ResolutionConfig.trade_them_test_offset_y = ResolutionConfig.trade_click_y_them - ResolutionConfig.screenshot_trade_them_y

def clickStashItem(x, y, isQuadTab):
    xadjustment = ResolutionConfig.item_slot_adjustment*(int(x))
    yadjustment = ResolutionConfig.item_slot_adjustment*(int(y))
    if not isQuadTab:
        xadjustment *= 2;
        yadjustment *= 2;
    pyautogui.keyDown('ctrl')
    pyautogui.moveTo(ResolutionConfig.stash_click_xoffset+xadjustment, ResolutionConfig.stash_click_yoffset+yadjustment, 0.2)
    pyautogui.click(ResolutionConfig.stash_click_xoffset+xadjustment, ResolutionConfig.stash_click_yoffset+yadjustment)
    pyautogui.keyUp('ctrl')


def clickInvItem(x, y):
    xadjustment = ResolutionConfig.item_slot_adjustment*2*x
    yadjustment = ResolutionConfig.item_slot_adjustment*2*y

    pyautogui.keyDown('ctrl')
    pyautogui.moveTo(ResolutionConfig.inv_click_xoffset + xadjustment, ResolutionConfig.inv_click_yoffset + yadjustment, 0.05)
    pyautogui.click(ResolutionConfig.inv_click_xoffset + xadjustment, ResolutionConfig.inv_click_yoffset + yadjustment)
    pyautogui.keyUp('ctrl')

def changeTab(tabId):
    pyautogui.moveTo(ResolutionConfig.tab_dropdown_loc_x, ResolutionConfig.tab_dropdown_loc_y, 0.2)
    pyautogui.click(ResolutionConfig.tab_dropdown_loc_x, ResolutionConfig.tab_dropdown_loc_y)
    time.sleep(0.5)
    pyautogui.moveTo(ResolutionConfig.first_tab_loc_x, ResolutionConfig.first_tab_loc_y+(ResolutionConfig.tab_pixel_size*tabId), 0.2)
    pyautogui.click(ResolutionConfig.first_tab_loc_x, ResolutionConfig.first_tab_loc_y+(ResolutionConfig.tab_pixel_size*tabId))
    time.sleep(0.5)

def getItemStatusInv(x, y):
    xadjustment = ResolutionConfig.item_slot_adjustment * 2 * x
    yadjustment = ResolutionConfig.item_slot_adjustment * 2 * y
    pyautogui.moveTo(ResolutionConfig.inv_click_xoffset + xadjustment, ResolutionConfig.inv_click_yoffset + yadjustment, 0.05)
    poeCopyItemInfo()
    return getClipboardData()

def getItemStatusTradeThem(x, y):
    xadjustment = ResolutionConfig.item_slot_adjustment * 2 * x
    yadjustment = ResolutionConfig.item_slot_adjustment * 2 * y
    pyautogui.moveTo(335 + xadjustment, 228 + yadjustment, 0.05)
    poeCopyItemInfo()
    return getClipboardData()

def hitTradeAccept():
    pyautogui.moveTo(0, 0, 0.5)
    pyautogui.leftClick()

def getItemStatusStash(x, y, isQuadTab):
    xadjustment = ResolutionConfig.item_slot_adjustment * x
    yadjustment = ResolutionConfig.item_slot_adjustment * y
    if not isQuadTab:
        xadjustment *= 2;
        yadjustment *= 2;
    pyautogui.moveTo(ResolutionConfig.stash_click_xoffset+xadjustment, ResolutionConfig.stash_click_yoffset+yadjustment, 0.2)
    poeCopyItemInfo()
    return getClipboardData()

def poeCopyItemInfo():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def getClipboardData():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.SetClipboardText("")
    win32clipboard.CloseClipboard()
    #print("clipboard: " + data)
    return data

def screenInv():
    return pyautogui.screenshot(region=(ResolutionConfig.screenshot_inv_x, ResolutionConfig.screenshot_inv_y, ResolutionConfig.screenshot_inv_width, ResolutionConfig.screenshot_inv_height))

def screenTradeThem():
    return pyautogui.screenshot(region=(ResolutionConfig.screenshot_trade_them_x, ResolutionConfig.screenshot_trade_them_y, ResolutionConfig.screenshot_trade_them_width, ResolutionConfig.screenshot_trade_them_height))

def screenTradeMe():
    return pyautogui.screenshot(region=(ResolutionConfig.screenshot_trade_x, ResolutionConfig.screenshot_trade_y, ResolutionConfig.screenshot_trade_width, ResolutionConfig.screenshot_trade_height))

def countItemsOnMyTradeScreen():
    itemCount = 0
    screen = screenTradeMe()
    x = 0
    y = 0
    while x < 12:
        while y < 5:
            if checkTradeSlotMe(x, y, screen):
                itemCount += 1
        y += 1
    y = 0
    x += 1
    return itemCount

def openStash():
    pyautogui.moveTo(1171, 587, 0.5)
    pyautogui.leftClick()

def closeStash():
    pyautogui.press('esc')

def typeOutChat(message):
    pyautogui.press('enter')
    pyautogui.typewrite(message)
    pyautogui.press('enter')

def checkInvSlot(x, y, screenshot):
    xadjustment = ResolutionConfig.item_slot_adjustment * 2 * x
    yadjustment = ResolutionConfig.item_slot_adjustment * 2 * y
    pixel = screenshot.getpixel((ResolutionConfig.inv_test_offset_x + xadjustment, ResolutionConfig.inv_test_offset_y + yadjustment))
    # empty slot pixels
    if pixel[0] < 10 and pixel[1] < 10 and pixel[2] < 10:
        return False
    return True

def checkTradeSlotThem(x, y, screenshot):
    xadjustment = ResolutionConfig.item_slot_adjustment * 2 * x
    yadjustment = ResolutionConfig.item_slot_adjustment * 2 * y
    pixel = screenshot.getpixel((trade_them_test_offset_x + xadjustment, trade_them_test_offset_y + yadjustment))
    # empty slot pixels
    if pixel[0] < 10 and pixel[1] < 10 and pixel[2] < 10:
        return False
    print(format(pixel))
    return True

def checkTradeSlotMe(x, y, screenshot):
    xadjustment = ResolutionConfig.item_slot_adjustment * 2 * x
    yadjustment = ResolutionConfig.item_slot_adjustment * 2 * y
    pixel = screenshot.getpixel((trade_me_test_offset_x + xadjustment, trade_me_test_offset_y + yadjustment))
    # empty slot pixels
    if pixel[0] < 10 and pixel[1] < 10 and pixel[2] < 10:
        return False
    print(format(pixel))
    return True

def getForegroundWindowName():
    user32 = ctypes.windll.user32

    h_wnd = user32.GetForegroundWindow()
    #pid = wintypes.DWORD()
    #user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))

    length = user32.GetWindowTextLengthW(h_wnd)
    buf = create_unicode_buffer(length + 1)
    user32.GetWindowTextW(h_wnd, buf, length + 1)

    if buf.value:
        return buf.value
    else:
        return None