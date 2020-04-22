#!flask/bin/python
from flask import Flask
from  wiotp.sdk.application import ApplicationClient
import json
from pymongo import MongoClient
import time

appConfig = {
	"auth":{
		"key":"a-x0o63c-xgjjldmpaz",
		"token":"w6NA&AodFYSJPU-R8*"
	}
}

app = Flask(__name__)

mongo_client = MongoClient("mongodb+srv://projetosi:projetosi@projetosi-kvwhk.mongodb.net/test?retryWrites=true&w=majority")

types = ['sensor_gas', "sensor_umidity", "sensor_temp"]

def eventCallback(event):	
	
	db = mongo_client.iot
	time.sleep(1)
	print(event.deviceId)
	if(event.typeId == "sensor_gas"):
		db.gas.insert_one(event.data)
		return True
	elif(event.typeId == "sensor_umidity"):
		db.umidity.insert_one(event.data)
		return True
	elif(event.typeId == "sensor_temp"):
		db.temp.insert_one(event.data)
		return True

@app.route('/gas')
def getGas():
	doc = mongo_client.iot.gas.find_one()
	doc.pop("_id")
	return doc

@app.route('/temp')
def getTemp():
	doc = mongo_client.iot.temp.find_one()
	doc.pop("_id")
	return doc

@app.route('/umidity')
def getUmidity():
	doc = mongo_client.iot.umidity.find_one()
	doc.pop("_id")
	return doc

if __name__ == '__main__':
	client = ApplicationClient(config=appConfig)
	client.deviceEventCallback = eventCallback
	client.connect()
	client.subscribeToDeviceEvents()
	app.run(debug=True)
