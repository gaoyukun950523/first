import os
import time
from datetime import datetime
import shutil

usb_path="G:/"
save_path="E:/"
while True:
    if os.path.exists(usb_path):
        shutil.copytree(usb_path,os.path.join(save_path,datetime.now().strftime("%Y%m%d_%H%M%S")))
        break
    else:
        time.sleep(10)