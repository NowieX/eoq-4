import time
import serial
import serial.tools.list_ports
import random
from simple_board_printer import board_printer, print_crowd
from Python.WaterRowerConnection import WaterRowerConnection


class Example:
    def __init__(self):
        self.all_events = []
        self.port = None
        self.connection = None
        self.pulses = 0
        self.player_run_speed = 0

    def onDisconnect(self):
        self.connection = None

    def start_countdown(self):
        print("Get ready...")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        print("Go!!!")

    def run(self):
        # Start monitoring in the background, calling onEvent when data comes in.
        self.connect()

        # This is where you run your main application. For instance, you could start a Flask app here,
        # run a GUI, do a full-screen blessed virtualization, or just about anything else.

        self.start_countdown()
        while self.connection:

            self.connection.requestStatistic("watts")
            if self.pulses > 0:
                print(self.all_events)
                speed_value = self.all_events[-1].get('value')
                speed_value = 0 if speed_value is None else speed_value // 10

                self.player_run_speed += speed_value
            board_printer(self.player_run_speed)
            print_crowd()

            # calc_calories(self.pulses)
            time.sleep(1)

    def onEvent(self, event):
        """Called when any data comes."""
        if event["type"] != "pulse":
            # print('event', event, flush=True)
            self.all_events.append(dict(event))
        if event["type"] == "pulse":
            self.pulses += event["value"]
            # pass

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


Example().run()