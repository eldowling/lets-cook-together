## Testing

Extensive testing was required to be carried out at each stage of the project. Testing was performed during the development of all new functions in the site, and after each function had been completed, some more testing was performed to ensure it was working correctly, or if any issue was found it could be corrected and retested before proceeding to creating the next function.

The while designing the initial layout, a simple format was chosen for a mobile first approach. The layout for some pages are changed slightly to allow the data fill out on larger screens more, while it is kept more compact for smaller screens which makes it easier to read. Testing was carried out on a mobile device, tablet and medium and large screen
devices to ensure the layout was adjusted for each screen size. Different browsers were also tested to check that the layout remained the same on each - these included Chrome,  Firefox, and Microsoft Edge.

The scenarios used for testing each of the sites components are detailed below:

1. Registration Form:
	1. Open form from the login page, then click the "Sign up here" link. Checked that form opens and displays the correct fields.
	2. Test the required fields and field length are validated before allowing to submit the form.
	3. Create a new user to test their login, when new user is created they are automatically logged in and the Recipe Catalog page is displayed. 
2. Login Form
	1. Open the form using the Login link in the navbar, check that the correct fields have been display when the form is opened.
	2. Test the username and password validation: 
		1. There was originally an issue with with password validation when the user tried to log on, as the password was originally being encrypted using the Bcrypt function, together with a randomly generated salt. This meant when it tried to compare a hashed value of the plain text password against the saved hashed password in the database, they could never match.
		2. I followed some tutorials to try and resolve the issue but it seemed to cause lots of errors. I was directed to use Werkzeug Security functions to generate and check password hashes. This worked much better and allowed me to test a new username being registered and then logged in successfully using this function.
		3. If a valid username with an incorrect password is entered a flash message should display to indicate "Invalid username / password combination".
		4. If an invalid username and / or password combination is entered, the same flash message will also be displayed.
		5. When the correct username and password are entered, the user is logged in and "Welcome, [username]" is displayed below the navbar for mobile users, or inside the navbar for larger screens.
		6. Redirect to the page that you came from after you have logged in. Some pages such as Add Recipe / Rating / Maintenance require a log in to access their functionality. After the user logs in they should be redirected back to these pages, otherwise they will be logged in and shown the recipe catalog page.
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
	1. Click on the recipe title from the catalog list of recipes, a page displaying "General" tab of the recipe details is displayed.
	2. "General" Tab:
		1. Make sure the correct recipe details are displayed, as well as the author of the recipe showing in the top bar beside the recipe title.
		2. Check that the recipe image is being displayed at the top of the General tab.
		3. Recipe Ratings:
			1. Check that the ratings stars are being displayed and calculated as the average for the recipe - if the recipe has already been rated by the current user
			2. Log in as a new user, check the Rate button is displayed because the user has not rated the recipe before.
			3. Rate the recipe as this user and check that the average rating value has changed based on the rating that was just applied.
		4. Ensure that all the rows and columns are displayed with the correct details in each.
		5. Test the layout with different screen sizes to check that the layout is being updated, in particular in the nutritional values between small and medium screens.
		6. Check that the tools listed in a recipe all contain links that can be opened.
	3. Select the "Ingredients" tab:
		1. Make sure that the selected / highlighted tab changes and the fields from the General tab are no longer visible.
		2. Check that all ingredients are listed in a check-mark unordered list.
	4. Select the "Preparation Steps" tab:
		1. Make sure that the selected / highlighted tab changes and the fields from the Ingredients tab are no longer visible.
		2. Check that all the preparation are listed in an ordered list .
	5. Edit and Delete button availability.
		1. View a recipe that was created by a different user to the current user.
		2. Check that neither the Edit nor the Delete buttons are visible to this user at the end of the Show Recipe page.
		3. Select a recipe that was created by the current user. Check that both Edit and Delete buttons are available for this user.
		4. Edit Button:
			1. Click the Edit button and ensure that the correct recipe is loaded with all the fields populated with the correct recipe details.
			2. An issue encountered with the text area for ingredients and preparation steps on this page, was that extra lines and spaces were being added while the fields were being read from the array in the database into the text area. The function .html().trim() was originally used to resolve this issue. But on further investigation I found that it is better to use the minus sign in the jinja code to remove whitespace from the start or end of the text. In testing this then the .html().trim() function could be removed.
			3. Make some updates to values, such as adding tools, changing some nutritional information, adding or removing ingredients / preparation steps.
			4. Click on the Update button to save the recipe.
			5. When it has been saved the recipe will be displayed again in the show recipe page.
			6. Check for the updates that were made during edit, and that they are displayed correctly.
			7. Check for updates made to ingredients and preparation steps lists, so that these lists are still displayed correctly.
		5. Delete Button:
			1. Click on the Delete button on the selected recipe.
			2. When message box is displayed to confirm delete - click Cancel.
			3. Check that you are returned to the recipe after this.
			4. Click Delete again, this time selecting Delete to confirm that this recipe should be deleted.
			5. Catalog page will be loaded after delete. Check the catalog to make sure this recipe is no longer listed.
