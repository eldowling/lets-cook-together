# Let's Cook Together - Recipe Catalog

The Recipe catalog was created to allow users to share their own recipes in an easily accessible catalog, which allows registered users to add new recipes simply, and to share with other users of the recipe catalog. 
Recipes can be easily found through the use of either a search bar or two filter buttons. 
- The search bar can look for key words in the title or description of any recipe
- The filter buttons allows the user to select from either the list of courses or cuisines, and displays a selection of recipes from the course or cuisine that was selected by the user. 
- Pagination is used to allow the catalog to be displayed in smaller lists, this can be useful in particular for mobile users to provide shorter lists and limit data usage as well as providing faster page loading.

When each recipe is displayed the page is divided into three tabs: "General Information", "Ingredients", "Preparation Steps". The simple layout is mobile friendly and helps with providing the user with quick and easy access to the relevant section, without having to scroll too much.

While viewing the recipe a list of the tools used in the preparation or cooking of the recipe will be displayed to the user. This list is helpful to the user for preparation ahead of making the recipe, but it also provides a link for each tool which allows the user to view the tool information page, and will also allow the user to purchase any of these tools from the site.

The site provides the ability for any user to add a new recipe to the catalog, as well as being able to make updates or delete any of the user's own recipe that were previously added. When the user is adding a recipe they will have a list of options to complete, some of which are mandatory before being able to save the recipe. Some of the fields are populated with lists which makes it easier to categorise the recipes into groups.
When the user edits a recipe, all of these boxes will already be populated with the details that were previously saved for that recipe. The user can select the items that they wish to update, and will be returned to that recipe once it has been saved. The recipe author also has the option to delete a recipe if required.

All recipes can be rated by multiple users. If a recipe has not been rated by the session user, a button will be available for that user to rate the recipe. Otherwise the average rating for that recipe is displayed.

There is a Featured Tools page as part of the site. This is to promote and provide further details of any of the tools that are used in the recipes.
It provides a list of all tools, as well as an indivial page for each of the tools with additional information about each of the tools that are available. The site can be further developed to allow for any of the tools to be purchased by the user.

The site has a Maintenance section which is to allow a user to add to the lists such as Course and Cuisine, which are available when adding each recipe to categorize them. These categories are used to provide simple filter options on the main recipe catalog page.
Another feature of the maintenance section is to allow the list of Tools to be added to and updated. The user can view the list of tools that have already been entered. Each data item that is stored against the tool can then be updated. For example if the price increases, or if the item description of further information needs to be modified, it can be done through this tool maintenance. Additionally, new tools can be added to the tools list, and these will in turn appear in the available tools list when adding a new recipe / editing existing recipes or in the Featured Tools section of the site too.
 
## UX
 
The recipe catalog site is required to allow users easy access to a catalog of recipes, where users can share their own recipes, search for text within recipes, and filter recipes by certain categories.
The site should also allow the users to rate and view ratings for each recipe
Each recipe should allow the author to share details of some of the tools that were used in making the recipe. This list should have the ability to add to or modify details of existing tools.
There should be an area to view the list of all the tools featured on the site, as well as providing the user with further details to view for each of the tools listed. An online shop may be required further down the line, and the featured tools section should provide potential to create this easily.

The user stories below demonstrate the key features that were required from the recipe catalog. These are taken from different users points of view and show the functionality they required from the site:
- As a busy mother I want to be able to view recipes quickly and easily on my phone, so that I can follow them direcly from the screen while I'm in the kitchen
- As a parent of young children, I like to browse through specific recipe categories for lunch or dinner ideas. I also like to search for words from the recipe name when I want to find a recipe quickly. I like to have this available on my phone as I usually take some time to do this during my daily bus commute.
- As a keen cook, I have built a large collection of recipes over a number of years. These have come from many locations such as family recipes passed down from my mother and grandmother, some of my own recipe and also magazine pullouts. I would like a central location to store all of these, as well as to help with the safe keeping of family recipes. I'd also like to be able to share them with others, and hope that they get enjoyment from making & eating them too.
- I'm a student in a cookery school, I often browse recipes for inspiration and I find the recipe ratings useful in helping to decide on themes for my weekly menus. I would like to view the catalog on my laptop while preparing my course work, or sometimes on my phone or tablet.
- As the business manager of ToolsPro I would like to be able to promote our products and allow users of the site to see clearly which of our tools are available to use in each recipe. I would also like the users of the site to have access to our full range of ToolsPro products, and have a plan for further development to allow them to purchase these products directly from the site.
- As the ToolsPro sales administrator, I need functionality to add to the lists in used on the pages in the site. In particular the range of ToolsPro products that are available in order to add to this list or update the price or any details regarding each of the products.

The wireframes were developed through the use of these user stories to outline the content required in the recipe catalog, as well as forming the basis of what the site would look like and how it would work.
The wireframes are available to view at https://balsamiq.cloud/svy4yos/pgpn73q

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
