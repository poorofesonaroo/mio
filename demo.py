#!/usr/bin/env python
from flask import Flask, render_template, request
import time
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def move():
	result = ""
	if request.method == 'POST':
		
		if request.form['submit'] == 'push16':
			result="pushed button"
			os.system("python push16.py")
		if request.form['submit'] == 'strike18':
			result="switched relay 5 secs"
			os.system("python buzz.py")

		return render_template('servo.html', res_str=result)
                        
	return render_template('servo.html')

if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', debug=True, threaded=False)
	except:
		pass
