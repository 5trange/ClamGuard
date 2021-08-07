# This gets executed during ClamGuard's install process to update the config file according to the system setup.
import sys
import fileinput
import os

# System vars
program_data = os.environ['PROGRAMDATA']
dbloc = program_data + '\.clamguard\db'
dbloc.replace("/","\\")

# clamd.conf
with open('clamd.conf', 'r') as file:
  data = file.read()

data = data.replace('%DBLOC%', dbloc)

with open('clamd.conf', 'w') as file:
  file.write(data)

# freshclam.conf
with open('freshclam.conf', 'r') as file:
  data = file.read()

data = data.replace('%DBLOC%', dbloc)

with open('freshclam.conf', 'w') as file:
  file.write(data)