5. Add Recipe
	1. Sign out of the application and then click on the Add Recipe button on the navbar.
	2. The login form will then be displayed, as the user must be logged in to access this function.
	3. After logging in the user is directed back to the Add Recipe page.
	4. From the Recipe Catalog page click on the Add recipe button from the navbar, an empty recipe form is displayed.
	5. Check that the list boxes for Course, Cuisine and Tools are populated.
	6. Form Validation:
		1. Enter a recipe title and try to click on the Update button to add the new recipe without any further details.
		2. The course list is highlighted and a message displayed to select an item from the list.
		3. Select a course from the list box, and then click on the Update button again.
		4. The Ingredients text area is then highlighted with a message to fill out the field.
		5. Check the minimum field length is being validated by entering under 5 characters.
		6. Error is shown to tell the user the details of the invalid entry "Please enter at least 5 characters (You are currently using 3 characters)" - Field remains red to indicate it is invalid.
		7. Enter some ingredients with the valid minimum number of characters, the field changes to green to indicate the entry is valid once above 5 characters, click Update again.
		8. The Preparation Steps text area is now highlighted to show that there is an invalid entry, and it must also be populated.
		9. Check the minimum field length is being validated by entering under 5 characters.
		6. Error is displayed for the invalid entry "Please enter at least 5 characters (You are currently using 4 characters)" - Field remains red to indicate it is still invalid.
		7. Enter some prep. steps with the valid minimum number of characters, the field changes to green to indicate the entry is valid once above 5 characters.
		8. Click Update and the recipe is saved as all required fields have now been completed. 
		9. The recipe that was just added is displayed in the Show Recipe page. Check that all data that was entered in the Add Recipe are populated on the different tabs.
		10. Click on Edit Recipe to check that you can return to editing this current recipe.
		11. Test the URL validation is working on the Image URL field. Enter an invalid URL and click the Update button.
		12. Message is displayed to enter a valid URL, and field is highlighted red to indicate the issue.
		13. The highlighted field changes to green after a valid URL has been entered. Click on Update to save the changes.
		14. When the recipe is displayed again the recipe image that was entered should be displayed at the top of the General tab. If there is no image, the course name will then be displayed.
6. Featured Tools Catalog
	1. View Full Featured Tools List:
		1. Click on the Featured Tools List link from the navbar.
		2. A list of all the available featured tools will be displayed and sorted in alphabetical order.
		3. The tool name is displayed with a link available to show further information. 
		4. A picture of the tool and the short description are also displayed on the tools catalog page.
	2. Search Bar:
		1. Check that the field length is validated before searching.
		2. Search text will be searched for in the following fields: Tool Name, Description, Further Information.
		2. Enter text that is not contained in any of the 3 search text fields. A message is displayed to indicate that no tools were found for the search text entered.
		3. Enter different combinations of key words that are contained in the search text fields. Check that the tools matching this criteria are displayed.
		4. Clicking the clipboard button to the right of the search bar is to return the full list of tools, 
	3. View Tool Details:	
		1. Click on the link from the tool name from the featured tools catalog.
		2. The tools details page is opened. Check that the details for the selected tool are displayed.
		3. The tool name and price are displayed in the title bar at the top of the details.
		4. The large tool image is displayed below this as well as a purchase button.
		5. Clicking the purchase button will display a modal to indicate that the on-line shopping section is not yet available
		6. A tab for the "Full Details" of the tool is displayed, an unordered bullet list is displayed with all of the details from the further_info field.
	4. Link from Recipe to Tool Details
		1. In the show recipe section, check the list of tools for a selected recipe
		2. Click on the link for the 1st tool name and check that the tool details page is correctly displayed.
		3. Compare with the view tool details page, that was previously tested from the featured tools catalog
		4. Return to the recipe and click on another tool to ensure that each tool listed in the recipe is opening the correct tool information.
