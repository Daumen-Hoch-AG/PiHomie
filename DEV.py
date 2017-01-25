#!/usr/bin/python
# -*- coding: utf-8 -*-

# Wo sammelt man die Imports ???
# (wenn auch Klassen darauf zugreifen)
import os
import datetime
import requests
################################


# Module - Services
import modules.services.Logging as Logging
import modules.services.Forecast as Forecast
import modules.services.Schedule as Schedule

# Module - Hardware
import modules.hardware.RollerShutter as RollerShutter
import modules.hardware.RollerShutter_Fibaro_FG222 as RollerShutter_Fibaro_FG222



if __name__ == '__main__':
	print "Zum Testen und importieren in eine interaktive Python-Shell"
	# from DEV import *
	# e.g. R = RollerShutter.Actor(1, "MyFoo")