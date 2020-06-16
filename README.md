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

### Features Left to Implement
The recipe catalog site could be further expanded to include some of the following features, which have not yet been implemented:
- Expand on the filters and search functionality, to allow the user to select a search by option on the recipe catalog page (For example: ingredients / tools)
- Include sorting functionality to allow the user to sort recipes by different fields such as rating, or cuisines
- Enhance the maintenance section by adding super user levels of access to this section, so as only selected users could make updates to the sites lists and tools.
- Develop an on-line shop to allow users to purchase tools from the site.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

The scenarios used for testing each of the sites components are detailed below:

1. Registration Form:
	1. Open form from the login page, then click the "Sign up here" link. Checked that form opens and displays the correct fields.
	2. Test the required fields and field length are validated before allowing to submit the form.
	3. Create a new user to test their login, when new user is created they are automatically logged in and the Recipe Catalog page is displayed. 
2. Login Form
	1. Open the form using the Login link in the navbar, check that the correct fields have been display when the form is opened.
	2. Test the username and password validation: 
		1. If a valid username with an incorrect password is entered a flash message should display to indicate "Invalid username / password combination".
		2. If an invalid username and / or password combination is entered, the same flash message will also be displayed.
		3. When the correct username and password are entered, the user is logged in and "Welcome, [username]" is displayed below the navbar for mobile users, or inside the navbar for larger screens.
		4. Redirect to the page that you came from after you have logged in. Some pages such as Add Recipe / Rating / Maintenance require a log in to access their functionality. After the user logs in they should be redirected back to these pages, otherwise they will be logged in and shown the recipe catalog page.
	3. Signout and Login links availability:
		1. Signout button is available in the navbar once a user is logged in. 
		2. Clicking the Signout button will log the user out and display a flash message to show that the user has been signed out. 
		3. Login button is available from the navbar after the user has been signed out.
3. Recipe Catalog
	1. Full Catalog
		1. Catalog page should be displayed as main landing page.
		2. A list of all recipies should be displayed and grouped by the recipe course.
		3. Each course should have it's own group header before listing recipes for that course below the header.
		4. The page pagination numeric links should be displayed at the end of the page, showing a max of 5 recipes per page. 
		5. The pagination should only show 2 page numbers either side of the current page, and "<" or ">" at the beginning or end of the numeric list if there are more pages either side of the edge numbers of the list.
		6. Test that the left/right arrows in the pagination list work to display the previous or next page in the number sequence. The max number of recipes per page was reduced from 5 to 2 so that this could be fully tested.
	2. Search Bar
		1. Check that the field length is validated before searching.
		2. Enter text that is not contained in the recipe title or description. Message is displayed to indicate that no recipes were found for the search text entered.
		3. Enter different combinations of key words that are contained in the title and description. Check that recipes are displayed for these key words, and that they are shown under their correct Course group header.
	3. Course Filter
		1. Select a course filter from the dropdown list. Check that recipes from that course are displayed.
		2. Check that the pagination works when the course filter is used, and that only recipes for that course are displayed when the next page is selected.
		3. Select another course filter, ensure that recipes for only that course have been displayed, and that recipes for the previously selected course are no longer available.
		4. Select a course without any recipes. The message "No recipes found for selected course: [CourseName] " is displayed to indicate to the user that no recipes were found.
		5. Select "All Courses" from the course dropdown list to check that the full catalog of recipes is display and correctly grouped by their course.
	4. Cuisine Filter
		1. Select a cuisine filter from the dropdown list. Check that recipes from that cuisine are displayed.
		2. Check that the pagination works when the cuisine filter is used, and that only recipes for that cuisine are displayed when the next page is selected.
		3. Select another cuisine filter, ensure that recipes for only that cuisine have been displayed, and that recipes for the previously selected cuisine are no longer available.
		4. Select a cuisine without any recipes. The message "No recipes found for selected cuisine: [CuisineName] " is displayed to indicate to the user that no recipes were found.
		5. Select "All Cuisines" from the cuisine dropdown list to check that the full catalog of recipes is display and correctly grouped by their course.
4. Show Recipe
5. Add Recipe
6. Edit Recipe
7. Delete Recipe
8. Tools Catalog
	1. View Tools List
	2. View Tool Details
	3. Link from Recipe to Tool Details
9. Maintenance
	1. Add Course
	2. Add Cuisine
	3. Add Tool
	4. Edit Tool

## Deployment

The project was developed using Gitpod which is an on-line IDE for GitHub which uses a ready to code development environment, and deployed to the GitHub repository hosting service during development. The project was deployed to Heroku cloud hosting platform.

The project was committed to the GitHub repository at regular intervals during development, or when an element of the project had been completed. Comments are entered on each commit in order to track updates that have been made.

There are no differences between the deployed and development versions. Any components that were implemented in the development stage were uploaded to GitHub and then to Heroku for final deployment.

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
- [How to validate select option for a Materialize dropdown? by Stackoverflow](//stackoverflow.com/questions/34248898/how-to-validate-select-option-for-a-materialize-dropdown)
- [New line in text area - Stack Overflow](//stackoverflow.com/questions/8627902/new-line-in-text-area)
- [Why is textarea filled with mysterious white spaces? - Stackoverflow](//stackoverflow.com/questions/2202999/why-is-textarea-filled-with-mysterious-white-spaces)
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
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
