#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Testen der Funktionalität
# - Hinzufügen von Log-Nachrichten
# ===========================

import ISetableSceneElement
import INotifiable

class SceneFunction(object, ISetableSceneElement, INotifiable):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.sensorsConditionDictionary = {} #{sensor1:value,sensor2:value}
        self.actorParamDictionary = {} #{actor1:param,actor2:param}
    
    def set(self):
        for actor in self.actorParamDictionary:
            actor.setParam(self.actorParamDictionary[actor])

    def sensorValueChanged(self, sensor):
        #Neue Klasse SensorCondition die Sensor, Wert und Kriterium (gleich, größer, kleiner) enthält und die .check(testvalue) Methode Gibt rgebnis zurück.

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description
    
    def setDescription(self, newDescription):
        self.description = newDescription

