# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# import the scraping python file I created...
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

#create route that renders index.html and finds documents from mongo
@app.route("/")
def index():
    mars = mongo.db.collection.find()
    return render_template('index.html', mars=mars)

#create scraping route
@app.route("/scrape")
def scrape():

    mars = scrape_mars.scrape()
    mongo.db.collection.drop()
    mongo.db.collection.insert_one(mars)

    return "Mars Scraping Successful"

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)