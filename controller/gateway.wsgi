#!/usr/bin/python3

import sys
import os

if sys.version_info[0]<3:	# (require python3)
	raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from PiHomieController import app as application
