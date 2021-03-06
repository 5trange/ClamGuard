# -----------------------------------------------------------------------------
# filesystemMonitor.py [Monitor Filesystem]

# -----------------------------------------------------------------------------
# Name:        filesystemMonitor.py
# Product:     ClamGuard
#
# Authors:      Adith, Bilal, Vinayak
#
# Created:     2021/Feb/09
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
# File System Monitor for realtime protection using WatchDog
# Uses Multiprocessing module to split the core count of the CPU into half to watch the folders.
# Maybe use string splicing to correct the string? Then we can use watchdog instead.

import watchdog.events
import os
import watchdog.observers
from multiprocessing import Process
from typing import Optional

processes = []
cpu_cont = int(os.cpu_count() / 2)
sysDrive = os.environ['SYSTEMDRIVE']
ignoreRec: str = sysDrive + r'$Recycle.Bin'
print("Starting Service..")
watchableFiles = ['*.txt', '*.cmd', '*.exe', '*.msi', '*.dll', '*.zip', '*.7z', '*.bat', '*.rar', '*.sys', '*.bin']


class SystemHandler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=watchableFiles, ignore_patterns=None,
                                                             case_sensitive=True)

    def on_created(self, event):
        buffer = event.src_path
        buffer = buffer.replace(":", ":\\")
        print(f"File was created at {buffer}")


event_handler = SystemHandler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, sysDrive, recursive=True)
observer.start()
print("Service Started.")
observer.join()

"""
import os
import win32file
import win32con

ACTIONS = {
    1: "Created",
    2: "Deleted",
    3: "Updated",
    4: "Renamed from something",
    5: "Renamed to something"
}
# Thanks to Claudio Grondi for the correct set of numbers
FILE_LIST_DIRECTORY = 0x0001

path_to_watch = "C:\\"
hDir = win32file.CreateFile(
    path_to_watch,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
)
while 1:
    #
    # ReadDirectoryChangesW takes a previously-created
    # handle to a directory, a buffer size for results,
    # a flag to indicate whether to watch subtrees and
    # a filter of what changes to notify.
    #
    # NB Tim Juchcinski reports that he needed to up
    # the buffer size to be sure of picking up all
    # events when a large number of files were
    # deleted at once.
    #
    results = win32file.ReadDirectoryChangesW(
        hDir,
        1024,
        True,
        win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
        win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
        win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
        win32con.FILE_NOTIFY_CHANGE_SIZE |
        win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
        win32con.FILE_NOTIFY_CHANGE_SECURITY,
        None,
        None
    )
    for action, file in results:
        full_filename = os.path.join(path_to_watch, file)
        print(full_filename, ACTIONS.get(action, "Unknown"))
"""
