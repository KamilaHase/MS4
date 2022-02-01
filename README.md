![Mockup]()

# Good Oils
Good Oils is an e-commerce website built for study purposes at Code Institute. It is a specialized website for the best quality of oils: virgin oils and oils used for cosmetic purposes. Customers can visit the website and order online the products of their choices as well as learn more about certain products in the Good Oils Magazine. The shop is oriented on organic and best quality oils that are on the market in order to target the market trend of healthy lifestile closer to the nature.
The website was developed for study purposes only and all content is fictional.
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

1. **Customer**
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


1. **Seller**
 - I am a representative of an oil producer (or an oil producer himself/herself) who wants to promote products to Good Oils store owners
 - I spend some time on the website reading information about the available products, compatibility with products I offer and possible competition
 - Most likely I will finally register myself to be able to see reviews of products and comments about article posts

    - Goal of a Seller to visit the website: 
        - To get in touch with Good Oils store owners and offer my products to present on the website
        - To gather more information
        - To check availability or price of products
        - Possibly to make a purchase of a product of interest in order to check competition or to check the smoothness of the ordering process

1. **Admin**
 - I am an administrator of the website closely connected to the store owners (if I am not the store owner myself)
 - I want to have control over the page and feedback from customers in all forms
 - I am registered as administrator - superuser

    - Goal of an Admin to visit the website: 
        - Add new products 
        - Update or delete existing products
        - Access reviews of products
        
        - Access messages from website visitors via Contact form
        - Add new posts to Magazine
        - Update or delete existing posts
        - Access Comments of posts


### Design of the website:
#### Typography
#### Colors

#### Imagery
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

- **Carousel stutters**
    - The last image on carousel "stutters" - doesn´t slide smoothly and stops for a short while while sliding away. Assumption is that it is caused by the Bootstrap class "active". Bug left for future development.

- **Contact app and sending emails**
   - Issue that took a long time to resolve was a bug where the command return was placed before the code to actually send messages. This took a long time to resolve including deleting the app and installing it again, before it was resolved thanks to the tutor team.

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