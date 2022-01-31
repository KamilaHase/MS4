![Mockup]()

# Good Oils

### Project Construction:
## UX
### User stories:
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