import os

from .linux import LinuxService
from .windows import WindowsService

# Automatically load the correct service based on the OS
if os.name == "nt":
    platform_service = WindowsService()
else:
    platform_service = LinuxService()
