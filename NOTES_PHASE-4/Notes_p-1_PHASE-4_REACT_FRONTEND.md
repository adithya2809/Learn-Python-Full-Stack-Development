# **PHASE-4 REACT FRONTEND**



#### **Lesson 1 — What is React?**



Before we write any code, let's answer a fundamental question.



Imagine you have this plain HTML page:

*<h1>Students</h1>*

*<ul>*

&#x20;   *<li>John</li>*

&#x20;   *<li>Alice</li>*

*</ul>*



Now suppose a new student, David, is added.



In plain HTML/JavaScript, you would have to manually find the <ul>, create a new <li>, and append it to the DOM.



React takes a different approach.

Instead of telling the browser how to update the page step by step, you simply describe what the UI should look like for the current data.



For example, if your data is:

*const students = \["John", "Alice", "David"];*



You tell React:

"Render this list based on the students array."



If the array changes, React figures out the necessary DOM **updates automatically.**



This is called **declarative UI.**



###### **Declarative vs Imperative**



**Imperative (Vanilla JavaScript):**



Find element

↓

Create new element

↓

Set text

↓

Append element

You specify every step.



**Declarative (React):**



Data changes

↓

React compares UI

↓

React updates only what changed

You describe the **desired result,** and React **handles** the **implementation details.**



###### **Why React became popular**



React solves several problems that become difficult in larger applications:

It breaks the UI into **reusable components.**

It **automatically updates** the page when data changes.

