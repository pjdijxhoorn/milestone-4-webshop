# Happy Bonsai

View the live website here. [link](https://happy-bonsai.herokuapp.com/)

Happy Bonsai was designed, built and deployed by Paul Dijxhoorn as his final project to achieve his full-stack development diploma of Code institute. The purpose of this website is to show the acquired skills of Paul during this course. This website is designed to give users a smooth and effortless shopping experience. Specifically aimed at customers who enjoy the beauty of nature and tranquility. The website is not designed with a particular device in mind and will work well on phone tablet and pc.

![A image that shows how the website looks on different devices.]()

## Table of contents
1. [UX](#ux)
    - 1.1 [Goals](#goals)
        - 1.1.1 [Visitor Goals](#visitor-goals)
        - 1.1.2 [Business Goals](#business-goals)
    - 1.2 [User Stories](#user-stories)
    - 1.3 [Design Choices](#design-choices)
        - 1.3.1 [Color scheme](#color-sheme)
        - 1.3.2 [Typography](#Typography)
        - 1.3.3 [Imagery](#Imagery)
    - 1.4 [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Shop Page](#ashop-page)
        - [Listing Detail Page](#listing-detail-page)
        - [About Page](#about-page)
        - [Frequently Asked Questions Page](#frequently-asked-questions-page)
        - [Contact Page](#contact-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Account Page](#account-page)
        - [Log out Page](#log-out-page)
        - [Cart Page](#cart-page)
        - [Checkout](#checkout)
        - [Terms and Conditions / Privacy Policy pages](#terms-and-conditions-privacy-policy-pages)
    - [Features for Future Releases](#features-for-future-releases)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [Products App Model](#products-app-model)
        - [Cart App Models](#cart-app-models)

4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Frameworks](#Frameworks)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

5. [Testing](#testing)
    - See separate [TESTING.md](TESTING.md) file.
    

6. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)
    - [disclaimer](#disclaimer)
    - [reflection](#reflection)

8. [Contact](#contact)


##  UX
### Goals
#### Visitor Goals 

The central target audience for Happy Bonsai are:
- People who enjoy nature.
- People who have interest for japanese culture.
- People who are searching for a unique gift.
- People who are looking for beautiful in or outdoor  plants 

Users goals are:
- Find a unique gift  
- Enjoy looking at all the beautiful bonsai
- Easily navigate the site
- Buy from a trustworthy site


The Happy Bonsai webshop is a amazing way to meet these needs because: 
- The products can be found easily by category, price, rating, name. by using the text search products can be found by name and description making it easy to find specific products. 
- The lay out and navigation of Happy Bonsai are build upon the conventions of well laid out shops.  
- The products have clear photo's and the information about the products is easy to find.

#### Business Goals
The Happy Bonsai business goals are:
- To give of a professional, trustworthy and safe feeling to users so that they can buy products without doubt.
- To make sales easy for buyers to boost sales.
- to keep track of sales data to see popularity of products.

### User Stories

- Viewing and Navigation

| AS A    | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User |   View list of purchasable products           |      See what choices i have       |
| Site User |   View details of products                    |      see if the products are what I am looking for       |
| Site User |   Quickly find deals and special offers       |      Get all the best deals       |
| Site User |   See the total of my purchases while shopping|     Cant get surprised of the cost       |
<br/>
- Registration and User Accounts

| AS A    | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User |    Quickly and easily register        |      use all the extra functionality       |
| Site User |    Quickly login in and out           |      use all the functions i want and close my account       |
| Site User |    Easily Recover password            |      recover my password when lost       |
| Site User |    See a Record of bought products    |      see the cost and products I ordered       |
<br/>

- Sorting and searching

| AS A    | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User |    Sort list of items                      |      See the specific product I am looking for quicker       |
| Site User |   Sort specific items                      |        See the specific product I am looking for quicker     |
| Site User |   Sort categories                          |      See the specific product I am looking for quicker       |
| Site User |   Search by name or description            |      See the specific product I am looking for quicker       |
| Site User |   Get a good display what I have searched  |      See the specific product I am looking for quicker       |
| Site User | Being able to make a list of items that i like (favourites)|      buy products on a later moment and i dont have to look for them.       |
<br/>

- Shopping cart, Purchasing and Checkout

| AS A    | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User |    View items in my cart          |      See that my order is right and i can see the prices       |
| Site User |   Adjust my bag         |      Adjust when i am not happy with the current bag       |
| Site User |    Enter my payment info  |      Pay and get my products       |
| Site User |   Safely and securely use personal payment info      |      So i will not be stolen from or hacked       |
<br/>
- Admin

| AS A    | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Admin |    add update and delete products in the store            |      Change and evolve my store       |
| Admin |    Add categories                                         |       Expand products sold       |
| Admin |    manage orders                                          |       Know products to send and where      |
| Admin |    manage profiles and reviews                            |      Help my customers when the lose account info       |
<br/>

### Design Choices
#### color scheme
![The used colors with their codes]()

The color test -

The color test was done [here](https://contrastchecker.com/)

#### Typography
        
MedievalSharp was used for the logo text
roboto was used for all the regular text

![font.]()
#### imagery

### Wireframes

buttons grow  on hover over.


## Features

### Elements on every Page

- The navigation bar  is responsive for phone and ipad users. When seen on the phone or ipad it shows a hamburger menu with all the same options as on a computer. The buttons are interactive for computer. When hovered over the links show conformation by slightly growing.
- On all the devices you can see and use the search function on whatever page you are.

### Home Page
-   The Home page has the 4 newest products displayed for users that come more frequently.
-   Beneath that there is a call to action/ shop button

### Products Page
-   The product page has all the products. which can be sorted in several ways.(price,rating,name or category)
-   The product cards link to detail pages which give more detailed info about the products. the cards are kept small so you can oversee as much products as possible.
-   When logged in you can see green favourites buttons you can toggel these to add the product to your favourites list.

### product Detail Page
-   The product detail page displays just one product but now the image is bigger and a description is visible.
-   underneath the description there is a input and 2 buttons to specify how many of the product you want to add. Beneath that there is a button to keep shopping or to add the product to your bag.
- Under the image there is a review/ rating field where you can see the reviews/ ratings or add them. If you are not logged in you will be send to login first.
- in the top you can see a favourites button again

### favourites page
- This page displays all the products you added to your wishlist/ favourites. When clicking the green favourite button you remove that product from your favourites.
- When clicking on one of the products you will be send to the product_detail page of that product.

### Register Page
### Login Page
### Profile Page
### Log out Page
### bag Page
### Checkout
### future features
    - See the amount of favourites that you have in the favourites icon at the top nav bar.
    - If there are no reviews there should be text saying: write the first review.
    - Connect the individual review score to the product rating
    

## Information Architecture

    - [Database choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [Products App Model](#products-app-model)
        - [Cart App Models](#cart-app-models)

## Technologies Used
### Tools
 - Git/github
 - Gitpod
 - PIP
 - Code spell checker

### framework
### Databases
- Heroku postgres
### Libraries
- bootstrap
### Languages
-   HTML5
-   CSS3
-   Javascript
-   Python

## Testing
    - See separate [TESTING.md](TESTING.md) file.

### known-bugs
    - When using the link forgot password  some users got no email send.
    - When removing or adding a favourite you are not returned to the same spot on the website.
    -

## Deployment
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

## Credits
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

### disclaimer

This website is created for educational purpose only. 
the content of the website is entirely fictional. 


### reflection

I really love coding however I sadly couldn't enjoy this project as much as I would have like due to time constrains.
Because of that I couldn't really style the website or add all the features that I would have liked. This led that was constantly trying to rush to get everything rolled out and making way more rash decisions that cost me more time on the long run and made the project sloppier then it had to be. And on top of that I feel like I learned less then with the previous projects. A lesson to be learned here.  


## Contact

feel free to contact me at pjdijxhoorn(at)hotmail(dot)com
