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



if __name__ == "__main__":

    sh_data   = DATA(read=True)
    log_queue = Queue()
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
            sys.stdout.write(qrx)
            srv_queue.task_done()

    thread_SERVER.join()
