# REACT FRONTEND PART-2



#### **Lesson 12 — Build Your First Interactive React App**



We're going to build a small Counter App.

The goal isn't the counter itself. It's to make sure you can independently use the concepts you've learned.



We'll have:

&#x20;       Counter

&#x20;         0



&#x20;  \[-]   \[+]   \[Reset]



&#x20;    Count is at zero



And we'll add one rule:

The count should never go below 0.



##### **Step 1 — Start with the state**

In App.jsx:



*import { useState } from "react";*



*function App() {*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>Counter</h1>*

&#x20;     *<h2>{count}</h2>*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



At this point:

count = 0



and:



{count}

displays the current state.



##### **Step 2 — Add Increase**



Add:

*<button onClick={() => setCount(count + 1)}>*

&#x20; +

*</button>*



Now:

0

&#x20;↓

Click +

&#x20;↓

1

&#x20;↓

Click +

&#x20;↓

2



##### **Step 3 — Add Decrease**

We could simply write:

*<button onClick={() => setCount(count - 1)}>*

&#x20; -

*</button>*



But there's a problem.



The user could do:

0 → -1 → -2 → -3...



We don't want that.

So we need a condition.



##### **Step 4 — Conditional Logic**

We can use the ternary operator we learned earlier:

*count > 0 ? count - 1 : 0*



Meaning:

Is count greater than 0?



&#x20;      YES → subtract 1

&#x20;      NO  → stay at 0



So:

*<button onClick={() => setCount(count > 0 ? count - 1 : 0)}>*

&#x20; -

*</button>*



##### **Step 5 — Reset**

That's easy:

*<button onClick={() => setCount(0)}>*

&#x20; *Reset*

*</button>*



We're simply telling React:

Set the state back to 0.



##### **Step 6 — Add a Dynamic Message**



Now let's use conditional rendering.



We want:

count = 0

→ Count is at zero



and:

count > 0

→ You're counting!



We can use:

<p>

&#x20; {count === 0 ? "Count is at zero" : "You're counting!"}

</p>



Notice we're using an expression inside {}.



##### **Your Complete App**

Put this into App.jsx:



*import { useState } from "react";*



*function App() {*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>Counter</h1>*



&#x20;     *<h2>{count}</h2>*



&#x20;     *<button onClick={() => setCount(count > 0 ? count - 1 : 0)}>*

&#x20;       *-*

&#x20;     *</button>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *+*

&#x20;     *</button>*



&#x20;     *<button onClick={() => setCount(0)}>*

&#x20;       *Reset*

&#x20;     *</button>*



&#x20;     *<p>*

&#x20;       *{count === 0 ? "Count is at zero" : "You're counting!"}*

&#x20;     *</p>*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



Run it and test:

Click + several times.

Click -.

Keep clicking - when the count is 0.

Click Reset.

Observe the message changing.





#### **Lesson 13 — React Event Handling**



You've already used:

*<button onClick={() => setCount(count + 1)}>*

&#x20; *Increase*

*</button>*



Now let's understand why this syntax works and why this doesn't:

*<button onClick={increase()}>*

&#x20; *Increase*

*</button>*



This distinction is extremely important.



##### **1. Define the function**

Instead of putting everything inside the JSX:



*function App() {*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *function increase() {*

&#x20;   *setCount(count + 1);*

&#x20; *}*



&#x20; *return (*

&#x20;   *<button onClick={increase}>*

&#x20;     *Increase*

&#x20;   *</button>*

&#x20; *);*

*}*



Here:

onClick={increase}



means:

"React, here's the function. Call it when the user clicks."



The function isn't executed yet.



##### **2. Why not increase()?**



If you write:



*<button onClick={increase()}>*

&#x20; *Increase*

*</button>*



the parentheses mean:

Execute increase() right now.



So when React renders the component:



App renders

&#x20;  ↓

increase() executes immediately

&#x20;  ↓

setCount(...)

&#x20;  ↓

React renders again

&#x20;  ↓

increase() executes again

&#x20;  ↓

...



You can end up with an unwanted render/update loop.



##### **The Difference**



###### **Pass the function ✅**

*onClick={increase}*



Means:

"Here's the function.

Call it later when clicked."



###### **Call the function ❌**

*onClick={increase()}*



Means:

"Execute this function right now

and give me its result."



##### **3. Why does the arrow function version work?**



You used:

*onClick={() => setCount(count + 1)}*



This is actually a function too.



Conceptually:

*() => setCount(count + 1)*



means:

Create a function

↓

Don't execute it yet

↓

React will call it when clicked



So these are functionally similar:

**Method 1**

*function increase() {*

&#x20; *setCount(count + 1);*

*}*



*<button onClick={increase}>*

&#x20; *Increase*

*</button>*



**Method 2**

*<button onClick={() => setCount(count + 1)}>*

&#x20; *Increase*

*</button>*



##### **4. Why do we sometimes need the arrow function?**



Consider:

*function increase() {*

&#x20; *setCount(count + 1);*

*}*



We can simply pass:

*onClick={increase}*



But suppose we need to pass an argument:



*function increase(amount) {*

&#x20; *setCount(count + amount);*

*}*



Now we want:

*<button onClick={increase(5)}>*

&#x20; *Increase by 5*

*</button>*



❌ That's wrong because increase(5) executes immediately.



Instead:

*<button onClick={() => increase(5)}>*

&#x20; *Increase by 5*

*</button>*



Now the arrow function waits for the click.



Click

&#x20;↓

() => increase(5)

&#x20;↓

increase(5)



This pattern is extremely common.



##### **5. React's Event Object**



React also gives your event handler an event object.



Example:

*function handleClick(event) {*

&#x20; *console.log(event);*

*}*



Then:

*<button onClick={handleClick}>*

&#x20; *Click Me*

*</button>*



When you click, React passes information about the event into the function.



For example:

event

├── target

├── type

├── currentTarget

└── ...



We'll use this heavily with **forms.**



##### **6. Example**

*function handleClick(event) {*

&#x20; *console.log("Button clicked!");*

&#x20; *console.log(event.target);*

*}*



The event.target refers to the element that triggered the event.



For:

*<button onClick={handleClick}>*

&#x20; *Click*

*</button>*



the target is that button.



##### **7. Common React Events**



You'll frequently encounter:

onClick

onChange

onSubmit

onFocus

onBlur

onMouseEnter

onKeyDown



For our API integration later, the most important ones will be:

onChange

onSubmit

onClick



For example, our login form will eventually look conceptually like:

*<form onSubmit={handleLogin}>*



and:

*<input onChange={handleUsernameChange} />*



Those events will eventually trigger calls to your API authentication endpoints.





#### **Controlled Inputs**



Before moving to useEffect, we need one very important React skill:



**Forms and controlled inputs**



We'll build:



Name:    \[\_\_\_\_\_\_\_\_\_\_\_\_]



Email:   \[\_\_\_\_\_\_\_\_\_\_\_\_]



Password:\[\_\_\_\_\_\_\_\_\_\_\_\_]



&#x20;        \[ Register ]



And you'll learn why React applications usually do:



*<input*

&#x20; *value={username}*

&#x20; *onChange={...}*

*/>*



instead of letting the browser manage the input independently.

This is directly relevant to our eventual Login/Register pages, where the values will be sent to your backend.



**Look at this:**

*const \[name, setName] = useState("");*



*<input*

&#x20; *value={name}*

&#x20; *onChange={(event) => setName(event.target.value)}*

*/>*



There are two directions happening.



###### **User → React**

User types

&#x20;  ↓

onChange

&#x20;  ↓

event.target.value

&#x20;  ↓

setName(...)

&#x20;  ↓

React state



###### **React → Input**

React state

&#x20;  ↓

value={name}

&#x20;  ↓

Input displays current state



So React is controlling the input's value.



That's why it's called a **controlled component.**



&#x20;         React State

&#x20;         name = "Agney"

&#x20;            ↕

&#x20;      ┌─────────────┐

&#x20;      │   <input>   │

&#x20;      └─────────────┘

&#x20;            ↕

&#x20;         User types



##### **Complete flow**

User types

&#x20;   ↓

onChange fires

&#x20;   ↓

event.target.value

&#x20;   ↓

setEmail(newValue)

&#x20;   ↓

React updates state

&#x20;   ↓

React re-renders App

&#x20;   ↓

email contains latest value

&#x20;   ↓

{email}

&#x20;   ↓

<p> displays latest value



**For example, when the user types a:**

"a"

&#x20;↓

setEmail("a")

&#x20;↓

state = "a"

&#x20;↓

re-render

&#x20;↓

<p>a</p>



**Then they type g:**

"ag"

&#x20;↓

setEmail("ag")

&#x20;↓

state = "ag"

&#x20;↓

re-render

&#x20;↓

<p>ag</p>



That's the controlled input pattern. 





