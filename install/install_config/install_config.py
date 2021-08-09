# This gets executed during ClamGuard's install process to update the config file according to the system setup.
# Replaces the variable %DBLOC% with actual database location.
# Also can be used to set the location of log files.
import sys
import fileinput
import os

# System vars
program_data = os.environ['PROGRAMDATA']
program_data.replace("/","\\")
dbloc = program_data + '\ClamGuard\db'
clamdloc = program_data + '\ClamGuard\log\clamguard_clamd.log'
freshloc = program_data + '\ClamGuard\log\clamguard_fresh.log'

# clamd.conf
with open('clamd.conf', 'r') as file:
  data = file.read()

data = data.replace('%DBLOC%', dbloc)
data = data.replace('%LOGLOC%', clamdloc)

with open('clamd.conf', 'w') as file:
  file.write(data)

# freshclam.conf
with open('freshclam.conf', 'r') as file:
  data = file.read()

data = data.replace('%DBLOC%', dbloc)
data = data.replace('%LOGLOC%', freshloc)

with open('freshclam.conf', 'w') as file:
  file.write(data)
