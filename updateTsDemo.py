import predix.app
app = predix.app.Manifest('manifest.yml')
ts = app.get_timeseries()
ts.queue('test', 123)
ts.send()