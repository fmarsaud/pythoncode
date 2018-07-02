import requests
from flask import Flask
from flask import render_template
from config import Configuration

# create Flask app
app = Flask(__name__)
app.config.from_object(Configuration)

# GET request to ip.jsontest.com
def home():
	# My microservice!
    return render_template('home.html')

def rest_request_example():
    print (requests.get("http://129.157.179.180:3000/shield/33/45/blue/fmarsaud").text)

rest_request_example()
	
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
