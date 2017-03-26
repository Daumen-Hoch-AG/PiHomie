#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Testen der Funktionalität
# - Hinzufügen von Log-Nachrichten
# ===========================

class INotifiable(object):
    def sensorValueChanged(self, sensor):
        raise NotImplementedError("Abstrakte Methode wird in abgeleiteter Klasse definiert!")