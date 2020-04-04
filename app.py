import os
from flask import Flask, render_template, redirect, request, url_for, session
#from flask.ext.bcrypt import Bcrypt
#import flask_bcrypt
import bcrypt
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
#bcrypt = Bcrypt(app)
#bcrypt = flask_bcrypt.Bcrypt(app)
#mongo = PyMongo(app)
app.config["MONGO_DBNAME"] = 'recipie_catalog'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-pwjgy.mongodb.net/recipie_catalog?retryWrites=true&w=majority'
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')

@app.route('/get_catalog')
def get_catalog():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

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
    
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('get_catalog'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')
     
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
#    all_categories =  mongo.db.categories.find()
    return render_template('recipe.html', recipe=the_recipe)

@app.route('/add_recipe')
def add_edit_recipe():
    return render_template('add-recipe.html', 
                            courses=mongo.db.courses.find(),  
                            cuisines=mongo.db.cuisine.find(),
                            tools=mongo.db.tools.find(), recipe='NEW')

@app.route('/insert_recipe/<recipe_id>', methods=['POST'])
def insert_recipe(recipe_id):

    if request.method == "POST":
        ingredients = request.form.get("ingredients").splitlines()
        prep_steps = request.form.get("prep_steps").splitlines()
        tools_list = request.form.getlist("tools")
        
        save_recipe = {
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "course": request.form.get("course"),
            "cuisine": request.form.get("cuisine"),
            "tools": tools_list,
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "no_servings": request.form.get("no_servings"),
            "kcal": request.form.get("kcal"),
            "fat": request.form.get("fat"),
            "carbs": request.form.get("carbs"),
            "salt": request.form.get("salt"),
            "sugars": request.form.get("sugars"),
            "fibre": request.form.get("fibre"),
            "ingredients": ingredients,
            "prep_steps": prep_steps,
            "image_url": request.form.get("image_url")
        }

    recipes = mongo.db.recipes
    if recipe_id != 'NEW':
        recipes.update_one( {'_id': ObjectId(recipe_id)},
                     {"$set":save_recipe})
    else:
        recipes.insert_one(save_recipe)
    return redirect(url_for('get_catalog'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('add-recipe.html', recipe=the_recipe, 
                            courses=mongo.db.courses.find(),  
                            cuisines=mongo.db.cuisine.find(),
                            tools=mongo.db.tools.find())

@app.route('/maintenance')
def maintenance():
    return render_template("maintenance.html", courses=mongo.db.courses.find(), 
                        cuisines=mongo.db.cuisine.find(), tools=mongo.db.tools.find())
    
    
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            

@app.route('/filter_catalog/<course>')
def filter_catalog(course):
    return render_template("catalog.html", recipes=mongo.db.recipes.find({ "recipes.course": course }))