JS will interact with the web page using DOM.

Browsers will construct the DOM, that is to store all HTML tags as JS objects.

To see the DOM of a website type document in the console. 

To see the actual objects type console.dir(document).

## important attributes:

1. document.URL ->  will return the URL of the website
2. document.body -> will return the entire HTML body.
3. document.head -> will return all that is in the head
4. document.links -> all the links that are on the page

## methods for grabbing the elements from DOM:

1. document.getElementById() -- Returns the element with the id
2. document.getElementsByClassName() -- Returns list of all elements belonging to a class
3. document.getElementsByTagName() -- Returns list of all elements with the tag
4. document.querySelector() -- Returns the first object matching the CSS style selector
5. document.querySelectorAll() -- Returns all objects matchin the CSS style selector


## If you want to change the text,html content, or attributes you can use the following:

1. myvariable.textContent - This returns just the text
2. myvariable.innerHTML - This returns the actual html
3. myvariable.getAttribute() - This returns the original attribute
4. myvariable.setAttribute() - This allowed you to set an attribute

## Making changes by listening to an event

reference -> https://developer.mozilla.org/en-US/docs/Web/Events

1. myvariable.addEventListener(event, func)

Many types of events possible like: 
1. Clicks
2. Hovers
3. Double clicks
4. Drags and so on..