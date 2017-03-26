#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Testen der Funktionalität
# - Hinzufügen von Log-Nachrichten
# ===========================

class House(object):
    def __init__(self, name):
        self.name = name
        self.floors = list()
        
        PIHOMIE.logs('STATUS', "Hello, I am your new HOUSE, {}".format(self.name))
    
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def addFloor(self, floor):
        self.floor.append(floor)
    
    def removeFloor(self, floor):
        self.floors.remove(floor)