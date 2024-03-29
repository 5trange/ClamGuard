# -----------------------------------------------------------------------------
# Name          :   filesystemMonitor.py
# Product       :   ClamGuard
# Authors       :   Adith, Bilal, Vinayak
# Created       :   Mar-05-2021
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------

# Imports
import watchdog.events
import threading
import os
import subprocess
import watchdog.observers
from subprocess import *

program_data = os.environ['PROGRAMDATA']
program_data.replace("/","\\")
quarantine = program_data + '\\ClamGuard\\quarantine'
sysDrive = os.environ['SYSTEMDRIVE']+"\\"
ignoreRec: str = sysDrive + r'$Recycle.Bin'
print("Starting ClamGuard WatchDog Service..")
watchableFiles = ['*.cmd', '*.exe', '*.msi', '*.dll', '*.zip', '*.7z', '*.bat', '*.rar', '*.sys', '*.vbs']


class SystemHandler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=watchableFiles, ignore_patterns=None,
                                                             case_sensitive=True)

    def on_created(self, event):
        buffer = event.src_path
        buffer = buffer.replace(":", ":\\")
        self.watchdog_thread = threading.Thread(target = self.scan , args=[buffer])
        self.watchdog_thread.start()

    def scan(self, path):
        print(path)
        self.process = Popen(['clamdscan.exe', '--multiscan', f'--move={quarantine}', path], stdout=PIPE, encoding='utf8', creationflags = CREATE_NO_WINDOW )
        while self.process.poll() is None:
            self.ret = self.process.stdout.readline()
            if self.ret == '':
                break
            else:
                print(self.ret)


event_handler = SystemHandler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, sysDrive, recursive=True)
observer.start()
print("WatchDog Service Started.")
