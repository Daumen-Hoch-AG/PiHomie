#!/usr/bin/python
# -*- coding: utf-8 -*-

# Modules for main
#import os



# Systemobjekt initialisieren und in die Namespaces hineinreichen
import modules.services.Systemservice as Systemservice
PIHOMIE= Systemservice.PiHomieObject()


# Modules - Services
import modules.services.Forecast as Forecast
Forecast.PIHOMIE = PIHOMIE

import modules.services.Schedule as Schedule
Schedule.PIHOMIE = PIHOMIE


# Modules - Hardware
import modules.hardware.Generic as Generic
Generic.PIHOMIE = PIHOMIE

import modules.hardware.RollerShutter as RollerShutter
RollerShutter.PIHOMIE = PIHOMIE

import modules.hardware.RollerShutter_ZWAVE as RollerShutter_ZWAVE
RollerShutter_ZWAVE.PIHOMIE = PIHOMIE

import modules.hardware.Thermometer_GPIO as Thermometer_GPIO
Thermometer_GPIO.PIHOMIE = PIHOMIE

import modules.hardware.Hygrometer_GPIO as Hygrometer_GPIO
Hygrometer_GPIO.PIHOMIE = PIHOMIE


#print 2*"\n","--- FOR DEV : ---"
##
#print 'H = Hygrometer_GPIO.Sensor(1,"Fo", SysSrv)'
#H = Hygrometer_GPIO.Sensor(1,"Fo", SysSrv)
#print 'T = Hygrometer_GPIO.Sensor(1,"Fo", SysSrv)'
#T = Thermometer_GPIO.Sensor(2,"Ba", SysSrv)

print 'G = Generic.Actor(1,"Fo")'
G = Generic.Actor(1,"Foo")
print 'RS = RollerShutter.Sensor(2, "Bar")'
RS = RollerShutter.Sensor(2, "Bar")
#RS = RollerShutter_ZWAVE.GenericActor(2, "Bar", SysSrv)
#
#print "[ - FINISHED - ]"


if __name__ == '__main__':
	print 2*"\n"
	# from DEV import *
	print "Zum Testen und importieren in eine interaktive Python-Shell\n"

	#print "H.getValue"
	#print H.getValue('Feuchte')
	#print "T.getValue"
	#print T.getValue('Temperatur')
	##GA = Generic.Actor(1,"Foo",SysSrv)
	#RS = RollerShutter_ZWAVE.GenericActor(2, "Bar", SysSrv)
	