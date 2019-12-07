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

@app.route('/get_catalog')
def get_catalog():
    return render_template("catalog.html", recipes=mongo.db.recipes.find())

@app.route('/get_catalog/<course>')
def get_catalog_bycourse(course):
    recipes_bycourse = list(mongo.db.recipes.find({"course": course}))
    return render_template("catalog.html", recipes=recipes_bycourse)

##@app.route('/get_catalog')
##def get_catalog():
#    if course == '':
#        return render_template("catalog.html", recipes=mongo.db.recipes.find())
#    if course != '':
 #       return render_template("catalog.html", recipes=mongo.db.recipes.find({ "course": 'breakfast' }))
    
#@app.route('/get_catalog/<course_id>')
#def show_recipe(recipe_id):
#    course =  mongo.db.recipes.find_one({"course": ObjectId(course)})
#    all_courses =  mongo.db.categories.find()
#    return render_template('catalog.html', task=the_recipe,
#                           categories=all_categories)
    
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
#    all_categories =  mongo.db.categories.find()
    return render_template('recipe.html', recipe=the_recipe)

@app.route('/add_recipe')
def add_edit_recipe():
    return render_template('add-recipe.html')

@app.route('/add_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('add-recipe.html', recipe=the_recipe)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

@app.route('/filter_catalog/<course>')
def filter_catalog(course):
    return render_template("catalog.html", recipes=mongo.db.recipes.find({ "recipes.course": course }))