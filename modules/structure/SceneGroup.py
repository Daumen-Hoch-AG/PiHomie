#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Testen der Funktionalität
# - Hinzufügen von Log-Nachrichten
# ===========================
import ISetableSceneElement

class SceneGroup(object, ISetableSceneElement):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.scenes = list()

    #Aufrufen aller Scenen in der Gruppe
    def set(self):
        for scene in self.scenes:
            scene.set()
    
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, newDescription):
        self.description = newDescription

    def addScene(self, newScene):
        self.scenes.append(newScene)
    
    def removeScene(self, scene):
        self.scenes.remove(scene)