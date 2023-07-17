# Woodland Whispers Retreat


Discover a serene lakeside getaway at Woodland Whispers Retreat. Our Django-based website offers a seamless platform for exploring and booking cozy cabin rentals in a picturesque setting. Immerse yourself in nature, enjoy excellent fishing, embark on kayaking adventures, hike scenic trails, swim in refreshing lake waters, and even explore nearby caves. Experience the perfect blend of tranquility and outdoor recreation at Woodland Whispers Retreat. Book your cabin today and create unforgettable memories in this lakeside haven.

![Home Screen](/documentation/readme_images/am-i-responsive.PNG)

[View Woodland Whispers Retreat live website here](https://woodland-whispers-retreat.herokuapp.com/)
- - -

## Table of Contents

---

## User Experience (UX)

Immerse yourself in a seamless and captivating user experience at Woodland Whispers Retreat. Our website offers intuitive navigation, stunning visuals, and a hassle-free booking process. Personalized recommendations, comprehensive information, and responsive support ensure that your needs are met every step of the way. Enjoy a mobile-friendly experience, easily planning your lakeside getaway from any device. Discover tranquility and outdoor adventures at Woodland Whispers Retreat, where your journey from exploration to booking is effortlessly delightful.

### Project Goals

The goal of the Woodland Whispers Retreat project is to create an immersive and user-friendly online platform that allows visitors to explore, book, and enjoy a serene lakeside getaway. The project aims to provide a seamless user experience, showcasing the beauty of the retreat through captivating visuals and comprehensive information and a booking process for their dream retreat.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writting the user stories and using Project Boards on Github. Template was created to help write User Stories and define Epics

* Epics were written containing possible user stories and based on that the website was made.
* User stories were created by looking at epics and through iterations the project was advancing.
* Project Board is set to public.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns
* Labels were added to sort the issues based on the importance.

<details>
<summary> User Stories Template
</summary>

![User Stories Template](documentation/readme_images/template.PNG)
</details>

<details>
<summary> User Stories, Issues
</summary>

![User Stories, Issues](documentation/readme_images/issues.PNG)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](documentation/readme_images/project-board.PNG)
</details>

### User Stories

#### Epics
* Initial Deployment
* Home Page
* User Registration
* Website Admin and Bookings
* Maintain consistent design with responsiveness in mind

#### User Stories
1. Initial Deployment
* Create new Heroku application
* Link Github repository to the Heroku app
2. Home Page
* Create a navigation bar
* Create a footer
3. User Registration
* Sign Up page
* User registration, log in, log out
* Display users name
4. Website Admin and Bookings
* Alert messages
* Crud functionality
* Cabin pagination
* Admin panel
* Double bookings
* Book Amenities
* Total Price
4. Maintain consistent design with responsiveness in mind
* Maintain consistent design
* Test responsiveness

