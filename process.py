# -----------------------------------------------------------------------------
# process.py [Run Functions]

# -----------------------------------------------------------------------------
# Name:        process.py
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

# Imports
import os
import subprocess
from subprocess import Popen, PIPE
from shlex import split


class RunProcess:
    def run_command(self, cmd):
        try:
            self.process = Popen(cmd, stdout=PIPE, shell=True, encoding='utf8')
            while True:
                output = self.process.stdout.readline()
                #yield output
                if output == '':
                    break
                else:
                    yield output
                    continue

        except:
            print('Process stopped!')

    def kill_command(self):
        try:
            self.process.kill()
        except:
            print('Process cannot be stopped!')
