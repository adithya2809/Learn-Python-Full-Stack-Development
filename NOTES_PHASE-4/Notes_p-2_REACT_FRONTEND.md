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





#### **Lesson 14 — React Forms \& onSubmit**



You've already learned how a single controlled input works:

*const \[email, setEmail] = useState("");*



*<input*

&#x20; *value={email}*

&#x20; *onChange={(event) => setEmail(event.target.value)}*

*/>*



Now we'll put multiple inputs inside a form.

This is directly preparing us for our eventual **Login and Register pages**.



##### **1. The Basic Form**



A normal HTML form looks like:

*<form>*

&#x20;   *<input>*

&#x20;   *<button type="submit">Submit</button>*

*</form>*



In **React**, we do:

*<form onSubmit={handleSubmit}>*

&#x20;   *...*

*</form>*



The important difference is:

*onSubmit={handleSubmit}*



We're telling React:

"When this form is submitted, call handleSubmit."



##### **2. Create the Submit Handler**

*function handleSubmit(event) {*

&#x20;   *event.preventDefault();*



&#x20;   *console.log("Form submitted");*

*}*



Now:

*<form onSubmit={handleSubmit}>*



When the user clicks Submit:

Submit button

&#x20;     ↓

Form submission

&#x20;     ↓

onSubmit

&#x20;     ↓

handleSubmit()

&#x20;     ↓

"Form submitted"



##### **3. Why event.preventDefault()?**

This is important.



By default, an HTML form submission causes the browser to perform its traditional form behavior, which can include navigating/reloading the page.

We don't want that in a React application.



Instead:

*event.preventDefault();*



means:

"Stop the browser's default form submission behavior. Let React handle it."



So:

**Without preventDefault()**

&#x20;       ↓

Browser handles form

&#x20;       ↓

Possible page reload/navigation



**With preventDefault()**

&#x20;       ↓

React handles form

&#x20;       ↓

We control what happens



This becomes especially important when we eventually send the form data to API using fetch().



##### **4. Multiple Controlled Inputs**

Let's build a small login-style form.



*import { useState } from "react";*



*function App() {*

&#x20; *const \[username, setUsername] = useState("");*

&#x20; *const \[password, setPassword] = useState("");*



&#x20; *function handleSubmit(event) {*

&#x20;   *event.preventDefault();*



&#x20;   *console.log(username);*

&#x20;   *console.log(password);*

&#x20; *}*



&#x20; *return (*

&#x20;   *<form onSubmit={handleSubmit}>*

&#x20;     *<input*

&#x20;       *type="text"*

&#x20;       *value={username}*

&#x20;       *onChange={(event) => setUsername(event.target.value)}*

&#x20;     */>*



&#x20;     *<input*

&#x20;       *type="password"*

&#x20;       *value={password}*

&#x20;       *onChange={(event) => setPassword(event.target.value)}*

&#x20;     */>*



&#x20;     *<button type="submit">*

&#x20;       *Login*

&#x20;     *</button>*

&#x20;   *</form>*

&#x20; *);*

*}*



*export default App;*



Now we have two separate pieces of state:

username → state

password → state



##### **5. What Happens When the User Types?**



Suppose the user enters:

username: Agney

password: hello123



**For username:**



User types "Agney"

&#x20;      ↓

onChange

&#x20;      ↓

event.target.value

&#x20;      ↓

setUsername("Agney")

&#x20;      ↓

username state = "Agney"



**For password:**



User types "hello123"

&#x20;      ↓

onChange

&#x20;      ↓

event.target.value

&#x20;      ↓

setPassword("hello123")

&#x20;      ↓

password state = "hello123"



Then the user clicks:

Login



The form executes:

*handleSubmit(event)*



and:

*event.preventDefault();*

prevents the browser from doing its default form submission.



Then:

*console.log(username);*

*console.log(password);*



prints:

Agney

hello123



##### **6. Important: type="submit"**

Notice:



*<button type="submit">*

&#x20; *Login*

*</button>*



This tells the browser:

This button submits the form.



Because it's inside:

*<form onSubmit={handleSubmit}>*



clicking it triggers:

button

&#x20;↓

form submit

&#x20;↓

onSubmit

&#x20;↓

handleSubmit()



This is better than putting onClick on the Login button for form submission.



**Why?**

Because a form can also be submitted by pressing Enter inside an input.



With onSubmit, both cases are handled:

Click Login

&#x20;     ↓

&#x20;  onSubmit



Press Enter

&#x20;     ↓

&#x20;  onSubmit



That's why we generally use onSubmit for forms.



##### **7. From Here to Backend**



Eventually:



React Login Form

&#x20;      ↓

username

password

&#x20;      ↓

