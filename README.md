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
    + [Feature 6 Profile Page](#feature-6-profile-page)
      - [Description feature 6](#description-feature-6)
      - [User Stories feature 6](#user-stories-feature-6)
    + [Feature 7 Product Management](#feature-7-product-management)
      - [Description feature 7](#description-feature-7)
      - [User Stories feature 7](#user-stories-feature-7)
    + [Feature 8 Bag and Checkout](#feature-8-bag-and-checkout)
      - [Description feature 8](#description-feature-8)
      - [User Stories feature 8](#user-stories-feature-8)
    + [Feature 9 Admin](#feature-9-admin)
      - [Description feature 9](#description-feature-9)
      - [User Stories feature 9](#user-stories-feature-9)
    + [Feature 10 Favorites](#feature-10-favorites)
      - [Description feature 10](#description-feature-10)
      - [User Stories feature ](#user-stories-feature-10)
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

#### Physical Database model

- This model contains all fields stored in the database collections and their data type and mimics the structure of what is actually stored in the Postgres database
<br>![Database model](/readme-images/data_schema.png)


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


## Scope
### User Stories Customer
The user stories for the regular user eg: "shopper user" (a potential or existing customer) are described as follows: 
- User Story 1.1: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, and shopping bag icons on a desktop device
- User Story 1.2: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, and shopping bag icons on a mobile/tablet device
- User Story 1.3: As a regular user not logged in, I see a Register/Login link under the My Account dropdown
- User Story 1.4: As a regular logged in, I am brought to the Favourites page if I click on the Favourites icon
- User Story 1.5: As a regular user logged in/not logged in, I am brought to my shopping bag if I click on the Bag icon
- User Story 1.6: As a regular/admin user logged in, I see a "My Profile"/Logout under the My Account dropdown
- User Story 1.7: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
- User Story 1.8: As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
- User Story 1.9: As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
- User Story 1.10: As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
- User Story 1.11: As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
- User Story 1.12: As a regular/admin user I can click on the "Candles" filter, and filter by soy or beewax
- User Story 1.13: As a regular/admin user I can click on the "Soaps" filter, and filter by solid or liquid
- User Story 1.14: As a regular/admin user if I encounter an error on the site, I will be navigated to the 404 error page
- User Story 2.1: As an admin/regular user four text messages are displayed with icons regarding delivery, packaging, dispatch and knowledge
- User Story 2.2: As a regular user the footer is displayed with a logo, product links(Candles,Soaps), website links(About, All products)
- User Story 3.1: As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
- User Story 3.1: As a regular user I will receive an email to verify my account after registering
- User Story 3.1: As a regular user I can log in to my account once I click on the verification link in the email I receive regarding my registration
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 5.1: As a regular user I can view the products page with product count and with each product image, title, category, price
- User Story 5.2: As a regular user I can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- User Story 5.3: As a regular user if I click on a product I will be navigated to the product detail page
- User Story 5.4: As a regular user I can view the product image, description, colour, code, rating, category
- User Story 5.5: As a regular user I can click on the Keep Shopping button on the product detail page, and it will navigate the user to the products page
- User Story 5.6: As a regular user I can set the product quantity for a product (one plus/minus)
- User Story 9.1: As a regular user I can view my order history(Order Number, Date, Items and Order Total)
- User Story 9.2: As a regular user I can click on an order number to view the order information (Order number, Order date/time, Full Name, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)
- User Story 10.1: As a regular user I can click on a product, set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed, and a toast will be displayed with the bag contents
- User Story 10.2: As a regular user I can click on the bag icon, I will be brought to my bag. If there are no items in the bag, a message will be displayed
- User Story 10.3: As a regular user I can click on the bag icon, I will be brought to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed
- User Story 10.4: As a regular user I can update the quantity or remove an item from my shopping bag
- User Story 10.5: As a regular user I can click on the Secure Checkout button on the bag page or toast message, and I will be brought to the Checkout page
- User Story 10.6: As a regular user on the checkout page I can set my details(Full Name, email address, both mandatory) and Delivery Information(Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory), which is populated from my profile if filled in
- User Story 10.7: As a regular user on the checkout page if I click "Save this delivery information to my profile", the details entered will be saved on the users profile
- User Story 10.8: As a regular user on the checkout page if I click the Complete Order button, and the transaction is not successful, a message will be displayed
- User Story 10.9: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the user will be navigated to a checkout success page, and an email is sent to the user
- User Story 10.10: As a regular user not logged in, I can add items to my bag and make a purchase

### User Stories Website Owner
The user stories for the website owner(admin/administrator user) are described as follows: 
There is a lot of overlap between the two user types, the admin user has more administrative rights throughout but their roles and responsibilities
are defined
- User Story 1.1: As an admin/regular user the navigation bar is displayed with a logo on all pages with a search box, My account and shopping bag icons on a desktop device
- User Story 1.2: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account and shopping bag icons on a mobile/tablet device
- User Story 1.8: As an admin user logged in, I see a Product Management/News Item Management/My Profile/Logout under the My Account dropdown
- User Story 1.9: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
- User Story 1.10: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage
- User Story 1.11: As an admin user logged in, if I click on Product Management under My Account I am brought to the Product Management(Add Product) page
- User Story 1.12: As an admin user logged in, if I click on News Item Management under My Account I am brought to the News Item Management page
- User Story 1.13: As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
- User Story 1.15: As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
- User Story 1.16: As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
- User Story 1.17: As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
- User Story 1.18: As a regular/admin user I can click on the "Candles" filter, and filter by soy or beewax
- User Story 1.19: As a regular/admin user I can click on the "Soaps" filter, and filter by solid or liquid
- User Story 1.20: As a regular/admin user if I encounter an error on the site, I will be navigated to the 404 error page
- User Story 2.1: As an admin/regular user four text messages are displayed with icons regarding delivery, packaging, dispatch and knowledge
- User Story 2.2: As an admin user logged in the footer is displayed with a logo, product links(Candles and Soaps), website links(Product Management, About)
- User Story 3.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 3.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in
- User Story 4.1: As an admin user I can view the Add product page by clicking on the Product Management link.
- User Story 4.2: As an admin user I can view the Edit product page by clicking on the Edit button on the product. 
- User Story 4.3: As an admin user I can click on a product, and I am navigated to the product detail page. I can edit or delete the product by clicking on the Edit or Delete links on the page
- User Story 5.1: As an admin user I can add a product by clicking on the Product Management link in My Account. I must enter a name, category, price, colour, code, description, has Sizes(Unknown, Yes, No), Rating, Image url, upload an image and click the 
Add Product button. Clicking cancel navigates the user to the product page.
- User Story 5.2: As an admin user I can edit a product by clicking on the Edit button on the Products page for the product. I can update the name, category, price, colour, code, description, feature (1-4), has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, update an image and click the 
Edit Product button. Clicking cancel navigates the user to the product page
- User Story 5.3: As an admin user I can delete a product by clicking on the Delete button on the product. A modal will appearing asking to confirm, and a message displayed once I confirm.
- User Story 6.1: As an admin user I can view users orders in the django admin page and can view order number, date, full name, order total, delivery cost, grand total
- User Story 6.2: As an admin user I can view users orders in the django admin page and can search by order number, full name and filter by order number, full name and order date
- User Story 6.3: As an admin user I can view products in the django admin page and can view a products code, name, category, has sizes, price, presale price, rating, image, image url
- User Story 6.4: As an admin user I can view products in the django admin page and can view search and filter by code, category, name and price
- User Story 6.5: As an admin user I can view users in the django admin page and can view their username, email address, first name, last name
- User Story 6.6: As an admin user I can view categories in the django admin page and can view a category name and friendly name


## Skeleton
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


## Surface
### Color Palette
I have gone for a simple and minimal design for the website, with predominately black, grey, white, and gold colours
There are 4 colours in the color palette
- Black and grey colour for the nav and footer on the website
- White for background
- Gold and grey for text

I believe the colours complement each other, and I choose those colours to give the website the feel of luxury.


### Typography
The Cormorant Garamond font is the main font used throughout the whole website with Sans Serif as the fallback in case the Cormorant Garamond cannot be imported into the website correctly. This font is from the Google fonts library.
![Font](/readme-images/font.png)


# Features
The website has 13 distinct features, and they are described below
What is important to detail is what pages are accessible by the three types of users
1. A customer user not logged into the site
2. A customer user logged into the site
3. An admin user
The navigation buttons update depending on whether a user is logged in or not, and whether that user is the admin:

 Nav Link              |Not logged in  |Logged in as regular user|Logged in as admin
:-------------         |:------------- |:----------------|:------------- |
Home     |&#9989;        |&#9989;          |&#9989; |
Products           |&#9989;        |&#9989;          |&#9989; |
Product Detail           |&#9989;        |&#9989;          |&#9989; |
Product Management(Add Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Edit Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Delete Product)     |&#10060;       |&#10060;         |&#9989; |
My Profile             |&#10060;       |&#9989;          |&#9989; |
Order History         |&#10060;       |&#9989;          |&#9989; |
Log out               |&#10060;       |&#9989;          |&#9989; |
Register               |&#9989;        |&#10060;         |&#10060; |
Log in               |&#9989;        |&#10060;         |&#10060; |
Bag |&#9989;        |&#9989;          |&#9989; |
Checkout |&#9989;        |&#9989;          |&#9989; |
Checkout success |&#9989;        |&#9989;          |&#9989; |


## Existing Features
### Feature 1 Navigation Bar and Homepage
#### Description feature 1
- The homepage consists of a background image and text, a header/nav bar and footer
- The header and footer is consistent across all pages
- The navigation bar is displayed with a logo on all pages with a search box, My account, and shopping bag icons on a desktop device
<br>![Homepage desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/homepage.png)
- The navigation bar is displayed on all pages with a search box, My account, shopping bag icons on a mobile/tablet device
<br>![Homepage tablet](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/homepage_tablet.png)
<br>![Homepage mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/homepage_mobile.png)
- A regular user logged in, I see a "My Profile"/Logout under the My Account dropdown
- An admin user logged in, I see a Product Management/My Profile/Logout under the My Account dropdown
<br>![Homepage admin desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/super_my_account.png)
- On a desktop device there is a number of filters described below: All Products, Candles , Soaps
<br>![Homepage desktop filter price](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/desktop_filter.png)
- If a user encounters an error, the relevant error page is displayed (400, 403, 404 or 500)
<br>![404](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/404_page.png)

### Feature 2 Footer
#### Description feature 2
- A footer is displayed at the bottom of the page
<br>![Footer](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/footer.png)
- The footer contains some text, social media icons(that open in a new tab)

### Feature 3 Register
#### Description feature 3
- A regular user can register for an account.
- The user must provide a valid email address, email address(confirmation), username, password, password confirmation
<br>![Register](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/register.png)
- These 5 fields are  mandatory and a user cannot register the same details twice for an account
<br>![Register error](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/register_error.png)
- A confirmation link is sent to the users email address, they must click on the verification link to verify the account.
<br>![Email content](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/email_confirmation.png)
- Once that is done they can sign in to the website with their username/email address and password

### Feature 4 Login
#### Description feature 4
- An admin/regular user can log in to the website using their username or email address and password
- Both fields are mandatory
- Once logged in the user will be navigated to the homepage
<br>![Login](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/login.png)
- The user must have an account in the system, and they must enter the correct  username or email address and password
- If the user needs to request a password, they can click on the Forgot Password link
<br>![Forgot Password](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/login_error.png)
- They enter their email address, and they are emailed reset their password. Once they do this they can log in

### Feature 5 Products and Product Detail Pages
#### Description feature 5
- A user view the products page with product count and with each product image, title, category, price
<br>![Products Desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/products.png)
<br>![Products Mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/products_mobile.png)
- The user can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- A product detail page displays all the product information (image, description, colour, code, rating, category, description, features and reviews(the latest first))
<br>![Products Detail](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/product_detail.png)

### Feature 6 Profile Page
#### Description feature 6
- A regular user can update their default delivery information as per the user stories below
- A user must be logged in to see their profile page
- This is the information that is displayed when the user is checking out an order
- A user can view and update their Default delivery information
<br>![Default delivery information](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/my_profile.png)
- The user can also view their past orders and click on an order to view the order details

### Feature 7 Product Management
#### Description feature 7
- An admin user can add, edit and delete products
- To add a product the user can click on the Product Management link in My Account
- They must enter a name, category, price, colour, code, description, has Sizes(Unknown, Yes, No), Rating, Image url, upload an image
<br>![Add Product](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/add_a_product.png)
- The product is then added and visible on the products page, and by clicking on the product itself
- The image is stored in the AWS S3 bucket
- An admin user can edit a product, by updating the relevant field(s)
<br>![Edit Product](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/edit_product.png)
- An admin user can delete a product, by clicking on the delete link on the product detail page or the delete button on the products page

### Feature 8 Bag and Checkout
#### Description feature 8
- A user can add items to a bag, if the bag is empty a message is displayed
- A user can update the quantity or remove an item from their shopping bag
<br>![Bag Empty](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/empty_bag.png)
<br>![Bag Desktop](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/bag_desktop.png)
<br>![Bag Mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/bag_mobile.png)
- The user can "checkout" and their details will be displayed.
- The fields are: (Full Name, email address, both mandatory) and Delivery Information: Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory)), which is populated from my profile if filled in
<br>![Checkou](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/checkout.png)
<br>![Checkout mobile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/checkout_mobile.png)
- The user receives a confirmation and also email to their email address supplied
<br>![Order Success](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/order_success.png) 
- The order is available on the user profile page, and they can click on the order itself
<br>![User profile](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/order_available.png)
- A regular user not logged in, I can add items to the bag and make a purchase

### Feature 9 Admin
#### Description feature 9
- As per the user stories below there are a number of admin views that have been configured at https://kandl-ms4.herokuapp.com/admin
- They give excellent CRUD operations to the data in the Postgres database as well as search and filter options
- They are as follows:
- Order
<br>![Order](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/admin_orders.png)
- Products
<br>![Products](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/admin_products.png)
- Users
<br>![Users](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/admin_users.png)
- Categories
<br>![Categories](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/features/admin_categories.png)

### Feature 10 Favorites
#### Description feature 10
- A regular user can add their most loved products to favorites
- A user must be logged in to add the product to favorites
- Add to favorites 
<br>![Add to favorites]()
- Favorites
<br>![Favorites]()

### Feature 11 Contact
#### Description feature 11
- A regular user can contact us for any issue or question
- A user can click on the contact icon, fill the required details, and send us a message.
- Contact 
<br>![Contact]()


##  Features Left to Implement
- I am content with what was implemented, however, here are some additional "nice to have" features and updates that could be added to the project

Number | Update  
 ------------ | ------- |
1 | Add reviews by customers and comments |
2 | A newsletter section |
3 | Improved searching and filtering on the products page, a side panel filter |
4 | Integration with a Continuous Integration application, for example: Travis CI or Semaphore CI |
5 | Improved pagination look/feel on products page |
6 | The functionality to add and display multiple images per product |


# Technologies Used
## Languages 
- HTML (https://en.wikipedia.org/wiki/HTML)
    - The project uses html to build the relevant pages
- CSS (https://en.wikipedia.org/wiki/CSS)
    - The project uses CSS to style the relevant pages
- Javascript (https://www.javascript.com/)
    - Javascript was used for all scripting on the site 
- Django (https://www.djangoproject.com/)
    - Django is the framework used in this project
    - The Django templating language was used to render pages
    - The Django unit test library was used for unit tests (https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
- Python v3.9 (https://www.python.org/)
    - Python was used for server side coding on the project, a number of libraries were also used(The requirements.txt file 
  contains this list):
      - asgiref==3.4.1 (Support for Python asynchronous web apps and servers to communicate with each other) 
      - boto3==1.18.47 (Python SDK for AWS)
      - botocore==1.21.47 (Python SDK for AWS) 
      - dj-database-url==0.5.0 (Support for DATABASE_URL environment variable)
      - Django==3.2.7 (Web framework)
      - django-allauth==0.41.0 (Web framework authentication)
      - django-countries==7.2.1 (ISO 3166 countries list)
      - django-crispy-forms==1.12.0 (Django rendering of forms)
      - django-storages==1.11.1 (Django storage backend for AWS S3)
      - gunicorn==20.1.0 (Python WSGI Http server)
      - jmespath==0.10.0 (Full suite of data driven testcase)
      - oauthlib==3.1.1 (Framework for oauth1 and oauth2)
      - Pillow==8.3.2 (Imaging library)
      - psycopg2-binary==2.9.1 (Postgres adapter)
      - python3-openid==3.2.0 (Support for the OpenID decentralized identity system)
      - pytz==2021.1 (Interface to the IANA database, which uses ASCII name)
      - requests-oauthlib==1.3.0 (Authentication support for Requests)
      - s3transfer==0.5.0 (Python library for managing Amazon S3 transfers)
      - sqlparse==0.4.1 (Non-validating SQL parser for Python)
      - stripe==2.60.0 (SDK for processing payments)

## Libraries and other resources
- Bootstrap 5.0 (https://getbootstrap.com/docs/5.0)
    - The project uses the bootstrap library for some UI components in the website (Buttons, Card, Carousel, Modal, Pagination, Navbar)
- Postgres (https://www.postgresql.org/)
  - The deployed project on Heroku uses a Postgres database
- SQLLite (https://www.sqlite.org/index.html)
  - The database uses in local development was a SQLLite database
- Gitpod (https://gitpod.io/)
    - Gitpod was used as an IDE for the project initially, then I switched to Pycharm
- Pycharm (https://www.jetbrains.com/pycharm/)
    - Pycharm was the main IDE used on the project
- Github (https://github.com/)
    - GitHub was used to store the project code in a repository
- Google Fonts (https://fonts.google.com/)
    - Google font Poppins was used as the website font
- Balsamiq (https://balsamiq.com/)
    - Balsamiq was used to create the website wireframes
- Font Awesome (https://fontawesome.com/)
    - Font awesome was used to provide the relevant fonts/icons for the website
- JQuery (https://jquery.com)
    - JQuery was used in some javascript files for DOM manipulation
- CSS Validation Service (https://jigsaw.w3.org/css-validator/)
   - CSS validation service for validation the css in the project  
- HTML Markup Validation Service (https://validator.w3.org/)   
    - HTML validation service for validation the css in the project  
- Chrome dev tools (https://developers.google.com/web/tools/chrome-devtools)
    - For troubleshooting and debugging of the project code
- Chrome Lighthouse (https://developers.google.com/web/tools/lighthouse)
    - For performance, accessibility, progressive web apps, SEO analysis of the project code
- Responsive Design (http://ami.responsivedesign.is/)
    - Website for generating the responsive image in this README
- Python online interpreter (https://www.programiz.com/python-programming/online-compiler/)
    - For testing python code snippets
- Unittest (https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
    - For Python unit testing
- JSHint (https://jshint.com/)
  - For javascript code quality
- PEP8 (https://www.python.org/dev/peps/pep-0008/)
  - I used the pep8 code analysis plugin in Pycharm to check for pep8 errors
- Stripe (https://www.stripe.com)
  - For processing a test credit card to test a payment as part of an order

# Testing
---

#### HTML Validation

I used [W3C Markup Validation Service](https://validator.w3.org/) to validate the HTML code.

Results here: [HTML](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/tests/HTML.png)
              
#### CSS Validation

I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate the CSS code.

Result here: [CSS](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/tests/CSS.png)

#### Performance

I used [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) to check performance of the website and it passes with scores between 90 and 100 on all pages on all 4 criterias Performance/ Accesibility/ Best Practices/ SEO. However on my maschine, I had a problem with the lighthouse app wich didn't displayed one of the criteria properly. I contacted tutors, they said that from theyr part everything is ok and it's not a problem of coding, and I got this photo from them.

Results here: [Lighthouse](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/tests/lighthouse_home.png)
              [Tutor](https://github.com/robertdavid1205/ms4-kandl/blob/main/readme-images/tests/tutor_lighthouse.png)

#### Performed tests on:

* HP Envy
* Iphone SE
* Samsung Galaxy A52
* Samsung Galaxy Tab S6

##### Tests performed:

1. Page links and icons redirect the user to the corect place on both desktop and mobile versions.
2. The pages scrollable in mobile and tablet views.
3. Nav bar links are able to redirect users to the correct page and there are no broken links.
4. In the case of an incorrect URL, the user is redirected to a 404 page wich will direct them back to the home page. 
5. The login page works correctly.
6. The register page works correctly.
7. All the buttons function correctly.

##### Results:

* All the devices passed all tests.

#### Testing user stories
---
1. As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, and shopping bag icons on a desktop device
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on the icons from the navbar of the site</td>
            <td>To find out information about the site</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user1.png)

2. As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, and shopping bag icons on a mobile/tablet device
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on the icons from the navbar of the site</td>
            <td>To find out information about the site</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user2.png)

3. As a regular user not logged in, I see a Register/Login link under the My Account dropdown
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on the my account button on the navbar</td>
            <td>To find register/login link</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user3.png)

4. As a regular logged in, I am brought to the Favourites page if I click on the Favourites icon
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on the my profile button under my account button on the navbar</td>
            <td>To find my favourites</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 

5. As a regular user logged in/not logged in, I am brought to my shopping bag if I click on the Bag icon
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on the shopping bag button on the navbar</td>
            <td>To find my shopping bag</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user5.png)

6. As a regular/admin user logged in, I see a "My Profile"/Logout under the My Account dropdown
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on my account button on the navbar</td>
            <td>To find logout button</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user6.png)

7. As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on my profile button under my account button on the navbar</td>
            <td>To find my profile page</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user7.png)

8. As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on kandl perfect candles button on the navbar</td>
            <td>To find homepage</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user8.png)

9. As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on  by price button under the all products button on the navbar</td>
            <td>To find the products sorted by price</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user9.png)

10. As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on  by rating button under the all products button on the navbar</td>
            <td>To find the products sorted by rating</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user10.png)

11. As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on  by category button under the all products button on the navbar</td>
            <td>To find the products sorted by category</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user11.png)

12. As a regular/admin user I can click on the "Candles" filter, and filter by soy or beewax
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on  candles button on the navbar</td>
            <td>To find the candles sorted by soy or beeswax</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user12.png)

13. As a regular/admin user I can click on the "Soaps" filter, and filter by solid or liquid
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>Click on soaps button on the navbar</td>
            <td>To find the candles sorted by solid or liquid</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user13.png)

14. As a regular/admin user if I encounter an error on the site, I will be navigated to the 404 error page
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>misstype the address</td>
            <td>To be redirected to the 404 page</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user14.png)

15. As an admin/regular user four text messages are displayed with icons regarding delivery, packaging, dispatch and knowledge
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>order a product, and pay for the product</td>
            <td>To see the text messages displaying info about your order</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user15.png)

16. As a regular user the footer is displayed with the copyright text, website links(socials)
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>See the footer</td>
            <td>To see the copyright text and the website links(socials)</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user16.png)

17. As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on the register button under the my account button</td>
            <td>To see  register on the website by providing an email address, email address(confirmation), username, password, password confirmation</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user17.png)

18. As a regular user I will receive an email to verify my account after registering
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>register as a new user with a email address</td>
            <td>To receive the confirmation email</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user18.png)

19. As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click login button under the my account button, enter your username and password</td>
            <td>To login and see confirmation message displayed</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user19.png)

20. As a regular user I can view the products page with product count and with each product image, title, category, price
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click all products button</td>
            <td>get redirected to all products page and see product count, each product image, title, category, price</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user20.png)

21. As a regular user I can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on sort by button on all products page</td>
            <td>to sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user21.png)

22. As a regular user if I click on a product I will be navigated to the product detail page
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on any product</td>
            <td>get redirected to the product detail page</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user22.png)

23. As a regular user I can click on the Keep Shopping button on the product detail page, and it will navigate the user to the products page
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on keep shopping button</td>
            <td>get redirected to the products page</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user23.png)

24. As a regular user I can set the product quantity for a product (one plus/minus)
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on + / - button on the product detail page</td>
            <td>set the product quantity for a product (one plus/minus)</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user24.png)

25. As a regular user I can view my order history(Order Number, Date, Items and Order Total)
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on my profile button under the my account button</td>
            <td>view my order history(Order Number, Date, Items and Order Total)</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user25.png)

26. As a regular user I can click on an order number to view the order information (Order number, Order date/time, Full Name, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on any order in my profile page</td>
            <td>view the order information (Order number, Order date/time, Full Name, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user26.png)

27. As a regular user I can click on a product, set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed, and a toast will be displayed with the bag contents
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on add to bag for any product</td>
            <td>set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed, and a toast will be displayed with the bag contents</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user27.png)

28. As a regular user I can click on the bag icon, I will be brought to my bag. If there are no items in the bag, a message will be displayed
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on my bag button in the navbar</td>
            <td>get redirected to my bag page. If there are no items in the bag, a message will be displayed</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user28.png)

29. As a regular user I can click on the bag icon, I will be brought to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on my bag button in the navbar</td>
            <td>get redirected to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user29.png)

30. As a regular user I can update the quantity or remove an item from my shopping bag
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on + / - buttons on my bag page</td>
            <td>to update the quantity or remove an item from my shopping bag</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user30.png)

31. As a regular user I can click on the Secure Checkout button on the bag page or toast message, and I will be brought to the Checkout page
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on secure checkout button on my bag page</td>
            <td>to be redirected to the Checkout page</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user31.png)

32. As a regular user on the checkout page I can see my details(Full Name, email address, both mandatory) and Delivery Information(Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory), which is populated from my profile if filled in
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on my profile button under the my account button</td>
            <td>to set my details(Full Name, email address, both mandatory) and Delivery Information, which is populated from my profile if filled in</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user32.png)

33. As a regular user on the checkout page if I click "Save this delivery information to my profile", the details entered will be saved on the users profile
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on "Save this delivery information to my profile" in the checkout page</td>
            <td>to save details entered to the users profile</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user33.png)

34. As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the user will be navigated to a checkout success page, and an email is sent to the user
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on "complete order" button in the checkout page</td>
            <td>be navigated to a checkout success page, and an email is sent to the user</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user34.png)

35. As a regular user not logged in, I can add items to my bag and make a purchase
  <table>
        <tr>
            <th>Feature</th>
            <th>Action</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
        </tr>
        <tr>
            <td>Home Page</td>
            <td>click on "add to bag" button in the product detail page</td>
            <td> to add items to my bag and make a purchase</td>
            <td>Works as expected</td>
        </tr>
  </table> 
 
&nbsp;[Screenshot](/readme-images/testing_user_stories/user35.png)


#### Browser compatibility

* *Google Chrome*: Website and user stories work as expected.
* *Safari*: Website and user stories work as expected.
* *Microsoft Edge*: Website and user stories work as expected.
* *Firefox*: Website and user stories work as expected.


# APIs and configuration
The project also uses a number of API's and configuration, below are the steps to configure the API in your environment

## Google emails
To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
2. Turn on 2-step verification and follow the steps to enable
3. Click on app passwords, select Other as the app and give the password a name, for example Django
4. Click create and a 16 digit password will be generated, note the password down
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
7. Set and confirm the following values in the settings.py file to successfully send emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>
8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

## Stripe
1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in
3. Under Developers, click on the API keys section
4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>
6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://kandl-ms4.herokuapp.com/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting

# Deployment
There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

## Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket named "ci-ms4-rugby-shop"
3. Uncheck the "Block All Public access setting"
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit
5. Enable the setting, and set the index.html and the error.html values
6. In the Permissions section, click edit on the CORS configuration and set the below configuration
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)
8. In the permissions section, click edit on the Access control list(ACL)
9. Set Read access for the Bucket ACL for Everyone(Public Access)
10. The bucket is created, the next step is to open the IAM application to set up access
11. Create a new user group named "ci-ms4-rugby-shop"
12. Add the "AmazonS3FullAccess" policy permission for the user group
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource"
16. Give the policy a name and click "Create Policy"
17. Add the newly created policy to the user group
18. Go to Users and create a new user
19. Add the user to the user group
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup
22. The user is now created with the correct user group and policy
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files 


## Local Deployment
To run this project locally, you will need to clone the repository
1. Login to GitHub (https://wwww.github.com)
2. Select the repository robertdavid1205/ms4-kandl
3. Click the Code button and copy the HTTPS url, for example: https://github.com/robertdavid1205/ms4-kandl
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/robertdavid1205/ms4-kandl```

5. The repository will now be cloned in your workspace
6. Create an env.py file(do not commit this file to source control) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<br><code>import os</code>
<br><code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_PUBLIC_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_SECRET_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_WH_SECRET", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("AWS_ACCESS_KEY_ID", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("AWS_SECRET_ACCESS_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("EMAIL_HOST_USER", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("EMAIL_HOST_PASS", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("USE_AWS", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("DATABASE_URL", TO BE ADDED BY USER)</code>
7. Some values for the environment variables above are described in different sections of this readme
8. Install the relevant packages as per the requirements.txt file
9. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
10. Ensure debug is set to true in the settings.py file for local development
11. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
12. Run "python3 manage.py showmigrations" to check the status of the migrations
13. Run "python3 manage.py migrate" to migrate the database
14. Run "python3 manage.py createsuperuser" to create a super/admin user
15. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
16. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
17. Run "python3 manage.py loaddata news.json" on the news file in news/fixtures to create the news items(optional)
18. Start the application by running <code>python3 manage.py runserver</code>
19. Open the application in a web browser, for example: http://127.0.0.1:8000/

## Heroku and Postgres Database
To deploy this application to Heroku, run the following steps.
1. Create an account at heroku.com
2. Create an app, give it a name for example ms4-kandl, and select a region
3. Under resources search for postgres, and add a Postgres database to the app    
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
5. Install the plugins dj-database-url and psycopg2-binary.
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text: web: gunicorn rugby_shop.wsgi:application for example
8. In the settings.py ensure the connection is to the Heroku postgres database
9. Ensure debug is set to false in the settings.py file
10. Add localhost/127.0.0.1, and ms4-kandl.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
15. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
16. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
17. From the CLI login to Heroku using the command heroku git:remote -a ci-ms4-loverugby
18. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-ms4-loverugby
19. Push the code to Heroku using the command git push heroku master
20. Connect the app to GitHub, and enable automatic deploys from main
21. Click deploy to deploy your application to Heroku for the first time
22. Click on the link provided to access the application
23. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

# Credits
- The project is based on the Boutique Ado project by the Code Institute and was used as a basic for my project (https://github.com/Code-Institute-Solutions/boutique_ado_v1/)
- I used html/css code from bootstrap then tweaked it accordingly for the site footer.
- For the shop button in the home page I used and tweaked some code from https://cssbuttons.io/

# Content
- Font Awesome (http://fontawesome.com)    
    - The icons used on the site from font awesome
- Fonts (https://fonts.google.com/)    
    - The text font(Poppins) is from Google fonts

<br>

# Media
- Photos taken from https://neomorganics.eu/
- Background photo made by George Chipuc
 <br>

# Acknowledgements
- I would like to thank to all the tutors who helped me with the problems I had during the process, and my mentor Mo Shami for his input, help and feedback.
