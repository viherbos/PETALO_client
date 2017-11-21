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


class Logger(Thread):

    def __init__(self,upper_class,stopper):
        self.uc = upper_class
        super(Logger,self).__init__()
        self.stopper = stopper

    def run(self):
        server_sock = sk.socket()
        server_sock.bind((self.uc.daqd_cfg['localhost'],
                          self.uc.daqd_cfg['server_port']+1))
        server_sock.listen(4)

        while not self.stopper.is_set():
            try:
                client, client_address = server_sock.accept()
                data = client.recv(8192)
                print data
            except:
                pass
                # Wait for another timeout



if __name__ == "__main__":

    sh_data = DATA(read=True)
    stopper = Event()

    thread_Logger   = Logger(sh_data,stopper)


    thread_Logger.start()

    while not stopper.is_set():
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print ("KeyBoard Interrupt")
            break

    stopper.set()

    thread_Logger.join()
