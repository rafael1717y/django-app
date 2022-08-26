

import os

try:
    DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE")
    if DEVELOPMENT_MODE:
        DEVELOPMENT_MODE = False
        print('l 9', DEVELOPMENT_MODE)
except:
    DEVELOPMENT_MODE = True 
    print(DEVELOPMENT_MODE)
