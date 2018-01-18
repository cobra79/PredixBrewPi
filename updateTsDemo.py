import predix.app
from  w1thermsensor import W1ThermSensor
import time
import random

app = predix.app.Manifest('manifest.yml')
ts = app.get_timeseries()

while True:
    print('Send datapoint')
    sensor_1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0517c1a4f1ff")
    temp_in_c = sensor_1.get_temperature()
    print("Sensor 1:", temp_in_c)
    #ts.queue('meshtun', random.uniform(40, 78))
    #ts.queue('wortkettle', random.uniform(95, 103))
    #ts.queue('fermentation', random.uniform(14, 25))
    #ts.queue('keezer', random.uniform(4,6))
    #ts.send()
    time.sleep(20)