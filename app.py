import requests
from flask import Flask
from flask import render_template

# create Flask app
app = Flask(__name__)
app.config.from_object(Configuration)

# GET request to ip.jsontest.com
def home():
    return render_template('home.html')

def rest_request_example():
    print (requests.get("http://ip.jsontest.com/").text)

rest_request_example()
	
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
