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


print "Teste Logging-Service...."
Log = Logging.Logger(first=True)


if __name__ == '__main__':
	print 3*"\n"
	# from DEV import *
	print "Zum Testen und importieren in eine interaktive Python-Shell\n"
	print '> R = RollerShutter.Actor(1, "Foo")'
	R = RollerShutter.Actor(1, "Foo")
	#print '> R.log("Bar", "status")'
	#R.log("Bar", "error")
	