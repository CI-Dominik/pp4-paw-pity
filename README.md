# **PAW PITY**: Give pets a chance to go home

Paw Pity represents a business with the goal to reunite lost pets with their owners.

Link to the live website: [Link to Paw Pity](https://pp4-paw-pity-7345de0c3b74.herokuapp.com/)<br>
Link to the website's project board: [Link to the GitHub Project](https://github.com/users/CI-Dominik/projects/6)

![Mockup image of the Homepage](docs/mockup.jpg)

## **TABLE OF CONTENTS**

[**USER EXPERIENCE**](#user-experience)
  * [Target audience](#target-audience)
  * [User's journey](#users-journey)
  * [Intuitive and consistent design](#intuitive-and-consistent-design)
    
<br>

[**FEATURES**](#features)
  * [Navigation](#navigation)
  * [Footer](#footer)
  * [Registration](#registration)
  * [Login](#login)
  * [Logout](#logout)
  * [Recent Reports](#recent-reports)
  * [Your Animals](#your-animals)
  * [Missing Animals](#missing-animals)
  * [Animal Details](#aninmal-details)
  * [Hints & Comments](#hints--comments)
  * [Report a Comment](#report-a-comment)
  * [Complaints](#complaints)
  * [Admin Panel](#admin-panel)
  * [Database Connection](#database-connection)

<br>

[**DESIGN**](#design)
  * [Color choice](#color-choice)
  * [Wireframes](#wireframes)
    * [Mobile view](#mobile-view)
    * [Desktop view](#desktop-view)
    
<br>

[**TECHNOLOGIES**](#technologies)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Django](#django)
  * [Visual Studio Code](#visual-studio-code)
  * [GitHub](#github)
  * [Adobe Photoshop](#adobe-photoshop)
  * [Fontawesome](#fontawesome)
    
<br>

[**TESTING**](#testing)
    
<br>

[**VALIDATOR TESTING**](#validator-testing)
  * [HTML validator](#html-validator)
  * [CSS validator](#css-validator)
  * [JavaScript validator](#javascript-validator)
  * [Flake8 validator](#flake8-validator)

<br>

[**USED PLATFORMS AND DEVICES**](#used-platforms-and-devices)
  * [Browsers](#browsers)
  * [Smartphones](#smartphones)

<br>

[**BUGS**](#bugs)
  * [Unfixed bugs](#unfixed-bugs)

<br>

[**ACCESSIBILTIY**](#accessibility)
  * [Lighthouse testing](#lighthouse-testing)
  * [WAVE extension](#wave-extension)
  * [Goal of accessibility measures](#goal-of-accessibility-measures)
    
<br>

[**DEPLOYMENT**](#deployment)
  * [GitHub](#github-1)
    * [Visual Studio Code connection](#visual-studio-code-connection)
    * [Cloning, committing and pushing via Visual Studio Code](#cloning-committing-and-pushing-via-visual-studio-code)
    * [Deployed page on GitHub](#deployed-page-on-github)
  * [Heroku](#heroku)
    * [Creating a new app](#creating-a-new-app)
    * [Naming the app](#naming-the-app)
    * [Deploy the app](#deploy-the-app)
    * [Configure possible Config Vars](#configure-possible-config-vars)
    * [Select a branch to deploy](#select-a-branch-to-deploy)
    * [Waiting for the project to deploy](#waiting-for-the-project-to-deploy)
    
<br>

[**CREDITS**](#credits)
  * [Fontawesome](#fontawesome-1)
  * [Techsini](#techsini)
  * [HTML validator](#html-validator-1)
  * [CSS validator](#css-validator-1)
  * [JavaScript validator](#javascript-validator-1)
  * [Flake8 Extension](#flake8-extension)
  * [W3Schools](#w3schools)
  * [Favicon generator](#favicon-generator)
  * [YouTube](#youtube)
  * [Visual Studio Code](#visual-studio-code-1)

---

## **USER EXPERIENCE**

## Target audience
* Our platform is designed for all pet owners and animal lovers who care deeply about the well-being of animals. Whether you've lost a pet, found one wandering alone, or simply want to help reunite families with their beloved companions, this website is for you. Together, we can make a difference in bringing lost pets back home.

## User's journey
* When users arrive at our website, they are welcomed with a clear and intuitive interface. The platform is divided into two main areas:

My Pets: Here, users can add detailed profiles for their pets. This includes essential information like their name, breed, and photos, making it easier to act quickly if a pet ever goes missing.
Missing Animals: This section showcases a list of pets that have been reported missing. Users can browse through the profiles, filter based on location or type, and provide helpful hints if they’ve seen a reported pet.
Every step of the way, the goal is to create a community that supports each other in reuniting with their beloved pets.

## Intuitive and consistent design
* The homepage embraces a simple, welcoming design with turquoise and white as the primary colors. These hues were chosen to evoke a sense of calm, trust, and compassion. The minimalist layout ensures that users can navigate easily without distractions, focusing on the core purpose of the site: helping lost animals find their way back home.

---

## **FEATURES**

## Navigation
* A navigation bar that holds the page's title as a hyperlink to the starting page and several links to navigate to each of the homepage's sections. The active site gets highlighted in bold font weight.

<br>

![Screenshot of the Navigation](docs/features/navigation.jpg)

## Footer
* A footer containing pieces of information about Paw Pity, links to the homepage's sites and contact information. The email address and telephone number are clickable to open the needed app for communication.

<br>

![Screenshot of the Footer](docs/features/footer.jpg)

## Registration
* A registration page to create a new user. The username, email address and password need to be set here to create a unique user. Each username can only be used once, just like the email address.

<br>

![Screenshot of the Registration](docs/features/registration.jpg)

## Login
* A login form to log into a user account. Only registered users can sign in and only then some of the homepage's features are unlocked, like the comment function for each animal.

<br>

![Screenshot of the Login](docs/features/login.jpg)

## Logout
* A logout modal to securely log out the user.

<br>

![Screenshot of the Logout](docs/features/logout.jpg)

## Recent Reports
* An overview over the last entries into the reports database, shown on the starting page.

<br>

![Screenshot of the Recent Reports](docs/features/recent-reports.jpg)

## Your Animals
* An overview over the registered animals for a user.

<br>

![Screenshot of the Your Animals Page](docs/features/your-animals.jpg)

## Missing Animals
* An overview over the missing animals reported by all users. Users can get details about the animal, like the location, if it is approachable or other things.

<br>

![Screenshot of the Missing Animals](docs/features/missing-animals.jpg)

## Animal Details
* A detailed view over the animal's information.

<br>

![Screenshot of the Animal Details](docs/features/animal-details.jpg)

## Hints & Comments
* A comment area on the animal details page to leave hints for the whereabouts of the animal.

<br>

![Screenshot of the Hints & Comments](docs/features/hints-comments.jpg)

## Report a Comment
* A form to report a comment for false information and rude behaviour.

<br>

![Screenshot of the Report a Comment Feature](docs/features/report-comment.jpg)

## Complaints
* An overview over the complaints made for comments, with the ability to approve or deny.

<br>

![Screenshot of the Complaints](docs/features/complaint.jpg)

## Admin Panel
* An admin panel to manage database entries.

<br>

![Screenshot of the Admin Panel](docs/features/admin-panel.jpg)

## Database Connection
* A database was used to store relevant pieces of information like usernames, animal data and comment complaints.

![Screenshot of the Database Diagram](docs/database/database_diagram.jpg)

---

## **DESIGN**

## Color choice
* As the main colors and tones, a dark turquoise, white and black were chosen to keep a clean design and provide enough contrast for every device.

<br>

![Color palette of the homepage](docs/colors.jpg)

## Wireframes

### Mobile view

*INDEX PAGE*

![Picture of the index page](docs/wireframes/index-mobile.jpg)

*ANIMALS PAGE*

![Picture of the animals page](docs/wireframes/animals-mobile.jpg)

*REPORTS PAGE*

![Picture of the reports page](docs/wireframes/reports-mobile.jpg)

*COMPLAINTS PAGE*

![Picture of the complaints page](docs/wireframes/complaints-mobile.jpg)

### Desktop view

*INDEX PAGE*

![Picture of the index page](docs/wireframes/index-desktop.jpg)

*ANIMALS PAGE*

![Picture of the animals page](docs/wireframes/animals-desktop.jpg)

*REPORTS PAGE*

![Picture of the reports page](docs/wireframes/reports-desktop.jpg)

*COMPLAINTS PAGE*

![Picture of the complaints page](docs/wireframes/complaints-desktop.jpg)

---

## **TECHNOLOGIES**

### HTML
* HTML (HyperText Markup Language) was used to create the structure of the homepage.

### CSS
* All styled were applied by using and linking a CSS (Cascading Style Sheet) file.

### JavaScript
* JavaScript was used to create the functionality of the homepage.

### Python
* Python was used as a programming language for editing backend code.

### Django
* Django was used as a framework to manage views, URLs, models and HTML templates.

### Visual Studio Code
* Visual Studio Code was used to clone the GitHub repository, edit the homepage's code and commit / push the results to GitHub.

### GitHub
* GitHub was used to store the homepage's files. Everything was deployed using GitHub Pages.

### Adobe Photoshop
* Adobe Photoshop was used to create the wireframes.

### Fontawesome
* Fontawesome was linked in the homepage's code to include icon files.

---

## **TESTING**

* All manual tests can be viewed in the testing file: **[Testing File](TESTING.md)**

---

## **VALIDATOR TESTING**

### HTML validator
* All pages were checked for their HTML structure by the W3C Markup Validation Service. No document showed any errors.

<br>

![Screenshot of the HTML validation](docs/validation/html-validation.jpg)

### CSS validator
* The custom stylesheet file styles.css was checked via the W3C CSS Validation Service. No errors were found.

<br>

![Screenshot of the CSS validation](docs/validation/css-validation.jpg)

### JavaScript validator
* The deleteModal.js file was tested using the JSHint validator. Only warnings pointing to the use of ES6 syntax and a reference to the bootstrap variable used elsewhere were mentioned.

![Screenshot of the JavaScript validation for deleteModal.js](docs/validation/js-validation-deleteModal.jpg)

* The commentDeleteModal.js file was tested using the JSHint validator. Only warnings pointing to the use of ES6 syntax were mentioned.

![Screenshot of the JavaScript validation for commentDeleteModal.js](docs/validation/js-validation-commentDeleteModal.jpg)

* The deleteComplaintsModal.js file was tested using the JSHint validator. Only warnings pointing to the use of ES6 syntax were mentioned.

![Screenshot of the JavaScript validation for commentDeleteModal.js](docs/validation/js-validation-deleteComplaintsModal.jpg)

### Flake8 validator
* Flake8 was used in Visual Studio Code to check the Python code in all files that were used, changed and adjusted. No errors occured.

---

## **USED PLATFORMS AND DEVICES**

## Browsers
* Google Chrome
* Mozilla Firefox
* Microsoft Edge

## Smartphones
* Poco F5 Pro
* Samsung S21
* Samsung S23
* iPhone XS

## **BUGS**

## Unfixed bugs
* No unfixed bugs are known at this point.

---

## **ACCESSIBILITY**

## Lighthouse testing

### Mobile view
* In mobile view, the results in performance drop down to about 74. This is due to the fact that Bootstrap was used locally and not via a link to the online version. This choice was made, because the styling should be available at all times and not dependent on an external service.<br>
In addition, user-uploaded pictures in JPG format decreased the performance as well. This is an expected result, as most users will later upload their photos as a JPG file.

*INDEX PAGE*

![Picture of the index page's results](docs/lighthouse/index-mobile.jpg)

*ANIMALS PAGE*

![Picture of the animals page's results](docs/lighthouse/animals-mobile.jpg)

*REPORTS PAGE*

![Picture of the reports page's results](docs/lighthouse/reports-mobile.jpg)

*COMPLAINTS PAGE*

![Picture of the complaints page's results](docs/lighthouse/complaints-mobile.jpg)

### Desktop view

*INDEX PAGE*

![Picture of the index page's results](docs/lighthouse/index-desktop.jpg)

*ANIMALS PAGE*

![Picture of the animals page's results](docs/lighthouse/animals-desktop.jpg)

*REPORTS PAGE*

![Picture of the reports page's results](docs/lighthouse/reports-desktop.jpg)

*COMPLAINTS PAGE*

![Picture of the complaints page's results](docs/lighthouse/complaints-desktop.jpg)

## WAVE extension
* The WAVE extension in Google Chrome was used to determine the accessibility rating of the homepage. Some alerts point to skipped heading levels which were used to better suit their content and redundant links which are the result of the use of buttons and navigation links on the same site.

*INDEX PAGE*

![Picture of the WAVE results for the index page](docs/wave-extension/index.jpg)

*ANIMALS PAGE*

![Picture of the WAVE results for the animals page](docs/wave-extension/animals.jpg)

*REPORTS PAGE*

![Picture of the WAVE results for the reports page](docs/wave-extension/reports.jpg)

*COMPLAINTS PAGE*

![Picture of the WAVE results for the complaints page](docs/wave-extension/complaints.jpg)

## Goal of accessibility measures

* The goal of accessibility is the same result, performance and view of the content for any person, regardless of their condition. For example, the colors are chosen in a way that all people can use the site without any problems. The contrast needs to be high enough to read every text.<br>

---

## **DEPLOYMENT**

## GitHub

### Visual Studio Code connection
* A connection between Visual Studio Code and GitHub was established using the built-in function to include the ability to clone, stage, commit and push content directly to GitHub.
Once you start Visual Studio Code with no connection, you simply need to click on the person icon in the lower left corner and select "GitHub". From there, you can connect your existing account to Visual Studio Code.

<br>

![Screenshot of the menu to connect Visual Studio Code with GitHub](docs/vscode-connection.jpg)

### Cloning, committing and pushing via Visual Studio Code
* Visual Studio code was used to stage all changed files and commit them with an included message directly to GitHub.

<br>

![Screenshot of the menu to commit changes to GitHub](docs/vscode-commit.jpg)

### Deployed page on GitHub
* The system is hosted via Heroku, but still available in the pages menu of GitHub.

<br>

![Screenshot of the deployed page in GitHub](docs/deployment-pages.jpg)

## Heroku

### Creating a new app
* In the dashboard, navigate to the button *New* and *Create new app*.

<br>

![Screenshot of Heroku deployment 01](docs/heroku/01.jpg)

### Naming the app
* Give the app a new name and select the host region (US/EU). Then click *Create app*.

<br>

![Screenshot of Heroku deployment 02](docs/heroku/02.jpg)

### Deploy the app
* Click on the *Deploy* button on the top. In the bottom, select the platform on which the code is hosted, select the username and insert the name of the repository. GitHub was chosen here.

<br>

![Screenshot of Heroku deployment 03](docs/heroku/03.jpg)

<br>

![Screenshot of Heroku deployment 04](docs/heroku/04.jpg)

### Configure possible Config Vars
* Config vars are a way to securely store need information for connections like the PostgreSQL connection used in this project. Insert a key and value pair and add it.

<br>

![Screenshot of Heroku deployment 05](docs/heroku/05.jpg)

### Select a branch to deploy
* A GitHub branch that should be deployed can be found on the *Deploy* page. Here, the main branch was used to create the project.

<br>

![Screenshot of Heroku deployment 08](docs/heroku/08.jpg)

### Waiting for the project to deploy
* A window with all needed pieces of information will be displayed to inform the user of the current action. After successfully deploying the app, a *View* button will appear. It contains the link to the live site.

<br>

![Screenshot of Heroku deployment 01](docs/heroku/09.jpg)

<br>

![Screenshot of Heroku deployment 10](docs/heroku/10.jpg)

---

## **CREDITS**

## [Fontawesome](https://fontawesome.com/)
* Used to implement website icons.

## [Techsini](https://techsini.com/multi-mockup/index.php)
* Used to create the mockup in the readme file.

## [HTML validator](https://validator.w3.org/)
* Used to verify HTML code.

## [CSS validator](https://jigsaw.w3.org/css-validator/)
* Used to verify CSS code.

## [JavaScript validator](https://jshint.com/)
* Used to verify JavaScript code.

## [Flake8 Extension](https://flake8.pycqa.org/en/latest/)
* Used to verify Python code.

## [W3Schools](https://www.w3schools.com/)
* Used to lookup tips for the code.

## [Favicon Generator](https://favicon.io/)
* Used to generate the favicon for the homepage.

## [YouTube](https://youtube.com)
* Videos for understanding some code areas.

## [Visual Studio Code](https://code.visualstudio.com/)
* Used to generate HTML boilerplate code and code editing.