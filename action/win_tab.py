# import pywinctl as pwc
# import time
# time.sleep(2)
# # Get the active window
# win = pwc.getActiveWindow()
# if win is not None:
#     print("Active window:", win.title)
#     win.minimize() # Minimize the active window
#     time.sleep(2)
#     win.restore()   # Restore the minimized window
#     #win.close()
# else:
#     print("No active window found")


import pyautogui
pyautogui.hotkey("win" , "down", "down")