7. Maintenance
	1. Sign out of the application and then click on the Maintenance button on the navbar.
	2. The login form will then be displayed, as the user must be logged in to access this function.
	3. After logging in the user is directed back to the Maintenance page.
	4. Check that all 3 lists are displayed. Click the down arrow for each to show the items in each list under their list name headings.
	5. Each list has an "Add New" button to add new items to the lists. Test each of these by click the Add New button.
	6. Add Course:
		1. Click on the Add new button for the Course list. 
		2. Opens a modal form with the Course code and Name / Description field.
		3. Try to Add without completing either field, get a warning to complete both fields.
		4. Enter code and description below the minimum field length, it displays an error to indicate the minimum length for that field.
		5. Max length for both fields tests, and it restrict data entry above that value.
		6. Completed both fields with valid data, then clicked Add, it was saved. 
		7. Checked the Courses list on the maintenance page, new course code & description are available in the list.
	7. Add Cuisine:
		1. Click on the Add new button for the Cuisine list. 
		2. Opens a modal form with the Cuisine code and Name / Description field.
		3. Try to Add without completing either field, get a warning to complete both fields.
		4. Enter code and description below the minimum field length, it displays an error to indicate the minimum length for that field.
		5. Max length for both fields tests, and it restrict data entry above that value.
		6. Completed both fields with valid data, then clicked Add, it was saved. 
		7. Checked the Cuisine list on the maintenance page, new Cuisine code & description are available in the list.
	8. Add Tool:
		1. Click on the Add new button for the Tools list. 
		2. Opens a modal form with all 6 fields available to add the new tool details.
		3. Validation:
			1. Tested field validation for min and max field length on all of the following fields: Code, Tool Name, Short Description, Further Information.
			2. It displays warnings and shows the helper text for each of these field, cannot save without completing all with valid entries.
			3. Tested field validation for price. It only allows numeric entries, with comma or decimal values. 
			4. Displayed a warning for invalid price entered. Error was cleared after a valid numeric entry was completed.
			5. Tested the Image URL field is correctly validated for a valid URL entry.
			6. Completed all fields with valid data, then clicked Add, the new tool was saved. 
			7. Checked the Tools list on the maintenance page, the new tool entry is available in the list.
	9. Edit Tool:
		1. Check that an Edit button is displayed beside each tool in the tools list.
		2. Click on the Edit button beside one of the tools. 
		2. The modal form is displayed, and the tool details are populated in all 5 fields available. Tool code field is not displayed as it shouldn't be modified.
		3. When the modal form was loaded with these fields populated, there was an issue with the labels overlapping the field data, instead of being above the field. Different solutions were tested to try and resolve this issue:
			1. Added the active class to the labels
			2. Added the function: Materialize.updateTextFields(); to reinitialize all the Materialize labels on the page
			3. Searched for other solutions where others had experiences similar issues. Tried some different solutions found with CSS, but none of these worked.
			4. It seemed to be an issue caused by using a modal instead of using a page to load the edit tools form. The reason for this, is that these input fields don't cause the same issues on the edit recipe form. If I was to re-do this section, I would use an edit tools form instead of using the modal.
			5. As a workaround for the issue, I added some dummy disabled input fields above the real input fields, so that the user could identify each field.
			6. I tried to add some CSS to style these dummy inputs further, but this is being ignored when the modal loads.
		4. Another issue encountered with the edit tool modal form, was that the text area wouldn't auto resize with the populated text when displayed on the form. And also that some formatting being done on the populated text is not fully resolved. Again my conclusion is to use an edit tool page, where similar issues have already been resolved for editing the recipe.
			1. Added the function: M.textareaAutoResize($('#tool_further_info')); to the maintenance page to try and have the field auto resized when the edit form modal was loaded. This field does not auto-resize until the user clicks into the field.
			2. Used functions to replace / split / join in order to remove some of the characters from the further_info field which is stored in the database as an array. Most of these characters are being removed, but still have some remaining apostrophes at the end of lines being displayed.
		5. Validation:
			1. Tested field validation for min and max field length on all of the following fields: Tool Name, Short Description, Further Information.
			2. It displays warnings and shows the helper text for each of these field, cannot save without completing all with valid entries.
			3. Tested field validation for price. It only allows numeric entries, with comma or decimal values. 
			4. Displayed a warning for invalid price entered. Error was cleared after a valid numeric entry was completed.
			5. Tested the Image URL field is correctly validated for a valid URL entry.
			6. Updated all fields with valid data, then clicked the Update button to save the modified data for that tool. 
			7. Checked the Tools list on the maintenance page, the new tool entry is available in the list.
			8. Edited another tool and deleted the price value. Then clicked on Update button. 
			9. Record was saved as this is not a required field, and validation is only needed if data is entered in the field.
			9. Checked the entry in the tools list and could see the tool listed with no price assigned.