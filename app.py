from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/sheetsdb'
mongo = PyMongo(app)

@app.route('/')
def index():
  sheet = mongo.db.sheets
  sheet_id = sheet.insert(sample_sheet)
  return jsonify({'result]':sheet.find_one({'_id':sheet_id})})

sample_sheet = {
  "ID":"tom_petty_runnin_down_a_dream",
  "Song":"Runnin Down a Dream",
  "Artist":"Tom Petty",
  "Sheet":"         E\nIt was a beautiful day, the sun beat down\n          D               E\nI had the radio on, I was drivin\nE\nTrees flew by, me and Del was singin\n       D              E\nLittle Runaway, I was flyin\n"
}