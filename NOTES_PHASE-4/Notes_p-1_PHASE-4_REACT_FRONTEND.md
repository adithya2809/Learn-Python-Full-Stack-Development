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

&#x20;         │

&#x20;         ▼

<script src="/src/main.jsx">

&#x20;         │

&#x20;         ▼

&#x20;      main.jsx

&#x20;         │

&#x20;         ▼

&#x20;Imports App.jsx

&#x20;         │

&#x20;         ▼

&#x20;Renders <App />

&#x20;         │

&#x20;         ▼

&#x20;Places it inside

<div id="root"></div>

&#x20;         │

&#x20;         ▼

&#x20;Browser shows UI



Everything begins here.



##### **Line 1**

*import { StrictMode } from 'react'*



What is import?

You've already seen this in Python.



Python:

*from math import sqrt*



**React:**

*import { StrictMode } from 'react'*



Same concept.

You're importing something from another module.



###### **What is StrictMode?**



This confuses almost every beginner.

StrictMode does NOT affect your users.



It is only **active during development.**



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

"Hey...

This could become a bug later."



**In production:**

npm run build

↓

StrictMode disappears



It does not make your application slower for users.



##### **Line 2**

*import { createRoot } from 'react-dom/client'*



This is probably the **most important** import.



Notice something interesting.



We imported from:

react

Earlier.



Now we're importing from:

*react-dom/client*



Why two different packages?

Because they do different jobs.



###### **React**

React understands:

Components

JSX

State

Hooks



It knows what the UI should be.



###### **ReactDOM**

ReactDOM knows **how to display** that UI inside a web browser.



Think of it like this:

React

↓

Creates UI Description

↓

ReactDOM

↓

Displays it in Browser



###### **What is createRoot()?**



Imagine your HTML:

*<div id="root"></div>*



React asks:

"Where should I place my application?"



The answer:

*document.getElementById("root")*



That gives React this element:

*<div id="root"></div>*



Then:

createRoot(...)



creates a **React root** inside it.



Think of it as:



Empty Container

↓

React takes **ownership**

↓

Everything will be **rendered** here



##### **Line 3**

*import './index.css'*



Simple.

It imports the global stylesheet.



Exactly like:

*<link rel="stylesheet" href="style.css">*



in HTML.



##### **Line 4**

*import App from './App.jsx'*



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



##### **Now the Most Important Line**

*createRoot(document.getElementById('root')).render(*



Let's break it apart.



###### **Part 1**

*document.getElementById("root")*



Does this look familiar?



You've probably used it in JavaScript before.



It searches:

*<div id="root"></div>*

and returns it.



###### **Part 2**

*createRoot(...)*



Now React says:

"Great.

I know where to render."



###### **Part 3**

*.render(...)*



Now React says:

"Render this component inside that root."





###### **What is Render?**

Render means:

**Convert** React components into **actual DOM elements** and **display** them.



So this:

<App />

becomes **real HTML** on your **webpage.**





###### **Why <App />?**

Notice:

<App />



instead of

App()



**Why?**

Because React components are represented using **JSX syntax.**



Behind the scenes:

<App />



is conceptually similar to:

*React.createElement(App)*



React then calls your component function when it needs to produce the UI.





##### **Finally**

*<StrictMode>*

*<App />*

*</StrictMode>*



means



Run App

↓

Monitor for Problems

↓

Show Warnings

↓

Help Developer



Nothing more.



##### **Entire Flow**

index.html

↓

<div id="root"></div>

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