handleSubmit()

&#x20;      ↓

fetch()

&#x20;      ↓

API /login

&#x20;      ↓

JWT

&#x20;      ↓

React stores authentication state

&#x20;      ↓

Dashboard





##### **Lesson 15 — Objects in React State**

So far, we've used separate state variables:

*const \[username, setUsername] = useState("");*

*const \[email, setEmail] = useState("");*

*const \[password, setPassword] = useState("");*



Now let's combine them into one object.

*const \[formData, setFormData] = useState({*

&#x20; *username: "",*

&#x20; *email: "",*

&#x20; *password: ""*

*});*



The state looks like:

formData

│

├── username: ""

├── email: ""

└── password: ""



This is useful for forms with many fields.



###### **The Problem**

Suppose the user types:

Agney



We might think:

*formData.username = "Agney";*



But ❌ don't do this in React.



**Why?**

Because you're directly modifying the existing state object.



React expects us to use the setter:

***setFormData(...)***



to tell it that state has changed.



##### **The Solution — Spread Operator**



Remember JavaScript's spread operator?

*const user = {*

&#x20; *name: "Agney",*

&#x20; *age: 22*

*};*



*const updatedUser = {*

&#x20; *...user,*

&#x20; *age: 23*

*};*



The ...user copies the existing properties:

{

&#x20; name: "Agney",

&#x20; age: 22

}



Then:

age: 23



overwrites the old age.



Result:

{

&#x20; name: "Agney",

&#x20; age: 23

}



##### **Apply This to React**

Our state:



*const \[formData, setFormData] = useState({*

&#x20; *username: "",*

&#x20; *email: "",*

&#x20; *password: ""*

*});*



Suppose the user types "Agney".



We can update only username:



*setFormData({*

&#x20; *...formData,*

&#x20; *username: "Agney"*

*});*



React now gets a new object:

{

&#x20; username: "Agney",

&#x20; email: "",

&#x20; password: ""

}



The other fields weren't lost.



##### **Why Is ...formData Important?**



Suppose you wrote:

*setFormData({*

&#x20; *username: "Agney"*

*});*



You might expect:

{

&#x20; username: "Agney",

&#x20; email: "",

&#x20; password: ""

}



But that's not what happens.



The new state becomes:

{

&#x20; username: "Agney"

}



The old email and password properties are gone.



That's why we spread the existing object:

***setFormData({***

&#x20; ***...formData,***

&#x20; ***username: "Agney"***

***});***



Now Connect It to onChange



We can write:



*<input*

&#x20; *value={formData.username}*

&#x20; *onChange={(event) =>*

&#x20;   *setFormData({*

&#x20;     *...formData,*

&#x20;     *username: event.target.value*

&#x20;   *})*

&#x20; *}*

*/>*



The flow becomes:



User types

&#x20;   ↓

onChange

&#x20;   ↓

event.target.value

&#x20;   ↓

copy existing formData

&#x20;   ↓

replace username

&#x20;   ↓

setFormData()

&#x20;   ↓

React re-renders

&#x20;   ↓

input displays new value



##### **But There's a Better Pattern**

If we have:

username

email

password



we don't want to write three different handlers.



We can use the input's name:

*<input*

&#x20; *name="username"*

&#x20; *value={formData.username}*

&#x20; *onChange={handleChange}*

*/>*



Then:

*function handleChange(event) {*

&#x20; *const { name, value } = event.target;*



&#x20; *setFormData({*

&#x20;   *...formData,*

&#x20;   *\[name]: value*

&#x20; *});*

*}*



This might look strange:

*\[name]: value*



But remember JavaScript's computed property names.



If:

*name = "username"*

*value = "Agney"*



then:

*\[name]: value*



becomes:

***username: "Agney"***



If:

*name = "email"*

*value = "agney@example.com"*



it becomes:

***email: "agney@example.com"***



So one handler can handle multiple inputs.





*import {useState} from "react";*









*function App(){*

&#x20; *const \[formData,setFormData]=useState({*

&#x20;   *"username":"",*

&#x20;   *"email":"",*

&#x20;   *"password":""*

&#x20; *})*



&#x20; *function handleChange(event){*

&#x20;   *const\[name,value]*

&#x20; *}*

&#x20; *function handleSubmit(event){*

&#x20;   *event.preventDefault();*



&#x20;   *console.log(username);*

&#x20;   *console.log(email);*

&#x20;   *console.log(password);*

&#x20; *}*



&#x20; *return(*

&#x20;   *<>*

&#x20;   *<form onSubmit={handleSubmit}>*

&#x20;     *<input type="text" name="username" value={formDatausername}* 

&#x20;     *onChange={(event)=> setUsername(event.target.value)}/>*





