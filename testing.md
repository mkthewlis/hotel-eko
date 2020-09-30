## Testing

To return to the previous document, please click [here](https://github.com/mkthewlis/hotel-eko/blob/master/README.md).

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
    - [Using different screen sizes](#Using-different-screen-sizes)
- [**Manual tests**](#Manual-tests)
    - [Menu bar](#Menu-bar)
    - [Footer](#Footer)
    - [Home](#Home)
    - [Reviews](#Reviews)
    - [Retreat](#Retreat)
    - [Owner Blog](#Owner-blog)
    - [Payment](#Payment)
    - [404 page](#404-page)

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

##### Checkout menu item

![Checkout menu item](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/menu_checkout.png)

##### Review sample of a user in session

![Review sample](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/review_sample.png)

##### Message to confirm updated quantity

![Updated quantity](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/success_updated_quantity.png)

##### Error notifying maximum quantity has been exceeded

![Error maximum quantity](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/error_10_items.png)

##### 404.html

![404.html](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/error_404.png)

##### 500.html

![500.html](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/error_500.png)

##### iPhone 5: empty retreat

![Empty retreat](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/iphone5_empty_retreat.png)

##### iPhone 5: service cards

![Service cards](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/iphone5_service_cards.png)

##### iPhone 6: overview prompt

![Overview prompt](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/iphone6_overview_prompt.png)

##### iPad: Home page

![Home page](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_index.png)

##### iPad: retreat

![Retreat](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_retreat.png)

##### iPad Pro: 'My Details' page

![My Details](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_pro_my_details.png)

##### iPad Pro: service sample

![Service sample](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_pro_service_sample.png)

##### iPad Pro: Sign In

![Sign In](https://github.com/mkthewlis/hotel-eko/blob/master/documentation/testing_screenshots/ipad_pro_sign_in.png)