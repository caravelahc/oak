import gc
from network import WLAN, AP_IF, STA_IF
import webrepl


AP_WLAN = WLAN(AP_IF)
STA_WLAN = WLAN(STA_IF)

AP_WLAN.active(False)
# AP_WLAN.config(essid='pyoak2', password='deprecated')

STA_WLAN.active(True)
STA_WLAN.connect('caravela', 'deprecated')
while not STA_WLAN.isconnected():
    pass

webrepl.start()

del WLAN, AP_IF, STA_IF, webrepl
gc.collect()
del gc
