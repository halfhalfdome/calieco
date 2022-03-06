from flask import Flask, render_template
from replit import web
import lob
app = Flask(__name__)
lob.api_key = 'secretapikeythatiwilladdlater'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/info')
def info(): 
  return render_template("info.html")

@app.route('/getinvolved')
def getinvolved():
  return render_template("getinvolved.html")
  
@app.route('/signup')
def signup():
  return render_template("signin.html")
  
def postcard(name, address_line1, address_line2, address_city, address_state, address_zip):
  card = lob.Postcard.create(
    to_address = {
      'name': name,
      'address_line1': address_line1,
      'address_line2': address_line2,
      'address_city': address_city,
      'address_state': address_state,
      'address_zip': address_zip
    },
  front = '<html style="padding: 1in; font-size: 50;">Front HTML </html>',
  back = '<html style="padding: 1in; font-size: 20;">Back HTML</html>',
  ) # Hard code the personal jpgs into front and back. 
  return card
  
def dispCard():
  list = lob.Postcard.list(limit=10)
  return list
  
def get_name(): 
  return 
web.run(app)