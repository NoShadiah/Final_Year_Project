# Import flask and datetime module for showing date and time
from flask import Flask
import datetime
from flask_cors import CORS
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
CORS(app)
  
# The index route
@app.route("/")
def index():
    return "Bumpt to Joy, A pathway to maternal Bliss"
  
# Running app
if __name__ == '__main__':
    app.run(debug=True)