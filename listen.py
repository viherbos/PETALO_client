from threading import Thread, Event
from Queue import Queue, Empty
import subprocess as sbp
import sys
import os
import json
import time

# from config import DATA
# from comms import SCK_server, SCK_client
from pypetalo.config import DATA as DATA
from pypetalo.comms import SCK_server as SCK_server
from pypetalo.comms import SCK_client as SCK_client


class Logger(Thread):

    def __init__(self,queue,stopper):
        super(MSG_executer,self).__init__()
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
                self.item = json.loads(self.qrx)

                if (self.item['command']=="OUTPUT"):
                        sys.stdout.write(self.item['arg1'])

                self.queue.task_done()


if __name__ == "__main__":

    srv_queue = Queue()
    stopper = Event()
    
    thread_Logger   = Logger(msg_queue,stopper)

    thread_Logger.start()

    while not stopper.is_set():
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print ("KeyBoard Interrupt")
            break

    stopper.set()
    thread_Logger.join()
