import predix.app
import time
import random

app = predix.app.Manifest('manifest.yml')
ts = app.get_timeseries()

while True:
    print('Send datapoint')
    ts.queue('meshtun', random.uniform(40, 78))
    ts.queue('wortkettle', random.uniform(95, 103))
    ts.queue('fermentation', random.uniform(14, 25))
    ts.queue('keezer', random.uniform(4,6))
    ts.send()
    time.sleep(20)