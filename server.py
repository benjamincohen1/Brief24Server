'''
This application uses Flask as a web server and jquery to trigger
pictures with SimpleCV

To use start the web server:
>>> python flask-server.py

Then to run the application:
>>> python webkit-gtk.py

*Note: You are not required to run the webkit-gtk.py, you can also
visit http://localhost:5000

'''



from flask import Flask, jsonify, render_template, request
from werkzeug import SharedDataMiddleware
import tempfile, os
import simplejson as json



app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def main():
    print "We're in main."
    



if __name__ == '__main__':
       
    app.run()
