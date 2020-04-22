#!flask/bin/python
from flask import Flask
import wiotp.sdk.device


my_config = {
	"identity":{
		"orgId":"x0o63c",
		"typeId":"sensor_gas",
		"deviceId":"sensor_gas_1"
	}
}


app = Flask(__name__)

@app.route('/')
def index():
    client = DeviceClient(config=my_config)
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
