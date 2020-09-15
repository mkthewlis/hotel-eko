# WORK IN PROGRESS

The project will soon be deployed to Heroku, where it can be viewed publically. 

# Hotel Eko:

## Code Institute: Milestone Project 4

*Hotel Eko* is a fictional retreat located in the north of Sweden. Having worked in the hotel industry earlier, my idea for this project was to combine my knowledge of guest experiences with everything that I have learnt from my programming journey so far. The result is a hotel website that allows users to create their own hotel retreat personalized after their wishes for their stay, as well as the ability for guests to leave reviews and view blog updates from the hotel owner.

This was the last of four Milestone Projects that made up the Full Stack Web Development Program at *The Code Institute*. The main requirements were to build a full-stack website with the use of HTML, CSS, JavaScript, Python, Django and a relational database. Accommodating payment services was another requirement for this project and this was achieved through the use of Stripe.

If you would like to test the payment functionality of this project, please use the card number 4242 4242 4242 4242 with any address details, expiry date and CVC that you choose. 

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
- [**Features**](#Features)
    - [Database structure](#Database-structure)
    - [Existing features](#Existing-features)
    - [Features left to implement](#Features-left-to-implement)
- [**Technologies used**](#Technologies-used)
- [**Testing**](https://github.com/mkthewlis/Milestone-Project-3/blob/master/testing.md)
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

2.	Scope plane: With the basic website concept and types of users in place, I began to work on how to put these into practice by considering the features. I firstly knew that the features would need to be divided between three categories: external (anonymous users), users logged in to their accounts and the hotel owner (superuser). For instance, all users should be able to view the hotel reviews, but only users logged in with their account could add, edit or remove a review. Similarly, only the owner would be able to change the services provided by the hotel. With this in mind, I decided on these rough feature ideas: login system, ability to leave reviews, a blog from the owner, the ability to customize a retreat and confirm the stay with a payment through Stripe. 
