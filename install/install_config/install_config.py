# This gets executed during ClamGuard's install process to update the config file according to the system setup.
import sys
import fileinput
import os

# System vars
program_data = os.environ['PROGRAMDATA']

# clamd.conf
with open('clamd.conf', 'r') as file:
  data = file.read()

data = data.replace('%DBLOC%', program_data)

with open('clamd.conf', 'w') as file:
  file.write(data)
