# Bookcytocin, evolve to your best self

Main MS3README.md file [here]()
View the live project [here]()


## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator - `Success`
W3C CSS Validator - `Success`
JShint - `Success`
Pep8 - `Success`
Jinja - `Success` to validate Jinja code is to open up a webpage in your app, right click the page, click view source, and copy that code into the W3 HTML validator. That will give you the rendered HTML code - i.e. all of the Jinja will have been converted into HTML that can be validated.

Lighthouse - [Results](assets/testing/lighthousems3_results.png)

### Testing User Stories from User Experience (UX) Section

Most common paths through the website:
1. Reaflix > Collections > Community > MyBookLog
2. MyBookLog > Community > Reaflix > Collections


#### As a reader and a new visitor to the website :

* As a reader, I want to have access to a great book library online so that I can have plenty of choice to select my next book to read
- 
- 

* As a reader, I want to buy a book in few steps so that I can progress quickly on my reading goals
- 
- 

* As a reader, I want to have access to recommendations/ reviews about books so that it can help me to choose the next book to read
- 
- 

* As a reader, I want to sell books I read already so that I can invest in buying new ones
- 
- 

* As a reader, I want to exchange the books I read with other readers so that I can save money and interact with the readers community
- 
- 

#### As a reader and returning visitor to the website :


* As a reader, I want to be encouraged to read more so that I can reach my reading goal 
- 
- 

* As a reader, I want to see my reading goals progress so that I can be motivated to read more
- 
- 

* As a reader, I want to be able to share reviews about my readings so that I can also help others to decide their reading 
- 
- 

* As a reader, I want to recommend the books I read so that I can have the feeling to be part of a community and it will motivates me to reach my goal
- 
- 

* As a reader, I want to be able to eupload online a book to sell so that I can market it better or remove it when it is sold out
- 
- 


#### As a reader and returning visitor to the website :

* As a reader, I want to see the most liked/successful/trendy books on a certain period to not miss out so that I can be up to date about trendy readings
- 
- 

* As a reader, I want to be informed about new books releases, events, masterclass so that I can improve my learning skils in general. 
- 
- 


### Manual (logical) testing of all elements and functionality on every page.

#### Readflix

1. Header / Navigation bar
- Go to "Readflix" from a desktop
- Click on the logo : we are redirected to the main page "Books"
- Click on a different tab of the navigation bar to check if the active tab is highlighted when clicked and visiting the related page
- Click on each
- Click on button ""
- Check if navigation bar is responsive on tablet and mobile. Confirm navigation bar collapses to become a toggle menu with a dropdown of the navigation links.

2. Footer
- Go to "Readflix" from a desktop
- Scroll down to the bottom of the page
- Check if content is not hidden behind footer and is responsive.
- Click on social media links Facebook, Twitter, Linkedin. The three links redirects to the respective social media.

3. Hero image
- Go to "Books" from a desktop
- Confirm hero image is visible and responsive on all devices.
- Confirm mouse hover hero image works by zooming on content

4. Website purpose / description
- Go to "Books" from a desktop
- Confirm that the purpose is stated and all destinations are listed.
- Confirm the headings are responsive on all devices.

> For every point mentionned above : Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool,

#### Collections

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Dropdown to select a destination
- Go to "Dimensions"from a desktop
- The Dimension page appears with ...

> For every point mentionned above : Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool,

#### Community

1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Profiles
- Go to "Experts" from a desktop
- Check if the title  and the image of the report article (main article) appears
- Check if the smal articles appears well with the description
- Check the quality of the content/image displayed for each article


> Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

#### MyBookLog
1. Header / Navigation bar
- Navbar code is identical on all html pages. Testing already completed.

2. Footer
- Footer code is identical on all html pages. Testing already completed.

3. Contact form
- Go to "MyBookinnerLab" from a desktop
- Check contact form layout and colors
- Check if functionality " required field" works properly
- Check for the contact form to clear up as soon as the form if submitted with the send button
- Check if email is received via email.js

> Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool

## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX (using developper tool)
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Known Bugs

* Contact Form not active : user won't receive a free ebook
* Insights saved books and reviews numbers are not generating the correct number (to be build with javascript)
* Carousel : after finishing displaying all the slides, not possible to use the arrow to back to first slide
* 


## Feedback

If you have any feedback, please reach out to the developper of the this project Florence Mezino at florence.mezino@outlook.com 