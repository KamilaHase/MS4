![Mockup](documentation/images/mockup2.png)

# Good Oils
Good Oils is an e-commerce website built for study purposes at Code Institute. It is a specialized website for the best quality of oils: virgin oils and oils used for cosmetic purposes. Customers can visit the website and order online the products of their choices as well as learn more about certain products in the Good Oils Magazine. The shop is oriented on organic and best quality oils that are on the market in order to target the market trend of healthy lifestile closer to the nature.
The website was developed for study purposes only and all content is fictional. Currently the website would serve in real world as functional starter website where more development is recommended for better user experience. 

View live version of website can be seen via Heroku here.

## Table of Contents
- [Project Construction](#project-construction)
- [UX](#ux)
    - [UX](#ux)
    - [Business Goals](#business-goals)
    - [User stories](#user-stories)
    - [Design of the website](#design-of-the-website)
    - [Wireframes](#wireframes)
    - [Mockup](#mockup)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#Acknowledgements)

## Project Construction:
This website contains full options for an e-commerce website: it is a full-stack website with authentication mechanism together with CRUD requirement functionalities (create, read, update, delete). Functionality is created using Django, Python, HTML5, CSS and JavaScript. As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment. Bootstrap framework was used in building fronted structure to make sure website is as responsive as possible and can be used on multiple screen sizes.
Website offers a registration and login system with password hashing to protect each user. 

## UX
The web has been built to provide simple yet clear information to all users. The overall look is designed to present calm, "earthy" feeling to evoque feelings of nature, freshness and good health. 

### Business Goals:
- To build a brand image for the best quality oils on market
- To target customers who look for good quality oils
- To raise interest of customers about good quality products in the oils area - lure customers who primarily looked for food oils to look into the cosmetics oils option and vice versa. To raise up the idea oils can be used for the health internally and externally as well. 
- To extend the profit of a store owner by providing wider range of products - oils for food and for cosmetics
- To provide information to the customers via Magazine section where more information about the use and effects of oils can be found. Therefore the customers may raise their interest in producst they otherwise wouldn't search for.
- To clearly communicate the available products
- To allow customers to contact with the store owners via Contact form, Comment section in Magazine or via Reviews and provide valuable feedback
- To generate orders through this website


### User stories:
1. **Prospective Customer**
 - I am a person who visits the website for first or more times, I am looking around and checking the products that raised my interest.
 - I am a person who visits the website for the sake of finding more information about oils either on the Product detail sites or at the Magazine section. 
 - I can be registered to the website if I want to see Reviews of Products and Comments to Magazine
 - I don't have to be registered to the website yet 

    - Goals of a Prospective Customer to visit the website: 
        - To find information about products
        - To find information about use of the products at Magazine section
        - To gather more information
        - To check availability or price of products
        - To get in touch with store owners/admin team with my queries
        - If customer is registered to the website: 
            - To see and to post a review to products
            - To create, read, update and delete own product review
            - View comments and add own comment to Magazine posts
        - If customer is not registered to the website: 
            - To see reviews of products 

2. **Customer**
 - I am a person who visits the website with an intention to make a purchase
 - I spend some time looking at Products and finally make an order
 - I can be registered to the website if I want to see Reviews of Products, Comments to Magazine and save my purchase information for future orders
 - I don't have to be registered to the website

    - Goal of a Customer to visit the website: 
        - To make a purchase of the product of my first interest
        - To make a purchase of more products than I initially intended
        - To find information about products
        - To find information about use of the products at Magazine section
        - To gather more information
        - To check availability or price of products
        - To get in touch with store owners/admin team with my queries
        - If customer is registered to the website: 
            - To see and to post a review to products
            - To create, read, update and delete own review
            - View comments and add own comment to Magazine posts
        - If customer is not registered to the website: 
            - To see reviews of products 


3. **Seller**
 - I am a representative of an oil producer (or an oil producer himself/herself) who wants to promote products to Good Oils store owners
 - I spend some time on the website reading information about the available products, compatibility with products I offer and possible competition
 - Most likely I will finally register myself to be able to see reviews of products and comments about article posts

    - Goal of a Seller to visit the website: 
        - To get in touch with Good Oils store owners and offer my products to present on the website
        - To gather more information
        - To check availability or price of products
        - Possibly to make a purchase of a product of interest in order to check competition or to check the smoothness of the ordering process

4. **Admin**
 - I am an administrator of the website closely connected to the store owners (if I am not the store owner myself)
 - I want to have full control over the page and feedback from customers in all forms
 - I am registered as administrator - superuser

    - Goal of an Admin to visit the website (e.g."goodoils.com"): 
        - To add new products 
        - To update, read or delete existing products
        - To access reviews of products
        - To delete reviews of others
        - To create, read, update and delete own review
        - To add new posts to Magazine
        - To update or delete existing posts
        - To access Comments of posts
    
    - Goal of an Admin to visit the the Admin site (Django Admin site): 
        - To have full acces the admin site of the e-shop
        - To add new products 
        - To update or delete existing products
        - To have full acces to product reviews, is able to create, read, update and delete them
        - To access messages from website visitors via Contact form, able to delete them as well as create,read and update them
        - To add new posts to Magazine
        - To update or delete existing posts
        - To have full access to comments of posts in Magazine section, is able to create, read, update and delete them
        - To create new categories and brands of products
        - To have access to queries from Contact form
        - To have access to orders and manage them accordingly


### Design of the website:
Design has been chosen to present classic yet modern look in earth/golden colors as that would be a color of an oil.

#### Typography
- For most of texts on the website have been chosen font 'Jost' which brings light and modern-classic feeling.
- Logo and motivational slogan on index.html are written with font 'Style Script'
- Good Oils Magazine also uses font 'Style Script' in order to clearly visualize different section of the website. It is used for the title Good Oils Magazine, link on the bottom of index.html (again to visualize it links to a different section of the site) and links to read an article.
- All fonts come from [Google Fonts](https://fonts.google.com/ "Google Fonts").

#### Colors
As mentioned above, the website uses earthy/golden beige color together with black and white:
 - #7b621a - for logo Good Oils
            - icons on large screen view
            - class btn-submit-brown used for submit buttons ("Agree with an action" buttons)
            - motivational slogan on index.html - cursive text
            - varieties for specific classes where darker/lighter versions were needed are: #352904, #AB9C6E, #bd8e00
 - #555 - as main body text color
 - #b3b1ac - as it's grey variety for borders and small background areas
 - #000 as black color
 - #fff as white color

 The golden/brown color has been given to actions where it is in "agreement" such buttons add, order, sign in etc. Black and white has been assigned for buttons where the action is to cancel.

Good Oils Magazine uses red to show it is a different section of the site:
 - #c32938 for logo Good Oils Magazine with its variant for div's background #91252f

Certain Bootstrap color palettes were adapted to fit the "earthy" feeling.

Admin navbar is presented in Bootstrap primary color in order to clearly distinguish what are the actions dedicated only for an administrator.

#### Imagery
Images on website are to be found under these links (all have been downloaded from [Shutterstock](https://www.shutterstock.com/).)

- [magazine article](https://www.shutterstock.com/cs/image-photo/different-cooking-oils-on-blue-wooden-1605581422)
- [olive oils: lables](https://www.shutterstock.com/cs/image-vector/olive-oil-labels-collection-hand-drawn-435373711)
- [olive oils: bottles](https://www.shutterstock.com/cs/image-photo/olive-oil-bottles-isolated-on-white-669076666)
- [cosmetic oils: bottles](https://www.shutterstock.com/cs/image-vector/set-realistic-glass-bottles-dropper-box-1158265597)
- [cosmetic oils: bottles](https://www.shutterstock.com/cs/image-photo/set-glass-bottle-cosmetics-dropper-liquid-1770196145)
- [essential oils: bottles](https://www.shutterstock.com/cs/image-vector/realistic-essential-oil-brown-bottle-mock-451075381)
- [magazine article](https://www.shutterstock.com/cs/image-photo/pecs-hungray-febr-27-2021-illustrative-1938731431)
- [essential oils: bottles](https://www.shutterstock.com/cs/image-photo/various-amber-glass-bottles-cosmetics-natural-1460464658)
- [products: coconut oil](https://www.shutterstock.com/cs/image-photo/nutrition-concept-healthy-food-diet-detox-774696967)
- [index.html carousel](https://www.shutterstock.com/cs/image-photo/selection-essential-oils-various-herbs-flowers-684766534)
- [index.html carousel](https://www.shutterstock.com/cs/image-photo/dropper-lavender-essential-oil-over-bottle-1481069378)
- [index.html carousel](https://www.shutterstock.com/cs/image-photo/different-sorts-cooking-oil-bottles-on-1600238197)
- [contacts: Nina Ali](https://www.shutterstock.com/cs/image-photo/close-isolated-studio-shot-good-looking-640005094)
- [contacts: Anna Smith](https://www.shutterstock.com/cs/image-photo/beautiful-woman-blue-eyes-portrait-619769840)
- [magazine article](https://www.shutterstock.com/cs/image-photo/herbal-medicine-natural-cosmetic-phytotherapy-concept-1447910942)
- [magazine article](https://www.shutterstock.com/cs/image-photo/coconut-milk-tropical-useful-dessert-1580400694)
- [magazine article](https://www.shutterstock.com/cs/image-photo/hazelnut-butter-on-wooden-background-1269963892)

All images that have not been listed above were used from Microsoft Office icons library. Other images (such as product labels) I created in Microsoft Power Point.

### Wireframes
### Mockup - main page

## Features
### Existing Features
1. **Features presented on each page** 
- the overall website displays certain features that are loaded from templates: 
    - **base.html** contains:
        - **Logo** Good Oils representing the brand of the page
        - **Search bar** allows users to search among available products
        - **Link to My Profile**: 
            - for unregietred users offers dropdown menu:
                - Register: leading to /accounts/signup/ (see below)
                - Login: leading to /accounts/login/ (see below)
            - for registered users offers dropdown menu: 
                - My Profile: leading to /profile (see below)
                - Logout leading to /accounts/logout/ (see below)

        - **Link to Bag**: shopping bag of the products a user clicked in order to purchase, links goes to /bag site (see bellow) 
        - **Delivery banner** - a banner presenting free delivery for purchases over 25 €. Banner can be closed by clicking/tapping on close button

    - **main_nav.html** contains:
        - **Navbar menu:** 
            - links to products that are sorted according to categories:
            - *Virgin Oils* with dropdown: 
                - Olive Oils (/products/?category=olive_oils)
                - Nut Oils (/products/?category=nut_oils)
                - Seed Oils (/products/?category=seed_oils)
                - All Virgin Oils (/products/?category=olive_oils,nut_oils,seed_oils)

            - *Cosmetic Oils* with dropdown: 
                - Body Oils (/products/?category=body_oils)
                - Essential Oils (/products/?category=essential_oils)
                - All Cosmetic Oils (/products/?category=body_oils,essential_oils)
            
            - *All Products* with dropdown: 
                - By Price (/products/?sort=price&direction=asc)
                - By Category (/products/?sort=category&direction=asc)
                - By Brand (/products/?sort=brand&direction=asc)
                - All Products (/products/)
            
            - *Contact Us* - contact.html
            - *Good Oils Magazine* - magazine.html
            - Registered Admin sees another menu link *Admin Section* with a dropdown:
                - Add Product (add_product.html)
                - Add Magazine Post (add_post.html))

            - **Toggle button for small screens**
            - these sites are described bellow
    
    - **mobile_top_header.html**
          - displays toggle button with *Navbar menu* listed in main_nav.html
          - *Logo Good Oils*
          - *Search bar*
          - *My Profile* button - see below
          - *Shopping Bag* button

    - **footer.html** - presents links to Contact Us form (below), links to to social media (Instagram, Facebook, Twitter) - external resources of information about the project(fictional) and Copyright (fictional).

    - **toast messages** - to comment the process of an action (succes, error, info, warning), toast messages with according message appear in the riht top corner.

2. **Home - home.html** 
    - **Carousel** 
         - presenting motivational images, currently listed 3 images
         - motivational slogan with button leading to all products
    - **Quote** - motivational quote promoting good quality oils
    - **Description of Virgin and Cosmetics Oils from the shop** - in order to raise awareness of good quality oils the website offers, there are two "educational" texts providing description of the oils offered on the shop
    - **Advertisement for Good Oils Magazine** - link to Good Oils Magazine offering more information about the oils

3. **Products - products.html** 
    - Pages where users can see all products and sort them by required criteria: category, brand, price, alphabet
    - Each product displays its image, product name, category, brand, amount and price
    - Products are visible for both registered and unregistered users
    - If Admin is the registered user, he/she can also see links to edit or delete product
    - if a user clicks on image of the product, he is linked to the product detail - product_detail.html

4. **Product Detail - product_detail.html**   
    - Product detail page shows all information available for a certain product: its image, name, category, brand, bottle content, short description. 
    - Buttons to add product in a shopping bag or go back to all products
    - Long descripton od a product
    - Product rating - described on rating page
    - Signed in Admin may also update or delete product

5. **Add Product - add_product.html - ADMIN only**
    - For registered admin user
    - A form to add a new product
    - Accessible from from menu navbar

6. **Edit Product - edit_product.html - ADMIN only**
    - For registered admin user
    - A form to edit an existing product
    - Accessible from products.html page and from product_detail.page

4. **Product Reviews - reviews.html** 
   - In case there are no reviews available yet, a message "No customers have rated .....(name of product)" and a suggestion to "be the first to review the product". 
    - To rate a product a user has to be signed in. Therefore the button "be the first.." leads to sign in page in case the user has not signed in. For users who are already signed in, the button leads them to page add_review.html
    - In case product already contains some reviews, a heading states "Customers rated .....(name of product) as:", below is a scale of 5 empty stars, the average rating is displayed graphicaly by filled stars. Next is placed a button with text "Add review".
    - Reviews are visible to both registered and unregistered users, new review can be added only by a user that is signed in.
    - User can can also update and delete own product review.
    - Admin can delete a product review of another user but has no ability to update it from the website.

5. **Contact Us - contact.html** 
    - Gives the user to contact the company either directly or by a form.
    - Direct contacts are presented on left side of the page, on right side of the page is a form to send in.

6. **Good Oils Magazine - magazine.html** 
    - Site presenting list of articles dedicated to oils. Each article is presented by a card containing short introduction to an article, link to read more and date and author of the article. 

7. **Good Oils Magazine - Post Detail - post_detail.html** 
    - Article in its full length. Contains button with a link to all articles - magazine.html
    - *Comments section* 
        - Signed in users have the option to add their comment on an article
        - Users who have not signed in or registered are linked to sign in page in case they want to see the comments and add their own

8. **Good Oils Magazine - Add Post - add_post.html - ADMIN only** 
    - For registered admin user
    - A form to add a new post
    - Accessible from from menu navbar

9. **Good Oils Magazine - Edit Post - edit_post.html - ADMIN only**
    - For registered admin user
    - A form to edit an existing post
    - Accessible from from post_detail.page

8. **Shopping Bag - bag.html** 
    - Users can see all products they have added to their shopping bag. Page contains image of the product, its name, brand, price, quantity and subtotal price.
    - User has the option to add or decrease the amount of the chosen products.
    - On the bottom of the page is a summary of all ordered products (Bag total costs, delivery costs and total costs) together with link to "continue shopping" or "secure checkout".

9. **Checkout - checkout.html, checkout_success.html** 
    - Section displays a summary of the order and a checkout form where user writes his/hers delivery information for shipping together with his payment card number.
    - Payment field uses Stripe element. 
    - If the user has a saved profile, then checkout form is prefilled with personal and shipping information
    - Webhooks are used to ensure secure and safe purchase.
    - User has also the option of going back and adjusting their bag if he/she wishes to.
    - If a purchase went well, a page checkou_success.html is displayed a confirmation of a successful purchase together with purchase summary.

10. **My Profile** 
    - Registered and signed in user can see all his/hers previous orders and shipping information

11. **Login - login.html**, **Sign Out logout.html**, **Register signup.html** and other social account pages
    -  Based on built in functionalities of [django-allauth](https://django-allauth.readthedocs.io/en/latest/) Python package: "Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication." 
    - Register (sign up page)
        - User provides username, email and password
        - Register button
    - Login 
        - User provides username or email and password. 
        - Remember me option to save information.
        - Sign in button
        - Help for forgotten password
    - Sign Out
        - sign out (logout) page for confirming the wish to logout of the current session

12. **403, 404 & 500 Pages**
    -  Pages explain an encountered error. Button returns user to Good Oils homepage.

13. **Django Admin site https://good-oils.herokuapp.com/admin**
    - As [Django](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/) explains, the admin site is an "automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool."
    - Provides complete control over the website content.

### Features Left to Implement
As already mentioned the website in the current state would serve as a good e-commerce starter page but many features can be added for better user experience. Some of them would be: 
   - **Modal for delete - actions** - for better user experience, it is recommended to add modals for deleting items.
   - **Update and delete comments for articles** - currently no user (apart in the Django Admin site) can update or delete comments in Good Oils Magazine section. For better user experience, it is highly recommended to add these functionalities.
   - **Product detail - load products from same brand** - another of the project idea parts were to load products from the same brand on product detail page. 
   - **About us page** - currently there is no "About us" page which would give better understanding of the e-commerce store owners and their approach to the business. It is highly recommended to include in future development for better user experience as well as for better marketing purposes.
   - **Sign up vs. Register** - for a better user experience it is recommended to fully align the uses of terms "register" vs. "sign up", "login" vs. "sign in". From time reasons those have not been properly corrected in the allauth files. 
   - **Button styling** - during the development of the website, my intent was to unify all buttons. However few of them on the page still kept their styling from django forms and Code Institute tutorial (such as "insert image") or "Add post" in the Magazine section. 
   - **Search functionality accross the entire page** - currently the search bar searches only among the products. It would be better if it searches through the entire page and includes the magazine posts as well. 
   - **Magazine Posts** - include buttons to share posts via social media or email.
   - **Convenient allerts for Admin** - currently the Admin is not informed via email about new orders or new contact messages. It is recommended to include in future development. 

## Technologies Used
### Frameworks, Libraries & Programs Used: 

### Database
The project was built with SQLite, which is Django built-in database for development mode and Heroku Postgres for used for production mode. AWS (Amazon Web Services) are used to store all static files and folders for the website in the production mode.

Database schema is following: 

### Languages: 
- HTML5 for markup
- CSS3 for styles
- JavaScript for interaction
- Python3 as a backend programming language

### Frameworks, Libraries & Tools Used: 
- **GitHub** - used to store the project's code after being pushed from Gitpod.
- **Gitpod** used to develop the project.
- **Git** - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 
- **Django** - The high-level Python web framework used as the main Python framework, including its specific dependencies
- **Stripe** – Allows individuals and businesses to make and receive payments over the Internet.
- **Heroku** - platform for the website deployement
- **AWS (Amazon Web Services)** - for hosting static files and images
- **SQLite3** (Django built-in database) as a database in development mode
- **PostgreSQL** (Heroku built-in) as a database in production mode
- **Google Fonts** - Google fonts were used to import fonts into the style.css file which is used on all pages throughout the project
- **Bootstrap 4** - was used to assist with the responsiveness and styling of the website
- **Font Awesome** - for icons in footer, shopping bag and my profile
- **jQuery** - JavaScript library to provide support with JavaScript codes


Tools used for wireframes and images:
- **MS Office Power Point** - used for creating wireframes, adjusting all print screens
- **techsini.com** for mockup

## Testing
Testing can be found in a separate file [here](/documentation/TESTING.md)

#### Bugs and problems in development:
- **Add Brand filter**
    - First bug I experienced was adding Brand as another option to filter products. As it was the first functionality to be implemented, I managed to make some unknown serious errors that unfortunately did not lead to be solved even with a massive help of Code Institute tutor. In the end I decided to reopen the workspace from GitHub. Second try days later was successful therefore products can be now filtered according to their brands.

- **Missing secret keys due to opening new workspace**
    - Another serious bug that was connected to the first one was that the env.py file was not pushed to GitHub and therefore there were no secret keys logged into settings.py file. The bug was mainly presented by not working Stripe payments. Again, with an extensive help of a tutor, this has been resolved and the payments work well now. 

- **Contact app and sending emails**
   - Issue that took a long time to resolve was a bug where the command return was placed before the code to actually send messages. This took a long time to resolve including deleting the app and installing it again, before it was resolved thanks to the tutor team.

- **Webhook not sending emails**
   - Similar issue but with different sourse happened later on with checkout app. The purchase was proceeded successfully, order shown on Admin site but email was not printed to the terminal. Issue was resolved: gitpod changed the url of the current workspace (from number 28 to 29). Once the number was corrected in Stripe Webhooks, everything worked well again. 

- **Carousel stutters**
    - The last image on carousel "stutters" - doesn´t slide smoothly and stops for a short while while sliding away. Assumption is that it is caused by the Bootstrap class "active". Bug left for future development.

- **Registration failed**
    - After the deployment and correcting files for PEP8 requirements, I splited AUTH_PASSWORD_VALIDATORS in settings.py in an incorrect way, therefore registration of a new user was failing. Thanks to the tutor team, this has been fixed and now works properly.

- **Footer**
    - It was difficult for me to provide a footer that would always stick to the bottom while not covering some of the content. If there is not enough content on page that would push footer down, on some devices the footer may be floating on the page. To correct that I was adding a CSS class "bottom-footer" although I still see it as a bug as it is not sufficient for all types of devices. Also, a mistake can easily appear if the programmer wouldn't remember to add the CSS class in further development. 

## Deployment
Ensured deployed page on Heroku loads up correctly. Ensured Debug variable is set to False. There is no difference between the deployed version and the development version.
Made sure that the env.py file is included in the gitignore file.

(Following section of the deployment adapted accordingly from: https://github.com/Franciskadtt/happybean/blob/main/README.md)
### To clone the project:
From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal: 
```
git clone https://github.com/KamilaHase/MS4-Good-Oils.git
```

#### To install required software:
In the terminal at first delete all the authomatically installed dependencies and extentions by inserting: 
```
pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt
```
Afterwards, type pip3 install -r requirements.txt, which will install all the required softwares to run the project:
```
pip3 install -r requirements.txt
```

#### Setup an enviroment for variables
You now need to set up the database with environment variables. Create a file titled env.py and make sure it is placed in the of this file structure, on the same level as the app.py file. You can also add these in your workspace variable section. 

Option 1: Env.py file:
```
 os.environ['SECRET_KEY'] = ('your_variable_here')
 os.environ["DEVELOPMENT"] = "True"
 os.environ['STRIPE_PUBLIC_KEY'] = ('your_variable_here')
 os.environ['STRIPE_SECRET_KEY'] = ('your_variable_here')
 os.environ['STRIPE_WH_SECRET'] = ('your_variable_here')
 ```
- In ` settings.py`  add:
```
if os.path.exists("env.py"):
    import env
```
-  Add your env.py file to `.gitignore`, before pushing your changes.


<br>Option 2: Workspace Variables:
```
KEY = 'SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'DEVELOPMENT', VALUE = 'True'
KEY = 'STRIPE_PUBLIC_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_SECRET_KEY', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_CH', VALUE = '<your_variable_here>'
KEY = 'STRIPE_WH_SECRET_SUB', VALUE = '<your_variable_here>'
KEY = 'AWS_ACCESS_KEY_ID', VALUE: '<your_variable_here>'
KEY = 'AWS_SECRET_ACCESS_KEY', VALUE: '<your_variable_here>'
KEY = 'USE_AWS', VALUE: 'True'
 ```

- In ` settings.py`  add:
 ```
 SECRET_KEY = os.environ.get('SECRET_KEY', '')
 ```

#### DEBUG 
```
DEBUG = os.environ.get('DEBUG')
```

### **Heroku Deployment**
- Go to the [Heroku](https://www.heroku.com/) website. Register for an account and click on "Create a new app".
- Setup a Heroku app within the Heroku dashboard - Type in the app name and select region the click on create app.
- In Heroku, in your app, click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
- Search for your repo (or sign in and connect GitHub account) and select this.
- Then click "Hide Config Vars" in Heroku.
- Go to the resources tab and search for Heroku Postgres. Choose the “hobby dev - free” option and submit the order form.
- On the `settings.py file`, you will need to comment out the 'SQLite and Postgres databases' section and uncomment the 'PostgreSQL Database' section. (this is temporary, nothing should be pushed/committed just yet).
- Add the database URL from Heroku & migrate your models to the PostgreSQL database with: 
    ```
    python3 manage.py migrate
    ```
- Create a superuser with the following command, and fill in the required information.:
    ```
    python3 manage.py createsuperuser
    ```
- In the `settings.py` file, you can now delete the 'PostgreSQL Database' section and uncomment the 'SQLite and PostgreSQL Databases' section. This means that either database can now be used interchangeably.
- Install gunicorn and freeze that to the requirements file with the following commands:
    ```
    pip3 install gunicorn
    pip3 freeze --local > requirements.txt
    ```
- Create a Procfile and inside, add the following:
    ```
    web: gunicorn good-oils.wsgi:application
- In `settings.py`, use an if statement so that when the app runs on Heroku, you will connect to Postgres, and otherwise, it will connect to sqlite3, like so:
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
- Copy the variables from the variable enviroment one by one into the heroku config vars. They would be:
   ```
    KEY: 'SECRET_KEY', VALUE: “your_variable_here”
    KEY: 'DEVELOPMENT', VALUE: "True"
    KEY: 'STRIPE_PUBLIC_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_SECRET_KEY', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_CH', VALUE: "your_variable_here"
    KEY: 'STRIPE_WH_SECRET_SUB', VALUE: "your_variable_here"
    KEY: AWS_ACCESS_KEY_ID, VALUE: "AWS access key ID"
    KEY: AWS_SECRET_ACCESS_KEY, VALUE: "AWS secret access key"
    KEY: USE_AWS, VALUE: "True"
    ```
- Login to Heroku in the CLI and temporarity disable collectstatic, with the following command:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app good-oils
    ```
- Add your Heroku app and local host to allowed hosts in `settings.py.`
- Push to Github, and then to Heroku master (main). 
- In Heroku, go to the 'Deploy' tab. In the section 'Deployment Method' click on 'Github - Connect to Github'. Make sure your Github profile is displayed. Add the repository name and click on 'Search'. After Heroku has found the repository, click on 'Connect'. This will connect your Heroku app to your GitHub repository. Click 'Enable automatic deploys'. Your code will automatically be deployed to Heroku as well. 

### **AWS (Amazon Web Services)**
Create an account with [AWS](www.aws.amazon.com), follow the steps and sign in. 
- Go to the AWS management console and go to the S3 service. There, create a new bucket. Uncheck 'block all public access' and acknowledge that the bucket will be public.
- Go to the buckets properties, and turn on static website hosting. Select 'Use this bucket to host a website', and fill in index.html and error.html, then click 'save'.
- Go to the permissions tab, and go to CORS configuration. Paste in a CORS configuration:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- Go to the Bucket policy tab and click 'policy generator', to create a policy. Choose 's3 bucket policy', allow all principals by typing a star. From the action dropdown menu select 'GetObject'. Copy the ARN and paste it into the ARN box. Then click 'add statment' and then click 'generate policy'. Copy the policy into the bucket policy editor. Add a slash star onto the end of the resource key. Click 'save'. 
- Go to access control list tab, under public access, click on 'Everyone', select 'List Objects'. Then click 'save'. 
- Go to IAM (from services menu), click on 'groups' and create a new user group. Give the group a group name (f.e. 'manage-good-oils'). Then click 'create group'. 
- Click 'policies' in the dashboard, and then click 'create policy'. Go to the JSON tab. Click 'import managed policy'. Import 'AmazonS3FullAccess'. Get the bucket ARN from the bucket policy page in S3, and paste that in after 'Resource', as a list (first the ARN, then also the ARN with a slash and star). Click 'next tags' and then 'next review'. Give it a name and description. Click 'create policy'. 
- Go to 'groups'. Click the manage-good-oils group. Go to 'permissions'. Click 'attach policy'. Select the policy you just created. Click 'add permissions' and then 'Attach policy'.
- Go to 'users'. Click 'add user'. As username write 'good-oils-staticfiles-user. Give programmatic access. Click 'next'. Add the user to the group. Click through to the end. Download the .csv file. 

### **Connecting DJANGO to S3**
- Go back to GitPod. Install boto3 and Django storages, and freeze them to the requirement file with the following commands:
    ```
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```
- Add 'storages' to the installed apps in the settings.py file.
- Add the following if statement:
    ```
    if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'good-oils'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
- On Heroku, add the AWS keys to the Config Variables (they can be found in the csv file you downloaded earlier). Also, add USE_AWS and set it to True. 
- Remove the DISABLE_COLLECTSTATIC from the variables. 
- In GitPod, create a file called custom_storages.py and add:
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    ```
- To the before mentioned if statement from above, in settings.py, also add:
    ```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
- Add, commit and push these changes. If you now go to the bucket, you will see all the static files. 
- Go to your bucket and add a new folder called media. Inside it, click 'upload' and then 'add files'. Then select all the images you'd like to use. Click 'next'. Under 'manage public permissions', select 'grant public read access'.
- On Stripe, add a new webhook endpoint, with the URL of your Heroku app, followed by 
```/checkout/wh/```. Select 'receive all events' and click 'add endpoint'.

### GitHub Pages
(credit: https://github.com/Code-Institute-Solutions/SampleREADME)
The project was deployed to GitHub Pages using the following steps:
1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
4. Scroll down on the left list of options to find "Pages" section, alternatively scroll down the Settings page until you locate the "GitHub Pages" Section. 
5. Under "Source", click the dropdown called "None" and select "Master Branch".
6. The page will automatically refresh.
7. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

### Forking the GitHub Repository
1. By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:
2. Log in to GitHub and locate the GitHub Repository
3. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
4. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
7. $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
8. Press Enter. Your local clone will be created.


## Credits
#### Overall structure of the website: 
Tutorial from Code Institute - Boutique Ado, https://github.com/Code-Institute-Solutions/boutique_ado_v1

#### Contact app:
Based on: https://github.com/PiotrWojniak/MS4/tree/main/contact
Inspiration from: 
    - https://github.com/AmyOShea/MS4-ARTstop/blob/main/contact/views.py
    - https://learndjango.com/tutorials/django-email-contact-form

#### Reviews app: 
Based on: https://github.com/gomathishankar28/ms4_bubbles/tree/main/reviews

#### Magazine app: 
Based on: https://github.com/gomathishankar28/ms4_bubbles/tree/main/blog

### Other overall inspiration from:
https://docs.djangoproject.com/en/4.0/
https://github.com/Franciskadtt/happybean
https://github.com/gomathishankar28/ms4_bubbles
https://github.com/PiotrWojniak/MS4
https://github.com/AmyOShea/MS4-ARTstop
https://github.com/Sojasmine/alana


### Text content:
Text content was translated mainly from Czech websites dedicated to oils using Google Translate. Oil sites that served as content sources were:
- products: 
    - https://www.grizly.cz/
    - https://www.renovality.cz/
    - https://www.zdrave-oleje.cz/
    - https://www.saloos.cz/
    - https://phytos.cz/
    - https://eshop.nobilis.cz
    - https://www.zdravykos.cz

- magazine: 
    - https://aromatics.cz/blog/
    - https://www.goodie.cz/blog/orechove-kremy-popularni-delikatesa-a-zdroj-energie/

- quote about oils adapted from: https://www.goodreads.com/quotes/tag/essential-oils


## Acknowledgements
Many thanks to mentor Daisy who provided me with inspiration, valuable tips and boosted my motivation.
Many thanks to tutors of Code Institue who´s help was highly appreciated and saved my nerves.