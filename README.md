# WORK IN PROGRESS

The project will soon be deployed to Heroku, where it will be open to public viewing.

# Hotel Eko:

## Code Institute: Milestone Project 4

*Hotel Eko* is a fictional retreat located in the north of Sweden. Having worked in the hotel industry earlier, my idea for this project was to combine my knowledge of guest experiences with everything that I have learnt from my programming journey so far. The result is a hotel website that allows users to create their own hotel retreat personalized after their wishes for their stay, for them to be able to pay securely to confirm their reservation, to leave reviews when signed in and view blog updates from the hotel owner.

This was the last of four Milestone Projects that made up the Full Stack Web Development Program at *The Code Institute*. The main requirements were to build a full-stack website with the use of HTML, CSS, JavaScript, Python, Django and a relational database. Accommodating payment services was another requirement for this project and this was achieved through the use of Stripe.

If you would like to test the payment functionality of this project, please create an account and use the card number 4242 4242 4242 4242 with any address details, expiry date and CVC that you choose. 

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
    - [Database design](#Database-structure)
        - [Designing the database](#Tablet-User)
        - [Data models](#Data-Models)
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

-	To implement Stripe payment for users looking to make hotel reservations.

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
- [Samsara Ubud]( https://www.samsaraubud.com/)
- [Fäviken Magasinet]( http://favikenmagasinet.se/)
- [Arctic Bath]( https://arcticbath.se//)
- [Juvet]( https://juvet.com//)
- [the Arctic Hideaway]( http://thearctichideaway.com/en/)

#### Design process: UX Design

1.	Strategy plane: Having spent some time looking at websites for hotels and resorts based in Scandinavia, I was beginning to form an idea of the atmosphere that I wanted to create with this project. However, my research also led me to understand that the website would have to meet the needs of the hotel owner and potential guests alike, as all categories of users would need to be met within one well-planned design. The website would therefore have several functions: embody the brand and atmosphere of the hotel, inspire users to make a reservation, encourage them to add as many extra features to their booking as possible, successfully accept card payments to confirm bookings, allow the owner to modify their offers and provide a way for guests and the owner to share their views. 

2.	Scope plane: With the basic website concept and types of users in place, I began to work on how to put these into practice by considering the features. I firstly knew that the features would need to be divided between three categories: external (anonymous users), users logged in to their accounts and the hotel owner (superuser). For instance, all users should be able to view the hotel reviews, but only users logged in with their account could add, edit or remove a review. Similarly, only the owner would be able to change the services provided by the hotel. With this in mind, I decided on these rough feature ideas: login system, ability to leave reviews, a blog from the owner, the ability to customize a retreat and confirm the stay with a payment through Stripe. In order to keep the user informed throughout their experience on the website, I also decided to add a notification system, confirming a user’s actions (eg. deleting an item from their retreat).Furthermore, the website would have to meet certain content requirements to provide users with information about the hotel, including pricing, contact details and what the hotel offers. 

3.	Structure plane: Once I had narrowed down what features I wanted to include for the project, I began to consider how they would be presented through the structure of my design. I realized that the website would have to meet the needs of anonymous users browsing through the pages with open access, whilst barring them from viewing others that are only accessible to users logged in with their account or to the hotel owner. To create this distinction, I knew that the backend logic would have to make this possible and that it would be achieved through a changing menu bar. Certain items would be available to all users, while others would only be viewable to users who had been granted access to it. With this decision made, I wanted to make it easy for users to find what they were looking for with an intuitive navigation system so users could immediately get the information they were looking for. However, I also wanted to make the design progressive, so browsing users would enjoy the experience of learning more about the hotel at a leisurely pace. Ultimately, I decided to separate the hotel services into three categories: Stay (hotel rooms), Relax (spa treatments and yoga) and Eat (menu items). Users would be able to browse their individual details and add them to their retreat before paying to confirm their reservation. Their reservations would then be visible in their account page, with their profile details viewable there too. Blog posts from the hotel owner would also be exclusively viewable to users who had logged in to their account, and these users would also be able to navigate to the ‘about’ page to leave their review.

4.	Skeleton plane: With the concept and structure in place, I began to plan the navigation route through the design. After opening the website, the users would arrive at the home page to immediately experience the atmosphere of the hotel with the hero image and introductory message welcoming them in. Below, links to the different services would encourage them to browse through the offering. By navigating to ‘About’, they would read more about the hotel, the steps needed to make a reservation and a list of all user reviews. They could then click on the ‘Stay’, ‘Relax’ and ‘Eat’ pages to discover more about the options belonging to each respective category, clicking on an individual item to learn more. From there, a user could click on ‘Reservations’ to open a dropdown menu with the choice to sign up or sign in. Once in session, they could click on the same dropdown menu to view their ‘My Details’ page and be prompted to start adding items to their retreat, or read the messages from the hotel owner. Similarly, they could choose the ‘My Retreat’ option to view what they have added, with the ability to progress to the checkout and payment page from there. They also have the choice to return to the ‘About’ page to leave a review of the hotel. Once satisfied with their time on the website, they could sign out from the menu (with a prompt to confirm) and then return to the home page.

5.	Surface plane: 
* The first stylistic decision I made was to really focus on the atmosphere and branding of the hotel, as this would be part of the strategy to keep the user inspired to make a reservation. However, as the website would contain so many different elements and aspects, I knew that the visual design could not interfere with a user’s ability to navigate through the each page, but rather add to the experience of doing so.
* With the idea of the type and style of design that I was after, I started a workspace on [Figma]( https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=469%3A338) and began experimenting with my wireframes for desktop, tablet and mobile devices. As with my earlier three Milestone Projects, I found it useful to have my hero image in place, as doing so prompts me to choose the tone and theme for the rest of the design. I selected an image of a woman sitting on a bridge by a mountain lake, as I thought that image would inspire users to long for the change to unwind at the hotel. From this image, I began to extract the colors I would use and created a color palette with [coolors](https://coolors.co/), as shown below. I chose this palette as the colors are soothing, represent nature and offer an inviting feeling to users looking for a place to relax.
* I turned to Google Fonts to select the fonts I would use for this project. I wanted to find two compatible fonts that were modern, as although the website was meant to be atmospheric, it should not come across as outdated. I found that Poiret One and Open Sans met this criteria.

### Documenting the design process

Selected color palette:
![Color palette created with coolors.co]()

Design for desktop devices:
![My workspace on Figma]()

Design for mobile devices:
![My responsive design for mobile devices]()

Design for tablet devices:
![My responsive design for tablet devices]()

[The entire workspace can be viewed on Figma with this link.]( https://www.figma.com/file/Hv9GYC33ydTGLuwIxydgRr/Code-Institute?node-id=469%3A338)

### Database structure

As I built my project with Django, I used the built-in sqlite3 database during all development stages. When I then deployed the project to Heroku towards completion, I changed to a PostgresSQL database as that is provided by Heroku as an add-on for production. 
I also relied on Django’s default user model for authorization, allowing me to meet one of the project requirements of separating features by anonymous users, users in session and superusers. Further information about this feature can be found here: [django.contrib.auth.models](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/). Finally, the structure of the Checkout and Services apps were inspired by my studies with Code Institute, namely the Boutique Ado project found here: [Boutique Ado]( https://github.com/mkthewlis/boutique-ado).


#### Designing the Database

While working on the Scope and Structure planes of the design process, I also began working on the database structure. The first stage included drawing a basic idea of what the database would look like, and how data would relate to each other within it. The result of that process led to the following simplistic sketch of the idea: [Handrawn database sketch]()

With this complete, I had a better understanding of how I could develop the database and continued with a Microsoft Excel document. This eventually led to the structure outlined visually below. 

#### Data models

##### Profiles App

**Profile Model**

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

