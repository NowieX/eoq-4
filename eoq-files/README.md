WATERROWER Hardware getting started
===

Let's get you setup with our hardware provided by WATERROWER!

The development kit in front of you consists of a few bits and pieces:

- S4 Monitor (the screen)
- Rowing simulator (the magic box with the logo)
- Sensor cable
- Mini USB cable

In order to wire everything up make sure to power the S4 monitor by plugging the Mini USB cable into your PC or Android device (or whatever you're working with), through this cable you'll receive the data. After connecting a "PC" symbol should appear on the LCD screen.

Now hook up the sensor cable on the S4 Monitor, there should only be place one that fits, you'll find it on the left side of the PCB.

The simulator is only needed if you want to have fake rowing data, it'll do the workout for you. Plug the USB cable into some kind of power supply (or just your laptop) and hook up the other end into the sensor cable going to the S4. If you want to stop rowing just unplug the USB power to the simulator (use the USB plug rather than the sensor cable, it's a bit finnicky and sensitive).

Testing on the Rower
---

Behind the big tablets in the VESA mount itself on the rowing machines there is a tiny micro USB port that implements the exact same protocol as the S4 monitor (we call this thing a Little Black Box or LBB for short). Make sure the jack is still plugged into the other input on the LBB (this is the sensor cable). After that you should receive rowing data from the rowing machine. 

Documentation
---

The document "Water Rower S4 S5 USB Protocol Iss 1 04.pdf" contains the description of the USB protocl used by most WATERROWER equipment, it's a bit of an antique protocol but it has been working for over two decades now.

Basic premise:

- Setup connection and activate broadcasting by sending some initialisation messages
- Receive number of pulses per 25 ms (more on this later)
- Receive SS and SE events (stroke start and stroke end)
- Request memory addresses to get calculated data stored in the S4's memory.

The calculated data has gone through all kinds of processing and is quite slow to respond to interactions with the rowing machine.
The pulses/25ms is based on the sensor wheel inside of the WaterRower, this sensor wheel consists of numerous pillars that go past a simple IR reader, the protocol will provide you with the number of pulses counted in 25ms. Which will be super responsive (in other words: use this if you want to create a gamified experience)
 
SECRET INTERNAL NOT YET RELEASED HARDWARE

There is a second document in the .zip called "V3 hardware vs software int 1.3.docx" which contains the protocols of two yet unreleased bits of hardware: the Pulley and LightRing USB.

The Pulley you can ignore since it simply isn't finished yet and its numbers are still all over the place however the LightRing over USB can be found under the provided rowing machines. It constists of 52 individually addressable lights that you can animate, dim, tune and do your bidding.

We only have two USB enabled LightRings so only a few groups can work with it. Please note, since this is prototype hardware we do not yet have any example code so you'll be responsible for implementing the protocol as provided in the document.


Happy hacking!
