import time
import serial
import tkinter
import serial.tools.list_ports

from Python.WaterRowerConnection import WaterRowerConnection


class Example:
    def __init__(self):
        self.port = None
        self.connection = None
        self.pulses = 0
        self.window = tkinter.Tk()

    def onDisconnect(self):
        self.connection = None

    def handle_gui(self):
        self.window.title("App")
        self.window.after(1000, self.run)
        self.window.mainloop()

    def run(self):
        # Start monitoring in the background, calling onEvent when data comes in.
        self.connect()

        # This is where you run your main application. For instance, you could start a Flask app here,
        # run a GUI, do a full-screen blessed virtualization, or just about anything else.
        while self.connection:
            print("Do awesome stuff here! Total pulses:", self.pulses)
            self.connection.requestStatistic("total_distance_m")
            self.window.after(1000,self.run)
            time.sleep(1)

    def onEvent(self, event):
        """Called when any data comes."""
        print('event', event, flush=True)
        if event["type"] == "pulse":
            self.pulses += event["value"]

    def connect(self):
        """This will start a thread in the background, that will call the onEvent method whenever data comes in."""
        print("Connecting to WaterRower...")
        self.port = self.findPort()
        print("Connecting to WaterRower on port %s" % self.port)
        self.connection = WaterRowerConnection(self.port, self.onDisconnect, self.onEvent)

    def findPort(self):
        attempts = 0
        while True:
            attempts += 1
            ports = serial.tools.list_ports.comports()
            for path, name, _ in ports:
                if "WR" in name:
                    print("port found: %s" % path)
                    return path

            # message every ~10 seconds
            if attempts % 10 == 0:
                print("Port not found in %d attempts; retrying every 5s" % attempts)

            time.sleep(1)


Example().handle_gui()