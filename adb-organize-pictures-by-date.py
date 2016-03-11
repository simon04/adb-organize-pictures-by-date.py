#!/usr/bin/env python3
from string import Template
import subprocess

def get_new_file(old_dir, filename, date):
    return Template('/sdcard/Pictures/by-date/$date/').substitute(date=date)

old_dir = '/sdcard/Pictures/'
filename_pattern = '*.*'
for l in subprocess.check_output(['adb', 'shell', 'ls -l %s%s' % (old_dir, filename_pattern)]).decode().splitlines():
    parts = l.split()
    date = parts[4][0:7]
    filename = parts[6]
    old_file = old_dir + filename
    new_file = get_new_file(old_dir, filename, date)
    print('adb shell mv -v %s %s' % (old_file, new_file))
