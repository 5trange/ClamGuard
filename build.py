# This File exist to build the project data use this file before running the project

import subprocess
from pathlib import Path

if not Path("src/resources/resources_rc.py").is_file():
    process = subprocess.Popen(
        [
            "pyside6-rcc",
            "./resources/resources.qrc",
            "-o",
            "./src/core/resources_rc.py",
        ]
    )
    return_code = process.wait()
    if return_code != 0:
        print("Error : Running the pyside6-rcc command")
