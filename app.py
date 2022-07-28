from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars



app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
mars_db = client.mars_db
mars_col = mars_db.mars_col

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")


@app.route('/')
def index():
    mars = mongo.db.mars_col.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars_col
    data = scrape_mars.scrape()
    mars.insert_one(
        {},
        data,
    )
    redirect("/", code=302)
   


if __name__ == "__main__":
    app.run(debug=True)