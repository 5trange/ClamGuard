from subprocess import *
print("Starting ClamAV Daemon.. Please wait..")
clamav_daemon= Popen(['clamd.exe'], stdout = PIPE, encoding = 'utf-8')
print("Starting ClamGuard WatchDog")
from filesystemMonitor import *
print("Starting ClamGuard")
from ui_start import *
