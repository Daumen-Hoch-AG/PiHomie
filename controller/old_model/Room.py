#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======== To Do ! ==========
# - Testen der Funktionalität
# - Hinzufügen von Log-Nachrichten
# ===========================

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.sceneGroups = list()
        self.scenes = list()

        PIHOMIE.logs('STATUS', "Hello, I am a new ROOM, {}".format(self.name))

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description
    
    def setDescription(self, newDescription):
        self.description = newDescription
    
    def addSceneGroup(self, newSceneGroup):
        self.sceneGroups.append(newSceneGroup)
    
    def removeSceneGroup(self, sceneGroup):
        self.sceneGroups.remove(sceneGroup)
    
    def addScene(self, newScene):
        self.scenes.append(newScene)
    
    def removeScene(self, scene):
        self.scenes.remove(scene)