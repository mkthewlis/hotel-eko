# Hotel Eko

## Code Institute: Milestone Project 4

![Hotel Eko Responsive Design](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/readme_images/am_i_responsive.png)

*Hotel Eko* is a fictional retreat located in the north of Sweden. Having previously worked in the hotel industry, my idea for this project was to combine my knowledge of guest experiences with everything that I have learnt from my programming journey so far. The result is a hotel website that allows users to create their own hotel retreat personalized after their wishes for their stay, for them to be able to pay securely to confirm their reservation, to leave reviews when signed in and view blog updates from the hotel owner.

This was the last of four Milestone Projects that made up the Full Stack Web Development Program at *The Code Institute*. The main requirements were to build a full-stack website with the use of HTML, CSS, JavaScript, Python, Django and a relational database. Accommodating payment services was another requirement for this project and this was achieved through the use of Stripe.

If you would like to test the payment functionality of this project, please create an account and use the card number 4242 4242 4242 4242 with any address details, expiry date and CVC that you choose. 

[Click here to view the project live.](https://hotel-eko.herokuapp.com/)

## Table of contents

- [**UX**](#UX)
    - [Main aims](#Main-aims)
    - [User Stories](#User-Stories)
        - [Project Stakeholders](#Project-Stakeholders)
        - [New Users](#New-Users)
        - [Returning Users](#Returning-Users)
        - [Tablet User](#Tablet-User)
    - [Design Process](#Design-Process)
    - [Documenting the design process](#Documenting-the-design-process)
    - [Database Structure](#Database-structure)
        - [Designing the database](#Designing-the-Database)
- [**Features**](#Features)
    - [Existing features](#Existing-features)
    - [Features left to implement](#Features-left-to-implement)
- [**Technologies used**](#Technologies-used)
- [**Testing**](https://github.com/mkthewlis/hotel-eko/blob/master/testing.md)
- [**Deployment**](#Deployment)
    - [Local deployment](#Local-Deployment)
    - [Deploying this project to Heroku](#Deploying-this-project-to-Heroku)
- [**Credits**](#Credits)
    - [Content](#Content)
    - [Images](#Images)
    - [Acknowledgements](#Acknowledgements)

## UX

### Main aims

- To create a hotel website with a structure that is intuitive for users to navigate and a design that meets contemporary industry standards.

- To create a full stack website where both the owner of the hotel and its users could satisfy all CRUD functions, allowing them to Create, Read, Update and Delete hotel offers or bookings respectively. 

- To implement Stripe payment for users looking to make hotel reservations.

- To make the website interactive, by adding JavaScript to create a positive user experience.

- To make navigation intuitive, by introducing prompts to guide the user in the right direction if lost and alert messages created with Bootstrap Toasts to confirm their actions.

- To create a design that would be fully responsive on all devices and screen sizes. 

### User Stories

The following User Stories helped me to create a design that would satisfy the needs of several different types of users.

#### Project stakeholders

-	As the hotel owner, I want to create a website that inspires users to make a reservation at the hotel. Ideally, I want to encourage them to book as many features as possible – as well as a hotel room – which will increase our revenue by keeping our guests at the hotel. 
-	I would like the website design to emphasize our brand aims: to offer peace and calm, by drawing on the natural beauty around the hotel.
-	To offer guests a platform to share reviews about their previous stays and view my welcoming thoughts prior to their arrival.

#### New users

- I am a user who relies on apps for all aspects of my life, from finding recipes, measuring the number of steps that I walk and monitoring the temperature of my home. Although I enjoy everything that technology gives me, I now want to learn more about this hotel in order to make a reservation to escape my apps for a weekend break!

- I have been recommended this hotel by a friend who stayed here last year. I would now like to find out more about what the hotel offers in order to decide whether I should make a reservation.

#### Returning users

- I have made a reservation and would like to confirm my booking number in order to share it with my friend who is joining me for the hotel stay. 
 
- My partner and I have stayed at the hotel before. We would now like to make another reservation with the same account that I used last time. 

#### Tablet user

- I am a user who primarily uses an iPad Pro to browse websites. I want to have a good experience on this website and view all the features in an equally aesthetic way. 

### Design Process

#### Design Process: UX Research 
Before beginning the formal design process, I began by exploring other hotel, resort and retreat websites. I found it inspiring and helpful to look at the designs featured on [Awwwards.]( https://www.awwwards.com/) and was particularly inspired by designs that drew on the atmosphere and beauty of the hotel’s local setting.  

Viewing other hotel website designs led me to the following conclusions: 
- I wanted to create a website that would offer information for new users to entice them to make a reservation, but also wanted to create a separate section that would only be for users who had created an account.
- The design should reflect the beauty of the Swedish mountains, which is where this fictional hotel is located. The aims of the hotel would be to offer guests the chance to unwind in a serene environment, and I wanted the design to begin the process by showing the users what kind of atmosphere they will experience. 
- The website would allow users to meet several goals: by finding information about the hotel, creating a personalized retreat, making a reservation, writing a review and reading personalized notes from the owner. 

##### The following websites were particularly useful during the research process:
- [Samsara Ubud](https://www.samsaraubud.com/)
- [Fäviken Magasinet](http://favikenmagasinet.se/)
- [Arctic Bath](https://arcticbath.se//)
- [Juvet](https://juvet.com//)
- [the Arctic Hideaway](http://thearctichideaway.com/en/)

#### Design process: UX Design

1.	Strategy plane: Having spent some time looking at websites for hotels and resorts based in Scandinavia, I was beginning to form an idea of the atmosphere that I wanted to create with this project. However, my research also led me to understand that the website would have to meet the needs of the hotel owner and potential guests alike, as all categories of users would need to be met within one well-planned design. The website would therefore have several functions: embody the brand and atmosphere of the hotel, inspire users to make a reservation, encourage them to add as many extra features to their booking as possible, successfully accept card payments to confirm bookings, allow the owner to modify their offers and provide a way for guests and the owner to share their views. 

2.	Scope plane: With the basic website concept and types of users in place, I began to work on how to put these into practice by considering the features. I firstly knew that the features would need to be divided between three categories: external (anonymous users), users logged in to their accounts and the hotel owner (superuser). For instance, all users should be able to view the hotel reviews, but only users logged in with their account could add, edit or remove a review. Similarly, only the owner would be able to change the services provided by the hotel. With this in mind, I decided on these rough feature ideas: login system, ability to leave reviews, a blog from the owner, the ability to customize a retreat and confirm the stay with a payment through Stripe. In order to keep the user informed throughout their experience on the website, I also decided to add a notification system, confirming a user’s actions (eg. deleting an item from their retreat).Furthermore, the website would have to meet certain content requirements to provide users with information about the hotel, including pricing, contact details and what the hotel offers. 

3.	Structure plane: Once I had narrowed down what features I wanted to include for the project, I began to consider how they would be presented through the structure of my design. I realized that the website would have to meet the needs of anonymous users browsing through the pages with open access, whilst barring them from viewing others that are only accessible to users logged in with their account or to the hotel owner. To create this distinction, I knew that the backend logic would have to make this possible and that it would be achieved through a changing menu bar. Certain items would be available to all users, while others would only be viewable to users who had been granted access to it. With this decision made, I wanted to make it easy for users to find what they were looking for with an intuitive navigation system so users could immediately get the information they were looking for. However, I also wanted to make the design progressive, so browsing users would enjoy the experience of learning more about the hotel at a leisurely pace. Ultimately, I decided to separate the hotel services into three categories: Stay (hotel rooms), Relax (spa treatments and yoga) and Eat (menu items). Users would be able to browse their individual details and add them to their retreat before paying to confirm their reservation. Their reservations would then be visible in their account page, with their profile details viewable there too. Blog posts from the hotel owner would also be exclusively viewable to users who had logged in to their account, and these users would also be able to navigate to the ‘about’ page to leave their review.

4.	Skeleton plane: With the concept and structure in place, I began to plan the navigation route through the design. After opening the website, the users would arrive at the home page to immediately experience the atmosphere of the hotel with the hero image and introductory message welcoming them in. Below, links to the different services would encourage them to browse through the offering. By navigating to ‘About’, they would read more about the hotel, the steps needed to make a reservation and a list of all user reviews. They could then click on the ‘Stay’, ‘Relax’ and ‘Eat’ pages to discover more about the options belonging to each respective category, clicking on an individual item to learn more. From there, a user could click on ‘Reservations’ to open a dropdown menu with the choice to sign up or sign in. Once in session, they could click on the same dropdown menu to view their ‘My Details’ page and be prompted to start adding items to their retreat, or read the messages from the hotel owner. Similarly, they could choose the ‘My Retreat’ option to view what they have added, with the ability to progress to the checkout and payment page from there. They also have the choice to return to the ‘About’ page to leave a review of the hotel. Once satisfied with their time on the website, they could sign out from the menu (with a prompt to confirm) and then return to the home page.

5.	Surface plane: 
* The first stylistic decision I made was to really focus on the atmosphere and branding of the hotel, as this would be part of the strategy to keep the user inspired to make a reservation. However, as the website would contain so many different elements and aspects, I knew that the visual design could not interfere with a user’s ability to navigate through the each page, but rather add to the experience of doing so.
* With the idea of the type and style of design that I was after, I started a workspace on [Figma](https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=469%3A338) and began experimenting with my wireframes for desktop, tablet and mobile devices. As with my earlier three Milestone Projects, I found it useful to have my hero image in place, as doing so prompts me to choose the tone and theme for the rest of the design. I selected an image of a woman sitting on a bridge by a mountain lake, as I thought that image would inspire users to long for the change to unwind at the hotel. From this image, I began to extract the colors I would use and created a color palette with [coolors](https://coolors.co/), as shown below. I chose this palette as the colors are soothing, represent nature and offer an inviting feeling to users looking for a place to relax.
* I turned to Google Fonts to select the fonts I would use for this project. I wanted to find two compatible fonts that were modern, as although the website was meant to be atmospheric, it should not come across as outdated. I found that Poiret One and Open Sans met this criteria.

### Documenting the design process

Selected color palette:
![Color palette created with coolors.co](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/wireframes/color_palette.png)

Design for desktop devices (in three parts):
![Desktop Workspace - One](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/wireframes/desktop_one.png)
![Desktop Workspace - Two](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/wireframes/desktop_two.png)
![Desktop Workspace - Three](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/wireframes/desktop_three.png)

Design for mobile devices:
![My responsive design for mobile devices](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/wireframes/mobile.png)

Design for tablet devices:
![My responsive design for tablet devices](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/wireframes/tablet.png)

[The entire workspace can be viewed on Figma with this link.](https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=469%3A338)

### Database structure

As I built my project with Django, I used the built-in sqlite3 database during all development stages. When I then deployed the project to Heroku towards completion, I changed to a PostgresSQL database as that is provided by Heroku as an add-on for production. 
I also relied on Django’s default user model for authorization, allowing me to meet one of the project requirements of separating features by anonymous users, users in session and superusers. Further information about this feature can be found here: [django.contrib.auth.models](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/). Finally, the structure of the Checkout and Services apps were inspired by my studies with Code Institute, namely the Boutique Ado project found here: [Boutique Ado]( https://github.com/mkthewlis/boutique-ado).

#### Designing the Database

While working on the Scope and Structure planes of the design process, I also began working on the database structure. The first stage included drawing a basic idea of what the database would look like, and how data would relate to each other within it. The result of that process led to the following simplistic sketch of the idea: [Handrawn database sketch](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/readme_images/database_sketch.png).

With this complete, I had a better understanding of how I could develop the database and continued with a Microsoft Excel document. This eventually led to the structure modelled below. 

#### Profiles App

*UserProfile Model*

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField 'User' |  on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Address Line1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Address Line2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
 Town/City | default_town_or_city | CharField | max_length=40, null=True, blank=True
 County | default_county | CharField | max_length=80, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True

#### Owner Blog App

*OwnerBlog Model*

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=modals.SET_NULL, null=True, blank=True, related_name="owner_profile"
 Title | title | Charfield | max_length=200
 Date Added | date_added | DateTimeField | auto_now_add=True
 Tought Content | thought_content | TextField | blank=True, null=True, default=""

#### Services App

*Services Model*

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Sku | sku | CharField | max_length=254, null=True, blank=True
 Name | name | CharField | max_length=254 
 Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
 Price | price | DecimalField | max_digits=6, decimal_places=2
 Description | description | TextField | max_length=900 
 Image | image | ImageField | null=True, blank=True
 Is Stay | is_stay | BooleanField | default=False
 Number of Guests | no_of_guests | IntegerField | null=True, blank=True
 Has Breakfast | has_breakfast | BooleanField | null=True, blank=True
 Is Relax | is_relax | BooleanField | default=False
 Length | length | IntegerField | null=True, blank=True
 Scents | scents | CharField | max_length=254, null=True, blank=True
 Is Eat | is_eat | BooleanField | default=False
 Protein | protein | CharField | max_length=254, null=True, blank=True
 Number of Courses | no_of_courses | IntegerField | null=True, blank=True
 
*Category Model*

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category | category | CharField | max_length=254

#### Checkout App

*Checkout Model*

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order Number | order_number | CharField | max_length=32, null=False, editable=False
 User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full Name | full_name | CharField | max_length=50, null=False, blank=False
 Email | email | EmailField | max_length=254, null=False, blank=False
 Country | country | CountryField | blank_label='Country*', null=False, blank=False
 Postcode | postcode | CharField | max_length=20, null=True, blank=True
 Town/City | town_or_city | CharField | max_length=40, null=False, blank=False
 Phone number | phone_number | CharField | max_length=20, null=False, blank=False
 Street Address 1 | street_address1 | CharField | max_length=80, null=False, blank=False
 Street Address 2 | street_address2 | CharField | max_length=80, null=False, blank=True
 County | county | CharField | max_length=80, null=True, blank=True
 Date | date | DateTimeField | auto_now_add=True
 Total Price | total_price | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Original Retreat | original_retreat | TextField | null=False, blank=False, default=''
 Stripe Pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

*OrderLineItem Model*
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems'
 Service | service | ForeignKey 'Service' | null=False, blank=False, on_delete=models.PROTECT
 Quantity | quantity | IntegerField | null=False, blank=False, default=0
 Lineitem Total | lineitem_total | DecimalField | max_digits=8, decimal_places=2, null=False, blank=False, editable=False

#### User Reviews App

*UserReviews Model*

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=modals.SET_NULL, null=True, blank=True, related_name="user_profile"
 Service | service | ForeignKey 'Service' | on_delete=models.SET_NULL, null=True, blank=True, related_name="user_service"
 Review Title | review_title | Charfield | max_length=200
 Review Content | review_content | TextField | blank=True, null=True, default=""

## Features

### Existing Features

#### Consistent features across all pages

- The menu at the top of the page and footer are consistent in design and are responsive throughout the website. However, the contents of the menu changes depending on if a user is logged in or not.
- The menu bar for users logged in features a 'Sign Out' link where the 'Sign Up' link usually is. When a user in session chooses to sign out, a toast message confirms this action and they are redirected back to the home page.
- Users with items added to their Retreat notice an additional 'Checkout' link in their navbar, allowing them direct access to go straight to checkout.
- The authentication pages (Sign In, Sign Up & Sign Out) were built with Django, and therefore include all Django's builtin features (including requesting an email for forgotten passwords.)
- Extra authentication prevents users not authenticated from access certain pages, including the checkout pages and the 'My Details' and 'My Retreat' pages.
- Each page features a 'scroll to top' arrow that becomes visible when the user has scrolled down the page.
- The active page is highlighted in a light blue colour to show the user which page they are on.
- All toast messages appear under the menu bar with the same fonts as used consistently in the theme. Depending on the type of message, the toast colour changes to reflect this message.
- Across all 'Service' pages (Stay, Relax & Eat), toast messages appear to confirm the contents of a user's retreat when they add new service items. This message also includes two buttons: 'View My Retreat' and 'Go To Checkout' to prompt users to continue towards making a reservation.
- An overlay with a spinner gif appears on all pages until the page has fully loaded.

#### Home

- The user begins by seeing the hero image of a woman sitting by a mountain lake.
- The user then scrolls down to see a textbox that slides upwards with an introduction to the hotel. Here a button prompts the user to 'Learn More', taking them to the About page.
- Below this, the user sees a fullwidth carousel that features buttons to the three services provided by the hotel: namely Stay, Relax and Eat.
- On smaller devices, the buttons on the carousel images are hidden, so the user only sees the images.

#### About

- A hero image of a couple at the retreat features at the top of this page.
- Below it, a user sees a section with the company ethos. The text slides upwards and the image changes size depending on screen width.
- The next section features user reviews. If a user is not signed in, they can only view the reviews added by other users and a prompt to sign in or register. If they have signed in, a form to add a review appears. 
- Users who have signed in and have already added reviews can click on the edit or delete buttons. These open respective modals to either edit or delete the review. 
- Below the reviews section, the process of making a reservation is described with three bullet points that also rise up when scrolled. The large number icons also change size and positioning to be responsive on smaller screens.
- The final section features three buttons to the hotel service pages: Stay, Relax and Eat.

#### Stay - Eat - Relax

- Although different pages, these three pages follow the same structure and are built with a generic 'services' template to avoid repetitive code.
- Each page is formatted to feature a hero image representing it's category with the category title at the top.
- As the user scrolls down, cards slide upwards, with one card for each service belonging to that category. 
- Each card contains the service title, image and a button to learn more about it. 
- Users who are signed in can add the service to their retreat directly. Anonymous users are instead faced with a prompt to sign in or sign up.
- Users are limited to adding 10 items of each service per order.

#### Stay - Eat - Relax: detail pages

- Users access these pages by clicking on the 'Learn More' button of the respective card.
- This page features the service image, title, all details about it and the price.
- If signed in, users can add the service to their retreat directly. Otherwise, they are prompted to sign in or sign up.
- Users are limited to adding 10 items of each service per order.

#### Sign In/ Sign Up

- These pages feature the same hero image as a background, reflecting the hero image on the home page.
- Ontop of the hero image, they feature the respective Sign In or Sign Up forms, prompting a user to access the parts of the website that require authentication.
- These pages can only be accessed when signed out / signed in respectively, so authorised users cannot sign in again.
- Once signed in, users are redirected to their 'My Account' overview page.

#### My Details

- The message at the top of the page changes depending on if the user is new to the site, if they have items already in their retreat and if they have previous orders. Users who have items in their retreat see an overview of what they have selected and see a link to prompt them to go to the My Retreat page to make changes.
- Below this setion, users can view and update their billing details. If users have made reservations in the past, a table with their booking history appears with a button to direct them to the initial 'booking success' page for that booking.
- The final section is the 'Thoughts from the Owner' blog. Here the hotel owner sees a form to submit new blog posts to the page, along with an edit and delete button that trigger their respective modals. Regular users can view the posts but cannot add, edit or delete posts from the page.

#### My Retreat

- This page is similar to a shopping cart on e-commerce sites: here the user can see each item in their retreat.
- All necessary information about the service item that a user has selected is included on this page, including price, quantity, subtotal and a thumbnail image that links them back to that page.
- A 'checkout' button prompts the user to confirm the reservation through payment.
- The page ends with three buttons linking users back to the services available: Stay, Relax & Eat.

#### Checkout

- If a user has signed in and added items to their retreat, the 'Checkout' link appears in the dropdown navigation menu.
- Otherwise, users can navigate to this page from the 'My Retreat' page through the button prompt.
- Here the user adds their details to an input form and can select whether to save the information to their profile for future reservations.
- An order summary also includes the name, price, quantity and thumbail link of each item in their retreat. 
- Below these features, a user can either select the 'Return to My Retreat' link or confirm the reservation with the 'Complete Order' button.

#### Checkout Success

- This page is accessed by completing the checkout process. However, it can also be accessed through the 'My Details' page when clicking on more information about a previous booking. In this case, an alert message confirms that the user is viewing a previous booking and that the confirmation email was sent at the time of payment.
- The title is personalized with the user's name above the same hero image as the one featured on the authorization pages. 
- Below a box contains a message from the hotel team explaining that they will be in touch to confirm a future arrival date. The order number and order details are also included below this message.

#### Sign Out

- This page features the same hero image as the Sign In/ Sign Up pages and can only be accessed by users that are not authenticated.
- Ontop of the hero image, a box includes a prompt that confirms that a user really does want to leave the site, with a 'Sign Out' button to do so.
- Once signed out, users are redirected back to the Home page.

#### Error pages: 404 and 500 pages

- Built with the same structure as the auth pages, these two pages have a large hero image with a textbox notifying the user of the issue they have come across.
- As well as the error message, they also feature buttons to take users back to the home page and include the hotel's email address if users want to get in touch.

### Features Left to Implement

- As most hotel websites offer, a future feature I would like to add is the ability to select a date of stay. I decided not to include this feature at this point, as building the logic required to caclulate the number of available rooms, for instance, was beyond the scope of this project. However, this would be the first feature that I would consider working on to develop the idea further.
- Another feature would be to include a chat app to allow users to get in touch with the reception team before their arrival. This would allow them to ask any questions or make specific requests that they may have.
- Creating a members club would be a nice feature, giving points to users depending on how much they spend on each reservation. These points could be used at the hotel and would be a good way to encourage regular users to return to earn more points, as it would provide another incentive for them to do so.
- I would also consider adding different levels of authentication, so the hotel owner and the reception team would have different levels of access to the features of the site.

## Technologies Used 

