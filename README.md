![Mockup]()

# Good Oils
Good Oils is an e-commerce website built for study purposes at Code Institute. It is a specialized website for the best quality of oils: virgin oils and oils used for cosmetic purposes. Customers can visit the website and order online the products of their choices as well as learn more about certain products in the Good Oils Magazine. The shop is oriented on organic and best quality oils that are on the market in order to target the market trend of healthy lifestile closer to the nature.
The website was developed for study purposes only and all content is fictional. Currently the website would serve in real world as functional starter website where more development is recommended for better user experience. 

View live version of website can be seen via Heroku here.

## Table of Contents
- [Demo](#demo)
 

### Project Construction:
This website contains full options for an e-commerce website: it is a full-stack website with authentication mechanism together with CRUD requirement functionalities (create, read, update, delete). Data handling document is database based on XXXXX. Functionality is created using Django, Python, HTML5, CSS and JavaScript. Bootstrap framework was used in building fronted structure to make sure website is as responsive as possible and can be used on multiple screen sizes.
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

All images that have not been listed above were used from Microsof Office icons library.

#### Wireframes
#### Mockup - main page

## Features

### Existing Features
### Features Left to Implement
## Technologies Used
### Database
### Frameworks, Libraries & Programs Used: 
## Testing
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


- **Buttons styling**

- **Buttons styling**

- **Buttons styling**

## Deployment
### Deploying to Heroku
### GitHub Pages
### Forking the GitHub Repository
### Making a Local Clone

### Gitpod
## Credits

### Acknowledgements





- future implementation: 
    - modal window for delete actions
    - correct rating - for each product
    - correct for add_product display "----" for Brands as default
    - correct footer position


Credits:

Overall structure of the website: Tutorial from Code Institute - Boutique Ado
- Contact app:
https://github.com/PiotrWojniak/MS4
https://github.com/AmyOShea/MS4-ARTstop/blob/main/contact/views.py


- quote about oils adapted from: https://www.goodreads.com/quotes/tag/essential-oils

- magazine: 
    - https://aromatics.cz/blog/
    https://www.goodie.cz/blog/orechove-kremy-popularni-delikatesa-a-zdroj-energie/