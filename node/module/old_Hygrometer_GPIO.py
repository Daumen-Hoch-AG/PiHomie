#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Erben von Thermometer_GPIO
# In Generic Thermoter die Schnittstellenmethoden 
# festlegen und dort auf interne Methoden verweisen
# die in *_GPIO dann definiert werden (sonst 0)
# ===========================

import Hygrometer
import spidev


class Sensor(Hygrometer.Sensor):
	"""Schnittstellendefinition für Temperatur und Feuchtigkeitsmessung"""
	def __init__(self, id, nickname, ServiceObject, description=""):
		super(Sensor, self).__init__(id, nickname, ServiceObject, description="")
		self.Runden_C = ServiceObject['Opt'].getint('Runden', 'celsius')
		self.Runden_P = ServiceObject['Opt'].getint('Runden', 'prozent')
		# Diese Informationen holen:
		self.channelTemp = 1
		self.channelHumm = 0
		# --------------------------
		self.log.status('Hygrometer über GPIO initialisiert: Temp.CH {}, Humm.CH {}'.format(self.channelTemp, self.channelHumm))


	def getAllValuesAsDictionary(self):
		# Temperatur als ADC lesen
		self.temp = self._ReadChannel(self.channelTemp)
		self.humm = self._ReadChannel(self.channelHumm)
		# ADC-Wert in Grad umrechnen
		t_volts = self._ConvertVolts(self.temp, 5)
		h_volts = self._ConvertVolts(self.humm, 5)
		# Spannung in lesbare Werte umrechnen
		self.temp = self._VoltsToCelsius(t_volts, self.Runden_C)
		self.humm = self._VoltsToHumidity(h_volts, self.temp, self.Runden_P)
		return {'Temperatur':[self.temp, "°C"], 'Feuchte':[self.humm, "% rel."]}


	# -- private methods --

	# SPI Wert der Kanäle des Temperatur- und Feuchtigkeitsfühlers lesen
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


	# relative Luftfeuchtigkeit ermittelt (Places nimmt die erwarteten Nachkommastellen an, Schwellenwerte aus der Dokumentation des Moduls)
	def _VoltsToHumidity(self, volts, temp, places):
		if temp <= 22.5:
			humm = (volts - 0.128) / 0.0286
		elif temp > 22.5 and temp <= 27.5:
			humm = (volts - 0.085) / 0.0294
		else:
			humm = (volts - 0.038) / 0.0296
		humm = round(humm, places)
		return humm


if __name__ == "__main__":
	print "Direct access not allowed..."