#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

if sys.version_info[0]<3:	# (require python3)
	raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from base.base_app import create_app
from node_handler import Node # variabel

config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")
application = create_app(Node, config_path)

### DEBUG ###
application.run(debug=True, host="0.0.0.0", port=3000)
### DEBUG ###