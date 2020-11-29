Venum MMA Store
Milestone Project #4 : Full Stack Development Milestone Project - Code Institute

## Demo

[Live demo](https://venum-mma-store.herokuapp.com/) is available here.

Venum MMA Store was designed and created to enable people who find an interest in Combative Arts and would like to be equiped with the best fighting gear in the world, VENUM!
To make a purchase one has to use the test credit card number provided by stripe:
-Card number: 4242 4242 4242 4242
-CVC: any 3 digit number
-Exparation Date: random date in the future.
-Address: random adress.

Admin login info may be provided on request at nikolasdrosatos@gmail.com

## UX

**Requirements**

- Store owner is able to add, edit and delete products and events to be promoted and sold.
- Store owner has easy access to a single admin panel from which the whole webstore can be controled. The panel should include all profiles and their info, all categories and products, all events, all emails sent by all users, all order made, etc. The owner should be able to view edit and delete the above easily.
- Potential customers are able to view all products in a single all products list, sort products in categories, prices, ratings, purchase product using a secure checkout system, create a personalized account, add and update personal info, card info, view promoted events, add products to wishlist and finally contact the owners.
- The store should be easy to navigate and aesthetically pleasing. It should also resemble other basic webstores as far as navigation and design goes in order to make it more user friendly (customers are more likely to visit a store that resembles stores that they are already familiar with and know how to use).

**Client Stories**

1. As a customer I would like to be able to view a list of product in order to be able to purchase the ones I want.
2. As a customer I would like to be able to view individual product details in order to be able to identify prices, description, rating, sizes and images.
3. As a customer I would like to be able view clearence, deals and other special offers in order to be able to purchase the most affordable products.
4. As a customer I would like to be able to add products to my bag in order to later be able checkout and purchase them.
5. As a customer I would like to be able view the balance of my bag at all times in order to stay within my means.
6. As a cstomer I would like to add products to a wishlist in order to be able to purchase them sometime in the future.
7. As a customer I would like to be able to view all products in my wishlist in order to choose which products I am planning to buy in the future.
8. As a user I would like tobe able to register for an account in order to have a personal profile that I am able to view.
9. As a user I would like to be able to log in and out in order to be able to access the account I have created.
10. As a user I would like to be able to recover my password in case I forget it in order to be able to access my account again.
11. As a user I would like to be able to receive a comfirmation email when I register an account in order to know that my registration went through.
12. As a user I would like to have a personilized profile in order to view my contact info, bank info and order history.
13. As a customer I would like to be able to sort the list of products in order to be able to view the best rated, best priced and most categorically relevant products I seek.
14. As a customer I would like to be able to sort a specific category of product in order to be able to then sort products within that category.
15. As a customer I would like to be able to sort multiple categories at the same time in order to be able to view the best rated, best priced products across categories.
16. As a customer I would like to be able to search for a product by name or description in order to be able directly find the particular product I seek.
17. As a customer I would like to be able to select size and quantity of each product in order to make sure both are correct.
18. As a customer I would like to be able to view the content of my bag, along with the subtotal and a list of the products I am purchasing in order to ensure that everything is correct before I complete my purchase.
19. As a customer I would like to be able to adjust the quantity or size of a product within my bag in order be able to correct mistakes I have made when I first added the product to the bag.
20. As a customer I would like to be able to remove a particular product from my bag before checking out in order to be able to get rid of products I regret adding to the bag.
21. As a customer I would like to be able to fill in my contact and payment info in order to be able to check out as quickly as possible.
22. As a customer I would like to have my contact and payment info saved and automatically generated upon checkout in order to avoid filling the same info every time I make a purchase.
23. As a customer I would like to view an order confirmation after checkout in order to be able to know that the payment went through.
24. As a customer I would like to receive a confirmation email after checkout in order to save it for myself.
25. As a customer I would like to be able to send and email to the store's owner in order to be able to ask specific questions I have.
26. As a customer I would like to be able to receive a confirmation of sorts that my email was sent in order to know that my question will eventually be answered.
27. As an admin I would like to be able to add a product in order to add new items to my store.
28. As an admin I would like to be able to update a product in order to be able to adjuct prices, sizes, description and possible mistakes I have made when adding a product.
29. As an admin I would like to be able to delete a product from my store in order to be able to remove items I no longer sell.
30. As an admin I would like to be able to add, update, delete events that I am sponsoring in order to be able to promote them to customers who buy our gear, for marketing purposes.
31. As an admin I would like to view all profiles, orders, emails, products and event in a single admin panel in order to navigate through the entire store easily.

## Design

**Framework**

Bootstrap and jquery were extensively used for almost all of the frontend.

**Color scheme**

In order to keep the project consistent and pleasant to the eye I tried to stick to colors that compliment each other. White, black and shades of grey with the occasional red or opaque black background were used throughout the project. Most pages that include numerous colorful products have a white overlay in the background because any other color in the background would make the page erratic to the eye considering the numerous colorful products desplayed. All buttons reverse colors when hovered to make the site more interactive and aesthetic.

**Icons**

All icons were taken from fontawesome.

**Typography**

Lato and sans-serif were used for the typography of the project.

**Wireframes**

These can be found in the static/wireframes folder of this project.

## Features

The features mentioned below are present and fully responsive in all screens regardless size, and are fully functional.

**Navbar**

For this project I have used two navbars. One that contains all categories with collapsible subcategories of the pages of the products the store is selling, as well as a second top main nav bar that contains the Venum logo, a search bar and apps such as my account (with dropdown to register, login, logout, product management for admin), wishlist (to view products saved in wishlist), bag (to view contents of the bag), events (to view sponsored events) and contact (to enable the user to contact the owners).

**Home**

The home page is the first page the customer lands in upon visiting our store. It includes a promotional slogan along with a big red hover on button that entices the customer to check our products. A nice background picture of a fighter staring at the customer infront of a boxing bag is displayed.

**Footer**

A nice opaque footer that contains three social media links that change colors on hover, is at the bottom of all pages, to promote Venum's social media and keep the customer in touch.

**My profile**
Located at the top main navbar, this is a dropdown menu. If the user is not authenticated he/she will have the option to register or login. If the user is authenticated he/she will have the option to visit his/her profile, view info and order history, log out, or if the user is an admin, he/she will have the option to access the product management form to add a product.

**Products**
All product categories are located in the dropdown menu of the second navbar beneath the main top navbar. A user many visit any category to view the products within it, sort it by name, price, rating, etc. The user sees the products in rows and the image as well as the name, category and rating is displayed. By clicking on a given product the user opens the individual product detail page.

**Product detail page**

This page pops up when a user clicks on a product. This pages includes more details about the product such as description, sizes, price and enables the user to add the product to the wishlist or the bag for purchase.

**Wishlist**

A user may add a given product here for later purchase. He/she may also update the quentity or size, and even delete a product from the wishlist.

**Bag**

A user may add a given product here for purchase. He/she may also update the quentity or size, and even delete a product from the bag. Moreover, the user may procede to purchase the contentsof the bag by clicking on checkout which forwards the user to the checkout page.

**Checkout**

Here the user may input his/her card and personal info in order to procede with the purchase. If the user is authenticated or a returning user the info may be stored and called on click. At the moment in order to make a purchase one has to input stripe's test card number.
-Card number: 4242 4242 4242 4242
-CVC: any 3 digit number
-Exparation Date: random date in the future.
-Address: random adress.

**Events**

The MMA events that VENUM sponsors are displayed here. The user may click on the buy tickets to be redirected to the ticket seller.

**Contact**

The user, authenticated or not may contact the store by filling the form with mail, name and message and the mail will be saved to the database to be view later by the admin through the admin panel. All messages are stored in the admin panel under "Contacts". Also an email is sent to the admin's email letting him/her know that they got a new message.

## Defensive Design

Here I focused mainly on authentication, Cross Site Request Forgeries and catching errors in a nice page.

- Authentication:
  Authentication is a crucial part of the webstore. I wanted to make sure that a user is authenticated in order to be able to do certain things on the webstore. For instance a user that is already loged in should not be required or be able to log in, a user who is authenticated may edit the profile for which he/she is authenticated. A user that is an Admin will have additional abilities mentioned below, while user that are not authenticated as admins will not.

- CSRF:
  The {% csrf_token %} prevents Cross Site Request Forgeries and is added on several templates.

- Required attribute:
  Makes sure that fields on numerous forms that are crucial are always filled and not neglected.

- Catching 404 error:
  I have created a nice template that catches that error and displays it nicely. It also asks the user to return to the website by clicking on a link.

## Admin

The admin is the superuser of the webstore. He/she may add edit and delete products both through the admin panel as well as directly through the website using the appropriate edit, delete buttons next to each product and add products with the use of the product management tab in the Myprofile app.
Moreover he/she may add, edit and delete events both through the admin panel. Messages sent by user are also store in the admin panel under "Contacts". Basically the admin panel is the heart of the project and the admin can view edit, add and delete everything through it. To access make an inquiry to nikolasdrosatos@gmail.com for log in info and then input the info provided to you to https://venum-mma-store.herokuapp.com/admin/login/.

## Database schema

**Profile App**

| Name             | DB KEY                  | Field Type   | Validation                                      |
| ---------------- | ----------------------- | ------------ | ----------------------------------------------- |
| Phone Number     | default_phone_number    | CharField    | max_length=20, null= True, blank =True          |
| Street Address 1 | default_street_address1 | CharField    | max_length=80, null= True, blank =True          |
| Street Address 2 | default_street_address2 | CharField    | max_length=80, null= True, blank =True          |
| Town or City     | default_town_or_city    | CharField    | max_length=40, null= True, blank =True          |
| County           | default_county          | CharField    | max_length=80, null= True, blank =True          |
| Postcode         | default_postcode        | CharField    | max_length=20, null= True, blank =True          |
| Country          | default_country         | CountryField | blank_label ='Country', null = True, blank=True |

**Contact App**

| Name       | DB KEY     | Field Type    | Validation                                |
| ---------- | ---------- | ------------- | ----------------------------------------- |
| First Name | first_name | CharField     | max_length=200                            |
| Last name  | last_name  | CharField     | max_length=200                            |
| From email | from_email | CharField     | max_length=200                            |
| Subject    | Subject    | CharField     | max_length=200                            |
| Message    | message    | TextField     | max_length=5000                           |
| Date       | date       | DateTimeField | default=datetime.now, blank=True          |
| User       | query_user | ForeignKey    | User, null=True, on_delete=models.CASCADE |

**Product App**

| Name        | DB KEY      | Field Type   | Validation                                                   |
| ----------- | ----------- | ------------ | ------------------------------------------------------------ |
| Category    | category    | ForeignKey   | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| SKU         | sku         | CharField    | max_length=254, null=True, blank=True                        |
| Name        | name        | CharField    | max_length=254                                               |
| Description | description | TextField    |                                                              |
| Has Sizes   | has_sizes   | BooleanField | default=False, null=True, blank=True                         |
| Price       | price       | DecimalField | max_digits=6, decimal_places=2                               |
| Rating      | rating      | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True        |
| Image Url   | image_url   | URLField     | max_length=1024, null=True, blank=True                       |
| Image       | image       | ImageField   | null=True, blank=True                                        |

**Categories**

| Name          | DB KEY        | Field Type | Validation                              |
| ------------- | ------------- | ---------- | --------------------------------------- |
| Name          | name          | CharField  | max_length=254                          |
| Friendly Name | friendly_name | CharField  | max_length=254, null= True, blank =True |

**Events**

| Name       | DB KEY     | Field Type | Validation                             |
| ---------- | ---------- | ---------- | -------------------------------------- |
| Name       | name       | CharField  | max_length=20, null= True, blank =True |
| Day        | day        | DateField  | max_length=80, null= True, blank =True |
| Start Time | start_time | TimeField  | max_length=80, null= True, blank =True |
| Location   | location   | CharField  | max_length=40, null= True, blank =True |
| Image url  | image_url  | URLField   | max_length=80, null= True, blank =True |
| Image      | image      | ImageField | max_length=20, null= True, blank =True |

## Technologies

- SQlite3
- PostgreSQL
- Django
- GIT POD
- Git Hub
- Heroku
- AWS S3 Bucket

**Front End**

- HTMI5
- CSS3
- JavaScript, Jquery
- Bootstrap
- Font awesome
- Google fonts
- Bulma

**Back End**

- Python
- Allauth
- Stripe
- Webhooks
- Crispy-forms
- Pillow 4.3.0
- Jinja
- Boto3
- Gunicorn
- Psycopg2

## Testing

- This web application was physically tested for display as well as gameplay across multiple browsers (Chrome, Safari, FireFox, Opera) and on multiple mobile devices using Google developer tool(iPad, iPad Pro, iPhone X, iPhone 6/7/8 (Plus), iPhone 5/SE, Pixel 2 (XL), Galaxy S5).
- The site is compatible and responsive in all of the above.
- I have tested for layout, functionality and responsive interactivity and it all runs smooth.
- I have also tested webhooks and stripe payments using the test credit card info provided by stripe and it works perfectly.
- I have run the python3 -m flake8 in order to view all problems of the project in a single list. I had two types pop up: E501 line too long and DJ01. As far as E501 goes I have corrected the ones that are possible to be corrected. In some cases it's just not possible to fix the line too long issues. If I was to break that line up for example it would break the variable. The DJ01 ones I ignored as instructed by the tutors.

## Validation

- HTML: All html code was validated at https://validator.w3.org/ .

- CSS: All css code was validated at https://jigsaw.w3.org/css-validator/.

- JavaScript: All JS code was validated at https://jshint.com/ .

## Development

- I used Gitpod for a developer tool (IDE) in this project.

## Known issues

- The toasts and messages need to be worked on since they appear at the top right under the bag app regardless of which app they may concern. Also I noticed that if the bag has items in it and I add somethign to my wishlist, the correct message does show but the bag dropdown also is activated, which may cause a customer to believe that the product was actually added to the bag also (which is not the case).
- Wishlist does persist when user closes the session but does not if user logs out and relogs. I have to make the wishlist persistent even after logout by adding to the models of the app in order to store them in the database.
- Banner for free delivery threshold appears in all pages which is not suitable and proper and should not do so. For instance there is no need to include the banner in the contact or events page as these pages do not concern the delivery or purchase of a product directly.

## Deployment

All requirements to run and execute project are included in requirements.txt. If you would like to clone the project press clone in the github project directory and the following command is required to install all requirements to your own workspace: 
• - pip3 install -r requirements.txt

- Note that gitpod was used to develop this project so if you are using a different IDE the command may vary.
- After cloning the project to your workspace make sure to run the makemigrations and migrate command.
- Remember to include the variables below to your IDE's setting or even an env file.
- Run the create super user command in order to create a super user for your project.
- Run the server.

**Variables**

The following variables were added to GITPOD's settings as well as the config vars in heroku settings. These details are not provided for public view.

SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
DATABASE_URL  
ADMINS_EMAIL
EMAIL_HOST_PASS
EMAIL_HOST_USER

**I took the following steps to remotely deploy my project on heroku:**
- I created a Heroku app,  on Heroku.com. 
- I gave the app a name that is unique and chose Europe as the region.
- In the deployment method section of the apps deploy tab on heroku, I selected the option GitHub connect to Github.
- I made sure my github profile was displayed when I pressed the Github connect to github button and wrote the repository's name before clicking search.
- Once the repo was found I clicked connect.

- Since I have  my environment variables in my gitpod settings, heroku won't be able to read them. So I had to tell heroku which vars are required:

SECRET_KEY - secret key used for your Django project
STRIPE_PUBLIC_KEY - provided in Stripe account
STRIPE_SECRET_KEY - provided in Stripe account
STRIPE_WH_SECRET - provided in Stripe account
DATABASE_URL  - Heroku Postgres database url
ADMINS_EMAIL - Used this to hide the actual adress from the project. Any adress will work.
AWS_ACCESS_KEY_ID - provided by amazons aws
AWS_SECRET_ACCESS_KEY - provided by amazons aws
EMAIL_HOST_PASS - created in Gmail using two-step authentication by creating an App password for a Django app in Gmail's Google Account Security page. Sends real emails.
EMAIL_HOST_USER - created in Gmail using two-step authentication by creating an App password for a Django app Gmail's Google Account Security page. Sends real emails.
USE_AWS - set to true

- I run following commands before deployment on my workspace's terminal:
pip3 freeze –local > requirements.txt, this command will create a requirements file which is required by heroku to install requirements before deploying project.
echo web: python app.py > Procfile This will create a Procfile. The Procfile is required by Heroku as the entry point for the project.
- I logged in to heroku through my workspace by running heroku login -i.
- I linked my Heroku app to my remote repository by running heroku git:remote -a venum-mma-store.
- Last but not least I run git push heroku master.

- Everything worked perfectly and the project was deployed and remotely updated every time I add and commit changes and run git push heroku.

## Features not yet added

- Make wishlist persistent after logout, currently it persists if session is closed but not if user logs out and relogs.
- Add review section for customers to add reviews.
- Allow customers to rate each and every product.
- Correct toasts and messages accuracy that is mentioned in the testing section above.
- Login via social media like insta, fb, etc.

### Acknowledgements and credits

- [Code Institute](https://www.codeinstitute.net/) I have learned a good chunck of the front and back end (html, css, js and python code) by following code institue's boutiqe Ado tutorials. I have adjuste alot to make the project my own and fit the aesthetics I find suitable, and I have also added to custom apps (contact and events) with two custom models.
- The images, prices, description used in the project were taken from Venum's official website. I do not own any of the right, I used them strictly for educational purposes.
- Icons are all from font awesome while the font is from google fonts.
- The events sponsored are fictional but the company that is supposedly sponsored is UFC.
- I leard how a contact app works in [learndjango.com](https://learndjango.com/tutorials/django-email-contact-form). I added to the view and models in order to satisfy the projects requirements and also better serve the functionality of the site for both admin and customers. I also received lots of help on both Contact and events app on slack from fellow students and tutors.
- Tutors Haley, Igor and Roman held my hand and helped me debug, deploy, set up aws, stripe, webhooks, get contact and admin apps to work and much more.
- Slack: My fellow students in Slack helped me debug and correct mistakes that are too many to mention in this readme: Anything from indentation, use of os variables like admins_email instead of the actual email adress in the code, to proper format of code and debuging of numerous E501 errors.
  **NOTE that I am in no way affiliated to either VENUM or UFC. This project is for educational purposes only and the store is a fictional business. All rights are reserved by VENUM.**
