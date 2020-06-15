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
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

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
	
    return render_template('index.html', form=form)

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

    return render_template('register.html', form=form)

@app.route('/signout')
def signout():
    session.pop('username', None)
    flash ('You were signed out')
    return redirect(url_for('get_catalog'))

def paginate_funct(page_num, filter_type, filter):
    page_size = 5
    skips = page_size * (page_num - 1)
    if filter_type == 'None':
        cursor = list(mongo.db.recipes.find().sort('course').skip(skips).limit(page_size))
        total_recs = mongo.db.recipes.count_documents({})        
    elif filter_type == 'Search':
        cursor = list(mongo.db.recipes.find({"$or": [{"title": {'$regex': filter, '$options': 'i'}}, 
            {"description": {'$regex': filter, '$options': 'i'}}]}).sort('course').skip(skips).limit(page_size));
        total_recs = mongo.db.recipes.count_documents({"$or": [{"title": {'$regex': filter, '$options': 'i'}}, 
            {"description": {'$regex': filter, '$options': 'i'}}]})
    elif filter_type == 'Course':
        cursor = list(mongo.db.recipes.find({"course": filter}).sort('course').skip(skips).limit(page_size))
        total_recs = mongo.db.recipes.count_documents({"course": filter})
    elif filter_type == 'Cuisine':
        cursor = list(mongo.db.recipes.find({"cuisine": filter}).sort('course').skip(skips).limit(page_size))
        total_recs = mongo.db.recipes.count_documents({"cuisine": filter})
        
    div_times = total_recs // page_size
    remain = total_recs % page_size
    
    if remain > 0:
        div_times += 1
    paginate_ret = (cursor, div_times)
    return paginate_ret

@app.route('/get_catalog')
def get_catalog():
    page_num = request.args.get('page', 1, type=int)
    cursor, div_times = paginate_funct(page_num, 'None', 'None')
    courses = mongo.db.courses.find().sort('course_desc')
    cuisine_list = mongo.db.cuisine.find().sort('cuisine_name')
    return render_template("catalog.html", recipes=cursor, page=page_num, div_times=div_times, 
                            sel_course="ALL", courses=courses, sel_cuisine="ALL", cuisine=cuisine_list)

@app.route('/get_catalog_bycourse/<course>')
def get_catalog_bycourse(course):
    page_num = request.args.get('page', 1, type=int)
    cursor, div_times = paginate_funct(page_num, 'Course', course)
    courses = mongo.db.courses.find().sort('course_desc')
    cuisine_list = mongo.db.cuisine.find().sort('cuisine_name')
    return render_template("catalog.html", recipes=cursor, page=page_num, div_times=div_times, 
                            sel_course=course, courses=courses, sel_cuisine="ALL", cuisine=cuisine_list)

@app.route('/get_catalog_bycuisine/<cuisine>')
def get_catalog_bycuisine(cuisine):
    page_num = request.args.get('page', 1, type=int)
    cursor, div_times = paginate_funct(page_num, 'Cuisine', cuisine)
    courses = mongo.db.courses.find().sort('course_desc')
    cuisine_list = mongo.db.cuisine.find().sort('cuisine_name')
    return render_template("catalog.html", recipes=cursor, page=page_num, div_times=div_times, 
                            sel_course="ALL", courses=courses, sel_cuisine=cuisine, cuisine=cuisine_list)

@app.route('/catalog_search', methods=['POST'])
def catalog_search():
    if request.method == 'POST':
        page_num = request.args.get('page', 1, type=int)
        search_text = request.form['search']
        cursor, div_times = paginate_funct(page_num, 'Search', search_text)
        courses = mongo.db.courses.find().sort('course_desc')
        cuisine_list = mongo.db.cuisine.find().sort('cuisine_name')
        return render_template("catalog.html", recipes=cursor, page=page_num, div_times=div_times, 
                                sel_course="Search", courses=courses, sel_cuisine="Search", cuisine=cuisine_list)

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    tools = list(mongo.db.tools.find())
    if 'username' in session:
        session_user = session['username']
        find_rating = mongo.db.ratings.find({"recipe_id": recipe_id, "user": session_user}).count()
        if find_rating > 0:
            rated="true"
        else:
            rated = "false"
    else:
        rated = "false"
    return render_template('recipe.html', recipe=the_recipe, rated=rated, tools=tools)

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
        avg_rate = 0
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
            "image_url": request.form.get("image_url"),
            "avg_rating": avg_rate
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

@app.route('/rate_recipe/<recipe_id>', methods=['POST'])
def rate_recipe(recipe_id):
    if request.method == "POST":
        #save the rating for the user
        form_rating = request.form.get("rating")
        save_rating = {
            "recipe_id": recipe_id,
            "user": session['username'],
            "rating": form_rating,
        }
        ratings = mongo.db.ratings
        ratings.insert_one(save_rating)
        
        #get all ratings for this recipe to find average
        rated_recipes = mongo.db.ratings.find({"recipe_id": recipe_id})
        count_ratings = rated_recipes.count()
        total_rating = 0
        for doc in rated_recipes:
            total_rating += int(doc["rating"])
            
        #update the recipe with an average rating
        avg_rating = total_rating / count_ratings
        avg_rating = int(avg_rating)
        recipes = mongo.db.recipes
        recipes.update_one( {'_id': ObjectId(recipe_id)},
                        {"$set": {"avg_rating": avg_rating}})
        
        return redirect(url_for('show_recipe', recipe_id=recipe_id))

@app.route('/featured_tools')
def featured_tools():
    tools = mongo.db.tools.find().sort('tool_name')
    return render_template("tools_catalog.html", tools=tools)

@app.route('/tools_search', methods=['POST'])
def tools_search():
    if request.method == 'POST':
        search_text = request.form['toolsearch']
        found_tools = mongo.db.tools.find({"$or": [{"tool_name": {'$regex': search_text, '$options': 'i'}}, 
            {"description": {'$regex': search_text, '$options': 'i'}}, {"further_info": {'$regex': search_text, '$options': 'i'}}]}).sort('tool_name')
        return render_template("tools_catalog.html", tools=found_tools)

@app.route('/show_tool/<tool_id>')
def show_tool(tool_id):
    sel_tool =  mongo.db.tools.find_one({"_id": ObjectId(tool_id)})
    return render_template('tool_info.html', tool=sel_tool)

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
    further_info = request.form.get("further_info").splitlines()
    save_tool = {
            "tool_code": request.form.get("code"),
            "tool_name": request.form.get("name"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description"),
            "further_info": further_info,
            "price": request.form.get("price")
    }
    tools.insert_one(save_tool)
    return redirect(url_for('maintenance'))

@app.route('/update_tool/', methods=['POST'])
def update_tool():
    if request.method == "POST":
        tools=mongo.db.tools
        tool_id = request.form.get("toolID")
        further_info = request.form.get("further_info").splitlines()
        save_tool = {
            "tool_name": request.form.get("tool_name"),
            "image_url": request.form.get("tool_url"),
            "description": request.form.get("tool_descr"),
            "further_info": further_info,
            "price": request.form.get("tool_price")
        }
        tools.update_one( {'_id': ObjectId(tool_id)},
                        {"$set":save_tool})
        return redirect(url_for('maintenance'))
    
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)