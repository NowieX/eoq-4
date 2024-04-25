import time

import serial
import serial.tools.list_ports

from WaterRowerConnection import WaterRowerConnection


# This class will make sure to always be connected to a WaterRower and will reconnect every time the connection is lost.
class WaterRowerConnector:

    def __init__(self, listener):
        self.listener = listener
        self.port = None
        self.connection = None

    def start(self):
        self.connect()

    def resetMonitor(self):
        if self.connection is not None:
            self.connection.resetMonitor()

    def onEvent(self, event):
        if event['type'] == "stroke_start":
            time.sleep(0.025)
            self.connection.requestAddress('088')

        if event['type'] == "watts":
            self.listener.onWatts(event['value'])

    def connect(self):
        print("Connecting to WaterRower...")
        self.port = self.findPort()
        print("Connecting to WaterRower on port %s" % self.port)

        self.connection = WaterRowerConnection(self.port, self.connect, self.onEvent)

    def findPort(self):
        attempts = 0
        while True:
            attempts += 1
            ports = serial.tools.list_ports.comports()
            for (i, (path, name, _)) in enumerate(ports):
                if "WR" in name:
                    print("port found: %s" % path)
                    return path

            # message every ~30 seconds
            if attempts % 6 == 0:
                print("Port not found in %d attempts; retrying every 5s" % attempts)

            time.sleep(5)
