import time
import json
import time
from datetime import datetime
try:
	import Adafruit_ADS1x15
except:
	pass
import sqlite3
from flask import Flask, Response, render_template
import random
app = Flask(__name__)
try:
	adc = Adafruit_ADS1x15.ADS1115()
except:
	adc = random.randint(0, 100)
@app.route('/')






def index():
	return render_template('index.html')
GAIN = 2/3
CHANNELS = 4
start = time.time()
def log_voltage(voltage, dbname, channel):
	conn = sqlite3.connect(dbname)
	curse = conn.cursor()
	sql_query = "INSERT INTO voltage{} values(datetime('now'), (?))".format(channel)

	curse.execute(sql_query, (voltage,))
	conn.commit()
	conn.close()
	return voltage

def grab_voltage(channel):
	raw = 1
	try:
		raw = adc.read_adc(channel, gain=GAIN)	
	except:
		raw = random.randint(0, 10)
	return 6.144*raw/32768.0000000


@app.route('/chart-data')
def chart_data():
	def pull_values():
		loop = False
		while loop:
			
			for i in range(CHANNELS):
				log_voltage(grab_voltage(i), 'voltage.db', 1)
#	
			
			json_data=json.dumps(
				{'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': grab_voltage(0) })
			yield f"dataL{json_data}\n\n"
			time.sleep(1)
		if not loop:
			json_data=json.dumps(
				{'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.randint(-1, 1)}
			)
			yield f"dataL{json_data}\n\n"
	def temp_generator():
		while True:
			json_data=json.dumps(
				{'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': log_voltage(0, 'voltage.db', grab_voltage(0))}
			)
			yield f"dataL{json_data}\n\n"
			time.sleep(1)

	return Response(temp_generator(), mimetype='text/event-stream')
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True)

#adc.stop_adc()



