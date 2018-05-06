# PredixBrewPi

Connect brewing kettles or fermenation equipment to the Predix cloud to monitor meshing or fermentation temperature.

Have a look at the [wiki](https://github.com/cobra79/PredixBrewPi/wiki) to see the hardware setup.

## Prepare the Raspberry

Install the Predix Python SDK and a package to work with the DS18B20
pip install python
pip install w1thermsensor

Edit the /boot/config.txt and add the following line to enable the 1-wire bus.
dtover=w1-gpio, gpiopin=4

Connect the DS18B20 sensors to the Raspberry PI.

As the sensor is using a bus system all sensors can be connected to the same pins.
Only 3 pins of the Raspberry Pi are required:
Power supply - I am using the 5V output, Ground (GND) and a data pin.
In my setup pin 1 is connected to 5V with a 4.7K Ohm resistor.

Each DS18B20 has a unique ID, that needs to be added to the manifest.yml,
You can get the IDs of the sensors with:
cat /sys/devices/w1_bus_master1/w1_master_slaves




