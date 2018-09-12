#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Crypto import Random
from Crypto.PublicKey import RSA
from flask import current_app
import base64, os, json

class BaseHandler(object):
    '''Basisklasse für alle Hosts, übernimmt Auswahl der behandlenden Methode sowie Ver- und Entschlüsselung'''
    def __init__(self):
        self.handler = dict()

    def handle_request(self, request):
        try:
            #Client identifizieren -> Zertifikat für die Antwort auswählen
            #remote_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr).replace('.','-')
            #client_cert = os.path.join(current_app.config['CLIENTCERTDIR'],remote_ip + '.pem')
            client_cert = ""

            #JSON aus dem Request ziehen
            message = request.get_json()
            #Wenn request.get_json() None zurückgibt -> nicht json formatiert
            if message is None:
                raise KeyError("Der Request hat das falsche Format.")
            command = message.get('command', None)
            data = message.get('data', None)
            options = message.get('options', None)
            if command: #options und data optional
                #Aufrufen des Handlers für das Command aus der entsprechenden Klasse des Hosts
                handler_func = self.handler.get(command, None)
                
                if handler_func:
                    
                    #data_dec = self.decrypt_data(data)
                    message_to_send,code = handler_func(options, data, request)
                    return self.send_response(code, message_to_send, client_cert)
                else:
                    raise NotImplementedError("Kommando nicht implementiert.")

            else:
                raise KeyError("Der Request hat das falsche Format.")
                
        except RSA.binascii.Error as ex:
            #Wenn Daten z.B. nicht verschlüsselt sind.
            msg = "RSA Error: "+str(ex)
            current_app.logger.error(msg)
            return self.send_error_response(500, msg, client_cert)
        except KeyError as ex:
            msg = "KeyError: "+str(ex)
            current_app.logger.error(msg)
            return self.send_error_response(400, msg, client_cert)
        except NotImplementedError as ex:
            msg =  "NotImplementedError: "+str(ex)
            current_app.logger.error(msg)
            return self.send_error_response(501,msg, client_cert)
        except Exception as ex:
            msg = "Unbekannter Fehler - " + str(ex)
            current_app.logger.error(msg)
            return self.send_error_response(500, msg, client_cert)


    #####################################################################
    #Methoden zur Ver- und Entschlüsselung sowie zum Senden der Response#
    #####################################################################
    def decrypt_data(self, data):
        '''Entschlüsselt das in "data" enthaltenen JSON mit Hilfe des privaten Schlüssels des Servers'''
        #Öffnen und importieren des privaten Schlüssels des Servers
        priv_cert = current_app.config['PRIVCERT']
        priv_key_file = open(priv_cert,'r').read()
        priv_key = RSA.importKey(priv_key_file,passphrase=current_app.config['PASSPHRASE'])

        #Entschlüsseln der Nachricht
        decoded_data_enc = base64.b64decode(data)
        decoded_data_dec = priv_key.decrypt(decoded_data_enc)
        return json.loads(decoded_data_dec)

    def encrypt_response(self, message, client_cert):
        '''Verschlüsselt die Nachricht "message" mit Hilfe des Client-Zertifikats "client_cert"'''
        #Öffnen und importieren des öffentlichen Schlüssels des Clients
        pub_key_file = open(client_cert,'r').read()
        pub_key = RSA.importKey(pub_key_file)

        #Verschlüsseln der Nachricht
        encrypted_data = pub_key.encrypt(json.dumps(message).encode('utf-8'), 32)[0]
        encrypted_data_enc = base64.b64encode(encrypted_data)
        return encrypted_data_enc.decode('utf-8')

    def send_response(self, code, message, client_cert):
        '''Verschlüsselt die Daten und gibt die fertige, sendebereite, response zurück! 
        Wird eine leere Nachricht übergeben wird ein leerer String zurückgegeben. -> Nur Status-Code wird zurückgegeben'''
        if len(message) > 0:
            #message_enc = self.encrypt_response(message,client_cert)
            message_to_send = {"data":message}
            
            return message_to_send, code
        else:
            return "", code

    def send_error_response(self, code, message, client_cert):
        '''Sendet eine Fehlermeldung'''
        data_to_send = {'message':message}
        #data_to_send_enc = self.encrypt_response(data_to_send,client_cert)
        message_to_send = {'data':data_to_send}
        return message_to_send, code