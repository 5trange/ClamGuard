# -----------------------------------------------------------------------------
# filesystemMonitor [Resident Shield]

# -----------------------------------------------------------------------------
# Name:        filesystemMonitor.py
# Product:     ClamGuard
#
# Authors:      Adith, Bilal, Vinayak
#   ________                ______                     __
#  / ____/ /___ _____ ___  / ____/_  ______ __________/ /
# / /   / / __ `/ __ `__ \/ / __/ / / / __ `/ ___/ __  /
#/ /___/ / /_/ / / / / / / /_/ / /_/ / /_/ / /  / /_/ /
#\____/_/\__,_/_/ /_/ /_/\____/\__,_/\__,_/_/   \__,_/
#
#
#
# Created:     2021/Mar/05
# Copyright:
# Licence:
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

##IMPORTS

import watchdog.events
import threading
import os
import subprocess
import watchdog.observers
from process import *

processes = []
cpu_cont = int(os.cpu_count() / 2)
sysDrive = os.environ['SYSTEMDRIVE']
ignoreRec: str = sysDrive + r'$Recycle.Bin'
print("   ________                ______                     __")
print("  / ____/ /___ _____ ___  / ____/_  ______ __________/ /")
print(" / /   / / __ `/ __ `__ \/ / __/ / / / __ `/ ___/ __  /")
print("/ /___/ / /_/ / / / / / / /_/ / /_/ / /_/ / /  / /_/ /")
print("\____/_/\__,_/_/ /_/ /_/\____/\__,_/\__,_/_/   \__,_/")
print("\n\nStarting Service..")
watchableFiles = ['*.cmd', '*.exe', '*.msi', '*.dll', '*.zip', '*.7z', '*.bat', '*.rar', '*.sys', '*.vbs']


class SystemHandler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=watchableFiles, ignore_patterns=None,
                                                             case_sensitive=True)

    def on_created(self, event):
        buffer = event.src_path
        buffer = buffer.replace(":", ":\\")
        #print(f"File was created at {buffer}")
        self.SingleThread = threading.Thread(target = self.scan , args=[buffer])
        self.SingleThread.start()

    def scan(self, path):
        print(path)
        process = Popen(['clamdscan.exe','--multiscan',path], stdout=PIPE, shell=True, encoding='utf8') #Using --multiscan to use multiprocessing
        while True:
            output = process.stdout.readline()
            #yield output
            if output == '':
                break
            else:
                print(output)



event_handler = SystemHandler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, sysDrive, recursive=True)
observer.start()
print("Service Started.")
observer.join()
