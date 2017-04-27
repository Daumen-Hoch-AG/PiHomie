#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
import Queue
import time

class ZWaveDummy(Thread):
    def __init__(self, node):
        Thread.__init__(self)
        self.queue = Queue.Queue()
        self.node = node
        self.alive = True
        #self.run()

    def run(self):
        while self.alive:
            if not self.queue.empty():
                text = self.queue.get()
                self.node.testPrint(text)
                print text, "<---- Dummy"
                if text == "kill":
                    self.alive = False
                time.sleep(5)
        print "Beende Dummy..."


    def addToQueue(self, command):
        self.queue.put(command)

    def kill(self):
        self.queue.put("kill")


if __name__ == '__main__':
    z = ZWaveDummy()
    z.run()
