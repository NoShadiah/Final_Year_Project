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
    return "Hello welcome to my react and flask profect"
  
# Route for seeing a data
@app.route('/book_data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Id':"1", 
        "Title":"Perfect Faith in perfect weakness",
        "Purchase_date":x, 
        "Author":"William Marrion Branham"
        }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)