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





