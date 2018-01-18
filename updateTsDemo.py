import predix.app
from  w1thermsensor import W1ThermSensor
import time
import random

app = predix.app.Manifest('manifest.yml')



ts = app.get_timeseries()

while True:
    
    mesh_kettle_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, app.manifest['env']['MESH_KETTLE'])
    wort_kettle_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, app.manifest['env']['WORT_KETTLE'])
    water_kettle_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, app.manifest['env']['WATER_KETTLE'])
    fermenter_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, app.manifest['env']['FERMENTER'])
    keezer_sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, app.manifest['env']['KEEZER'])
    
    mesh_temp_in_c = mesh_kettle_sensor.get_temperature()
    wort_temp_in_c = wort_kettle_sensor.get_temperature()
    water_temp_in_c = water_kettle_sensor.get_temperature()
    fermenter_temp_in_c = fermenter_sensor.get_temperature()
    keezer_temp_in_c = keezer_sensor.get_temperature()
    
    print("Mesh:", mesh_temp_in_c)
    print("Wort:", wort_temp_in_c)
    print("Water:", water_temp_in_c)
    print("Fermenter:", fermenter_temp_in_c)
    print("Keezer:", keezer_temp_in_c)
    
    ts.queue('meshtun', mesh_temp_in_c)
    ts.queue('wortkettle', wort_temp_in_c)
    ts.queue('waterkettle', water_temp_in_c)
    ts.queue('fermentation', fermenter_temp_in_c)
    ts.queue('keezer', keezer_temp_in_c)
    ts.send()
    time.sleep(20)
