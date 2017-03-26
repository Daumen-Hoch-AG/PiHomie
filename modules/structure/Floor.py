#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Testen der Funktionalität
# - Hinzufügen von Log-Nachrichten
# ===========================

class Floor(object):
    def __init__(self, number, name, description):
        self.number = number
        self.name = name
        self.description = description
        self.rooms = list()

        PIHOMIE.logs('STATUS', "Hello, I am the new FLOOR, {}".format(self.name))

    def getNumber(self):
        return self.number
    
    def setNumber(self, newNumber):
        self.number = newNumber
    
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, newDescription):
        self.description = newDescription

    def addRoom(self, newRoom):
        self.rooms.append(newRoom)
    
    def removeRoom(self, room):
        self.rooms.remove(room)
    
