#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Testen der Funktionalität
# - Hinzufügen von Log-Nachrichten
# ===========================
import ISetableSceneElement

class Scene(object, ISetableSceneElement):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.sceneFunctions = list()

    #Ruft alle SceneFunctions aus der Szene auf
    def set(self):
        for sceneFunction in self.sceneFunctions:
            sceneFunction.set()
    
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description
    
    def setDescription(self, newDescription):
        self.description = newDescription