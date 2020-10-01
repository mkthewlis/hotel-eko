## Testing

To return to the previous document, please click [here](https://github.com/mkthewlis/hotel-eko/blob/master/README.md).

- [**Defensive Design**](#Defensive-design)
- [**Testing User Stories**](#Testing-User-Stories)
    - [Project Stakeholders](#Project-stakeholders)
    - [New users](#New-users)
    - [Returning users](#Returning-users)
    - [Tablet user](#Tablet-user)
    - [Screenshots](#Screenshots)
- [**Validators and Lintners**](#Validators-and-lintners)
    - [HTML](#HTML)
    - [CSS](#CSS)
    - [JavaScript](#JavaScript)
    - [Python](#Python)
- [**Compatibility tests**](#Compatibility-tests)
    - [Using different browsers](#Using-different-browsers)
    - [Using different devices](#Using-different-devices)
- [**Manual tests**](#Manual-tests)
    - [Menu bar](#Menu-bar)
    - [Footer](#Footer)
    - [Home](#Home)
    - [Reviews](#Reviews)
    - [Retreat](#Retreat)
    - [Owner Blog](#Owner-blog)
    - [Payment](#Payment)
    - [404 page](#404-page)

### Defensive Design

As I used a 'mobile first' approach to developing this project, I continued to test the responsiveness of the design from the onset. As I added each new feature to the project, I used Google Chrome's Dev Tools to view the result on different screen sizes. Doing so helped me make minor adjustments to the margins, padding and font sizes of different aspects of the project, as well as checking that new features were compatible on all screens.
Similarly, I also continued to test the functionality of each feature as it was added to the project to notice issues as they arose. This process helped me locate where issues where coming from and was a useful way to keep track of the development process as each feature made the project more complex.

My approach to debugging often included using print statements to check where an issue was coming from. This helped me determine which part of a function was not working and allowed me to tackle the issue from there.

Below is an example from the early stages of developing the ```edit review``` function in the 'About' app's views.py file:

![Edit review debugging example](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/edit_review.png)

Although I came across several smaller issues during this process (including incorrect syntax and missing commas, fullstops or sets of {}s), three significant problems and solutions are outlined below:

1. Originally I had not planned to have a 'Categories' model within my 'Services' app. Instead, I had planned to only have a 'Services' model and that I would distinguish between the service types based on the Boolean value of three fields ('is_stay', 'is_relax' and 'is_eat'). I did so thinking that I would be able to categorise service items based on this. However, I quickly realised that this was not an efficient way of producing this project as I kept repeating the same function in my views for each type. I therefore decided to restructure my database, creating a 'Categories' model that helped determine what each service item was.
2. The second significant change that came as a resulting of testing my project early on was that I realised that I was repeating myself unneccessarily with my 'Services' templates. I had created three templates, with one for each service type, and each service had it's own set of functions within the views.py file. As with above, I realised I was repeating myself and that this was not complying to maintaining DRY code. I therefore restructured my templates to have one main 'services.html' template and one 'service-detail.html' template, with small 'includes' templates that would differ depending on the service's category. This drastically improved the structure of my code and saved me time repeating myself.
3. As my project began to grow, I made a few important changes to its design to make it more sleek and coherent. I decided to change the color of the footer, I changed the secondary font to a more modern variety and began to use a subtle off-white color for all boxes, modals and forms. This gave the project a much cleaner finish compared with the original design created on Figma. The results can be viewed in the screenshots below.

### Testing User Stories

The following tests were conducted to test the experience of each user outlined earlier in the 'User Stories' section.

#### Project stakeholders

- The main priority for the hotel owner was to have a website that would inspire users to make a reservation at the hotel. Beyond that, their aim was to inspire users to book as many features as possible from the Stay, Relax and Eat categories. This is achieved in the deployed project by including several prompts to encourage users to explore the different services that the hotel offers. Similarly, the user is prompted to continue to checkout with a button in the toast message that confirms when they have added an item to their retreat, and by including the 'Checkout' link to the menu dropdown list once they have items in their retreat.
- As the hotel owner wanted a design that suggested peace, calm and a focus on natural beauty, the website has been shaped by the colors extracted from a scenic mountain picture, which was used as the hero image for the home page. Soft color tones, minimalistic fonts and consistency created by using images from the same color scheme throughout achieve this aim.
- The hotel owner wanted guests to be able to share reviews and for the owner to feature welcoming messages to users logged in. This is achieved by allowing users who are logged in to add, edit and delete their reviews featured on the public 'About' page. If they aren't logged in they are prompted to do so and they are only able to make changes to their own reviews (with the exception of the hotel owner, who has access to all reviews.) Similarly, users who have logged in can view the hotel owner's blog featured on the 'My Details' page, whilst only the hotel owner can add, edit and review these blog posts.

#### New users

- The new user who relies on technology for all aspects of their lives but who would like to book a retreat to escape for the weekend would find this app easy to navigate. The sense of peace and calm would be clear through the design and color scheme and the ease of navigation would help convey a relaxing feeling to the user. This would encourage them to make the reservation and be able to put their device(s) down for a few days!
- The user who had been recommended this hotel by a friend would be able to explore the hotel and its services at a casual pace. They could follow the intuitive navigation from the Home to the About page, then gradually clicking their way through the different individual services. If they felt more curious about the hotel, they could follow the links to the Instagram and TripAdvisor pages beyond the site. Similarly, if they were keen to make a reservation, they would find it easy to set up an account, sign in and then add services to their retreat. Prompts would encourage them to confirm the reservation through the checkout pages and the email would confirm the payment. 

#### Returning users

- Users who want to find the reservation number of a previous booking could do so with a few short and intuitive steps. They would sign in with their existing account, automatically be redirected to their 'My Details' page and view the prompt to scroll down to see their previous reservations. From there, they would see a table with all of their earlier bookings, with a button to click to see the details of the reservation. With that link, they would then see the reservation number and could copy it to share it would their friends.
- Making a second reservation with the same account is a simple process for a returning user. They would have to sign in and could from their navigate between the different service categories to select which items they wanted to include on their next retreat. The checkout procedure would be the same as with previous stays - and once paid for and confirmed - the reservation would be included on their 'My Details' page.

#### Tablet user

- The tablet user would find that the app works just as well on a smaller screen. All features are responsive, including the carousel on the home page as the buttons linking users to different service categories are removed as they would otherwise be too small on narrower screens.

#### Screenshots

The screenshots below highlight a selection of testing different aspects of the website, its responsiveness and its relation to the user stories outlined above.

##### Checkout link featured in the menu of a user with items in their retreat:

![Checkout menu item](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/menu_checkout.png)

##### Sample review of a user in session:

![Review sample](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/review_sample.png)

##### Message to confirm the quantity of an item has been updated:

![Updated quantity](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/success_updated_quantity.png)

##### Error notifying that the maximum quantity has been exceeded:

![Error maximum quantity](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/error_10_items.png)

##### 404.html:

![404.html](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/error_404.png)

##### 500.html:

![500.html](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/error_500.png)

##### iPhone 5: empty retreat message:

![Empty retreat](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/iphone5_empty_retreat.png)

##### iPhone 5: service card sample:

![Service cards](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/iphone5_service_cards.png)

##### iPhone 6: prompt to return to the service overview

![Overview prompt](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/iphone6_overview_prompt.png)

##### iPad: Home page overview

![Home page](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_index.png)

##### iPad: 'My Retreat' overview for a user with items in their retreat

![Retreat](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_retreat.png)

##### iPad Pro: 'My Details' page, with booking history and address details

![My Details](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_pro_my_details.png)

##### iPad Pro: sample of a service page

![Service sample](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_pro_service_sample.png)

##### iPad Pro: Sign In

![Sign In](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_pro_sign_in.png)


### Validators and lintners

#### HTML
My HTML code was passed through the [W3C Markup Validation Service](https://validator.w3.org/).
Doing so brought up a few errors throughout the project related to using Django templates. These included:
1. An issue in using '{}' brackets as part of the source for ```<a>``` elements and ```<img>``` elements. However, this syntax is necessary to access static files and urls and was therefore ignored.
2. All html templates led to errors that the doctype and language were not declared. As the templates were based on the base.html template where these were addressed, this issue was also ignored.
3. Some Bootstrap Modals on the site returned errors with their 'aria-labelledby' attribute. This error was related to using templating language to specify the item the modal was related to, so this error was also ultimately ignored.
4. Further regarding Bootstrap Modals, the validator showed that some buttons had been listed as ```<a>``` elements with no 'href' attribute. This issue was rectified by changing the element to a ```<button>``` element as it should be. Doing so led to no further errors.
5. The base.html template returned a few errors shown on the screenshot below. However, these errors are related to using templating language in the html document and were therefore ignored as the validator was raising incorrect errors.

![base.html validator errors](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/base_template_validator.png)


#### CSS
I checked all CSS code with the [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/). 
All individual CSS files passed without any errors.

#### JavaScript
I used [JSHint](https://jshint.com/) to check my JavaScript code.
The only issue that came up with these checks was related to a forgotten semicolon within a JavaScript file inside the 'Checkout' app. Adding a ';' corrected this issue and returned no further errors.

#### Python
I used [PEP8](http://pep8online.com/checkresult) to check the Python code stored within each app.
This returned indentation errors and warnings that some lines that were too long within a few files. When these were corrected, there were no further errors.

### Compatibility tests

#### Using different browsers

I manually tested the project on the following web browsers, checking that all aspects worked as planned:
- Google Chrome 
- Mozilla Firefox 
- Apple Safari

This did not lead to any errors or problems.

#### Using different devices

The project has been tested on the following devices:
- Apple MacBook Air 13" 
- Apple iPhone 8
- Apple iPad Air
- Samsung Galaxy
- Huawei p30
- HP EliteBook
- Lenovo Thinkpad
- Benq 24" monitor

These tests led to the following errors and solutions:
1. Testing the project on a 24" monitor revealed that the 'About' page's hero image was too short, which distorted the image proportions. This led me to add a media query to increase the height of the image on larger screens.
2. I discovered the that ```background-attachment: fixed``` CSS property not compatible on all devices, as the hero images across the site were too enlarged, blurry and zoomed in. As a result, I added a media query to target smaller screens, changing the property to ```background-attachment: scroll``` for these particular images. This resolved the issue.

### Manual tests

#### Features consistent throughout the project
- The spinner overlay works on each template and covers the entire screen except the menu bar. It does not interfere with credit cards that require additional authentication.
- The return to top arrow scrolls smoothly to the top of the page regardless of which screensize the user has.
- Users who have not signed in are unable to access pages for authenticated users, and manually changing the url does not lead to any internal pages.
- Typing in the wrong url leads to a 'Page not found' error, where a user is met with a message explaining what has happened, the hotel email address for contact and a button to return to the Home page.
- Internal server errors lead to the 500.html message with a button to return home.

#### Menu bar
- *Logo* - clicking on the logo takes a user back to the home page.
- *Home* - as above, clicking on this link returns the user to the home page.
- *About* - directs a user to the About page.
- *Stay* - *Relax* - *Eat* - directs a user to the respective service pages.
- *Account* - opens a drop down menu with the following content:
    * Users not in session: *Sign In* and *Sign Up*, leading to respective forms.
    * Users who have signed in: *My Details*, *My Retreat* and *Sign Out*. Each link leads to their respective pages.
    * Users with items in their retreat: additionally, *Checkout* is added which directs them to the checkout page.

#### Footer
- Clicking on the TripAdvisor or Instagram icons directs the user to the respective websites on new tabs.
- The 'About', ' Stay', 'Relax' and 'Eat' links take the user to the correct service pages.

#### Home
- The 'Learn More' button takes users to the 'About' page.
- The 'Stay', 'Relax' and 'Eat' buttons ontop of the carousel take users to the correct service pages respectively.

#### About
- Users not in session can follow the prompts to 'Sign In' or 'Sign Up' to add a review, with the links working correctly to direct the users on. 
- Users who have signed in can add reviews through the the 'Add a Review' form. The form returns errors if the fields are blank or if there is not enough content.
- Users can only access the 'edit' and 'delete' modal buttons for the reviews that they have added (except the superuser, who can access all interactions with every user review).
- The links to the 'Stay', 'Relax' and 'Eat' direct users to the correct pages.

#### Service pages (Stay, Relax & Eat respectively)
- Each service page only shows items related to the relevant category. 
- The 'Learn More' button within each item card directly users to the correct service details page.
- Users not in session are prompted to Sign In or Sign Up to add items to their retreat.
- Users who have signed in can add the item directly from the service card, with a toast message that confirms this action. The toast box also features two buttons that link the user to their retreat or the checkout page respectively. However, users are limited to adding ten items of each to their retreat, with an error message explaining this.

#### My Details
- Different messages appear at the top of the page depending on if the user has no reservation history, if they have items in their retreat and if they are a returning user with previous bookings.
- The 'Account details' form updates when a user submits it.
- If a user has previous reservations, a table appears with a button that links back to the order overview. If they have not yet made a booking, they are again prompted to do so here.
- All users who have signed in can view the owner's blog posts that are displayed with the newest at the top. However, only the superuser can add, edit and delete previous entries.

#### My Retreat
- Users who have not yet added any items to their retreat see a message with prompts to the different service pages. These links direct the user to the right pages.
- Users with items in their retreat can edit the quantity of an item by clicking on the 'edit' modal. However, if they try to go above ten items of the same type they are warned with an error message. 
- Users can also delete items from their retreat. The confirmation message works as planned to notify the user that it has been done.
- Clicking on the thumbail image of an item directs the user to that service item's page.

#### Checkout
- Users have to complete the form to confirm their reservation.
- Incorrect card details result in an error message at the bottom of the form.
- Users who have made previous bookings and have saved their details in the past will notice that they are already filled in. Otherwise, users can select the 'save details' checkbox to successfully save their details.
- When a booking is complete, users are automatically redirected to the confirmation page.

#### Checkout Success 
- Users can see all of their booking details and the button linking to their profile works as it should.

#### Authorisation pages
- As these were created with [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html), I tested that they worked as they should. This included that emails were sent if a user registers an account, has forgotten their password or tries to register with a username that already exists. All of these features worked as they should.
- Trying to access the Sign In/ Sign Up pages when already in session does not work, just as accessing the Sign Out page when not authorised returns the user to the home page.

To return to the overview of the Hotel Eko project, please click [here](https://github.com/mkthewlis/hotel-eko/blob/master/README.md).
