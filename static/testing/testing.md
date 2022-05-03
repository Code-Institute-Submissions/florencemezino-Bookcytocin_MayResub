# Bookcytocin, evolve to your best self

View the live project [here](https://bookcytocin-project.herokuapp.com/)

## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator  / Jinja - `Success` 
> to validate Jinja code is to open up a webpage in your app, right click the page, click view source, and copy that code into the W3 HTML validator.

- W3C CSS Validator - `Success`
- Pep8 - `Success`

Lighthouse - [Results](static/assets/testing/lighthousems3_results_resubmit.png)

### Testing User Stories from User Experience (UX) Section

Most common paths through the website:
1. Reaflix > Collections > Community > MyBookLog
2. MyBookLog > Reaflix > Collections > Community


#### As a reader and a new visitor to the website :

* As a reader, I want to have access to a great book library online so that I can have plenty of choice to select my next book to read
- Reader receives suggestions of trendy books thanks to Readflix section. Every time a book gets added manually in the database, user will see it appearing in the Readflix page.
- Reader has access via a search bar in the page Collections to a large library of books organized in 12 collections. 

* As a reader, I want to buy a book in few steps so that I can progress quickly on my reading goals
- Reader is redirected in one click to amazon to buy the book of their choice.

* As a reader, I want to have access to recommendations/ reviews about books so that it can help me to choose the next book to read
- In the community page, the reader has access to reviews from members of the Bookcytocin club.
- Users gets recommendations and life advice through articles, events, matercass etc thank to the blog

TO BE TESTED
* As a reader, I want to save book in a wishlist so that I can buy it later
- User can find books in the collections and save them in their profile (wishlist format) in order to buy them later

* As a reader, I want to sell books I read already so that I can invest in buying new ones
> Listed as future feature in Readme file

* As a reader, I want to exchange the books I read with other readers so that I can save money and interact with the readers community
> Listed as future feature in Readme file


#### As a reader and returning visitor to the website :

* As a reader, I want to be encouraged to read more so that I can reach my reading goal 
- User can log in to access their personal profile in which they can complete a reading commitment goal to make sure they reach their goal.

* As a reader, I want to see my reading goals progress so that I can be motivated to read more
- Reader has access to a section Insights in their profile in which they can see the number of books saved and the numbers of books finished and reviewed.
> Listed as future feature in Readme file

TO BE TESTED
* As a reader, I want to be able to share reviews about my readings so that I can also help others to decide their reading 
- Reader can add a review about a book they read. User needs to be logged in first in order to proceed.
> Listed as future feature in Readme file

* As a reader, I want to recommend the books I read so that I can have the feeling to be part of a community and it will motivates me to reach my goal
- User is able to to submit their review via a "add review " functionnality. User gets notified that the review is being treated.
- The commnunity page shows a strong sense of validation that to the many format a recommendation can be give. In the blog from the community page, user can read articles, participate to events etc.


* As a reader, I want to be able to upload online a book to sell so that I can market it better or remove it when it is sold out
> Listed as future feature in Readme file


#### As a reader and returning visitor to the website :

* As a reader, I want to see the most liked/successful/trendy books on a certain period to not miss out so that I can be up to date about trendy readings
- Readers have access to a special selection of books provided via Readflix. (a specific focus every month)

* As a reader, I want to be informed about new books releases, events, masterclass so that I can improve my learning skils in general. 
- To be informed about lastest news , tips , events, user can visit the community page


### Manual (logical) testing of all elements and functionality on every page.

#### Bookcytocin

1. Website purpose / description
- Click on the logo "Bookcytocin"
- Check if it redirect to the welcome page
- Confirm that the purpose of the site is mentionned on each slide of the carousel
- Confirm the headings are responsive on all devices.

#### Readflix 

1. Navigation bar
- Go to "Readflix" from a desktop
- Click on a different tab of the navigation bar to check if the active tab is highlighted when clicked and visiting the related page
- Click on each sign up button in the nav bar and the user can access the sign up form
- Check if navigation bar is responsive on tablet and mobile. Confirm navigation bar collapses to become a toggle menu with a dropdown of the navigation links.

2. Footer
- Go to "Readflix" from a desktop
- Scroll down to the bottom of the page
- Check if content is not hidden behind footer and is responsive.
- Click on social media links Facebook, Twitter, Linkedin. The three links redirects to the respective social media.

3. Carousel
- Go to any page from the site, the carousel will appear and show 4 slides.
- Confirm images are visible and responsive on all devices.
- Confirm all buttons from each redirect to the desired / correct page.

4. Book collection focus
- cHECK IF 4 books of a specific collection appears
- Check if Amazon link redirect user to the book details on Aamazon to purchase
- Check if Save on wishlist button pushes data to profile

> For every point mentionned above : Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool,

#### Collections

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Search bar function
- Go to "Collection "from a desktop
- The Collection page appears with a section presentation of the page + a search
User can search by book title, author and collection types.

> For every point mentionned above : Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool,

#### Community

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Profiles
- Go to "Community" from a desktop
- Check if the images appears 
- Check if the member profiles are responsibve
- Check the quality of the content/image displayed for each article


> Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

#### MyBookLog
1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. 3 sections to verify
- Go to "MyBookLog" from a desktop
    - Check goal statement form if responsive and if form can be updated
    - Check that saved book are rendered using "save on wishlist" button


> Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

#### Log in
1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Log in is reachable through "MyBooklog" tab amd through last slide of carousel , button "Go"
- Go to "MyBookLog" from a desktop
    - Log in successful, there is a flash message welcoming the user.
    - Check if user have access to content from My Booklog page (goal statement, reviews)
    - Check for reviews section if possible view a review 
    - Check for reviews section if possible edit a review 
    - Check for reviews section if possible edit a review 

#### Log out
1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Log out appear
- Go to "MyBookLog" from a desktop
    - Log in through the form
    - Check for button sign up transform into button log out for when user wants to log out
    - Check when loggin out if flash appears : You are successfully logged out


#### Sign up

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Sign up buttons 
- Go to "Sign up" button in the top corner left from a desktop
    - Check buttons redirects to sign up form
    - Check if the link "already user" from the sign up workd
    - Check that the flash messages is working : Registration successful!
    - Check for an existing user, flash is working : User alread exist


## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX (using developper tool)
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.


## Known Bugs

a- Functions

- 


b- style

* Carousel : after finishing displaying all the slides, not possible to use the arrow to go back to previous slide
* User wishlist table has a flex issue on medium screen (blank space on the right)

## Feedback

If you have any feedback, please reach out to the developper of the this project Florence Mezino at florence.mezino@outlook.com 