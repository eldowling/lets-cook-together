# Let's Cook Together - Recipe Catalog

The Recipe catalog was created to allow users to share their own recipes in an easily accessible catalog, which allows registered users to add new recipes simply, and to share with other users of the recipe catalog. 
Recipes can be easily found through the use of either a search bar or the filter buttons, through these it will limit the list of recipes returned from the catalog, it allows the user to scroll through them easily. The user can then click on the recipe title to view the details of the recipe, which are all arranged into a tab format to cleary view each section under the headings of General details, Ingredients and Preparation Steps.

Registered users will have the option to add recipes, they will also have the facility to edit or delete their own recipes in the catalog. All registered users can also submit a rating value for any recipe in the catalog. If the user has already rated a recipe then the average rating for that recipe is displayed.

Recipes can also display information on the tools used to create the recipe. These can be selected from a list of the site's featured tools. A link is provided from the tools detailed in the recipe, so that they can view further information on any tool that is listed.

The list of featured tools can also be accessed from the main site menu. All tools featured by the site will be listed on this page, and each tool then has a link to view the information about the selected tool. 

The site also provides a maintenance section, this will allow a user to add to the list of courses and cuisines that populate the main catalog page as well as the recipe page.
The list of featured tools can also be maintained from here, the tools maintenance section allows the user to add new tools as well as updating existing tools, which is useful for price and information updates required for any tool.
 
## UX
 
The recipe catalog site is required to allow users easy access to a catalog of recipes, where users can share their own recipes, search for text within recipes, and filter recipes by certain categories.
The site should also allow the users to rate as well as view ratings for any recipe.
Each recipe should allow the author to share details of some of the tools that were used in making the recipe. This list should have the ability to add to or modify details of existing tools.
There should be an area to view the list of all the tools featured on the site, as well as providing the user with further details to view for each of the tools listed. An on-line shop may be required further down the line, and the featured tools section should provide potential to create this easily.

The user stories below demonstrate the key features that were required from the recipe catalog. These are taken from different users points of view and show the functionality they required from the site:
- As a busy mother I want to be able to view recipes quickly and easily on my phone, so that I can follow them directly from the screen while I'm in the kitchen
- As a parent of young children, I like to browse through specific recipe categories for lunch or dinner ideas. I also like to search for words from the recipe name when I want to find a recipe quickly. I like to have this available on my phone as I usually take some time to do this during my daily bus commute.
- As a keen cook, I have built a large collection of recipes over a number of years. These have come from many sources such as family recipes passed down from my mother and grandmother, some of my own recipe and also magazine pullouts. I would like a central location to store all of these, as well as to help with the safe keeping of family recipes. I'd also like to be able to share them with others, and hope that they get enjoyment from making and eating them too.
- I'm a student in a cookery school, I often browse recipes for inspiration and I find the recipe ratings useful in helping to decide on themes for my weekly menus. I would like to view the catalog on my laptop while preparing my course work, or sometimes on my phone or tablet.
- As the business manager of ToolsPro I would like to be able to promote our products and allow users of the site to see clearly which of our tools are available to use in each recipe. I would also like the users of the site to have access to our full range of ToolsPro products, and have a plan for further development to allow them to purchase these products directly from the site.
- As the ToolsPro sales administrator, I need functionality to add to the lists in used on the pages in the site. In particular the range of ToolsPro products that are available in order to add to this list or update the price or any details regarding each of the products.

The wireframes were developed through the use of these user stories to outline the content required in the recipe catalog, as well as forming the basis of what the site would look like and how it would work.
The wireframes are available to view at https://balsamiq.cloud/svy4yos/pgpn73q

## Features

This is a multi-page site which provides users access to different elements of the recipe catalog, as well as to the recipe related tools that are featured in the site. All of the features available to use in the site are detailed below.
 
### Existing Features

