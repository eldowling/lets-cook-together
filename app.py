import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm, AddEditReceipeForm
import functools
from os import path

if path.exists("env.py"):
  import env 

app = Flask(__name__)
#MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
#MONGO_URI = os.environ.get('MONGO_URI')
app.config["MONGO_DBNAME"] = 'recipie_catalog'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-pwjgy.mongodb.net/recipie_catalog?retryWrites=true&w=majority'

mongo = PyMongo(app)

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)

    return secure_function

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('get_catalog'))

    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    
    if form.validate_on_submit():
        next_url = request.form.get("next")
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        if login_user:
            db_pass = login_user['password']
            if check_password_hash(db_pass, request.form['password']):
                session['username'] = request.form['username']
                if next_url:
                    return redirect(next_url)
                return redirect(url_for('get_catalog'))
        else:
            flash('Invalid username/password combination')
	
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hash_form_pass = generate_password_hash(request.form['password'], "sha256")
            users.insert_one({'name' : request.form['username'], 'password' : hash_form_pass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        else:
            flash ('That username already exists!')

    return render_template('register.html')

@app.route('/signout')
def signout():
    session.pop('username', None)
    flash ('You were signed out')
    return redirect(url_for('get_catalog'))

def paginate_funct(page_num, filter):
    page_size = 5
    skips = page_size * (page_num - 1)
    if filter == 'None':
        cursor = mongo.db.recipes.find().sort('course').skip(skips).limit(page_size)
        total_recs = mongo.db.recipes.count()
    elif filter != '':
        cursor = list(mongo.db.recipes.find({"course": filter}).sort('course').skip(skips).limit(page_size))
        total_recs = mongo.db.recipes.find({"course": filter}).count()
    div_times = total_recs // page_size
    remain = total_recs % page_size
    
    if remain > 0:
        div_times += 1
    paginate_ret = (cursor, div_times)
    return paginate_ret

@app.route('/get_catalog')
def get_catalog():
    page_num = request.args.get('page', 1, type=int)
    cursor, div_times = paginate_funct(page_num, 'None')
    courses = mongo.db.courses.find().sort('course_desc')
    return render_template("catalog.html", recipes=cursor, page=page_num, div_times=div_times, sel_course="ALL", courses=courses)
    

@app.route('/get_catalog/<course>')
def get_catalog_bycourse(course):
    page_num = request.args.get('page', 1, type=int)
    cursor, div_times = paginate_funct(page_num, course)
    courses = mongo.db.courses.find().sort('course_desc')
    return render_template("catalog.html", recipes=cursor, page=page_num, div_times=div_times, sel_course=course, courses=courses)

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if 'username' in session:
        find_rating = mongo.db.ratings.find({"recpie_id": ObjectId(recipe_id), "user":'username'})
        #rated = find_rating._id
        rated = "true"
        print("rated")
        print(rated)
    else:
        rated = "false"
    return render_template('recipe.html', recipe=the_recipe, rated=rated)

@app.route('/add_recipe')
@login_required
def add_edit_recipe():
    if 'username' in session:
        form = AddEditReceipeForm()
        return render_template('add-recipe.html', 
                            courses=mongo.db.courses.find().sort('course_desc'),  
                            cuisines=mongo.db.cuisine.find().sort('cuisine_name'),
                            tools=mongo.db.tools.find().sort('tool_name'), recipe='NEW', form=form)
    else:
        flash('You must log in first to add a recipe')
        return redirect(url_for('index'))

@app.route('/insert_recipe/<recipe_id>', methods=['POST'])
def insert_recipe(recipe_id):
    form = AddEditReceipeForm()
    if form.validate_on_submit():
        ingredients = request.form.get("ingredients").splitlines()
        prep_steps = request.form.get("prep_steps").splitlines()
        tools_list = request.form.getlist("tools")
        save_recipe = {
            "author": session['username'],
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
            recipe_id = recipes.insert_one(save_recipe).inserted_id
        return redirect(url_for('show_recipe', recipe_id=recipe_id))
    else:
        flash('Validation errors in recipe')
    
    return render_template('add-recipe.html', recipe='NEW', 
                            courses=mongo.db.courses.find().sort('course_desc'),  
                            cuisines=mongo.db.cuisine.find().sort('cuisine_name'),
                            tools=mongo.db.tools.find().sort('tool_name'), form=form)

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    form = AddEditReceipeForm()
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    form.title.data = the_recipe.get("title")
    form.description.data = the_recipe.get("description")
    return render_template('add-recipe.html', recipe=the_recipe, 
                            courses=mongo.db.courses.find().sort('course_desc'),  
                            cuisines=mongo.db.cuisine.find().sort('cuisine_name'),
                            tools=mongo.db.tools.find().sort('tool_name'), form=form)

@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if request.method == "POST":
        recipe = mongo.db.recipes
        recipe.remove( {'_id': ObjectId(recipe_id)})
        flash('Recipe has been deleted')
        return redirect(url_for('get_catalog'))

@app.route('/maintenance')
@login_required
def maintenance():
    if 'username' in session:
        return render_template("maintenance.html", 
                        courses=mongo.db.courses.find().sort('course_desc'), 
                        cuisines=mongo.db.cuisine.find().sort('cuisine_name'), 
                        tools=mongo.db.tools.find().sort('tool_name'))
    else:
        flash('You must log in first to access the maintenance section')
        return redirect(url_for('index'))
    

@app.route('/insert_course', methods=['POST'])    
def insert_course():
    courses=mongo.db.courses
    save_course = {
            "course_code": request.form.get("code"),
            "course_desc": request.form.get("name")
    }
    courses.insert_one(save_course)
    return redirect(url_for('maintenance'))

@app.route('/insert_cuisine', methods=['POST'])    
def insert_cuisine():
    cuisine=mongo.db.cuisine
    save_cuisine = {
            "cuisine_code": request.form.get("code"),
            "cuisine_name": request.form.get("name")
    }
    cuisine.insert_one(save_cuisine)
    return redirect(url_for('maintenance'))

@app.route('/insert_tool', methods=['POST'])    
def insert_tool():
    tools=mongo.db.tools
    save_tool = {
            "tool_code": request.form.get("code"),
            "tool_name": request.form.get("name")
    }
    tools.insert_one(save_tool)
    return redirect(url_for('maintenance'))
    
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)