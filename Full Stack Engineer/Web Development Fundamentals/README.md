# codecademy
Notes: 
FULL STACK ENGINEER - HTML Basics


Web Development Foundation:


***MODULE 0: Helpful Resources***

- Some additional resources that are considered groundbreaking, significant, or classics in the industry
    - [MDN Web Docs](https://developer.mozilla.org/en-US/)
    - [W3](https://www.w3.org/TR/CSS2/selector.html)
    - [CSS-Tricks](https://css-tricks.com/)
    - [DEV Community](https://dev.to/)
    - [Stack Overflow](https://stackoverflow.com/)
    - [Can I use](https://caniuse.com/)
    - [Codecademy Workspaces](https://www.codecademy.com/workspaces/new)
- Optional Books
    - [HTML & CSS, Jon Duckett](https://bookshop.org/books/html-and-css-design-and-build-websites/9781118008188)
    - [Eloquent JavaScript](https://eloquentjavascript.net/) - a free EBook!
    - [Cracking the Coding Interview (6th Edition), Gayle Laakamann McDowell](https://bookshop.org/books/cracking-the-coding-interview-189-programming-questions-and-solutions/9780984782857)

***MODULE 1: 404 Status Code***

- When a server responds to a client, the server specifies a status code as a part of the response.
- Status codes indicate whether or not the HTTP request was successfully completed.
- If there was an error, they contain some information about the type of error that happened.
- The status code helps the browser know how to handle the data that was sent back with the response.
- The HTTP statuses below:

!https://content.codecademy.com/programs/code-foundations-path/web-dev-survey/table.svg

***MODULE 1: How Do Browsers Work?***

- All of the following steps happen in a split second:
    1. When a user types in a URL and presses enter, the server processes the request and sends the HTML file back to the client. *HTML* files hold the content of a website and they also contain links for any additional assets or code that are needed to display the site properly.
    2. The browser will begin to search for elements in the HTML file and it will start to make additional HTTP requests for any other external resources used by the HTML file. This often includes:
        - One or more CSS stylesheets. *CSS* stands for cascading style sheets; CSS creates the style and layout of a web page. The browser will request the CSS stylesheet, and when the server sends it back, the browser analyzes the CSS and starts applying the visual styles to the content of the site.
        - The request-response cycle also sends website assets, like images and videos, from the server to the browser. If these files are large, there might even be a noticeable delay before they are rendered by the browser.
        - One or more JavaScript files. *JavaScript* makes the webpage interactive. This programming language functions as the “behavior” of the web page. A webpage that does not use JavaScript is known as a *static* webpage.
    3. These additional requests are made in parallel. This means that these requests are initiated at the same time, and the browser does not wait to receive one resource before requesting the next resource.

***MODULE 2: Basics of Web 2.0?***

- The earliest static websites were composed of text, images, and links, with very little interactivity beyond browsing from one page to another
- These websites are called *static*, which means lacking in movement because they do not change based on user behavior.
- early 2000s created a cluster of web applications that are often called “Web 2.0”.
- Providing a dynamic user experience by offering content that responds to user input without forcing the page to reload. In the early web, user input would typically take the user to a new page — and they would have to wait for the new page to load. In Web 2.0, websites could just update selected regions of the page, avoiding the interruption caused by reloading.
- The rise of blogging, social media, and wikis in web 2.0 meant that users could generate content and share it with their friends.

***MODULE 2: Languages of Web Development***

- ********************What is HTML (2/13)********************
    - *HTML* is the skeleton of all web pages.
    - It provides structure to the content on a website, including text, images, buttons, videos, and more.
    - You can always open up your work-in-progress website with your browser and see what you’re building.
- ****HTML Markup (3/13)****
    - *ML* in HTML stands for *markup language*.
    - Markup refers to a way of *annotating* text that is distinguishable from the text itself.
- ****HTML Elements (4/13)****
    - paragraph element is made up of one opening tag (`<p>`) the content (“Hello World!” text), and a closing tag (`</p>`).
    - *HTML element* — a unit of content in an HTML document formed by HTML tags and the text or media it contains.
    - Opening Tag — the element name used to start an HTML element. The tag type is surrounded by opening and closing angle brackets.
    - Content — The information (text or other elements) contained between the opening and closing tags of an HTML element.
    - *Closing tag* — the second HTML tag used to end an HTML element. Closing tags have a forward slash (/) inside of them, directly after the left angle bracket.
        
        ![Screenshot 2023-09-01 at 5.45.21 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9dd1aa1c-f65e-4674-bc91-62c19f7609aa/6885d2b5-4f07-4d75-8c5a-318cd5367208/Screenshot_2023-09-01_at_5.45.21_PM.png)
        
- ****Common Tags (5/13)****
    - 
    
    ```html
    <h1>This is a heading, it emphasizes text.</h1>
    
    <p>This is a paragraph, it is the most common tag for larger chunks of text.</p>
    
    <a>This is an anchor tag, used to specify the text that is the "anchor" for a link.</a>
    
    <button>This is a button.</button>
    ```
    
- ****Hypertext and the World Wide Web (6/13)****
    - The H and T in HTML stands for **h**yper**t**ext.
    - Hypertext is text that is linked to other text.
- ****Adding Hyperlinks (7/13)****
    - An *attribute* in HTML provides additional information about an HTML element.
    - It comes in a name and value pair eg. `width="500"`.
    - `href`attribute, which stands for **h**yperlink **ref**erence
    - When we set the `href` attribute on an anchor tag (abbreviated to `<a>`) we can specify both the text that should be rendered for the user (the text within the anchor tag) and the URL that the browser should navigate to.
    - 
    
    ```html
    <a href="www.codecademy.com">Learn to code!</a>
    ```
    
- ****What is CSS? (8/13)****
- ****Applying CSS (9/13)****
    - HTML link element to apply the CSS file.
    
    ```html
    <link rel="stylesheet" href="style.css"> 
    ```
    
    - The `rel` attribute specifies the relationship between the current document and the linked resource.
    CSS stylesheet here
    - most common use-case for the `rel` attribute, but it can also indicate that a resource is an icon, or that a resource needs to be preloaded before the main document itself.
    - `href` attribute specifies the address of the linked document.
- ****What is JavaScript? (10/13)****
    - One of the defining features of JavaScript is its ability to respond to browser events.
    - These **events** happen in real time and can be triggered by a wide variety of user interactions, including:
        - the user clicking on a button
        - the user pressing enter on their keyboard
        - a video file finishing loading
        - the user re-sizing their window
        - the user hovering over text on the webpage
    - JavaScript can respond to is the position of the mouse
    - When a user puts the mouse near an HTML element, the `onmouseover` event is fired.
    - JavaScript uses functions, which are reusable blocks of code designed to perform a specific task.
- ****JavaScript Functions****
    - Building blocks of JavaScript: Functions and Events.
        - Functions allow us to write a chunk of code once that can be reused over and over.
        - Events allow JavaScript to respond to user behaviors, like the user hovering their mouse over an HTML element or resizing their window.
    - Events and functions combine to give JavaScript the ability to create interactive experiences.
    - `<script>` tag: alerts the browser that the page contains JavaScript and separates the JavaScript code from the HTML.
    - `document` keyword
    - HTML attributes can set events, where the **name** of the attribute is the event and the **value** of the attribute is the JavaScript function that we want to execute. eg:
    
    ```html
    <onclick= "changeColor">
    ```
    
- ****What is SQL? (12/13)****
    - **SQL**, which stands for **s**tructured **q**uery **l**anguage.
    - SQL stores information in tables, which is simply a collection of information organized into rows and columns.
    - To get the information, you would write a *query*, or a program that would retrieve data from the table.
    - an example of a query that would select all of the columns —the `*` keyword is a shorthand for “all”— from the `page_views` table: SELECT * FROM page_views;
- Extras:
    - https://codeburst.io/how-to-become-a-web-developer-101-5db4f11e611
    - https://www.vox.com/2014/6/16/18076282/the-internet


    # *Fundamentals of HTML*

## ***MODULE 1&2: Introduction to** Fundamentals of **HTML & Learn HTML Elements***

- ****Introduction to HTML (1/16)****
    - HTML stands for HyperText Markup Language:
        - A *markup* language is a computer language that defines the structure and presentation of raw text.
        - In HTML, the computer can interpret *raw text* that is wrapped in HTML elements.
        - *HyperText* is text displayed on a computer or device that provides access to other text through links, also known as *hyperlinks*. You probably clicked on a couple of hyperlinks on your way to this Codecademy course.
- **HTML Anatomy (2/16)**
    - HTML Element: <p>Hello World!</p> ---> a unit of content in an HTML document formed by HTML tags and the text or media it contains
    - HTML tag ---> the element name, surrounded by an openening (<) and closing (>) angle bracket  
    - Opening tag: <p> ---> the first HTML tag used to start an HTML element. Tah type is surrounded by opening and closing angle brackets
    - Content: Hello World! ---> The information (text or other elements) contained between the opening and closing tags of an HTML element.
    - Closing tag: </p> ---> the second HTML tag used to end an HTML element. Closing tags have a forward slash (/) inside of them, directly after the left angle bracket.

- ****HTML Structure (4/16)****
    - When an element is contained inside another element, it is considered the *child* of that element.
    - he child element is said to be *nested* inside of the *parent* element.
    - eg:
    
    ```html
    <body>
      <p>This paragraph is a child of the body</p>
    </body>
    ```
    
    - `<p>` element is considered a child of the `<body>` element, and the `<body>` element is considered the parent.
    - Can be multiple levels of nesting, this analogy can be extended to grandchildren, great-grandchildren, and beyond.
    - The relationship between elements and their ancestor and descendent elements is known as *hierarchy*.
    - Understanding HTML hierarchy is important because child elements can inherit behavior and styling from their parent element.
    
    ```html
    <body>
      <div>
        <h1>Sibling to p, but also grandchild of body</h1>
        <p>Sibling to h1, but also grandchild of body</p>
      </div>
    </body>
    ```
    

- ****Headings (5/16)****
    - HTML, there are six different *headings*, or *heading elements*.
    - https://www.codecademy.com/resources/docs/html/headings?page_ref=catalog
    
    ```html
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>
    ```

- ****Divs (6/16)****
    - `[<div>](https://www.codecademy.com/resources/docs/html/elements/div?page_ref=catalog)` is short for “division” or a container that divides the page into sections**.**
    - These sections are very useful for grouping elements in your HTML together.
    - Don’t inherently have a visual representation
    - Very useful when we want to apply custom styles to our HTML elements.
    - Allow us to group HTML elements to apply the same styles for all HTML elements inside.
    - We can also style the `<div>` element as a whole.
    
    ```html
    <body>
      <div>
        <h1>Why use divs?</h1>
        <p>Great for grouping elements!</p>
      </div>
    </body>
    ```
    
    - `<div>`s can contain any text or other HTML elements, such as links, images, or videos.
    - Remember to always add two spaces of indentation when you nest elements inside of `<div>`s for better readability.
- **********************Attributes (7/16)**********************
    - 
    
    https://www.codecademy.com/resources/docs/html/attributes?page_ref=catalog
    
    - Expands an element’s tag.
    - [Attributes](https://www.codecademy.com/resources/docs/html/attributes?page_ref=catalog) are content added to the opening tag of an element and can be used in several different ways, from providing information to changing styling.
    - Attributes are made up of the following two parts:
        - The *name* of the attribute
        - The *value* of the attribute
    - One commonly used attribute is the `id`.
        - We can use the `id`attribute to specify different content (such as `<div>`s) and is really helpful when you use an element more than once.
        - Have several different purposes in HTML, but for now, we’ll focus on how they can help us identify content on our page.
        - We add an `id` to a `<div>`, we place it in the opening tag
        
        ```html
        <div id="intro">
          <h1>Introduction</h1>
        </div>
        ```
        
- ****Displaying Text (8/16)****
    - display text in HTML, you can use a *paragraph* or *span*:f
        - *[Paragraphs* (`<p>`)](https://www.codecademy.com/resources/docs/html/elements/p) contain a block of plain text.
        - `[<span>](https://www.codecademy.com/resources/docs/html/elements/span?page_ref=catalog)` contains short pieces of text or other HTML. They are used to separate small pieces of content that are on the same line as other content.
        
        ```html
        <div>
          <h1>Technology</h1>
        </div>
        <div>
          <p><span>Self-driving cars</span> are anticipated to replace up to 2 million jobs over the next two decades.</p>
        </div>
        
        PS: <span> element separates “Self-driving cars” from the rest of the text in the paragraph.
        ```
        
    - It’s best to use a `<span>` element when you want to target a specific piece of content that is *inline*, or on the same line as other text. If you want to divide your content into *blocks*, it’s better to use a `<div>`.
- ****Styling Text (9/16)****
    - style text using HTML tags.
    - The `<em>` tag emphasizes text, while the `<strong>` tag highlights important text.
    - Default:
        - The `<em>` tag will generally render as *italic* emphasis.
        - The `<strong>` will generally render as **bold** emphasis.
        
        ```html
        <p><strong>The Nile River</strong> is the <em>longest</em> river in the world, 
        measuring over 6,850 kilometers long (approximately 4,260 miles).</p>
        
        Display on Website:
        
        **The Nile River** is the *longest* river in the world, 
        measuring over 6,850 kilometers long (approximately 4,260 miles).
        
        As we can see, “The Nile River” is bolded and “longest” is in italics.
        ```
        
- ****Line Breaks (10/16)****
    - The spacing between code in an HTML file doesn’t affect the positioning of elements in the browser.
    - If you are interested in modifying the spacing in the browser, you can use HTML’s *line break* element: `<br>`.
    - The line break element is unique because it is only composed of a starting tag.
    
    ```html
    <p>The Nile River is the longest river <br> in the world, measuring over 6,850 
    <br> kilometers long (approximately 4,260 <br> miles).</p>
    
    Display on Website:
    
    The Nile River is the longest river
    in the world, measuring over 6,850
    kilometers long (approximately 4,260
    miles).
    ```
    
- ****Unordered Lists (11/16)****
    - In addition to organizing text in paragraph form, you can also display content in an easy-to-read list.
    - *Unordered list* tag (`<ul>`) to create a list of items in no particular order.
    - An unordered list outlines individual *list items* with a bullet point.
    - The `[<ul>` element](https://www.codecademy.com/resources/docs/html/elements/ul?page_ref=catalog) should not hold raw text and won’t automatically format raw text into an unordered list of items.
    - Individual list items must be added to the unordered list using the `<li>` tag.
- ****Ordered Lists (12/16)****
    - *[Ordered lists* (`<ol>`)](https://www.codecademy.com/resources/docs/html/elements/ol?page_ref=catalog) are like unordered lists, except that each list item is numbered.
    - Useful when you need to list steps in a process or rank items.
    - You can create the ordered list with the `<ol>` tag and then add individual list items to the list using `<li>` tags.
- ****Images (13/16)****
    - So far all the tags were for text, what if we want to add image
    - The `<img>` tag allows you to add an image to a web page.
    - `<img>` tag is a *self-closing tag*.
    - **Note:** that the end of the `<img>` tag has a forward slash `/`.
    - Self-closing tags may include or omit the final slash — both will render properly.
    eg
    
    ```html
    <img src="image-location.jpg" />
    ```
    
    - The `<img>` tag has a required *attribute* called `src`.
    - The `src` attribute must be set to the image’s *source*, or the location of the image.
- ****Image Alts (14/16)****
    - In order to make the Web more inclusive, we need to consider what happens when assistive technologies such as screen readers come across image tags.
    - The `alt` attribute, which means alternative text, brings meaning to the images on our sites.
    - The `alt` attribute can be added to the image tag just like the `src`attribute. The value of `alt` should be a description of the image.
    
    ```html
    <img src="#" alt="A field of yellow sunflowers" />
    ```
    
    - also serves the following purposes:
        - If an image fails to load on a web page, a user can mouse over the area originally intended for the image and read a brief description of the image.
        - Visually impaired users often browse the web with the aid of screen reading software. When you include the `alt` attribute, the screen reading software can read the image’s description out loud.
        - Plays a role in Search Engine Optimization (SEO), because search engines cannot “see” the images on websites as they crawl the internet. Having descriptive `alt` attributes can improve the ranking of your site.
- ****Videos (15/16)****
    - `<video>` tag requires a `src` attribute with a link to the video source.
    - `<video>`element requires an opening and a closing tag.
    
    ```html
    <video src="myVideo.mp4" width="320" height="240" controls>
      Video not supported
    </video>
    ```
    
    - After the `src` attribute, the `width` and `height`attributes are used to set the size of the video displayed in the browser.
    - The `controls` attribute instructs the browser to include basic video controls such as pausing and playing.
    - The text, `Video not supported`, between the opening and closing video tags will only be displayed if the browser is unable to load the video.
- ****************************Review (16/16)****************************
    - Here are a few more resources to add to your toolkit:
        - [Codecademy Docs: HTML](https://www.codecademy.com/resources/docs/html)
        - [Codecademy Workspaces: HTML](https://www.codecademy.com/workspaces/new)
        - 
        
        https://www.youtube.com/watch?v=uxmB8MlO3m8&t=1s
        

[***Index:***](https://www.notion.so/Index-f6d5eb29e60044549439d41ba6f700e9?pvs=21) (Back to the Index)

## ***MODULE 3: Learn HTML: Structure***

****HTML DOCUMENT STANDARDS**

- ****************************Preparing for HTML (1/14)****************************
    - We can let web browsers know that we are using HTML by starting our document with a *document type declaration*.
    - `<!DOCTYPE html>`
    - Declaration is an instruction, and it must be the first line of code in your HTML document.
    - It tells the browser what type of document to expect.
    - What version of HTML is being used in the document.
    - To make sure your document is forever interpreted correctly, always include `<!DOCTYPE html>` at the very beginning of your HTML documents.
    - HTML code is always saved in a file with an **.html** extension.
- ****The <html> Tag (2/14)****
    - To create HTML structure and content, we must add opening and closing `[<html>](https://www.codecademy.com/resources/docs/html/elements/html?page_ref=catalog)` tags after declaring `<!DOCTYPE html>`:
    - Anything between these tags will be considered HTML code.
    - Without these tags, it’s possible that browsers could incorrectly interpret your HTML code.
- ****The Head (3/14)****
    - The `<head>` element contains the *metadata* for a web page.
    - It gives the browser some information about the page itself.
    - Metadata in the head is information about the page itself.
    - 
    
    ```html
    <head>
    
    </head>
    ```
    
- ****Page Titles (4/14)****
    - A browser’s tab displays the title specified in the `[<title>](https://www.codecademy.com/resources/docs/html/attributes/title?page_ref=catalog)` tag. The `<title>` tag is always inside of the `<head>`.
    - The `<title>` tag is always inside of the `<head>`.
    
    ```html
    <html>
      <head>
        <title>My Coding Journal</title>
      </head>
    </html>
    ```
    
    - Next, you will learn about new types of elements that go inside the body.
- ****Linking to Other Web Pages (6/14)****
    - You can add links to a web page by adding an *anchor* element `[<a>](https://www.codecademy.com/resources/docs/html/elements/a?page_ref=catalog)` and including the text of the link in between the opening and closing tags.
    `<a href="https://www.wikipedia.org/">This Is A Link To Wikipedia</a>`
    - 
- ****Opening Links in a New Window (7/14)****
    - When you click a link the page opens in a new browser window. This can be done by `target` attribute of element `<a>`
    - The `target` attribute specifies how a link should open.
    - Multiple links in a page and users should come back to your page that’s when you use `target` attribute.
    - new window ⇒ `target = “_blank”`
    - The `target` attribute can be added directly to the opening tag of the anchor element, just like the `href` attribute.
    - 
    
    ```html
    <a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">The Brown Bear</a>
    ```
    
- ****Linking to Relative Page (8/14)****
    - When making multi-page static websites, web developers often store HTML files in the *root directory*, or a main folder where all the files for the project are stored.
    - As the size of the projects you create grows, you may use additional folders within the main project folder to organize your code.
        
        ```
        project-folder/
        |—— about.html
        |—— contact.html
        |—— index.html
        
        Note: Three files in the above folder
        ```
        
    - HTML files are often stored in same folder
    - If the browser is currently displaying **index.html**, it also knows that **about.html**and **contact.html** are in the same folder.
    - Because the files are stored in the same folder, we can link web pages together using a *relative path*.
    - `<a href="./contact.html">Contact</a>`
    `<a>` tag is used with a relative path to link from the current HTML file to the `contact.html`file in the same folder. On the web page, `Contact` will appear as a link.
    - A relative path is a filename that shows the path to a *local file* (a file on the same website, such as `./index.html`)
    - Versus an absolute path (a full URL, like `https://www.codecademy.com/learn/learn-html` which is stored in a different folder)
    - `./` in `./index.html`tells the browser to look for the file in the current folder.
- ****Linking At Will (9/14)****
    - Turn images into links by simply wrapping the `[<img>](https://www.codecademy.com/resources/docs/html/elements/img?page_ref=catalog)` element with an `<a>` element.
    - 
    
    ```html
    <a href="https://en.wikipedia.org/wiki/Opuntia" target="_blank">
    	<img src="https://www.Prickly_Pear_Closeup.jpg" alt="A red prickly pear fruit"/>
    </a>
    ```
    
- ****Linking to Same Page (10/14)****
    - When users visit our site, we want them to be able to click a link and have the page automatically scroll to a specific section.
    - In order to link to a *target* on the same page, we must give the target an *id:*
        
        ```html
        <p id="top">This is the top of the page!</p>
        <h1 id="bottom">This is the bottom! </h1>
        ```
        
    - An `id` can be added to most elements on a webpage.
    - An `id` should be descriptive to make it easier to remember the purpose of a link.
    - The target link is a string containing the `#` character and the target element’s `id`.
    - The `<li>` element is the only valid direct child to `<ul>` and `<ol>` element.
- ****Whitespace (11/14)****
    - As the code in an HTML file grows, it becomes increasingly difficult to keep track of how elements are related.
    - Two tools help visualize relationship between elements:
    - *Whitespace*
    - *Indentation*
    - position of elements in a browser is independent of the amount of whitespace or indentation in the **.html** file.
    - For example, if you wanted to increase the space between two paragraphs on your web page, you would *not* be able to accomplish this by adding space between the paragraph elements in the **.html** file.
    - browser ignores *whitespace* in HTML files when it renders a web page, so it can be used as a tool to make code easier to read and follow.
- ****Indentation (12/14)****
    - [W3C](https://www.w3.org/Consortium/), is responsible for maintaining the style standards of HTML.
- **Comments (13/14)**
    - Comments begin with `<!--` and end with `-->` .
- ****HTML Tags (14/14)****
    - While some tags have a very specific purpose, such as image and video tags, most tags are used to describe the content that they surround, which helps us modify and style our content later.
    - [Full list of available HTML tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
    - `<nav>` element - navigation links
    - Notice that NOT all links of a document should be inside a `<nav>` element. The `<nav>` element is intended only for major blocks of navigation links.
    
    ```html
    <nav>
      <a href="/html/">HTML</a> |
      <a href="/css/">CSS</a> |
      <a href="/js/">JavaScript</a> |
      <a href="/python/">Python</a>
    </nav>
    ```
    

- Escape Characters:
    
    **Escaping** HTML characters in a string means replacing the:
    
    - less than symbol (<) with `&lt;`
    - greater than symbol (>) with `&gt;`
    - double quotes (") with `&quot;`
    - single quote (’) with `&#39;`
    - ampersand (&) with `&amp;`

**INTRO TO MOZILLA DEVELOPER NETWORK**

- For web development, one of the most well-known names in the industry is t he [Mozilla Developer Network](https://developer.mozilla.org/en-US/), or “MDN” for short.

**HTML ON MDN WEB DOCS: DEBUGGING**

[Debugging HTML - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Debugging_HTML)

- *Permissive Code*
    - Generally when you do something wrong in code, there are two main types of error that you'll come across:
        - **Syntax errors**: These are spelling or punctuation errors in your code that actually cause the program not to run, like the Rust error shown above. These are usually easy to fix as long as you are familiar with the language's syntax and know what the error messages mean.
        - **Logic errors**: These are errors where the syntax is actually correct, but the code is not what you intended it to be, meaning that the program runs incorrectly. These are often harder to fix than syntax errors, as there isn't an error message to direct you to the source of the error.
    - HTML itself doesn't suffer from syntax errors because browsers parse it permissively, meaning that the page still displays even if there are syntax errors.
    - Browsers have built-in rules to state how to interpret incorrectly written markup, so you'll get something running, even if it is not what you expected.

[***Index:***](https://www.notion.so/Index-f6d5eb29e60044549439d41ba6f700e9?pvs=21) (Back to the Index)

## *MODULE 4: Learn HTML: Tables*

**HTML TABLES**

- ****Introduction to Tables (1/13)****
    - Tabular data like stock prices, sports scores, invoice data, etc
    - Meaning table is often the best way of presenting the data.
    - HTML `<table>` element : present information in a two-dimensional table to the users.
- **Create a Table (2/13)**
    - create table: `<table>` element
    - The `<table>` element will contain all of the tabular data we plan on displaying.
    
    ```html
    <table>
    </table>
    ```
    
- ****Table Rows (3/13)****
    - In some languages table is predefined. In HTML all of the components must be created. Like rows, columns, cells and the data it will hold.
    - STEP 1: Add rows using *table row* element `<tr>`.
    
    ```html
    <table>
    	<tr>
    	</tr>
    	<tr>
    	</tr>
    </table>
    ```
    
- ****Table Data (4/13)****
    - Each cell element in a table must also be defined.
    - STEP 2: Add data using the *table data* element: `<td>`.
    
    ```html
    <table>
      <tr>
        <td>73</td>
        <td>81</td>
      </tr>
    </table>
    
    <!-- 2 data units added in single row -->
    <!-- one row and two columns -->
    ```
    
- ****Table Headings (5/13)****
    - STEP 3: Add titles to rows and columns using the *table heading* element: `<th>`.
    - table heading element is used just like a table data element, except with a relevant title.
    - Just like table data, a table heading must be placed within a table row.
    
    ```html
    <table>
      <tr>
        <th></th>
        <th scope="col">Saturday</th>
        <th scope="col">Sunday</th>
      </tr>
      <tr>
        <th scope="row">Temperature</th>
        <td>73</td>
        <td>81</td>
      </tr>
    </table>
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9dd1aa1c-f65e-4674-bc91-62c19f7609aa/864b8767-69e9-442d-92da-4c3885b305e6/Untitled.png)
    
    - the use of the `scope` attribute, which can take one of two values:
    1. `row` - this value makes it clear that the heading is for a row.
    2. `col` - this value makes it clear that the heading is for a column
- ****Table Borders (6/13)****
    - without borders it becomes difficult to read tables
    - In older versions of HTML, a border could be added to a table using the `border` attribute and setting it equal to an integer. This integer would represent the thickness of the border.
    - This has been deprecated now.
    
    ```html
    <table border="1">
      <tr>
        <td>73</td>
        <td>81</td>
      </tr>
    </table>
    ```
    
    - We use CSS to add style to HTML documents, because it helps us to separate the structure of a page from how it looks.
    - You can achieve the same table border effect using CSS.
    
    ```css
    table, td {
      border: 1px solid black;
    }
    ```
    
- ****Spanning Columns (7/13)****
    - Data can span columns using the `colspan` attribute.
    - The attribute accepts an integer (greater than or equal to 1) to denote the number of columns it spans across.
    
    ```html
    <table>
      <tr>
        <th>Monday</th>
        <th>Tuesday</th>
        <th>Wednesday</th>
      </tr>
      <tr>
        <td colspan="2">Out of Town</td>
        <td>Back in Town</td>
      </tr>
    </table>
    
    <!-- Out of Town spans the Monday and Tuesday table headings using the value 2 
    (two columns). The data Back in Town appears only under the Wednesday heading.-->
    ```
    
    ![Screenshot 2023-10-06 at 10.48.16 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/9dd1aa1c-f65e-4674-bc91-62c19f7609aa/6e6cf60b-dab7-4dae-a876-1f3b7af83695/Screenshot_2023-10-06_at_10.48.16_PM.png)
    
- ****Spanning Rows (8/13)****
    - Data can also span multiple rows using the `rowspan` attribute.
    - The `rowspan` attribute is used for data that spans multiple rows (perhaps an event goes on for multiple hours on a certain day). It accepts an integer (greater than or equal to 1) to denote the number of rows it spans across.
- ****Table Body (9/13)****
    - Long tables can be sectioned off using the *table body* element: `<tbody>`.
    - he `<tbody>` element should contain all of the table’s data, excluding the table headings
    - Couldn’t understand much
- ****Table Head (10/13)****
    - section off the table’s column headings using the `<thead>` element.
- ****Table Footer(11/13)****
    - The bottom part of a long table can also be sectioned off using the `<tfoot>` element.
    - 
    
    ```html
    <table>
      <thead>
        <tr>
          <th>Quarter</th>
          <th>Revenue</th>
          <th>Costs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Q1</th>
          <td>$10M</td>
          <td>$7.5M</td>
        </tr>
        <tr>
          <th>Q2</th>
          <td>$12M</td>
          <td>$5M</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th>Total</th>
          <td>$22M</td>
          <td>$12.5M</td>
        </tr>
      </tfoot>
    </table>
    ```
    
- ****Styling with CSS (12/13)****
    - 
    
    ```css
    table, th, td {
      border: 1px solid black;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    ```
    

## *MODULE 5: **SEMANTIC HTML***

- ****Introduction to Semantic HTML (1/9)****
    - we use a combination of non-semantic HTML and *Semantic HTML*.
    - semantic elements provide information about the content between the opening and closing tags.

    
- ****Header and Nav (2/9)****
    - A `[<nav>](https://www.codecademy.com/resources/docs/html/semantic-html/nav?page_ref=catalog)` is used to define a block of navigation links such as menus and tables of contents.
    - `<nav>` can be used inside of the `<header>`element but can also be used on its own.
- ****Main and Footer (3/9)****
    - Two more structural elements are `<main>` and `<footer>`.
    - The element `[<main>](https://www.codecademy.com/resources/docs/html/semantic-html/main?page_ref=catalog)` is used to encapsulate the dominant content within a webpage.
    - The tag is separated from the `[<footer>](https://www.codecademy.com/resources/docs/html/semantic-html/footer?page_ref=catalog)` and the `<nav>` of a web page since these elements don’t contain the principal content.
    
    ```html
    <main>
      <header>
        <h1>Types of Sports</h1>
      </header>
      <article>
        <h3>Baseball</h3>
        <p>
          The first game of baseball was played in Cooperstown, New York in the summer of 1839.
        </p>
      </article>
    </main>
    ```
    
    - The content at the bottom of the subject information is known as the *footer*, indicated by the `[<footer>](https://www.codecademy.com/resources/docs/html/semantic-html/footer?page_ref=catalog)` element.
    - The footer contains information such as:
        - Contact information
        - Copyright information
        - Terms of use
        - Site Map
        - Reference to top of page links
    
    ```html
    <footer>
      <p>Email me at Codey@Codecademy.com</p>
    </footer>
    ```
    
- ****Article and Section (4/9)****
    - `<section>` and `<article>` can go in body.
    - `[<section>](https://www.codecademy.com/resources/docs/html/semantic-html/section?page_ref=catalog)` defines elements in a document, such as chapters, headings, or any other area of the document with the same theme.
    - The `[<article>](https://www.codecademy.com/resources/docs/html/semantic-html/article?page_ref=catalog)` element holds content that makes sense on its own. It can hold content such as articles, blogs, comments, magazines, etc. An `<article>` tag would help someone using a screen reader understand where the article content (that might contain a combination of text, images, audio, etc.) begins and ends.
    
    ```html
    <section>
      <h2>Fun Facts About Cricket</h2>
      <article>
        <p>A single match of cricket can last up to 5 days.</p>
      </article>
    </section>
    ```
    
- ****The Aside Element (5/9)****
    - The `[<aside>](https://www.codecademy.com/resources/docs/html/semantic-html/aside?page_ref=catalog)` element is used to mark additional information that can enhance another element but isn’t required in order to understand the main content.
    - Can be used alongside other elements such as `<article>` or `<section>`.
    - Some common uses of the `<aside>` element are for:
        - Bibliographies
        - Endnotes
        - Comments
        - [Pull quotes](https://en.wikipedia.org/wiki/Pull_quote)
        - Editorial sidebars
        - Additional information
- ****Figure and Figcaption (6/9)****
    - `[<figure>](https://www.codecademy.com/resources/docs/html/semantic-html/figure?page_ref=catalog)` is an element used to encapsulate media such as an image, illustration, diagram, code snippet, etc, which is referenced in the main flow of the document.
    
    ```html
    <figure>
      <img src="overwatch.jpg">
    </figure>
    ```
    
    - It’s possible to add a caption to the image by using `<figcaption>`.
    - `[<figcaption>](https://www.codecademy.com/resources/docs/html/semantic-html/figcaption?page_ref=catalog)` is an element used to describe the media in the `<figure>` tag.
    
    ```html
    <figure>
      <img src="overwatch.jpg">
      <figcaption>This picture shows characters from Overwatch.</figcaption>
    </figure>
    ```
    
- ****Audio and Attributes (7/9)****
    - The `<audio>` element is used to embed audio content into a document.
    - Like `<video>`, `<audio>` uses `src` to link the audio source.
    
    ```html
    <audio>
      <source src="iAmAnAudioFile.mp3" type="audio/mp3">
    </audio>
    ```
    
    - Attributes allow us to do many different things to our audio file. There are many attributes for `<audio>` but today we’re going to be focusing on `controls` and `src`.
        - `controls`: automatically displays the audio controls into the browser such as play and mute.
        - `src`: specifies the URL of the audio file.
    - 
    
    [<audio>: The Embed Audio element - HTML: HyperText Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio#attributes)
    
- ****Video and Embed (8/9)****
    - By using a `<video>` element, we can add videos to our website.
    - Makes it clear that a developer is attempting to display a video to the user.
    - Some attributes that can alter a video playback include:
        - `controls`: When added in, a play/pause button will be added onto the video along with volume control and a fullscreen option.
        - `autoplay`: The attribute which results in a video automatically playing as soon as the page is loaded.
        - `loop`: This attribute results in the video continuously playing on repeat.
    
    ```html
    <video src="coding.mp4" controls>Video not supported</video>
    
    P.S.: The “Video not supported” will only show up if the browser is unable to display the video.
    ```
    
    - The `<embed>` tag is a self-closing tag, unlike the `<video>` (Deprecated tag) `<embed src="download.gif"/>`
- **Review (9/9)**
    
    ```html
     <!DOCTYPE html>
    <html>
    
      <head>
        <link rel="stylesheet" type="text/css" href="style.css">
      </head>
    
      <body>
    
        <header>
          <h1>Navigational Links</h1>
          <nav>
            <ul>
              <li><a href="#home">Home</a></li>
              <li><a href="#posts">Posts</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </nav>
        </header>
        
        <main>
          <section>
            <article>
              <h2>Facts About Dogs</h2>
              <p>
              Dogs have a sense of time. It's been proven that they know the difference between a hour and five. If conditioned to, they can predict future events, such as regular walk times.
              </p>
            </article>
            <aside>
              <p>A study was conducted on dogs being away from their owners for varying hours and the studies show that dogs who were away from their owners the longest showed the greatest amount of affection!
              </p> 
            </aside>
          </section> 
          <figure>
            <img src="https://content.codecademy.com/courses/SemanticHTML/dogimage.jpeg"/>
            <figcaption>A cute dog.</figcaption>
          </figure>  
          <audio controls>
            <source src="https://content.codecademy.com/courses/SemanticHTML/dogBarking.mp3" type="audio/mp3">
          </audio> 
          <video src="https://content.codecademy.com/courses/SemanticHTML/dog-video.mp4" controls>
          </video>
          <embed src="https://content.codecademy.com/courses/SemanticHTML/dog-on-beach.gif"/>
             
        </main>
        
        <footer>
          <p>Contact me at +1 234 567 8910 </p>
        </footer>
                  
      </body>
    </html>
    ```
    
- 

[HTML and CSS: Design and Build Websites a book by Jon Duckett](https://bookshop.org/p/books/html-and-css-design-and-build-websites-jon-duckett/10289632?ean=9781118008188)