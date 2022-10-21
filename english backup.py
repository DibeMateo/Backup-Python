import os
from pathlib import Path
import datetime
import shutil
from datetime import datetime
now = datetime.now()

def delete_old_backup():
    files = os.listdir("path old backup")

    for name in files:
        if name.endswith(".bak"):
            os.remove("path old backup\\%s " % name)
            print(name)

def copy_new_backup():
    backup_new = os.path.join("path new backup")
    backup_old = os.path.join("path old backup")
    files = os.listdir("path new backup")

    date_backup = date()

    for name in files:
        for i in range(100):
            if name.startswith("file name" + date_backup) or ("file name" + date_backup):
                print(name)
                shutil.copy2(backup_new, backup_old)

def date():
    year =  now.year
    month = now.month
    day = now.day

    return (str(year) + str(month) + str(day))