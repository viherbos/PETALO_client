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
                          5006))
        server_sock.listen(4)
        client, client_address = server_sock.accept()

        while not self.stopper.is_set():
            try:
                data = client.recv(1024)
                sys.stdout.write(data)
            except:
                client.shutdown(sk.SHUT_RDWR)
                # Wait for another timeout



if __name__ == "__main__":

    sh_data = DATA(read=True)
    stopper = Event()
    srv_queue = Queue()

    #thread_Logger   = Logger(sh_data,stopper)
    thread_SERVER = SCK_server(sh_data,srv_queue,stopper)

    #thread_Logger.start()
    thread_SERVER.start()


    while True:
        try:
            qrx = srv_queue.get(True,timeout=0.5)
        except KeyboardInterrupt:
            print ("KeyBoard Interrupt")
            stopper.set()
            break
        except Empty:
            pass
        else:
            print qrx


    thread_SERVER.join()
