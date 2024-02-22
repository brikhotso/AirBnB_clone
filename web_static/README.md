# AirBnB clone - Web static

HTML (HyperText Markup Language) is the standard markup language used to create web pages. It provides the structure and content of a webpage by using a system of tags and attributes to define various elements and their relationships.

To create an HTML page, you typically start with a basic template that includes the necessary structure. Here's a simple example:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. It typically uses tags to define elements within the document.

The DOM (Document Object Model) is a programming interface for web documents. It represents the structure of a document as a tree of objects, allowing programs to manipulate the structure, content, and style of a webpage dynamically.

An element or tag is a fundamental building block of HTML. It represents a particular structure or content within the document. For example, <p> represents a paragraph, <h1> represents a heading, and <div> represents a division or section.

An attribute provides additional information about an element and is placed within the opening tag of the element. Attributes are used to modify the behavior or appearance of an element. For example, the href attribute in an <a> tag specifies the URL of the link.

When a browser loads a webpage, it follows a series of steps including parsing the HTML to create the DOM, loading external resources like CSS and JavaScript, rendering the content, and executing scripts.

CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML. It defines how elements are displayed, including layout, colors, fonts, and other visual aspects.

To add style to an element using CSS, you can use selectors to target specific elements and apply properties to modify their appearance.
For example:

```
h1 {
    color: blue;
    font-size: 24px;
}
```

A class is a way to apply a set of styles to multiple elements. You can define a class in CSS and then apply it to HTML elements using the class attribute.

A selector is a pattern used to select the elements you want to style. It can be an element selector (like h1), a class selector (like .my-class), an ID selector (like #my-id), or more complex selectors.

CSS Specificity Value is a numerical representation of how specific a selector is. It determines which styles are applied to an element when multiple conflicting styles are defined. Specificity is calculated based on the type of selector used and the number of occurrences of each type of selector.

Box properties in CSS refer to properties that control the layout and dimensions of an element's box model. These properties include width, height, margin, padding, border, and position. They are used to control the spacing, positioning, and sizing of elements on a webpage.