Detailed look can be found in the [project board](https://github.com/users/Thomas-Tomo/projects/2)

### Target Audience

* Individuals seeking a serene and tranquil lakeside retreat experience.
* Travelers looking for a seamless and hassle-free booking process for their getaway.
* Outdoor enthusiasts interested in exploring nature and enjoying outdoor adventures.
* People who value a captivating and visually appealing online experience.
* Mobile users who want the convenience of planning their retreat from any device.
* Couples looking for a romantic and secluded getaway surrounded by nature's beauty.
* Families in search of a serene and family-friendly retreat to create lasting memories.
* Nature photographers or artists searching for picturesque landscapes and natural inspiration.

### First time user

* Simple and intuitive website navigation for easy exploration and discovery.
* Engaging visuals showcasing the beauty of the retreat and its surroundings.
* Informative content providing an overview of amenities, activities.
* User-friendly forms with clear validation messages to ensure accurate input.
* Easy Registration process.

### Registered User

* Seamless login process with a secure and personalized user account.
* Browsing available cabins
* Booking
* Access to a personalized dashboard displaying booking history and upcoming reservations.
* Ability to easily modify or cancel existing bookings for flexibility and convenience.

### Admin user

* Secure and separate login portal for admin users with appropriate access control.
* Access to an admin dashboard for managing cabins, amenities, and bookings.
* Ability to add, edit, or delete cabin listings, including details and availability.
* Management of amenity options, such as adding, updating, or removing amenities.
* Ability to delete user accounts, providing the necessary control for managing user data and accounts.
* Management of bookings, including the ability to view, modify, or delete bookings as needed.

## Design

The Woodland Whispers Retreat website boasts an inviting and visually pleasing design. Earthy tones and a warm color palette evoke a sense of tranquility. The navigation bar features a circular logo and easy-to-read text. Captivating photos are displayed in a bordered carousel with elegant captions. The about section utilizes a dark background and horizontal lines for clarity. Social media links are presented in the contact section, and the footer complements the overall design.

### Color Scheme
![Color Scheme](documentation/readme_images/color-scheme.PNG)

### Cabin Images

All cabin images were created using Artificial Inteligence, AI image generator [Craiyon](https://www.craiyon.com/).

### Logo

Logo was also created using AI image generator [Craiyon](https://www.craiyon.com/).

### Typography

The 'Lora' font is specified as the primary font, and the 'Domine' font is specified as a fallback font.

### Wireframes

<details>
<summary> Home Page
</summary>

![Home Page](documentation/wireframes/home-page.PNG)
</details>

<details>
<summary> Home Page when logged in
</summary>

![Home Page when logged in](documentation/wireframes/home-page-logged-in.PNG)
</details>

<details>
<summary> Contact Page
</summary>

![Contact Page](documentation/wireframes/contact-page.PNG)
</details>

<details>
<summary> Cabin Booking Page
</summary>

![Cabin Booking Page](documentation/wireframes/cabin-booking-page.PNG)
</details>

<details>
<summary> Make a Booking Page
</summary>

![Make a Booking Page](documentation/wireframes/make-a-booking-page.PNG)
</details>

<details>
<summary> My Booking Page
</summary>

![My Booking Page](documentation/wireframes/my-booking-page.PNG)
</details>

<details>
<summary> Edit Booking Page
</summary>

![Edit Booking Page](documentation/wireframes/edit-booking-page.PNG)
</details>

<details>
<summary> Delete Booking Page
</summary>

![Delete Booking Page](documentation/wireframes/delete-booking-page.PNG)
</details>

<details>
<summary> User Login Page
</summary>

![User Login Page](documentation/wireframes/user-login-page.PNG)
</details>

<details>
<summary> User Logout Page
</summary>

![User Logout Page](documentation/wireframes/user-logout-page.PNG)
</details>

<details>
<summary> User Sign Up Page
</summary>

![User Sign Up Page](documentation/wireframes/user-sign-up-page.PNG)
</details>

### Data Models

1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system
    * The User entity has a one-to-many relationship with the Booking entity. This means that a User can have multiple Bookings, but each Booking is associated with only one User.
---
2. Amenity Model
    * Data model created so admin can add amenities to the cabin booking, and regulate the name and price of the amenities
    * Only Admin can change the data in the backend.
    * User can book those amenities through the Booking Model
    * An Amenity can be associated with multiple Cabins, and a Cabin can have multiple Amenities. This is represented by the many-to-many relationship between Amenity and Cabin.
    * There are two amenites set up, which are cave exploration and kayak rental
---
3. Cabin Model
    * A Cabin can have multiple Bookings, but each Booking is associated with only one Cabin. This is represented by the foreign key relationship between Cabin and Booking.
    * Admin can add cabins through djangos admin panel.
    * Only Admin can change the data in the backend.
    * User can see the cabin information and image based on the chosen cabin.
    * Information provided is price, image, description, number of bedrooms, maximum guests, amenities
---
4. Booking Model
    * A User can have multiple Bookings, but each Booking is associated with only one User. This is represented by the foreign key relationship between User and Booking.
    * Booking model has a feature that prevents overlapping bookings, so users dont book on the same dates
    * Total price is also calculated in the backend that is then displayed to user to show the total price of the booking, that includes if a user also adds amenities to the booking.
    * Full CRUD functionality is available to the user.
    * User in order to book has to fill check-in, check-out dates, number of guests and optional amenities
    ---

### User Journey 

![User Journey](documentation/readme_images/user-journey.PNG)

### Database Scheme

Entity Relationship Diagram (ERD)

![DataScheme](documentation/readme_images/data-scheme.PNG)

* The Amenity entity represents amenities that can be associated with cabins, with fields id as the primary key, name for the amenity's name, and price for the amenity's price.
* The Cabin entity represents individual cabin listings, with fields id as the primary key, name for the cabin's name, description for the cabin's description, price for the cabin's price, image for the cabin's image, max_guests for the maximum number of guests allowed, and bedrooms for the number of bedrooms in the cabin.
* The Booking entity represents a booking made by a user for a specific cabin, with fields id as the primary key, cabin_id as a foreign key referencing the Cabin entity, user_id as a foreign key referencing the User entity, check_in_date for the booking's check-in date, check_out_date for the booking's check-out date, num_guests for the number of guests in the booking, cave_exploration_tickets for the optional quantity of cave exploration tickets, kayak_rentals for the optional quantity of kayak rentals, and total_price for the total price of the booking.

This data scheme allows for the management of users, amenities, cabins, and bookings. Users can make bookings for specific cabins, and each booking can have associated details such as the check-in and check-out dates, number of guests, and optional extras.

## Security Features

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### Login Decorator

* booking_create, booking_success, booking_overview, edit_booking, and delete_booking: These views involve operations related to user bookings and require authentication with the login_required decorator.
* This ensures that only authenticated users can access these views.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.

### Form Validation

* The booking_create view validates form input using the BookingForm class. It checks for various validation errors, such as the number of guests, check-in and check-out dates, overlapping bookings, and additional validations for cave exploration tickets and kayak rentals.

### Overlapping Booking

* In the booking_create view, the code checks for overlapping bookings by querying the database for existing bookings that match certain conditions. It compares the selected check-in and check-out dates with the dates of existing bookings for the same cabin. If any overlapping bookings are found, an error message is added to the form, and a warning message is displayed to the user.

### Custom error pages

* 404 Error Page, provides user with a button the redirect to home page.
* 500 Error Page, provides user with a button the redirect to home page.

## Features

* Home page showcases a rotating carousel that contains available cabins
* The website features a comprehensive list of amenities accompanied by detailed descriptions for each one.
* User can make an account and login
* When logged in, users get access to the cabin overview and are able to book cabins
* Users can edit and delete their bookings
* Every user action is accompanied by a corresponding message to ensure that users are promptly notified of any changes or updates.
* Total price of booking is displayed to users.

### Existing Features

* Home Page
    * Displays a navigation bar with logo, main heading, amenities details, carousel cabin view, about section, footer with socials

![Home Page](documentation/readme_images/home-page.PNG)

* Once logged in the Sign Up button changes to Book Now button

![Book Now](documentation/readme_images/book-now.PNG)


* Logo
    * Logo was created using [Craiyon](https://www.craiyon.com/) AI image generator, in which I used words to describe the logo and then it was generated.

![Logo](documentation/readme_images/logo.PNG)

* Navigation Bar
    * It differs if its a user, admin or just a visitor

    * Navigation bar for a visitor

    ![Visitor](documentation/readme_images/navigation-bar.PNG)

    * Navigation bar for a user
    ![User](documentation/readme_images/user-navigation-bar.PNG)
    ![User Dropdown](documentation/readme_images/user-dropdown.PNG)

    * Navigation bar for admin
    ![Admin](documentation/readme_images/admin-navigation-bar.PNG)
    ![Admin Dropdown](documentation/readme_images/admin-dropdown.PNG)

* Amenities
    * Description of the amenities which user might like to experience.

![Amenities](documentation/readme_images/amenities.PNG)

* Cabin Carousel
    * When on home page there is a carousel that displays all available cabins for booking, it also has controls to move left or right, name and description of the cabin, when its clicked it redirects users to cabin overview page and visitors are asked to create an account or login in order to view the cabins in greater detail.

![Cabin Carousel](documentation/readme_images/carousel.PNG)

* About Section
    * It contains a short description of Woodland Whispers Retreat and a short lake tale

![About](documentation/readme_images/about.PNG)

* Footer
    * Contains copyright information, creator and social links which are all linked to the creator of the website, becuase purpouse of this website is educational.

![Footer](documentation/readme_images/footer.PNG)

* Contact Page
    * For educational purposes, the website includes fictional contact information such as an address, phone number, and email. It also includes social links, which are all linked to developer for educational purposes.

![Contact](documentation/readme_images/contact.PNG)

* Sign up
    * User can create an account

![Sign Up](documentation/readme_images/sign-up.PNG)

* Login
    * User can login into an account, if they have created one

![Login](documentation/readme_images/login.PNG)
![Login Message](documentation/readme_images/login-message.PNG)

* Browse Available Cabins
    * Admin can create cabins through django admin panel
    * Cabins are paginated to display 6 cabins per page

![Browse Cabins](documentation/readme_images/browse-cabins.PNG)

* Cabin pagination
    * On the bottom of the page

![Pagination](documentation/readme_images/pagination.PNG)

* Logout
    * User can logout

![Logout](documentation/readme_images/logout.PNG)

* Make a Booking
    * Users can make a booking by clicking the cabin they want and then read details and fill in the booking form.
    * Form validation is implemented to make sure form are submitted correctly and if there is an error user will be notified with alert message, also if everything is good, user gets a message to notifiy them.
    * Form contains amenities which are completely optional and they dont have to be selected.

    ![Message](documentation/readme_images/alert-message.PNG)

![Make a Booking](documentation/readme_images/make-a-booking.PNG)

* Booking Succesful
    * If booking is succesfull, user gets a notified message and an overview of the booking they just made, which includes all the details and a total price of the booking, also there is a button for contact page and my booking button that leads to all of the users bookings.

![Booking Succesful](documentation/readme_images/booking-successful.PNG)

* Booking Overview
    * Includes all of the user bookings, which have buttons to edit or delete bookings.

![Booking Overview](documentation/readme_images/my-bookings.PNG)

* Already booked dates
    * User won't be able to book dates that are already booked.
    * Dates in the past are unavailable.

![Booked Dates](documentation/readme_images/booked-dates.PNG)

* Edit Booking
    * User can change their booking and save changes

![Edit Booking](documentation/readme_images/edit-booking.PNG)

* Delete Booking
    * User can delete their booking, before it is deleted it has to be confirmed.

![Delete Booking](documentation/readme_images/delete-booking.PNG)

* Alert messages
    * For every action there is an alert message to notify user
    * Here is one example

![Alert Message](documentation/readme_images/delete-message.PNG)

* Admin Features
    * Django built in admin panel allows admin control over the website.
    * Admin can access admin panel through his navigation bar
    * Can add, update, delete cabins.
    * Create amenities, update existing amenities which are connected to the cabins.
    * Delete accounts, verifiy emails, delete bookings...

* Error Pages
    * There are custom 404 and 500 error pages set up.
    * They contain buttons to redirect to home page if there is an error.

![Error](documentation/readme_images/error.PNG)

### Features Left to Implement 

* User Reviews: Allow users to leave reviews and ratings for cabins they have booked, providing valuable feedback for other users.
* Advanced Search: Implement an advanced search functionality, enabling users to search for cabins based on specific criteria such as price range, amenities, and availability.
* Cabin Recommendations: Develop a recommendation engine that suggests cabins to users based on their previous bookings, interests, or preferences.
* Online Payment: Implement an online payment system to allow users to securely make payments for their bookings directly through the website.
* For the purposes of this project these implemenation were not necessary.

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

* [ElephantSQL](https://www.elephantsql.com/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework
* [Bootstrap 4.6.1](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - CSS framework

### Programs Used

* [Github](https://github.com/) - Storing the code online
* [Gitpod](https://www.gitpod.io/) - To write the code.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [Figma](https://www.figma.com/) - Used to create wireframes and schemes
* [Craiyon](https://www.craiyon.com/) - Generate AI images of cabins and logo based on my words descriptions
* [Am I Responsive](https://ui.dev/amiresponsive) - To show the website image on a range of devices.
* [Git](https://git-scm.com/) - Version control
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine
* [Favicon Generator](https://realfavicongenerator.net/) - Used to create a favicon
* [JSHint](https://jshint.com/) - Used to validate JavaScript
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python
* [Colormind](http://colormind.io/) - Color Scheme

## Deployment and Local Developement

Live deployment can be found on this [View Woodland Whispers Retreat live website here](https://woodland-whispers-retreat.herokuapp.com/)

### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
3. Click the fork button in the top right corner

#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### ElephantSQL Database
[Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat) is using [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database

1. Click Create New Instance to start a new database.
2. Provide a name (this is commonly the name of the project: tribe).
3. Select the Tiny Turtle (Free) plan.
4. You can leave the Tags blank.
5. Select the Region and Data Center closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary
[Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat) is using [Cloudinary](https://cloudinary.com/)
1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.



### Heroku Deployment
* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Prepare enviroment and settings.py
* In your GitPod workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* CLOUDINARY_URL - Insert your own Cloudinary API key
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1 - this is temporary, and can be removed for the final deployment
* DATABASE_URL - Insert your own ElephantSQL database URL here

#### Heroku needs two additional files to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

Site is now live

## Testing
Please see  [TESTING.md]() for all the detailed testing performed.

## References
### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
* [Cloudinary](https://cloudinary.com/documentation/diagnosing_error_codes_tutorial)
* [Google](https://www.google.com/)

### Content

* All of the content is imaginary and written by the developer, me, Thomas-Tomo Domitrovic.
* All images were generated with Artificial intelligence (AI) based on my word input and description of the cabins and logo.

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to the Slack community for their continuous engagement and willingness to share knowledge. The collaborative environment provided a platform for learning, troubleshooting, and gaining inspiration from fellow developers.