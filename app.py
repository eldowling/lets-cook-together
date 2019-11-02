import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipie_catalog'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-pwjgy.mongodb.net/recipie_catalog?retryWrites=true&w=majority'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_catalog/<course>')
def get_catalog(course):
    if course == '':
        return render_template("catalog.html", recipes=mongo.db.recipes.find())
    elif course <> '':
        return render_template("catalog.html", recipes=mongo.db.recipes.find({ "recipes.course": course }))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

@app.route('/filter_catalog/<course>')
def filter_catalog(course):
    return render_template("catalog.html", recipes=mongo.db.recipes.find({ "recipes.course": course }))