# PredixBrewPi

Connect brewing kettles or fermenation equipment to the Predix cloud to monitor meshing or fermentation temperature.

## Prepare the Raspberry

Install the Predix Python SDK and a package to work with the DS18B20
pip install python
pip install w1thermsensor

Edit the /boot/config.txt and add the following line to enable the 1-wire bus.
dtover=w1-gpio, gpiopin=4

Connect the DS18B20 sensors to the Raspberry PI.

A the sensor is using a bus system all sensors can be connected in parallel.
Only 3 pins of the Raspberry Pi are required:
Power supply - I am using the 5V output / other setups are making use of the 3.3V output
Ground (GND)
A data pin - I am using pin 1 connected the 5V with a 4.7K Ohm resistor

You can get the IDs of the sensors with:
cat /sys/devices/w1_bus_master1/w1_master_slaves
These IDs (second part only) have to be copied in the manifest.yml to define which sensor belongs to which asset.



