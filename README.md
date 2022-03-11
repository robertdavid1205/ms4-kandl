# Kandl
Kandl is an ecommerce website that allows users to purchase hand made natural candles and soaps, developed for Milestone 4 as part of the Code Institute - Diploma in Software Development (Full stack) course.

- There are two types of users, and I have set up accounts for both
    - An admin(administrator) user account has been set up with username/password of rocoboco55/Primafirma100da
    - A regular(shopper) user account has been set up with username/password of testtest1/test2022
    - When making a payment as a regular user, a test credit card of 4242424242424242 has been set up for the card number
    - For the expiry date, cvc and postal code any series number(s) can be used(once they meet the mimimum values)
<br>

**View the live site [here](https://kandl-ms4.herokuapp.com/)**
<br><br>
![Responsive site example](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/responsive-demo.png)

# Table of Contents
- [Kandl shop](#love-rugby-shop)
- [Project Overview](#project-overview)
- [UX](#ux)
  * [Strategy](#strategy)
    + [Primary Goal](#primary-goal)
  * [Structure](#structure)
    + [Website pages](#website-pages)
    + [Code Structure](#code-structure)
    + [Database](#database)
      - [Models](#models)
        * [User Model](#user-model)
        * [UserProfile Model](#userprofile-model)
        * [Order Model](#order-model)
        * [OrderLineItem Model](#orderlineitem-model)
        * [Product Model](#product-model)
        * [Category Model](#category-model)
  * [Scope](#scope)
    + [User Stories Potential or Existing Customer](#user-stories-potential-or-existing-customer)
    + [User Stories Website Owner](#user-stories-website-owner)
  * [Wireframes](#wireframes)
  * [Surface](#surface)
    + [Color Palette](#color-palette)
    + [Typography](#typography)
- [Features](#features)
  * [Existing Features](#existing-features)
    + [Feature 1 Navigation Bar and Homepage](#feature-1-navigation-bar-and-homepage)
      - [Description feature 1](#description-feature-1)
      - [User Stories feature 1](#user-stories-feature-1)
    + [Feature 2 Footer](#feature-2-footer)
      - [Description feature 2](#description-feature-2)
      - [User Stories feature 2](#user-stories-feature-2)
    + [Feature 3 Register](#feature-3-register)
      - [Description feature 3](#description-feature-3)
      - [User Stories feature 3](#user-stories-feature-3)
    + [Feature 4 Login](#feature-4-login)
      - [Description feature 4](#description-feature-4)
      - [User Stories feature 4](#user-stories-feature-4)
    + [Feature 5 Products and Product Detail Pages](#feature-5-products-and-product-detail-pages)
      - [Description feature 5](#description-feature-5)
      - [User Stories feature 5](#user-stories-feature-5)
    + [Feature 6 Sale items page](#feature-6-sale-items-page)
      - [Description feature 6](#description-feature-6)
      - [User Stories feature 6](#user-stories-feature-6)
    + [Feature 7 Favourites page](#feature-7-favourites-page)
      - [Description feature 7](#description-feature-7)
      - [User Stories feature 7](#user-stories-feature-7)
    + [Feature 8 News Page](#feature-8-news-page)
      - [Description feature 8](#description-feature-8)
      - [User Stories feature 8](#user-stories-feature-8)
    + [Feature 9 Profile Page](#feature-9-profile-page)
      - [Description feature 9](#description-feature-9)
      - [User Stories feature 9](#user-stories-feature-9)
    + [Feature 10 Product Management](#feature-10-product-management)
      - [Description feature 10](#description-feature-10)
      - [User Stories feature 10](#user-stories-feature-10)
    + [Feature 11 News item Management](#feature-11-news-item-management)
      - [Description feature 11](#description-feature-11)
      - [User Stories feature 11](#user-stories-feature-11)
    + [Feature 12 Bag and Checkout](#feature-12-bag-and-checkout)
      - [Description feature 12](#description-feature-12)
      - [User Stories feature 12](#user-stories-feature-12)
    + [Feature 13 Admin](#feature-13-admin)
      - [Description feature 13](#description-feature-13)
      - [User Stories feature 13](#user-stories-feature-13)
  * [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Libraries and other resources](#libraries-and-other-resources)
- [Testing](#testing)
- [APIs and configuration](#apis-and-configuration)
  * [Stripe](#stripe)
- [Deployment](#deployment)
  * [Amazon WebServices](#amazon-webservices)
  * [Local Deployment](#local-deployment)
  * [Heroku and Postgres Database](#heroku-and-postgres-database)
- [Credits](#credits)
- [Content](#content)
- [Media](#media)
- [Acknowledgements](#acknowledgements)



# Project Overview
- This project is a website made for Code Institute - Diploma in Software Development (Full stack) course - milestone project 4.
- The website is deployed using Heroku pages at the following url: [Kandl](https://kandl-ms4.herokuapp.com/)
- The repository that contains the website source code: [Code Repository](https://github.com/robertdavid1205/ms4-kandl)
- The website was built with a responsive look and feel for desktop, tablet and mobile devices.


# UX
## Strategy
### Primary Goal
The primary goal of the website from site owners perspective is:
- To add, edit and delete products on the website, with the relevant information (price, description, rating, image, sizes and category) 
- To allow a user make a purchase of the products on the website
- To categorise sale items on the website

The primary goal of the website from site users perspective is:
- View a list of products on the website
- To register for an account on the website and receive an email after successful registration
- To login or logout from the website
- Search for a product by name or description and view the search results
- Have a personalised user profile with my delivery, payment information and order history
- View an individual product detail(price, description, rating, comments, image, sizes and category)
- To add an item to a shopping bag, and select the quantity and size if applicable
- Complete a purchase of items in a shopping bag
- To sort the list of available products by rating, price and category


## Structure
### Website pages
- I have structured the website into over 20 pages, each with clear, concise structure, information and purpose. I use the Bootstrap grid system throughout, which gave a consistent structure and responsive design "out of the box"
- Below are the main page's/features functionality wise, there are some others for password reset/verification etc. that are described in the user story section 
- All pages have a common look and feel and a common header/footer. On a tablet/mobile the look and feel is slightly different with a burger menu
- These pages are described in more detail in the user stories section

Page            |Description
:-------------         |:------------- 
Home     |The homepage consists of a background image and text about what we sell, and a button.    
Products           | The products page displays the products(image, price, rating) in a paginated way.  
Product Detail           | The product detail page displays the product image, description, price, add to bag buttons.   
Product Management(Add Product)     | A product can be added to the website.    
Product Management(Edit Product)     | A product can be edited to the website.     
Product Management(Delete Product)     | A product can be deleted from the website.    
My Profile             |The users profile(delivery information) and previous orders is displayed.       
Log out               | A logout button is provided under the My Account link to logout.
Register               | A user can register an account on the site with a valid email address.
Log in               | A user can login with a valid username and password.
Bag | A user can add products to a shopping bag which contains each item in the order and an overall price/delivery if applicable.   
Checkout | A user can enter their delivery details and credit card information to checkout an order.   
Checkout success | Once an order is successful, the user can view the checkout success.


### Code Structure
The project is divided into a number of apps, and built using the Django Framework
The project was built on the Boutique Ado project, that was part of the project content
The apps are :
- bag (part of Boutique Ado project): This app contains functionality regarding users shopping bag
- checkout (part of Boutique Ado project): This app contains functionality regarding users checking out and payment of an order
- home (part of Boutique Ado project): This app contains functionality regarding the users home page
- products (part of Boutique Ado project): This app contains functionality regarding a product.
- profiles (part of Boutique Ado project): This app contains functionality regarding users profile and order history

There are also:
- manage.py: Main python file for starting the website
- README.md: Readme documentation
- Procfile: To run the application
- ms4_kandl: Containing settings.py(Settings) and urls.py(Website urls) for example
- templates: Containing the base.html, about.html, allauth(django authentication) and includes html files
- static: Base css and Javascript files(toast and send_email)
- Requirements.txt: Containing the python libraries installed
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings


### Database
- The website is a data-centric one with html, javascript, css used with the bootstrap(version 4) framework as a frontend
- The backend consists of Python, with the Django framework and a database of Postgres for the deployed Heroku version.


#### Models
- The following models were created to represent the database model structure for the website

##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined

##### UserProfile Model
- The UserProfile model has a one-to-one relationship with User
- The model contains the following fields: default_phone_number, default_street_address1, default_street_address2
  default_town_or_city, default_county, default_postcode and default_country

##### Order Model
- The Order model contains information about orders made on the website.
- It contains UserProfile as a foreign-key.
- The model contains the following fields: order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1
, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid

##### OrderLineItem Model
- The OrderLineItem model contains information about an entry in an order, for orders made on the website.
- It contains Order and Product as foreign-keys.
- The model contains the following fields: order, product, product_size, quantity, lineitem_total

##### Product Model
- The Product Model represents a product and its details
- It contains Category as a foreign-key
- The model contains the following fields: name, category, price, colour, code, description, feature1, has_sizes, rating, image_url, image
- The image field contains the product image
- The image_url field contains the url to where the image file is physically stored, for example AWS S3 bucket

##### Category Model
- The Category model contains a product category
- The model contains the following fields: name, friendly_name


### Wireframes 
---
1. Home
* [mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/home_mobile.png)
* [tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/home_tablet.png)
* [desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/home_desktop.png)

2. Products
* [mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/products_mobile.png)
* [tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/products_tablet.png)
* [desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/products_desktop.png)

3. Products Detail
* [mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/products_detail_mobile.png)
* [tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/products_detail_tablet.png)
* [desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/products_detail_desktop.png)

4. Shopping Bag
* [mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/shopping_bag_mobile.png)
* [tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/shopping_bag_tablet.png)
* [desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/shopping_bag_desktop.png)

5. Checkout
* [mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/checkout_mobile.png)
* [tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/checkout_tablet.png)
* [desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/checkout_desktop.png)

6. Sign Up
* [mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/signup_mobile.png)
* [tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/signup_tablet.png)
* [desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/signup_desktop.png)

5. Log In
* [mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/login_mobile.png)
* [tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/login_tablet.png)
* [desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/wireframes/login_desktop.png)