- Full Recipe Catalog - This is the main page of the site and provides any user access to view all of the recipes stored in the site's recipe catalog.
- Catalog Search - The search bar located at the top of the recipe catalog allows the user to search for key words contained in the recipe title and description. When the user types a value into the search bar, it will then return any recipes that contain these key words.
- Catalog Filter - The Course and Cuisine filter lists can be used to select from the lists of available courses or cuisines, which are required data items when adding new recipes. These lists allow the simple filter to be applied and only recipes from the selected category will be displayed.
- Pagination - All pages from the recipe catalog, including filtered category lists will be paginated. This is to allow for a limited number of records to be returned for each page, which is essential for faster loading and reduces the use of mobile data.
- View Recipes - When each recipe is displayed the page is divided into three tabs: "General Information", "Ingredients", "Preparation Steps". The simple layout is mobile friendly and helps with providing the user with quick and easy access to the relevant section, without having to scroll too much.
- Add / Edit / Delete Recipes - The site provides the ability for any user to add a new recipe to the catalog, as well as being able to make updates or delete any of the user's own recipe that were previously added. Only registered users have access to these functions. When the user is adding a recipe they will have a list of options to complete, some of which are mandatory before being able to save the recipe. Some of the fields are populated with lists which makes it easier to categorize the recipes into groups.
When the user edits a recipe, all of these boxes will already be populated with the details that were previously saved for that recipe. The user can select the items that they wish to update, and will be returned to that recipe once it has been saved. The recipe author also has the option to delete a recipe if required.
- Add Recipe Rating - All recipes can be rated by multiple users. If a recipe has not been rated by the session user, a button will be available for that user to rate the recipe. Otherwise the average rating for that recipe is displayed.
- View Featured Tools - While viewing the recipe a list of the tools used in the preparation or cooking of the recipe will be displayed to the user. This list is helpful to the user for preparation ahead of making the recipe, but it also provides a link for each tool which allows the user to view the tool information page, and will also allow the user to purchase any of these tools from the site.
- Featured Tools Page - This section of the site is to promote and provide further details of any of the tools that are used in the recipes. It provides a list of all tools, as well as an individual page for each of the tools with additional information about each of the tools that are available. The site can be further developed to allow for any of the tools to be purchased by the user.
- List Maintenance - The site has a Maintenance section which is to allow a user to add to the lists such as Course and Cuisine, which are available when adding each recipe to categorize them. These categories are used to provide simple filter options on the main recipe catalog page.
- Another feature of the maintenance section is to allow the list of Tools to be added to and updated. The user can view the list of tools that have already been entered. Each data item that is stored against the tool can then be updated. For example if the price increases, or if the item description of further information needs to be modified, it can be done through this tool maintenance. Additionally, new tools can be added to the tools list, and these will in turn appear in the available tools list when adding a new recipe / editing existing recipes or in the Featured Tools section of the site too.
- A lot of issues were encountered with in implementing the "Edit Tools modal form" in trying to resolve how to pass the current tool field values from the button to the modal form. A considerable amount of work was involved in resolving the issue including Google searches to find information on passing it through a JQuery function when the Edit button was clicked. The tutor also provided me with some assistance and advice on the best approach to try and complete it using the method I had already partly implemented. If I was to re-do this section, I have learnt that it would be easier to have an Edit form rather than using a modal, as it would have been less complicated to have created a route for the Edit Tool that loaded the form details from the python side rather than doing it with JS and using the modal form.

### Features Left to Implement
The recipe catalog site could be further expanded to include some of the following features, which have not yet been implemented:
- Expand on the filters and search functionality, to allow the user to select a search by option on the recipe catalog page (For example: ingredients / tools)
- Include sorting functionality to allow the user to sort recipes by different fields such as rating, cuisines, recipe difficulty
- Allow users to add recipes to their favourites list, and ingredients from a recipe to be added to a printable shopping list
- Enhance the maintenance section by adding super user levels of access to this section, so as only selected users could make updates to the sites lists and tools.
- Additional sorting enhancements could be made to the tables to allow for a customised sort for some of the lists. For example the Courses or Cuisines lists are sorted alphabetically, but if a sort order field was put into Courses, then the administrator could choose in which order to display the courses, and have them displayed in order of when the course is eaten (i.e. Breakfast, Lunch, Starter, Main Course, etc.)
- Develop an on-line shop to allow users to purchase tools from the site.

