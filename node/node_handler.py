from base.base_handler import BaseHandler
from flask import current_app
import requests, uuid, json

#TODO: Noodle definitionen und Liste Zentral ablegen?
from .noodles import *

class Node(BaseHandler):
    def __init__(self):
        super().__init__()

        host = current_app.config['CONTROLLER']['HOST']
        port = current_app.config['CONTROLLER']['PORT']
        self.uuid = current_app.config['UUID'] #Setzt uuid aus Config
        self.controller_endpoint = "http://{}{}/api".format(host,port)
        self.init_node() 

        self.dict = {
            "setValue" : self.setValue,
            "setAll" : self.setAll,
            "setValuesAsDictionary" : self.setValuesAsDictionary,
            "getMainValue" : self.getMainValue,
            "getValuesAsDictionary" : self.getValuesAsDictionary,
            "getValue" : self.getValue,
        }
        self.noodle_classes = {
            ReadWriter.Writer.getTypeId():ReadWriter.Writer,
            ReadWriter.Reader.getTypeId():ReadWriter.Reader,
        }

        self.noodles = dict()

    def init_node(self):
        '''Erste Kontaktaufnahme mit dem Server, Initialisierung der Noodles.'''
        message = {"command":"init_node", "options":{"uuid":self.uuid},"data":{}}
        r = requests.get(self.controller_endpoint, json=json.dumps(message))
        if r.status_code == 200:
            #Initialisieren
            #Ausgehend von Response im Format, bsp: OK-200 {'options':{},'data':{[{
            # 'type':'Writer', 'options':{...}, 'data':{...}}]}
            for noodle in r["data"]:
                n = self.noodle_classes.get(noodle['type'],False)
                if n:
                    new_noodle = n(noodle['options'],noodle['data'])
                    self.noodles[new_noodle.id] = new_noodle
        else:
            raise Exception("Node konnte nicht initialisiert werden, für Details siehe Logs des Controllers bzw. des Nodes!")
        

    #def testNoodle(self, func):
    #    def wrapper(*args, **kwargs):
    #        if "id" in options:
    #            noodle = noodles.get(options["id"], False)
    #            if noodle:
    #                func(*args, **kwargs)
    #            else:
    #                return False #TODO: Qualifizerte Antwort als JSON
    #        else:
    #            return False #TODO: Qualifizierte Antwort als JSON
    #        return wrapper

    #@testNoodle
    def setValue(self, options, data):
        if "id" in options:
            noodle = self.noodles.get(options["id"], False)
            if noodle:
                return noodle.setValue(options, data)
            else:
                raise Exception("Noodle im Node nicht bekannt!") #TODO: Eigene Exception bauen
        else:
            raise Exception("Das Feld Noodle ID fehlt!") #TODO: Eigene Exception erstellen

    def setAll(self, options, data):
        if "id" in options:
            noodle = self.noodles.get(options["id"], False)
            if noodle:
                return noodle.setAll(options, data)
            else:
                raise Exception("Noodle im Node nicht bekannt!") #TODO: Eigene Exception bauen
        else:
            raise Exception("Das Feld Noodle ID fehlt!") #TODO: Eigene Exception erstellen
    
    def setValuesAsDictionary(self, options, data):
        if "id" in options:
            noodle = self.noodles.get(options["id"], False)
            if noodle:
                return noodle.setValuesAsDictionary(options, data)
            else:
                raise Exception("Noodle im Node nicht bekannt!") #TODO: Eigene Exception bauen
        else:
            raise Exception("Das Feld Noodle ID fehlt!") #TODO: Eigene Exception erstellen

    def getMainValue(self, options, data):        
        if "id" in options:
            noodle = self.noodles.get(options["id"], False)
            if noodle:
                return noodle.getMainValue(options)
            else:
                raise Exception("Noodle im Node nicht bekannt!") #TODO: Eigene Exception bauen
        else:
            raise Exception("Das Feld Noodle ID fehlt!") #TODO: Eigene Exception erstellen
    
    def getValue(self, options, data):        
        if "id" in options:
            noodle = self.noodles.get(options["id"], False)
            if noodle:
                return noodle.getValue(options)
            else:
                raise Exception("Noodle im Node nicht bekannt!") #TODO: Eigene Exception bauen
        else:
            raise Exception("Das Feld Noodle ID fehlt!") #TODO: Eigene Exception erstellen

    def getValuesAsDictionary(self, options, data):        
        if "id" in options:
            noodle = self.noodles.get(options["id"], False)
            if noodle:
                return noodle.getValuesAsDictionary(options)
            else:
                raise Exception("Noodle im Node nicht bekannt!") #TODO: Eigene Exception bauen
        else:
            raise Exception("Das Feld Noodle ID fehlt!") #TODO: Eigene Exception erstellen

