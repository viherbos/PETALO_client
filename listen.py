#!/home/viherbos/anaconda2/bin/python


from threading import Thread, Event
from Queue import Queue, Empty
import subprocess as sbp
import sys
import os
import json
import time
import socket as sk

# from config import DATA
# from comms import SCK_server, SCK_client
from pypetalo.config import DATA as DATA
from pypetalo.comms import SCK_server as SCK_server
from pypetalo.comms import SCK_client as SCK_client


class Logger_S(Thread):

    def __init__(self,upper_class,queue,stopper):
        self.uc = upper_class
        super(Logger,self).__init__()
        self.queue = queue
        self.stopper = stopper

    def run(self):
        while not self.stopper.is_set():
            try:
                self.qrx = self.queue.get(True,timeout=0.5)
                # Timeout should decrease computational load
            except Empty:
                pass
                # Wait for another timeout
            else:
                print self.qrx
                self.queue.task_done()



if __name__ == "__main__":

    sh_data   = DATA(read=True)
    log_queue = Queue()
    stopper = Event()

    thread_Logger = SCK_server( sh_data,
                                log_queue,
                                stopper,
                                int(sh_data.daqd_cfg['server_port'])+1)
    thread_Screen = Logger_S(   sh_data,
                                log_queue,
                                stopper)

    thread_Logger.start()
    thread_Screen.start()

    while not stopper.is_set():
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print ("KeyBoard Interrupt")
            break

    stopper.set()
    thread_Logger.join()
    thread_Screen.join()

    
