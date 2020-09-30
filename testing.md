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

As I used a 'mobile first' approach to developing this project, I continued to test the responsiveness of the design throughout development process. As I added each new feature to the project, I used Google Chrome's Dev Tools to view the result on different screen sizes. 
Doing so helped me make minor adjustments to the margins, padding and font sizes of different aspects of the project, as well as checking that new features were compatible on all screens.
However, as well as checking the design, I also continued to test the functionality of each feature as it was added to the project. Doing so revealed issues as they arose, with the significant ones outlined below in detail in the 'Compatibility Tests' and 'Manual Tests' sections.

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
1. An issue in using '{}' brackets as part of the source for <a> elements and <img> elements. However, this syntax is necessary to access static files and urls and was therefore ignored.
2. All html templates led to errors that the doctype and language were not declared. As the templates were based on the base.html template where these were addressed, this issue was also ignored.
3. Some Bootstrap Modals on the site returned errors with their 'aria-labelledby' attribute. This error was related to using templating language to specify the item the modal was related to, so this error was also ultimately ignored.
4. Further regarding Bootstrap Modals, the validator showed that some buttons had been listed as <a> elements with no 'href' attribute. This issue was rectified by changing the element to a <button> element as it should be. Doing so led to no further errors.
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
- The return to top arrow scrolls smoothly to the top of the page.

#### Home
- The 'Learn More' button takes users to the 'About' page.
- The 'Stay', 'Relax' and 'Eat' buttons ontop of the carousel take users to the correct service pages respectively.

#### About
- Users not in session can follow the prompts to 'Sign In' or 'Sign Up' to add a review, with the links working correctly to direct the users on. 
- Users who have added a review can add reviews through the the 'Add a Review' form. The form returns errors if the fields are blank or if there is not enough content.
- Users can only access the 'edit' and 'delete' modal buttons for the reviews that they have added (except the superuser, who can access all user reviews).



