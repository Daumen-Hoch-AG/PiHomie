from base.base_handler import BaseHandler
from flask import current_app
import requests, uuid, json
from functools import wraps

#TODO: Noodle definitionen und Liste Zentral ablegen?
from node.noodles import ReadWrite

class Node(BaseHandler):
    def __init__(self):
        super().__init__()
        self.noodles = dict()
        self.noodle_classes = {
            ReadWrite.Writer.getTypeId():ReadWrite.Writer,
            ReadWrite.Reader.getTypeId():ReadWrite.Reader,
        }

        host = current_app.config['CONTROLLER']['HOST']
        port = current_app.config['CONTROLLER']['PORT']
        self.uuid = current_app.config['UUID'] #Setzt uuid aus Config
        self.controller_endpoint = "http://{}:{}/api".format(host,port)
        self.handler = {
            "setValue" : self.setValue,
            "setAll" : self.setAll,
            "setValuesAsDictionary" : self.setValuesAsDictionary,
            "getMainValue" : self.getMainValue,
            "getValuesAsDictionary" : self.getValuesAsDictionary,
            "getValue" : self.getValue,
        }

        self.init_node()


    def init_node(self):
        '''Erste Kontaktaufnahme mit dem Server, Initialisierung der Noodles.'''
        message = {"command":"init_node", "options":{"uuid":self.uuid},"data":{}}
        r = requests.get(self.controller_endpoint, json=message)
        if r.status_code == 200:
            #Initialisieren
            #Ausgehend von Response im Format, bsp: OK-200 {'options':{},'data':[{
            # 'type':'Writer', 'options':{...}, 'data':{...}},]}
            r = r.json()
            for noodle in r["data"]:
                n = self.noodle_classes.get(noodle['type'],False)
                if n:
                    new_noodle = n(noodle['options'],noodle['data'], lambda x: print(x))#TODO: Callback definieren
                    self.noodles[new_noodle.id] = new_noodle
        else:
            raise Exception("Node konnte nicht initialisiert werden, für Details siehe Logs des Controllers bzw. des Nodes!")
        
    #Decorator für alle Aktionen die an einen Noodle gerichtet sind.
    #Die eigentliche Funktion bekommt durch den Decorator den zusätzlichen Parameter "noodle".
    #Aufgerufen wird diese aber nur mit den drei Parametern die der Wrapper erwartet!!
    def noodle_action(original_func):
        @wraps(original_func)
        def wrapper(self, options, data, request):
            if "id" in options:
                noodle = self.noodles.get(options["id"], False)
                if noodle:
                    return original_func(self, options, data, request, noodle)
                else:
                    raise Exception("Noodle im Node nicht bekannt!") #TODO: Eigene Exception bauen
            else:
                raise Exception("Das Feld Noodle ID fehlt!") #TODO: Eigene Exception erstellen
        return wrapper

    @noodle_action
    def setValue(self, options, data, request, noodle):
        return noodle.setValue(options, data)

    @noodle_action
    def setAll(self, options, data, request, noodle):
        return noodle.setAll(options, data)
    
    @noodle_action
    def setValuesAsDictionary(self, options, data, request, noodle):
        return noodle.setValuesAsDictionary(options, data)

    @noodle_action
    def getMainValue(self, options, data, request, noodle):        
        return noodle.getMainValue(options)
    
    @noodle_action
    def getValue(self, options, data, request, noodle):        
        return noodle.getValue(options)

    @noodle_action
    def getValuesAsDictionary(self, options, data, request, noodle):        
        return noodle.getValuesAsDictionary(options)
