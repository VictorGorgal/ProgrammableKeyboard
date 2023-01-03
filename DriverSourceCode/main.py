from Cache import Cache
from KeyboardFunctions import KeyboardFunctions


c = Cache()
for key in c.keys_map:
    c.press_key(key)
