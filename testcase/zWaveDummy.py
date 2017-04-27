#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
import Queue, time

class ZWaveDummy(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queue = Queue.Queue()

    def run(self):
        while True:
            if not self.queue.empty():
                print self.queue.get()
                time.sleep(5)

    def addToQueue(self, command):
        self.queue.put(command)




if __name__ == '__main__':
    z = ZWaveDummy()
    z.run()