## Technologies Used
Some of the technologies that I used to implement the features and functionality of the Recipe Catalog site are detailed below:

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - **HTML5** is the markup language used to structure and present the content of the website. It provides features allowing for use of forms and tables in the website.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - A **CSS Stylesheet** was used to define the style of the page such as images, headings and tables. Some Media Queries are also used in order to apply different settings depending on the screen size being used to view the site.
- [Google API Material Icons](https://materializecss.com/icons.html)
	- **Material Icons** are used with Materialize CSS and are a libary of material design icons, which can be used to style anything on the site using these icons. These icons were used in styling buttons, as well as on the pages as bullet points for unordered lists, or even to style the star ratings using filled or empty stars.
- [FontAwesome](https://fontawesome.com/)
    - **Font Awesome** icons on the page were also used similar to the Material Icons, if a required icon was not available in Material Icon, then font awsome icons were sought to provide addition icon styles.
- [Materialize CSS and JavaScript](https://materializecss.com)
    - **Materialize** was developed by Google it contains CSS and JavaScript based design templates which are used to style the pages, and keeps it to a uniform design and style accross all pages by using the same design templates for typography, forms, navbar and buttons.
- [JQuery](https://jquery.com)
    - **JQuery** is a JavaScript libary designed to simplify HTML DOM tree traversal and manipulation.
	- In this project it is used by some of the Materialize functions for event handling and CSS functionality. 
	- JQuery was used in order to activate dropdown lists, trigger modals, and even for the side navigation bar used on the mobile layout. Other components were for the tabs and chips used on the show recipe page.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
	- **MongoDB Atlas** stores data in JSON-like documents that can vary in structure, offering a dynamic, flexible schema.
	- The recipe catalog was built around a MongoDB Atlas database structure. The required tables could be added simply and could be easily accessed from the Python application.
- [Python](https://www.python.org/)
	- **Python** is a high-level programming language that can be used for developing desktop applications as well as web applications.
	- It was used in this project to perform a number of functions. It provides the route for each of the pages to be loaded in the web application, as it can perform the tasks to open / search / update and delete records from the MongoDB and allow these to be passed to the web page to be displayed in the application.
	- It also provided functions to check the user login, and form validation
	- Another purpose for using Python was the creation of function which performed calculations in order to work out the the correct number of page numbers to display at the bottom of the recipe catalog for the pagination numbers. There were also a number of criteria fed into this function so that it would work the same with or without using the search or course / cuisine filters.
	- Other calculations to work out the average recipe rating after a user rated an individual recipe were also used. This function would have to add the user's rating to one table in the MongoDB, it would then lookup the same table and find all ratings for that recipe in order to calculate the average rating value, and finally update the recipe to provide the newly calculated average. This in turn could then be displayed in the web application.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
	- **PyMongo** is the MongoDB driver used by Python to access the MongoDB database.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
	- **Flask** is a web framework written in Python, which provides the tools, libraries and technologies that allow you to build a web application.
	- Flask was used throughout the project for various functions in the python application in order to display flash messages, render templates or redirection to another page.
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)
	- **Jinja2** is a Python template engine used to create HTML, XML or other markup formats that are returned to the user via a HTTP response.
	- Jinja2 was used in this project to feed the Python / MongoDB data into the application forms and pages. It also allows If statements to be used in determine if some text or sections should or should not be displayed. For Loops were also used throughout the pages in order to load multiple values from a list or array in the database.
- [Werkzeug Security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
	- **Werkzeug Security** - two functions from this Python library were used in the user Registration and Login forms. It will store secure passwords with salted hashes and later verifies the password entered by the user in plain text against it's password hash stored in the database.
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/)
	- **WTForms** is a flexible validation and rendering library for Python web applications. It was used to create and validate fields on the Registration, Login and Add Recipe forms.
- [Heroku](https://www.heroku.com)
	- **Heroku** is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. The web application has been deployed to and run from the Heroku platform.

## Testing
The testing carried out in my project is available to view in the [Testing Documentation](./Testing.md) in this project

## Deployment

The project was developed using Gitpod which is an on-line IDE for GitHub which uses a ready to code development environment, and deployed to the GitHub repository hosting service during development. The project was deployed to Heroku cloud hosting platform.

The project was committed to the GitHub repository at regular intervals during development, or when an element of the project had been completed. Comments are entered on each commit in order to track updates that have been made.

There are no differences between the deployed and development versions. Any components that were implemented in the development stage were uploaded to GitHub and then to Heroku for final deployment. To deploy the project to Heroku the requirements.txt file were updated and then the GitHub repository was used to linked from Heroku and be deployed.
A manual deploy was done in Heroku to push through all of the latest build, and Automatic deploys has been enabled for future updates to be deployed directly from the GitHub Repository.

## Credits

### Content

The following articles and tutorials were used to learn about the different functions and methods I needed to use in order to implement parts of my web application. The examples that I found helped me to understand new functionality, so that I could then modify them as necessary to integrate them into my application.

**MongoDB Tutorials:**
- [Many to Many relation in mongoDB by Hitesh Choudhary](https://www.youtube.com/watch?v=L3Pltb46n-M)
- [Query an Array of Embedded Documents](https://docs.mongodb.com/manual/tutorial/query-array-of-documents/)
- [MongoDB Overview](https://www.tutorialspoint.com/mongodb/mongodb_overview.htm)
- [Get nested dict items using Jinja2 in Flask](https://stackoverflow.com/questions/24727977/get-nested-dict-items-using-jinja2-in-flask)
- [Python update db](https://www.tutorialspoint.com/python_data_access/python_mongodb_update.htm)
- [How to get the object id in PyMongo after an insert? - Stack Overflow](//stackoverflow.com/questions/8783753/how-to-get-the-object-id-in-pymongo-after-an-insert)
- [How To Query MongoDB Documents In Python: Use a Python iterator to print each document returned by MongoDB - Data Pilot](//kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-in-python-269)
- [How to Use a SQL LIKE Statement in MongoDB by AJ Welch ](//chartio.com/resources/tutorials/how-to-use-a-sql-like-statement-in-mongodb/)
- [How to query MongoDB with “like”? - Stack Overflow](//stackoverflow.com/questions/3305561/how-to-query-mongodb-with-like)

**Pagination:**
- [Python Flask Tutorial: Full-Featured Web App Part 9 - Pagination by Corey Schafer](https://www.youtube.com/watch?v=PSWf2TjTGNY)
- [Query Pagination in Flask and MongoDB - API Example by Pretty Printed](https://www.youtube.com/watch?v=Lnt6JqtzM7I)
- [Fast and Efficient Pagination in MongoDB by Arpit Bhayani](//www.codementor.io/@arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr)
- [Group By example](//jinja.palletsprojects.com/en/2.10.x/templates/#groupby)
- [Python Tutorial: Multiple parameters and return values by Datacamp](https://www.youtube.com/watch?v=GocXrnwBrAs)
- [MongoDB - $group (aggregation)](//docs.mongodb.com/manual/reference/operator/aggregation/group/)
- [Mongodb aggregation $group followed by $limit for pagination - Stack Overflow](//stackoverflow.com/questions/32065362/mongodb-aggregation-group-followed-by-limit-for-pagination)
- To fix an issue with assigning url_for on the pagination when using a filter [Jinja variables within the Flask url_for function - Stack Overflow](//stackoverflow.com/questions/23988561/jinja-variables-within-the-flask-url-for-function)

**User Authentication:**
- [Python Flask Tutorial: Full-Featured Web App Part 6 - User Authentication by Corey Schafer](https://www.youtube.com/watch?v=CSHx6eCkmv0)
- [How to store passwords securely using Werkzeug by Techmonger](//techmonger.github.io/4/secure-passwords-werkzeug/)
- [Flask signing in and signing out - Stack Overflow](//stackoverflow.com/questions/41416411/flask-signing-in-and-signing-out)
- [Handling the next URL when logging in with Flask by Jose Salvatierra](//blog.tecladocode.com/handling-the-next-url-when-logging-in-with-flask/)

**Form Validation:**
- [Python Flask Tutorial: Full-Featured Web App Part 3 - Forms and User Input by Corey Schafer](//www.youtube.com/watch?v=UIJKdCIEXUQ&t=745s)
- [Python and Flask - Web Forms with Flask-wtf by TheCodex](//www.youtube.com/watch?v=-O9NMdvWmE8)
- [Python and Flask - Getting data from Web Forms by TheCodex](//www.youtube.com/watch?v=f8qvLBvrIFI&list=PLB5jA40tNf3vX6Ue_ud64DDRVSryHHr1h&index=7)
- [Using Validators in Flask-WTF (Part 2 of 5) by Pretty Printed](//www.youtube.com/watch?v=jR2aFKuaOBs)
- [WTForms Validators](//wtforms.readthedocs.io/en/latest/validators/)
- [How to validate select option for a Materialize dropdown? by Stack Overflow](//stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown)
- [New line in text area - Stack Overflow](//stackoverflow.com/questions/8627902/new-line-in-text-area)
- [Why is textarea filled with mysterious white spaces? - Stack Overflow](//stackoverflow.com/questions/2202999/why-is-textarea-filled-with-mysterious-white-spaces)
- [Remove unnecessary whitespace from Jinja rendered template - Stack Overflow](https://stackoverflow.com/questions/35775207/remove-unnecessary-whitespace-from-jinja-rendered-template)
- [How to apply min and max on textarea? - Stack Overflow](//stackoverflow.com/questions/18184791/how-to-apply-min-and-max-on-textarea)
- [Text Input Patterns: Numbers with or without decimals by Frédéric Hewitt](http://html5pattern.com/Miscs)
- [Flask and JavaScript Confirm Before Deleting - Stack Overflow](//stackoverflow.com/questions/45874906/flask-and-javascript-confirm-before-deleting)

**Message Flashing:**
- [Message Flashing by Pallets Project](//flask.palletsprojects.com/en/1.1.x/patterns/flashing/)
- [Flask Flash function Tutorial](//pythonprogramming.net/flash-flask-tutorial/)
- [Create alert using materialize css - Stack Overflow](//stackoverflow.com/questions/38156282/create-alert-using-materialize-css)

**CSS:**
- [CSS Layout - Horizontal & Vertical Align by w3schools](//www.w3schools.com/css/css_align.asp)
- [Change Materialize tabs text colour](//github.com/Dogfalo/materialize/issues/2591)


### Media
The photos used for my application were obtained from the following sources:
- [Main Image - PeakPx.com](https://c1.peakpx.com/wallpaper/828/1010/470/chefs-spices-preparation-eat-cook-wallpaper-preview.jpg) The main image was originally obtained from the PeakPx site, but then modified to include the "Let's cook together" logo, and the text "Recipe Catalog" is added on top of the image. They are all combined together using paint.
- Recipe Images:
	- [Homestyle Pot Noodles](https://cdn.pixabay.com/photo/2019/08/05/17/56/noodles-4386591__480.jpg)
	- [Banana Pancakes with maple syrup](https://image.shutterstock.com/image-photo/stack-delicious-pancakes-banana-maple-600w-187148783.jpg)
	- [Shortbread cookies](https://cdn.pixabay.com/photo/2017/11/14/23/24/christmas-biscuits-2950295__480.png)
	- [Scotch Pancakes](https://image.shutterstock.com/image-photo/traditional-american-pancakes-on-plate-260nw-115767526.jpg)
	- [Mango and banana smoothie](https://image.shutterstock.com/image-photo/banana-mango-smoothies-on-dark-260nw-277342283.jpg)
	- [Porridge and banana](https://image.shutterstock.com/image-photo/bowl-porridge-bananas-selective-focus-260nw-126897488.jpg)
	- [Poached egg and kale on toast](https://image.shutterstock.com/image-photo/poached-eggs-on-toast-watercress-260nw-141967816.jpg)
	- [Salmon and Sweet Potato Fish Cakes](https://media.istockphoto.com/photos/tuna-fishcakes-with-salad-served-picture-id1170074607?b=1&k=6&m=1170074607&s=170667a&w=0&h=rPBHAsAj1zdVxZmT7alAyzZIGAuOu3EGf5hvbyh2RfQ=)
	- [Cappuccino Tiramisu](https://cdn.pixabay.com/photo/2016/09/01/14/20/tiramisu-1636223__480.jpg)
	- [Sweet and Sour Chicken, simple, no-fry](https://cdn.pixabay.com/photo/2020/03/31/01/56/general-tso-chicken-4985986__480.jpg)
	- [Lamb Koftas with mint yogurt and flatbread](https://live.staticflickr.com/7438/10332838805_fb8ab4dea0_b.jpg)
	- [Mexican Beef Chilli](https://upload.wikimedia.org/wikipedia/commons/0/0f/Pot-o-chili.jpg)
	- [Italian bean & olive salad](https://www.theglobeandmail.com/resizer/SwTyOWdZ_M6jb-YYBbKt2Hq7Dhw=/4288x0/filters:quality(80)/arc-anglerfish-tgam-prod-tgam.s3.amazonaws.com/public/C7RDGAT6RBDENMBQVO3DSCPOUU.jpg)
	- [Ultimate Makeover: French Onion Soup](https://live.staticflickr.com/2418/2132229379_32d319bbab_b.jpg)
	- [Chocolate Eclairs](https://upload.wikimedia.org/wikipedia/commons/a/ad/Chocolate_eclairs_%286792699085%29.jpg)
	- [Lychee & ginger sorbet](https://cdn.drweil.com/wp-content/uploads/2016/12/diet-nutrition_recipes_lemon-ginger-sorbet_2718x1808_000012681647.jpg)
- Tools Images:
	- [Copper Non-Stick Frying Pan](https://images-na.ssl-images-amazon.com/images/I/71OtNyCBmvL._AC_SL1500_.jpg)
	- [OptiGrill Elite 750D](https://images-na.ssl-images-amazon.com/images/I/71mImVP45IL._AC_SL1464_.jpg)
	- [Blender - Easy-Clean Performance Pro](https://cdn.pixabay.com/photo/2011/12/05/14/46/blender-10933__340.jpg)
	- [Non-stick Saucepan](https://images-na.ssl-images-amazon.com/images/I/51SlSNT%2B1qL._AC_SL1000_.jpg)
	- [Springform Cake Tin with Loose Base](https://images-na.ssl-images-amazon.com/images/I/71A%2BbAwYdJL._AC_SL1500_.jpg)

### Acknowledgments

- I would like to thank my Mentor Dick Vlaanderen, for his input, guidance and support over the course of the project.
- I would also like to thank all tutors in the Code Institute, as well as my fellow students on Slack for their help on and support on queries I had while I worked on implementing this project.
- I'd like to thank my family for their support and patience during the completion of my project.