It **minimizes unnecessary DOM** updates using the **Virtual DOM** (we'll cover this next).

It makes large applications easier to **organize** and **maintain.**





#### **Lesson 2 — The Virtual DOM**



This is one of the most frequently asked React interview topics.



Imagine this webpage

Page

├── Navbar

├── Sidebar

├── Profile

├── Posts

├── Footer



Now suppose only one like button changes.

Without any optimization, the browser could end up checking or redrawing much more of the page than necessary.

React **avoids unnecessary work** using the **Virtual DOM.**



##### **What is the Virtual DOM?**



The Virtual DOM is a **lightweight JavaScript representation** of the real DOM.



Think of it like a blueprint.



**Real DOM**

HTML Elements

↓



**Virtual DOM**

JavaScript Objects



Instead of immediately changing the browser's DOM, React first updates this **lightweight copy.**



**How React Updates the UI**



When data changes:

State Changes

↓

New Virtual DOM Created

↓

Compare with Previous Virtual DOM

↓

Find Differences

↓

Update Only Changed Elements

↓

Real DOM Updated



This comparison process is called **Reconciliation.**

The algorithm React uses is commonly known as the **Diffing Algorithm.**



Example

Initially:

**Students**

John

Alice



After adding David:

**Students**

John

Alice

David



React compares:

**Old Virtual DOM**

John

Alice



**New Virtual DOM**

John

Alice

David



It notices:

"Only one new <li> has been added."



So it updates only that **one element**, instead of **rebuilding the whole list.**



#### **Lesson 3 — JSX (JavaScript XML)**



##### **Why did React introduce JSX?**

JSX was introduced to make UI code easier to write, read, and maintain. Instead of manually creating and appending DOM elements using document.createElement(), developers can write HTML-like syntax inside JavaScript. This makes components more readable, reusable, and easier to develop.



**For example:**



**Without JSX:**

*const h1 = document.createElement("h1");*

*h1.textContent = "Hello";*

*document.body.appendChild(h1);*



**With JSX:**

*<h1>Hello</h1>*



Much cleaner, isn't it?



##### **What does JSX actually return?**

When you write:

*<h1>Hello React</h1>*



React (through **Babel**) converts it into JavaScript like this:

*React.createElement(*

&#x20;   *"h1",*

&#x20;   *null,*

&#x20;   *"Hello React"*

*);*



And React.createElement() returns a **JavaScript object**, not a real HTML element.



##### **Is JSX HTML?**

No. JSX is a **syntax extension** for JavaScript that looks like HTML. During compilation, **Babel converts JSX** into React.createElement() calls, which produce JavaScript objects representing UI elements.



##### **What is Babel?**



Browsers understand:

HTML

CSS

JavaScript



They do not understand JSX.



If you write:

*<h1>Hello</h1>*



The browser has no idea what this means.



So before your code reaches the browser:

Your JSX Code

↓

Babel (Compiler)

↓

Normal JavaScript

↓

Browser Executes It





##### **React Component**



You write:

*function App() {*

&#x20;   *return <h1>Hello React</h1>;*

*}*



**Step 1: Babel Converts JSX**

Babel changes it into:

*function App() {*

&#x20;   *return React.createElement(*

&#x20;       *"h1",*

&#x20;       *null,*

&#x20;       *"Hello React"*

&#x20;   *);*

*}*



**Step 2: React.createElement() Returns a JavaScript Object**

Conceptually:

*{*

&#x20;   *type: "h1",*

&#x20;   *props: {*

&#x20;       *children: "Hello React"*

&#x20;   *}*

*}*

This object is stored in the Virtual DOM.



**Step 3: React Creates the Real DOM**

React finally creates the actual HTML element:

*<h1>Hello React</h1>*



which the browser displays.

So the complete flow is:

JSX (what you write)

&#x20;       │

&#x20;       ▼

Babel

&#x20;       │

&#x20;       ▼

React.createElement()

&#x20;       │

&#x20;       ▼

JavaScript Object

&#x20;       │

&#x20;       ▼

Virtual DOM

&#x20;       │

&#x20;       ▼

Real DOM

&#x20;       │

&#x20;       ▼

Browser Screen





###### **Is JSX mandatory to use React?**



What would you say?

Most beginners immediately answer "Yes."



The correct answer is No.



**You can write React without JSX:**

*function App() {*

&#x20;   *return React.createElement(*

&#x20;       *"h1",*

&#x20;       *null,*

&#x20;       *"Hello React"*

&#x20;   *);*

*}*



This is perfectly valid React.

JSX is simply syntactic sugar—a cleaner, more readable way to write React.createElement() calls. It improves the developer experience but isn't required.



#### **Lesson 4 — Creating Your First React Project**

##### **Step 1: Open VS Code**

Open the terminal and navigate to the folder where you keep your projects.



Example:

cd D:\\Projects

(Use your own project directory.)



##### **Step 2: Create a React Project**



Run:

*npm create vite@latest react-frontend*



It will ask a few questions.



**Choose:**

Project Name:

react-frontend



Framework:

React



Variant:

JavaScript



**Why JavaScript and not TypeScript?**

Since this is your first React phase, we'll learn React concepts without TypeScript syntax getting in the way. Once you're comfortable with React, learning TypeScript will be much easier.



##### **Step 3: Enter the Project**

*cd react-frontend*



##### **Step 4: Install Dependencies**

*npm install*



**❓What is npm install doing?**

When Vite creates your project, it generates a package.json file that contains a list of required packages.



For example:

*{*

&#x20; *"dependencies": {*

&#x20;   *"react": "...",*

&#x20;   *"react-dom": "..."*

&#x20; *}*

*}*



Running:

*npm install*



downloads those packages into the node\_modules folder.



Think of it like this:

package.json

&#x20;       │

&#x20;       ▼

List of Required Packages

&#x20;       │

npm install

&#x20;       │

&#x20;       ▼

Downloads Packages

&#x20;       │

&#x20;       ▼

node\_modules



##### **Step 5: Start the Development Server**



Run:

*npm run dev*



You'll see something like:

*Local: http://localhost:5173/*



Open that URL in your browser.

You should see the default Vite + React page.





#### **Lesson 5 — Understanding the React Project Structure**



Your project should now look something like this:

react-frontend/

│

├── node\_modules/

├── public/

├── src/

│   ├── assets/

│   ├── App.jsx

│   ├── App.css

│   ├── main.jsx

│   └── index.css

│

├── index.html

├── package.json

├── package-lock.json

├── vite.config.js

└── eslint.config.js



We're going to understand every important file.



##### **1. package.json**

Open package.json.



You'll see something similar to:

*{*

&#x20; *"name": "react-frontend",*

&#x20; *"private": true,*

&#x20; *"version": "0.0.0",*

&#x20; *"scripts": {*

&#x20;   *"dev": "vite",*

&#x20;   *"build": "vite build"*

&#x20; *},*

&#x20; *"dependencies": {*

&#x20;   *"react": "...",*

&#x20;   *"react-dom": "..."*

&#x20; *}*

*}*



**What is package.json?**

Think back to FastAPI.



We had:

requirements.txt



It contained:

fastapi

uvicorn

sqlalchemy



In Node.js, the equivalent is:

package.json



Instead of Python packages, it stores JavaScript packages.



| Python              | React/Node   |

| ------------------- | ------------ |

| requirements.txt    | package.json |

| pip install         | npm install  |

| virtual environment | node\_modules |

| uvicorn             | vite         |

|**Python**|**React/Node**|
|-|-|
|requirements.txt|package.json|
|pip install|npm install|
|virtual environment|node\_modules|
|uvicorn|vite|



##### **2. node\_modules**

You'll notice this folder is huge.



Inside are:

React

ReactDOM

Vite

ESLint

and hundreds of supporting packages



You **never edit** this folder.



It is recreated whenever you run:

*npm install*



##### **3. public/**

This folder stores files that are **served** **directly** by the **browser**.



Examples:

logo.png

favicon.ico

robots.txt



Unlike files in src, these aren't processed by React.



##### **4. src/**

This is where you'll spend **95%** of your time.



Inside:

src/

&#x20;   App.jsx

&#x20;   main.jsx

&#x20;   assets/



**Everything** we **build** will live here.





##### **5. index.html**

This is one of the most misunderstood files.



Open it.

You'll see something like:



*<body>*

*<div id="root"></div>*

*<script type="module" src="/src/main.jsx"></script>*

*</body>*



Notice something...

There is almost **no HTML**.



Just one div.

Why?

Because React **creates everything** inside this **one element.**



Think of it like an empty house.

HTML

↓

<div id="root"></div>

↓

React fills the house



###### **Startup Flow**



When you visit:

localhost:5173



The browser loads:

index.html



Inside it:

*<script type="module" src="/src/main.jsx"></script>*



So the browser immediately executes:

**main.jsx**



That makes main.jsx the **entry point** of the React application.



Exactly like this:



**FastAPI**

main.py

↓

Server Starts



**React**

main.jsx

↓

Application Starts



#### **Lesson 6 — main.jsx (The Entry Point)**



Now open:

src/main.jsx



You should see something similar to:

*import { StrictMode } from 'react'*

*import { createRoot } from 'react-dom/client'*

*import './index.css'*

*import App from './App.jsx'*



*createRoot(document.getElementById('root')).render(*

&#x20; *<StrictMode>*

&#x20;   *<App />*

&#x20; *</StrictMode>*



###### **Complete Flow**

Before diving into each line, here's the big picture:



Browser opens localhost:5173

&#x20;         │

&#x20;         ▼

&#x20;     index.html

&#x20;        │

&#x20;        ▼

&#x20;        │

&#x20;       ▼

&#x20;    main.jsx

&#x20;        │

&#x20;        ▼

Imports App.jsx

&#x20;        │

&#x20;        ▼

&#x20;  Renders

&#x20;        │

&#x20;        ▼

Places it inside

&#x20;        │

&#x20;        ▼

Browser shows UI



**Everything begins here.**



###### **Line 1**

*import { StrictMode } from 'react'*



**What is import?**

You've already seen this in Python.



Python:

*from math import sqrt*



**React:**

*import { StrictMode } from 'react'*

Same concept.

You're importing something from another module.



**What is StrictMode?**

This confuses almost every beginner.

StrictMode does NOT affect your users.

It is only active during development.



Its job is to help developers detect:

unsafe code

deprecated APIs

accidental side effects

potential bugs

Think of it as a teacher watching your code.



Your Code

↓

StrictMode

↓

"Hey…

This could become a bug later."



**In production:**

npm run build

↓

StrictMode disappears

It does not make your application slower for users.



###### **Line 2**

*import { createRoot } from 'react-dom/client'*

This is probably the most important import.

Notice something interesting.



We imported from:

react

Earlier.

Now we're importing from:

react-dom/client



**Why two different packages?**

Because they do different jobs.



**React**

React understands:

Components

JSX

State

Hooks

It knows **what** the UI should be.



**ReactDOM**

ReactDOM knows **how** to display that UI inside a web browser.

Think of it like this:

React

↓

Creates UI Description

↓

ReactDOM

↓

Displays it in Browser

What is createRoot()?

Imagine your HTML:



React asks:

"Where should I place my application?"

The answer:

document.getElementById("root")

That gives React this element:



Then:

createRoot(…)

creates a React root inside it.

Think of it as:

Empty Container

↓

React takes ownership

↓

Everything will be rendered here

Line 3

import './index.css'

Simple.

It imports the global stylesheet.

Exactly like:



in HTML.

Line 4

import App from './App.jsx'

This imports your main component.

Think:

App.jsx

↓

Main Page of your application

Later we'll have:

Login.jsx

Dashboard.jsx

Navbar.jsx

Footer.jsx

But everything begins with:

App.jsx

Now the Most Important Line

createRoot(document.getElementById('root')).render(

Let's break it apart.

Part 1

document.getElementById("root")

Does this look familiar?

You've probably used it in JavaScript before.

It searches:



and returns it.

Part 2

createRoot(…)

Now React says:

"Great.

I know where to render."

Part 3

.render(…)

Now React says:

"Render this component inside that root."

What is Render?

Render means:

Convert React components into actual DOM elements and display them.

So this:



becomes real HTML on your webpage.

Why ?

Notice:



instead of

App()

Why?

Because React components are represented using JSX syntax.

Behind the scenes:



is conceptually similar to:

React.createElement(App)

React then calls your component function when it needs to produce the UI.

Finally







means

Run App

↓

Monitor for Problems

↓

Show Warnings

↓

Help Developer

Nothing more.

Entire Flow

index.html

↓



↓

main.jsx

↓

Import App

↓

Find root div

↓

Create React Root

↓

Render App

↓

Browser Displays UI



#### **Lesson 7 — What is a React Component?**

Before looking at the code, answer this:

If I ask you,



"What is a component?"

What would you say?



Most beginners answer:

"A reusable piece of UI."



That's correct...

But why?



Let's find out.



**Look at this**

*function App() {*



&#x20;   *return (*

&#x20;       *...*

&#x20;   *)*

*}*



Ignore everything else.

This is all I want you to see.



###### **Is App a normal JavaScript function?**

*function add(a, b) {*

&#x20;   *return a + b;*

*}*

*add(a,b);*

returns

15



**Now compare it with:**

*function App() {*

&#x20;   *return (*

&#x20;       *<h1>Hello React</h1>*

&#x20;   *)*

*}*



It is also...



Just a JavaScript function.

The only difference is what it **returns.**



**Normal Function**

*function greet() {*

&#x20;   *return "Hello";*

*}*



Returns:

String



Another example:

*function add() {*

&#x20;   *return 10;*

*}*



Returns:

Number



###### **React Component**

*function App() {*

&#x20;   *return <h1>Hello</h1>;*

*}*



Returns:

**React Element** (JavaScript Object)



Remember what we learned before?

JSX

↓

React.createElement()

↓

JavaScript Object



So technically,

App() returns a **JavaScript object** representing the **UI.**





###### **Why is it called a Component?**



Suppose you're building Amazon.



Instead of writing one gigantic file:

Amazon

Navbar

Products

Footer

Cart

Profile

Orders

Search

Wishlist

Payments



**React says:**

Break it into pieces.



Example:

App

│

├── Navbar

├── Hero

├── Products

├── Footer

Each piece is a Component.



###### **Why does the function start with a Capital Letter?**



Notice:

function App()

instead of

function app()

React uses a simple rule.



**Lowercase:**

<div>

<h1>

<button>

means

**HTML Elements**



**Uppercase:**

<App />

<Navbar />

<Login />

<ProductCard />

means

**React Components**



If you write:

<app />



React thinks:

"Oh...

that's an HTML tag."

It won't call your function.



###### **Let's Simplify Your App.jsx**

Delete everything inside App.jsx and replace it with:



*function App() {*

&#x20; *return (*

&#x20;   *<h1>Hello React</h1>*

&#x20; *)*

*}*

*export default App*



Run the application.



You should see:

**Hello React**



That's it.

No logos.

No buttons.

No CSS.

No Vite template.

Just your first React component.



#### **Lesson 8 — Why Can a React Component Return Only One Parent Element?**



This is one of the first errors every React developer sees.



Suppose you write:



*function App() {*

&#x20; *return (*

&#x20;   *<h1>Hello</h1>*

&#x20;   *<p>Welcome</p>*

&#x20; *)*

*}*

*export default App*



Do you think this is valid?

❌ No.



React will throw an error similar to:

***Adjacent JSX elements must be wrapped in an enclosing tag.***





###### **Why Does This Happen?**

Remember what we learned yesterday.

A React component is just a JavaScript function.

A JavaScript function can return only one value.



Example:

*function add() {*

&#x20;   *return 5;*

*}*

Valid ✅



**But this isn't valid:**

*function add() {*

&#x20;   *return 5;*

&#x20;   *return 10;*

*}*



A function **cannot return two separate values.**

The same applies to React.



**This is invalid:**

*function App() {*

&#x20;   *return (*

&#x20;       *<h1>Hello</h1>*

&#x20;       *<p>Welcome</p>*

&#x20;   *)*

*}*



because React sees two sibling elements being returned.



##### **Solution 1 — Wrap with a <div>**

*function App() {*

&#x20;   *return (*

&#x20;       *<div>*

&#x20;           *<h1>Hello</h1>*

&#x20;           *<p>Welcome</p>*

&#x20;       *</div>*

&#x20;   *)*

*}*



Now React sees:

One Parent

&#x20;    │

&#x20;    ▼

<div>

&#x20;   <h1>

&#x20;   <p>

</div>



The function returns **one root element** (<div>), which contains **two children.**



###### **But There's a Problem**

Suppose your HTML becomes:

*<div>*

&#x20;   *<Navbar />*

&#x20;   *<Hero />*

&#x20;   *<Footer />*

*</div>*



React renders:

*<div>*

&#x20;   *<nav>...</nav>*

&#x20;   *<section>...</section>*

&#x20;   *<footer>...</footer>*

*</div>*



What if you didn't actually want that extra <div>?



Extra wrapper elements can:

Make the DOM unnecessarily deep.

Affect CSS layouts (especially Flexbox and Grid).

Add elements that serve no purpose.





##### **React's Solution — Fragments**

Instead of:

*<div>*

&#x20;   *<h1>Hello</h1>*

&#x20;   *<p>Welcome</p>*

*</div>*



React lets you write:

*<>*

&#x20;   *<h1>Hello</h1>*

&#x20;   *<p>Welcome</p>*

*</>*



This is called a **Fragment.**

A Fragment **groups multiple elements** together **without** creating an **extra HTML element.**



###### **Fragment Syntax**

**Short Syntax**

*<>*

&#x20;   *<h1>Hello</h1>*

&#x20;   *<p>Welcome</p>*

*</>*



This is what you'll use 90% of the time.



**Long Syntax**

*import { Fragment } from "react";*



*function App() {*

&#x20;   *return (*

&#x20;       *<Fragment>*

&#x20;           *<h1>Hello</h1>*

&#x20;           *<p>Welcome</p>*

&#x20;       *</Fragment>*

&#x20;   *);*

*}*



Same result.

The short syntax is just shorthand.



##### **Visual Understanding**



Without Fragment:

App

↓

div

├── h1

└── p



**With Fragment:**

App

├── h1

└── p

**Cleaner DOM.**





#### **Lesson 9 — JavaScript Inside JSX (One of the Most Important Concepts)**



Now React starts becoming dynamic.



Suppose you write:

*function App() {*

&#x20;   *const name = "Agney";*



&#x20;   *return (*

&#x20;       *<h1>Hello name</h1>*

&#x20;   *);*

*}*



What will the browser display?

Hello name



because "name" is just text.



###### **How do we display the value of the variable?**

React gives us a special syntax:



*function App() {*

&#x20;   *const name = "Agney";*



&#x20;   *return (*

&#x20;       *<h1>Hello {name}</h1>*

&#x20;   *);*

*}*



Output:

Hello Agney



Notice the curly braces:

***{name}***



These tell JSX:

"Stop treating this as HTML-like markup. Evaluate this as JavaScript."



###### **Think of JSX as Two Worlds**

JSX (HTML-like)

↓

<h1>Hello</h1>



Static content.



Inside curly braces:

{name}

**React switches to JavaScript.**



Example:

*function App() {*

&#x20;   *const age = 22;*

&#x20;   *return (*

&#x20;       *<h1>Age: {age}</h1>*

&#x20;   *);*

*}*



Output:

Age: 22



You can even do calculations:

*function App() {*

&#x20;   *return (*

&#x20;       *<h1>{10 + 20}</h1>*

&#x20;   *);*

*}*



Output:

30



Or expressions:

*const firstName = "Agney";*

*const lastName = "Aditya";*



*<h1>{firstName + " " + lastName}</h1>*



Output:

Agney Aditya



**Function Calls**

*function greet() {*

&#x20;   *return "Good Evening";*

*}*



*<h1>{greet()}</h1>*



Output:

Good Evening



Notice we're calling a **JavaScript function** inside **JSX.**



**Ternary Operator**

*const isLoggedIn = true;*



*<h1>{isLoggedIn ? "Welcome" : "Please Login"}</h1>*



Output:

Welcome



We'll use this extensively when we build the login page.



##### **Expression vs Statement (This is Very Important)**

Expression ✅	Statement ❌

|**Expression**|**Statement**|
|-|-|
|10 + 20|if (...) {}|
|name.toUpperCase()|for (...) {}|
|add(5, 10)|while (...) {}|
|age >= 18 ? "Adult" : "Minor"|switch (...) {}|



Expressions **produce a value**. Statements **perform an action.**

Since JSX needs something it can **display**, it only **accepts expressions** inside **{}.**





###### **Imagine you have this component:**

*function Welcome() {*

&#x20;   *return <h1>Welcome!</h1>;*

*}*



If you want it to display:

Welcome Agney



and later:

Welcome Rahul



without creating two separate components...





**Think about normal JavaScript functions**

Suppose you have:



*function greet(name) {*

&#x20;   *return "Welcome " + name;*

*}*



Now you can call it like this:

*greet("Agney");*

Output:

Welcome Agney



or



*greet("Rahul");*

Output:

Welcome Rahul



Notice something?

The function doesn't create the variable.

The **caller passes** it in.





**React works the same way**

A React component is just a function.



So instead of this:

*function Welcome() {*

&#x20;   *return <h1>Welcome {name}</h1>;*

*}*



React allows us to do something conceptually similar to:

*function Welcome(name) {*

&#x20;   *return <h1>Welcome {name}</h1>;*

*}*



Now React can pass different values into the component.

But instead of passing a single parameter like JavaScript functions, React **passes an object**.



That object is called **props.**



So the real version looks like:

*function Welcome(props) {*

&#x20;   *return <h1>Welcome {props.name}</h1>;*

*}*



Then we use it like this:

<Welcome name="Agney" />

<Welcome name="Rahul" />

<Welcome name="Priya" />



**React automatically creates:**

*{*

&#x20;   *name: "Agney"*

*}*

and passes it into the component.





###### **Visual Flow**

<App />

&#x20;       │

&#x20;       ▼

<Welcome name="Agney" />

&#x20;       │

React creates

&#x20;       │

&#x20;       ▼

props = {

&#x20;   name: "Agney"

}

&#x20;       │

&#x20;       ▼

Welcome(props)

&#x20;       │

&#x20;       ▼

<h1>Welcome Agney</h1>



This should remind you of something...

Look familiar?



Python:

*def greet(name):*

&#x20;   *return f"Welcome {name}"*



JavaScript:

*function greet(name) {*

&#x20;   *return `Welcome ${name}`;*

*}*



**React:**

*function Welcome(props) {*

&#x20;   *return <h1>Welcome {props.name}</h1>;*

*}*



They're all following the same idea:

Functions receive inputs and produce outputs.



The difference is that React **bundles the inputs** into a **single object** called **props.**





###### **Why does React pass an object (props) instead of a single variable?**



The main reason is **flexibility.**



Imagine React only allowed this:

*function Welcome(name) {*

&#x20;   *...*

*}*



Now suppose later you also need:

name

age

course

city

email



Would React have to call:

*Welcome("Agney", 22, "React", "Hyderabad", "agney@email.com")*



That becomes difficult to read and maintain.



Instead, React **bundles everything** into one object:

*props = {*

&#x20;   *name: "Agney",*

&#x20;   *age: 22,*

&#x20;   *course: "React",*

&#x20;   *city: "Hyderabad",*

&#x20;   *email: "agney@email.com"*

*}*



Now your component receives one parameter, but that parameter **contains many pieces of data.**



Interview-quality answer

React passes a **single props object** because it allows multiple values to be grouped together in one parameter. This makes components **flexible, scalable**, and **easier to maintain** as more data needs to be passed.





#### **Lesson 10 — Your First Reusable Component**

**Replace your App.jsx with this:**

*function Welcome(props) {*

&#x20; *return <h1>Welcome {props.name}</h1>;*

*}*



*function App() {*

&#x20; *return (*

&#x20;   *<>*

&#x20;     *<Welcome name="Agney" />*

&#x20;     *<Welcome name="Rahul" />*

&#x20;     *<Welcome name="Priya" />*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



Run it.



You should see:

Welcome Agney

Welcome Rahul

Welcome Priya



What Actually Happened?

Let's slow it down.



React first renders:

<App />



Remember:

<App />

↓

Call App()

↓

Return JSX



Now App() returns:

*<>*

&#x20;   *<Welcome name="Agney" />*

&#x20;   *<Welcome name="Rahul" />*

&#x20;   *<Welcome name="Priya" />*

*</>*



React now sees three more components.



###### **First Component**



React sees:

*<Welcome name="Agney" />*



Conceptually, it does something like:

*Welcome({*

&#x20;   *name: "Agney"*

*});*



Now inside the function:

*function Welcome(props) {*

&#x20;   *return <h1>Welcome {props.name}</h1>;*

*}*



**becomes**



*function Welcome(props) {*



&#x20;   *props = {*

&#x20;       *name: "Agney"*

&#x20;   *}*



&#x20;   *return <h1>Welcome Agney</h1>;*

*}*





##### **Visual Flow**

<App />

&#x20;       │

&#x20;       ▼

Calls App()

&#x20;       │

&#x20;       ▼

Returns



<Welcome />

<Welcome />

<Welcome />

&#x20;       │

&#x20;       ▼

React calls Welcome()



3 Times

&#x20;       │

&#x20;       ▼

Different props each time

&#x20;       │

&#x20;       ▼

Different Output



This is why React components are **reusable.**





##### **Props Destructuring**

Right now we write:

*function Welcome(props) {*

&#x20;   *return <h1>Welcome {props.name}</h1>;*

*}*



This works.



But React developers usually write:

*function Welcome({ name }) {*

&#x20;   *return <h1>Welcome {name}</h1>;*

*}*



This is a JavaScript feature.



Instead of:

*const name = props.name;*



JavaScript lets us write:

*const { name } = props;*



React simply combines that into the function parameter:



*function Welcome({ name }) {*

&#x20;   *return <h1>Welcome {name}</h1>;*

*}*



Nothing React-specific happened here.

It's just JavaScript **destructuring**.





##### **Predict exactly what will happen.**

When you click the button three times:



What will be printed in the console?

What will the browser display?



###### **The code**

*function App() {*



&#x20;   *let count = 0;*



&#x20;   *function increase() {*

&#x20;       *count++;*

&#x20;       *console.log(count);*

&#x20;   *}*



&#x20;   *return (*

&#x20;       *<>*

&#x20;           *<h1>{count}</h1>*



&#x20;           *<button onClick={increase}>*

&#x20;               *Increase*

&#x20;           *</button>*

&#x20;       *</>*

&#x20;   *);*

*}*



What happens when the page first loads?



React executes:

*App();*



At this moment:

*let count = 0;*



React renders:

Count: 0



So the browser shows:

0



**First Click**

The button calls:

*increase();*



Inside:

*count++;*



Now:

count = 1



Console prints:

1



✅ Correct.



But why doesn't the browser show 1?



Ask yourself:



###### **Who told React to execute App() again?**



Nobody.

React **rendered** the component once.

Changing this variable:

*count++;*



does not tell React:

"Hey, my UI has changed. Please render me again."



So React **never re-runs:**

App();



Therefore the browser still displays:

0



**Second Click**

Again:

*count++;*



Console:

2



Browser:

0



**Third Click**

Console:

3



Browser:

0



**Final Result**

Click	Console	Browser

Initial	—	0

Click 1	1	0

Click 2	2	0

Click 3	3	0



##### **Why?**

Because React only **updates** the UI when it **re-renders** the component.

Normal JavaScript variables don't trigger a re-render.



#### **This is exactly why useState() exists.**

Instead of:

*let count = 0;*



React gives us:

*const \[count, setCount] = useState(0);*



Now, instead of:

count++;



we do:

*setCount(count + 1);*



When React sees:

*setCount(...)*



it says:

**State changed!**

↓

Run App() again

↓

Update Virtual DOM

↓

Compare with previous Virtual DOM

↓

Update Real DOM

↓

Browser now shows new value



Notice how this connects to everything you've already learned:



useState()

↓

State Changes

↓

React Re-renders

↓

New Virtual DOM

↓

Reconciliation

↓

Real DOM Update



Everything we've studied since the beginning now fits together.



##### **React State**

*const \[count, setCount] = useState(0);*



*setCount(count + 1);*



State Changed

↓

React Knows

↓

Component Re-renders

↓

Virtual DOM

↓

Reconciliation

↓

Real DOM Updates

↓

UI Changes



#### **Understanding useState()**



Let's look at the famous line:

*const \[count, setCount] = useState(0);*



Most tutorials tell you:

"This creates a state variable."

That's true, but it doesn't explain **how it works**.



Let's build it from JavaScript.



##### **Step 1: What does useState(0) return?**



Imagine React internally has a function like this:

*function useState(initialValue) {*

&#x20;   *return \[initialValue, function];*

*}*



If you call:

*const result = useState(0);*



Then:

result = \[0, function]



Notice something?

It returns an array.



##### **Step 2: Array Destructuring**



Remember ES6?

*const numbers = \[10, 20];*



*const \[a, b] = numbers;*



*console.log(a); // 10*

*console.log(b); // 20*



Exactly the same thing happens here.



React returns:

*\[0, setFunction]*



We write:

*const \[count, setCount] = useState(0);*



So conceptually:

*count = 0*

*setCount = function*



###### **Visual Representation**

useState(0)

↓

Returns

↓

\[0, setCount]

↓

Destructuring

↓

count = 0



setCount = function



Nothing magical happened.

It's just JavaScript **array destructuring.**



#### **Let's Build Our First Counter**

Replace your App.jsx with this:



*import { useState } from "react";*



*function App() {*



&#x20; *const \[count, setCount] = useState(0);*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>Count: {count}</h1>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Increase*

&#x20;     *</button>*

&#x20;   *</>*

&#x20; *);*

*}*



**export default App;**

What Happens Internally?



Initially:

count = 0



Browser:

Count: 0



Click button.



React executes:

*setCount(count + 1);*



Since:

count = 0



React receives:

setCount(1);



**React now:**



Store new state

↓

Re-run App()

↓

count = 1

↓

Render again

↓

Browser shows



Count: 1



Click again:

setCount(2)



Browser:

Count: 2



Everything we've learned—**Virtual DOM, reconciliation, rendering**—is now happening behind the scenes.



##### **Why This Works**



Remember our earlier example?

*let count = 0;*

*count++;*



React had no idea the value changed.



Now:

*setCount(count + 1);*



does two things:

Updates the state.

Tells React to re-render.



That's the key difference.





##### **Let's Build Our First Counter**



Replace your App.jsx with this:



*import { useState } from "react";*



*function App() {*



&#x20; *const \[count, setCount] = useState(0);*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>Count: {count}</h1>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Increase*

&#x20;     *</button>*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



**Instead of:**

*<button onClick={() => setCount(count + 1)}>*

&#x20;   *Increase*

*</button>*



write:



*<button onClick={() => {*



&#x20;   *console.log("Before:", count);*



&#x20;   *setCount(count + 1);*



&#x20;   *console.log("After:", count);*



*}}>*

&#x20;   *Increase*

*</button>*

Before you run it...



Predict the output.



When you click the button once, what will the console show?



**Option A**

Before: 0

After: 1



**Option B**

Before: 0

After: 0



**Option C**

Before: 1

After: 1



**ANSWER: B**



Initially:

count = 0



###### **Step 1**

*console.log("Before:", count);*



Console:

Before: 0



###### **Step 2**

*setCount(count + 1);*



Does React immediately do this?

count = 1



**❌ No.**



Instead, React says:

"Okay, I received your request."



"I'll update the state after this event handler finishes."



Think of it as adding the update to a **queue.**



###### **Step 3**



Immediately after:

*console.log("After:", count);*



React hasn't re-rendered yet.



So count is still:

0



Console:

After: 0



Then What Happens?

Only after the click handler finishes:



Button Click

↓

setCount(1)

↓

Event Handler Ends

↓

React updates state

↓

React re-runs App()

↓

count becomes 1

↓

UI updates



So the browser shows:



Count: 1



But inside that same click handler, count was still 0.



###### **This Is Called an Asynchronous State Update**

It's not that React is "slow."

It's that React **batches** updates to make **rendering efficient.**

Instead of re-rendering immediately after every single setCount(), React waits until the current event is finished, then performs the update.



Calling setCount() **schedules** a **state update**. It **does not immediately** change the value of count in the current render.





##### **So How Do We Actually Increment Twice?**

React gives us **another** **form** of setState.



Instead of:

*setCount(count + 1);*



we write:

*setCount(previous => previous + 1);*



Notice something?

We're not using count anymore.



We're using:

*previous*



React supplies the latest state each time.



Now:

*setCount(previous => previous + 1);*



*setCount(previous => previous + 1);*



works like this:

previous = 0

↓

1



↓

previous = 1

↓

2



Browser finally shows:

2



This is called the **functional** **updater**, and it's the recommended approach whenever the next state **depends** on the previous state.



##### **Compare the Two Cases**

###### **Case 1**

*setCount(count + 1);*

*setCount(count + 1);*



React receives:

Update state to 1

Update state to 1



Both updates were calculated using the same old value.



Final state:

1



###### **Case 2**

*setCount(previous => previous + 1);*

*setCount(previous => previous + 1);*



React receives two functions, not two values.



Conceptually:

Update #1



previous = 0

↓

return 1



Now React immediately passes that updated value to the next updater:

Update #2



previous = 1

↓

return 2



If there is a third updater:

Update #3



previous = 2

↓

return 3



So React processes the queue like this:



Initial State = 10

↓

Updater #1

11

↓

Updater #2

12

↓

Updater #3

13

↓

Re-render



This is why the functional updater is so powerful.



###### **The Golden Rule**

Whenever your new state depends on the previous state, prefer:

*setCount(previous => previous + 1);*



instead of:

*setCount(count + 1);*



This is considered a React best practice.





