#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Erben von Thermometer_GPIO
# In Generic Thermoter die Schnittstellenmethoden 
# festlegen und dort auf interne Methoden verweisen
# die in *_GPIO dann definiert werden (sonst 0)
# ===========================

import Thermometer
import spidev


class Sensor(Thermometer.Sensor):
	"""Schnittstellendefinition für Temperatur und Feuchtigkeitsmessung"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Sensor, self).__init__(id, nickname, ServiceObject, description="")
		self.Runden_C = ServiceObject['Opt'].getint('Runden', 'celsius')
		# Diese Informationen holen:
		self.channelTemp = 1
		# --------------------------
		self.log.status('Thermometer über GPIO initialisiert: CH {}'.format(self.channelTemp))


	def getAllValuesAsDictionary(self):
		# Temperatur als ADC lesen
		self.temp = self._ReadChannel(self.channelTemp)
		# ADC-Wert in Grad umrechnen
		t_volts = self._ConvertVolts(self.temp, 5)
		# Spannung in lesbare Werte umrechnen
		self.temp = self._VoltsToCelsius(t_volts, self.Runden_C)
		return {'Temperatur':[self.temp, "°C"],}


	# -- private methods --

	# SPI Wert der Kanäle des Temperaturfühlers lesen
	def _ReadChannel(self, channel):
		spi = spidev.SpiDev()
		spi.open(0, 0)
		adc = spi.xfer2([1, (8 + channel) << 4, 0])
		data = ((adc[1] & 3) << 8) + adc[2]
		spi.close()
		return data


	def _ConvertVolts(self, data, places):  # implementit
		# Umwandlung des digitalen ADC-Wertes in Volt (Places nimmt die erwarteten Nachkommastellen an)
		volts = (3.3 / 1023)*data
		volts = round(volts,places)
		return volts


	# Umwandlung der Voltzahl in Grad Celcius (Places nimmt die erwarteten Nachkommastellen an)
	def _VoltsToCelsius(self, volts, places):
		kelvin = volts/0.01
		celcius = round(kelvin-273.15, places)
		return celcius


if __name__ == "__main__":
	print "Direct access not allowed..."