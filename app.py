import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipie_catalog'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-pwjgy.mongodb.net/recipie_catalog?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('get_catalog'))

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})
        if login_user:
            db_pass = login_user['password']
            if check_password_hash(db_pass, request.form['pass']):
                session['username'] = request.form['username']
                return redirect(url_for('get_catalog'))
        else:
            flash('Invalid username/password combination')
	
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hash_form_pass = generate_password_hash(request.form['pass'], "sha256")
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

@app.route('/get_catalog')
def get_catalog():
    #posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    ###
    #    """returns a set of documents belonging to page number `page_num`
    #where size of each page is `page_size`.
    page_num = request.args.get('page', 1, type=int)
    page_size = 2
    #page_num = page
    ## Calculate number of documents to skip
    skips = page_size * (page_num - 1)
    cursor = mongo.db.recipes.find().skip(skips).limit(page_size)
    total_recs = mongo.db.recipes.count()
    div_times = total_recs // page_size
    remain = total_recs % page_size
    if remain > 0:
        div_times += 1
    
    ## Return documents
    #return [x for x in cursor]
    return render_template("catalog.html", recipes=cursor, page=page_num, div_times=div_times)
    ###
    ##recipe=mongo.db.recipes.find().limit(5)
    ##return render_template("catalog.html", recipes=recipe)

@app.route('/get_catalog/<course>')
def get_catalog_bycourse(course):
    recipes_bycourse = list(mongo.db.recipes.find({"course": course}))
    return render_template("catalog.html", recipes=recipes_bycourse)

#@app.route('/filter_catalog/<course>')
#def filter_catalog(course):
#    return render_template("catalog.html", recipes=mongo.db.recipes.find({ "recipes.course": course }))

##@app.route('/get_catalog')
##def get_catalog():
#    if course == '':
#        return render_template("catalog.html", recipes=mongo.db.recipes.find())
#    if course != '':
 #       return render_template("catalog.html", recipes=mongo.db.recipes.find({ "course": 'breakfast' }))
    
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
#    all_categories =  mongo.db.categories.find()
    return render_template('recipe.html', recipe=the_recipe)

@app.route('/add_recipe')
def add_edit_recipe():
    if 'username' in session:
        return render_template('add-recipe.html', 
                            courses=mongo.db.courses.find(),  
                            cuisines=mongo.db.cuisine.find(),
                            tools=mongo.db.tools.find(), recipe='NEW')
    else:
        flash('You must log in first to add a recipe')
        return redirect(url_for('index'))

@app.route('/insert_recipe/<recipe_id>', methods=['POST'])
def insert_recipe(recipe_id):

    if request.method == "POST":
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