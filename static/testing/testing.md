# Bookcytocin, evolve to your best self

View the live project [Here](https://bookcytocin-project.herokuapp.com/)

## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator  / Jinja - `Success` 
> to validate Jinja code is to open up a webpage in your app, right click the page, click view source, and copy that code into the W3 HTML validator.

- W3C CSS Validator - `Success`
- JS - `Success`
- Pep8 - `Success`

Lighthouse - [Results](static/assets/testing/lighthousems3_results_resubmit.png)

### Testing User Stories from the User Experience (UX) Section

Most common paths through the website:
1. Reaflix > Collections > Community > MyBookLog
2. MyBookLog > Reaflix > Collections > Community


#### As a reader and a new visitor to the website :

* As a reader, I want to have access to a great book library online so that I can have plenty of choice to select my next book to read.
- Reader receives suggestions of trendy books thanks to Readflix section. Every time a book gets added manually in the database, user will see it appearing in the Readflix page.
- Reader has access via a search bar in the page Collections to a large library of books organized in 12 collections. 

* As a reader, I want to buy a book in few steps so that I can progress quickly on my reading goals.
- Reader is redirected in one click to amazon to buy the book of their choice.

* As a reader, I want to have access to recommendations/ reviews about books so that it can help me to choose the next book to read.
- In the community page, the reader has access to reviews from members of the Bookcytocin club.
- Users gets recommendations and life advice through articles, events, matercass etc thank to the blog.

* As a reader, I want to save book in a wishlist so that I can buy it later.
- User can find books in readflix and collections and save them in their profile (my booklog wishlist) in order to buy them later.


#### As a reader and returning visitor to the website :

* As a reader, I want to be encouraged to read more so that I can reach my reading goal.
- Users can log in to an accesersonal profile in which they can complete a reading commitment goal to make sure they reach their goal.

* As a reader, I want to see my reading goals progress so that I can be motivated to read more.
- Reader has access to a section Insights in their profile in which they can see the number of books saved and reviewed. It is specified that is feature is being worked on.

* As a reader, I want to build a list of my future readings, so that I don't lose time browsing online for new books.
- Users can save books from the readflix and collections page to their wishlist. This functionality is available only to the ones with an account.

* As a reader, I want to be able to manage a list of future readings so that I know what would be my next purchase.
- Reader has access to a wishlist section in their profile in which they can view and remove books.


#### As a reader and returning visitor to the website :

* As a reader, I want to see the most liked/successful/trendy books on a certain period to not miss out so that I can be up to date about trendy readings.
- Readers have access to a special selection of books provided via Readflix. (a specific focus every month).

* As a reader, I want to be informed about new books releases, events, masterclass so that I can improve my learning skils in general. 
- To be informed about lastest news , tips , events, user can visit the community page.


### Manual (logical) testing of all elements and functionality on every page.

#### Bookcytocin

1. Website purpose / description
- Click on the logo "Bookcytocin"
- Check if it redirects to the welcome page
- Confirm that the purpose of the site is mentioned on each slide of the carousel
- Confirm that Explore button redirects to the collections page
- Confirm the headings are responsive on all devices
- Confirm that new member gets a welcome flash message 

#### Readflix 

1. Navigation bar
- Go to "Readflix" from a desktop.
- Click on a different tab of the navigation bar to check if the active tab is highlighted when clicked and visiting the related page.
- Click on each sign up button in the nav bar and the user can access the sign up form.
- Check if navigation bar is responsive on tablet and mobile. Confirm navigation bar collapses to become a toggle menu with a dropdown of the navigation links.

2. Footer
- Go to "Readflix" from a desktop.
- Scroll down to the bottom of the page.
- Check if content is not hidden behind footer and is responsive.
- Click on social media links Facebook, Twitter, Linkedin. The three links redirects to the respective social media.
- Check if scroll to top button works.

3. Carousel
- Go to any page from the site, and the carousel will appear and show 4 slides.
- Confirm images are visible and responsive on all devices.
- Confirm all buttons from each redirect to the desired / correct page.

4. Book collection focus
- Check if 4 books of a specific collection appear.
- Check if the Amazon link redirects the user to the book details on Amazon to purchase.
- Check if Save on wishlist button pushes data to profile.
- Confirm that users get a flash message when they save book to wishlist.


> For every point mentioned above: Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

#### Collections

1. Header / Navigation bar
- The navbar code is identical on all HTML pages. Testing already completed.

2. Footer
- The footer code is identical on all HTML pages. Testing already completed.

3. Search by collection
- Go to "Collection "from a desktop.
- Click on one collection name and verify if related books are being pulled.
- Check if flash message indicating collection name pops up.

4. Search bar function
- Go to "Collection "from a desktop.
- The Collection page appears with a section presentation of the page + a search.
- User can search by book title, author, description and collection types.
- Check if flash message indicating search results details pops up.

5. Save book to profile.
- User can save books to their profile (wishlist).
- Confirm that users get a flash message when they save book to wishlist.

> For every point mentionned above : Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

#### Community

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Content
- Go to "Community" from a desktop.
- Check if the images appears.
- Check if the member profiles are responsive.
- Check the quality of the content/image displayed for each article.

> Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

#### MyBookLog

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Sections to verify
- Go to "MyBookLog" from a desktop
    * Wishlist
        - Check that saved book are rendered using "save on wishlist" button from readflix and collections page.
        - Verify that the following information are present in the wishlist:
            - book's image 
            - book's title and author 
            - actions: 
                - buy: check link open to amazon site
                - remove: check if book gets removed from wishlist and if flash message appears indicating : book removed
    * Goal
        - Check goal statement form if responsive and if form can be updated.
        - Check if goal form appears correctly for new member.
        - Check flash message: goal saved.
    * Delete profile
        - Check if delete profile function works.
        - Check flash message : profile deleted and user being redirected to sign up page.

> Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

#### Log in

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Log in is reachable through "MyBooklog" tab amd through last slide of carousel , button "Go"
- Go to "MyBookLog" from a desktop:
    - Log in successful, there is a flash message welcoming the user.
    - Check if user have access to content from My Booklog page (goal statement, wishlist).
    - Check flash message : "hello user" + check if user is redirected to their account my booklog.
 

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
    - Check that the flash messages is working : Registration successful! + redirect to home page
    - Check for an existing user, flash is working : User alread exists
    - Check content of warning message about criteria regarding the creation of username and password.
        - check length
        - check lower case

## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, and Safari browsers.
* Verify security of account / protect user account routing using a different browser (Safari) than the one used to develop this project (Google Chrome)
    - flash message appears : "Please login to complete this request"
* The website was viewed on a variety of devices such as Desktop, laptops, iPhone7, iPhone 8 & iPhone X (using developer tool)
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.




## Known Bugs

a- Functions

- The same book can be saved twice in the wishlist (future feature: implement if the book is already saved in the wishlist function)
- If a book is saved twice in the user's wishlist when clicking 'remove' all entries related to that book get removed.  The book doesn't get removed one by one.

b- Style

* Improve user's wishlist view on mobile 
* Improve global user-friendly aspect to prevent too much scrolling

## Feedback

If you have any feedback, please reach out to the developer of this project Florence Mezino at florence.mezino@outlook.com 