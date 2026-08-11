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





#### **Lesson 16 — Fetch API**

So far, our data has stayed inside React:



React Form

&#x20;  ↓

formData

&#x20;  ↓

console.log()



**But our actual goal is:**

React

&#x20;  ↓

HTTP Request

&#x20;  ↓

FastAPI/Backend

&#x20;  ↓

Database



The browser needs a way to make that HTTP request.



That's where fetch() comes in.



##### **1. What is fetch()?**

fetch() is a JavaScript API used to make HTTP requests.



For example:

fetch("http://localhost:8000/students");



This means:

"Browser, send an HTTP request to this URL."



By default, fetch() makes a GET request.



So conceptually:

React

&#x20; ↓

fetch()

&#x20; ↓

GET /students

&#x20; ↓

FastAPI



##### **2. GET Request**

Suppose your FastAPI backend has:



*@app.get("/students")*

*def get\_students():*

&#x20;   *...*



React can request it:

fetch("http://localhost:8000/students");



But there's an important thing:

fetch() returns a Promise.



##### **3. Using async/await**

We can write:

*async function getStudents() {*

&#x20; *const response = await fetch(*

&#x20;   *"http://localhost:8000/students"*

&#x20; *);*



&#x20; *console.log(response);*

*}*



The flow is:

getStudents()

&#x20;     ↓

fetch()

&#x20;     ↓

HTTP request

&#x20;     ↓

Wait for FastAPI response

&#x20;     ↓

response



##### **4. But response Isn't Yet the JSON Data**

This is an important distinction.



Suppose FastAPI returns:



\[

&#x20; {

&#x20;   "id": 1,

&#x20;   "name": "Agney"

&#x20; },

&#x20; {

&#x20;   "id": 2,

&#x20;   "name": "Rahul"

&#x20; }

]



After:

*const response = await fetch(url);*



response is a Response object.



It contains information about the HTTP response, such as:

response

├── status

├── ok

├── headers

└── body



To extract the JSON body, we use:

*const data = await response.json();*



So:

*async function getStudents() {*

&#x20; *const response = await fetch(*

&#x20;   *"http://localhost:8000/students"*

&#x20; *);*



&#x20; *const data = await response.json();*



&#x20; *console.log(data);*

*}*



Now data contains the actual JavaScript representation of the JSON.



##### **5. The Two awaits**



This is worth understanding.



***const response = await fetch(url);***



means:

Wait for the **HTTP response.**



Then:

***const data = await response.json();***



means:

Wait for the response body to be parsed as **JSON**.



So:

await fetch()

&#x20;     ↓

Response object

&#x20;     ↓

await response.json()

&#x20;     ↓

Actual data



##### **6. Checking HTTP Status**

Suppose FastAPI returns:

200 OK



or:



404 Not Found



or:



401 Unauthorized



You can inspect:

*response.status*



For example:

*if (response.ok) {*

&#x20; *console.log("Request successful");*

*} else {*

&#x20; *console.log("Request failed:", response.status);*

*}*



response.ok is true for successful HTTP responses in the 2xx range.



##### **7. POST Request**

Now we get to something directly relevant to your registration form.



Suppose:

*const formData = {*

&#x20; *username: "Agney",*

&#x20; *email: "agney@example.com",*

&#x20; *password: "abc123"*

*};*



We want to send this to FastAPI.



We use:

*fetch("http://localhost:8000/register", {*

&#x20; *method: "POST",*



&#x20; *headers: {*

&#x20;   *"Content-Type": "application/json"*

&#x20; *},*



&#x20; *body: JSON.stringify(formData)*

*});*



**Let's break this apart.**



###### **method**

*method: "POST"*



Tells the server:

This is a POST request.



###### **headers**

*headers: {*

&#x20; *"Content-Type": "application/json"*

*}*



Tells FastAPI:

The body I'm sending is JSON.



This is important because your FastAPI endpoint might expect a Pydantic model.



For example:

*class UserRegister(BaseModel):*

&#x20;   *username: str*

&#x20;   *email: str*

&#x20;   *password: str*



The JSON sent by React:

*{*

&#x20; *"username": "Agney",*

&#x20; *"email": "agney@example.com",*

&#x20; *"password": "abc123"*

*}*



can then be validated by FastAPI/Pydantic.



##### **8. Why JSON.stringify()?**

Your React state is a JavaScript object:



*formData = {*

&#x20; *username: "Agney",*

&#x20; *email: "agney@example.com",*

&#x20; *password: "abc123"*

*};*



But HTTP request bodies are transmitted as data, and for a JSON API we need to convert the JavaScript object into a JSON string.



So:

*JSON.stringify(formData)*



produces:

*"{\\"username\\":\\"Agney\\",\\"email\\":\\"agney@example.com\\",\\"password\\":\\"abc123\\"}"*



Conceptually:

JavaScript object

&#x20;      ↓

JSON.stringify()

&#x20;      ↓

JSON

&#x20;      ↓

HTTP request

&#x20;      ↓

FastAPI



##### **9. Complete POST Example**

*async function registerUser() {*

&#x20; *const formData = {*

&#x20;   *username: "Agney",*

&#x20;   *email: "agney@example.com",*

&#x20;   *password: "abc123"*

&#x20; *};*



&#x20; *const response = await fetch(*

&#x20;   *"http://localhost:8000/register",*

&#x20;   *{*

&#x20;     *method: "POST",*

&#x20;     *headers: {*

&#x20;       *"Content-Type": "application/json"*

&#x20;     *},*

&#x20;     *body: JSON.stringify(formData)*

&#x20;   *}*

&#x20; *);*



&#x20; *const data = await response.json();*



&#x20; *console.log(data);*

*}*



This is essentially the bridge between what you've already learned in FastAPI and what we're learning now in React.



##### **10. Connecting It to Your Form**

Eventually our form will look like:

User

&#x20;↓

fills form

&#x20;↓

formData

&#x20;↓

Submit

&#x20;↓

handleSubmit()

&#x20;↓

fetch()

&#x20;↓

POST /register

&#x20;↓

FastAPI

&#x20;↓

Database



And later for login:

User

&#x20;↓

username + password

&#x20;↓

React

&#x20;↓

POST /login

&#x20;↓

FastAPI

&#x20;↓

JWT

&#x20;↓

React

&#x20;↓

Protected Dashboard



That's the actual destination of Phase 4.





#### **Lesson 17 — CORS**

Right now you have:

React

localhost:5173

&#x20;      ↓

&#x20;    fetch()

&#x20;      ↓

FastAPI

localhost:8000



You might think:

"They're both running on my computer, so why can't React just call FastAPI?"



Because the browser sees these as different origins.



React:

http://localhost:5173



FastAPI:

http://localhost:8000



The port is different, so the origins are different.



##### **What is CORS?**



CORS stands for:

**Cross-Origin Resource Sharing**



It is a **browser security mechanism** that controls whether a frontend from one origin is allowed to access resources from another origin.



So when React tries:

*fetch("http://localhost:8000/register", {*

&#x20; *method: "POST",*

&#x20; *...*

*});*



the browser checks whether FastAPI allows the React origin.



If FastAPI hasn't allowed it, the browser can block the frontend from accessing the response.



##### **Configure FastAPI**

You already worked with FastAPI middleware in Phase 3 concepts, so this should look familiar.



In your FastAPI application:

*from fastapi import FastAPI*

*from fastapi.middleware.cors import CORSMiddleware*



*app = FastAPI()*



*app.add\_middleware(*

&#x20;   *CORSMiddleware,*

&#x20;   *allow\_origins=\["http://localhost:5173"],*

&#x20;   *allow\_credentials=True,*

&#x20;   *allow\_methods=\["\*"],*

&#x20;   *allow\_headers=\["\*"],*

*)*



The important line for our development setup is:

*allow\_origins=\["http://localhost:5173"]*



This tells FastAPI:

Allow requests coming from my React development server.



What Each Option Means



***allow\_origins***

allow\_origins=\["http://localhost:5173"]



Which frontend origins are allowed?

We're allowing your Vite React app.



***allow\_methods***

*allow\_methods=\["\*"]*



Allows HTTP methods such as:

GET

POST

PUT

PATCH

DELETE



The \* means all methods.

For development, that's convenient.



***allow\_headers***

*allow\_headers=\["\*"]*



Allows request headers.

This will become particularly important later when we send:

Authorization: Bearer <JWT>

to your protected FastAPI endpoints.



***allow\_credentials***

*allow\_credentials=True*



Allows credential-related cross-origin requests.

We'll discuss exactly when this matters when we get to authentication and JWTs.





#### **Now connect React → FastAPI**

Change your current handleSubmit() from:



*function handleSubmit(event) {*

&#x20; *event.preventDefault();*



&#x20; *console.log(formData);*

*}*



**to:**



*async function handleSubmit(event) {*

&#x20; *event.preventDefault();*



&#x20; *const response = await fetch("http://localhost:8000/register", {*

&#x20;   *method: "POST",*

&#x20;   *headers: {*

&#x20;     *"Content-Type": "application/json"*

&#x20;   *},*

&#x20;   *body: JSON.stringify(formData)*

&#x20; *});*



&#x20; *const data = await response.json();*



&#x20; *console.log(data);*

*}*



That's your first real frontend → backend request.



##### **Let's trace exactly what happens**

Suppose you enter:



Username: Agney

Email: test@gmail.com

Password: abc123



Your React state becomes:

*{*

&#x20; *username: "Agney",*

&#x20; *email: "test@gmail.com",*

&#x20; *password: "abc123"*

*}*



Then you click Register.



###### **1. Form submission**

*<form onSubmit={handleSubmit}>*

↓

*handleSubmit(event)*



###### **2. Prevent normal browser submission**

*event.preventDefault();*

↓



The page doesn't reload.



###### **3. Send request**

*fetch("http://localhost:8000/register", {*



with:

*method: "POST"*



and:

*headers: {*

&#x20; *"Content-Type": "application/json"*

*}*



and:



*body: JSON.stringify(formData)*



The actual JSON sent to FastAPI is:

*{*

&#x20; *"username": "Agney",*

&#x20; *"email": "test@gmail.com",*

&#x20; *"password": "abc123"*

*}*



###### **4. FastAPI receives it**



Your endpoint:

*@router.post("/register", response\_model=UserResponse)*

*def register(user: UserCreate, db: Session = Depends(get\_db)):*



FastAPI/Pydantic validates the incoming JSON against:

UserCreate



Then your code checks:

existing\_user



and:

existing\_email



If everything is valid:

hash password

&#x20;    ↓

create Users object

&#x20;    ↓

db.add()

&#x20;    ↓

db.commit()

&#x20;    ↓

return db\_user



Your endpoint returns:

201 Created



because you specified:

*status\_code=status.HTTP\_201\_CREATED*



###### **5. React receives the response**



This:

*const response = await fetch(...);*



gives us the HTTP response.



Then:

*const data = await response.json();*



extracts the JSON returned by FastAPI.



So:

*console.log(data);*



should show the data corresponding to your UserResponse.





#### **Proper Success \& Error Handling**



Right now we're doing:

*const data = await response.json();*

*console.log(data);*



But a real application shouldn't just print the response.



We want the UI to say something like:

Registration successful! 🎉



or:



Username already exists



So let's introduce state for the API response.



Add:

*const \[message, setMessage] = useState("");*

*const \[error, setError] = useState("");*



Then modify your submit handler:



*async function handleSubmit(event) {*

&#x20; *event.preventDefault();*



&#x20; *setMessage("");*

&#x20; *setError("");*



&#x20; *const response = await fetch("http://localhost:8000/register", {*

&#x20;   *method: "POST",*

&#x20;   *headers: {*

&#x20;     *"Content-Type": "application/json"*

&#x20;   *},*

&#x20;   *body: JSON.stringify(formData)*

&#x20; *});*



&#x20; *const data = await response.json();*



&#x20; *if (response.ok) {*

&#x20;   *setMessage("Registration successful!");*

&#x20; *} else {*

&#x20;   *setError(data.detail);*

&#x20; *}*

*}*



Then in your JSX:

*{message \&\& <p>{message}</p>}*

*{error \&\& <p>{error}</p>}*



##### **Why response.ok?**



You already saw:

201 → success

400 → error



Instead of manually checking every status code:

*if (response.status === 201)*



we can use:

*if (response.ok)*



response.ok is true for successful 2xx responses and false otherwise.



So:

201 → response.ok = true

400 → response.ok = false



##### **Why setMessage("") and setError("")?**

Imagine this sequence:



First attempt

→ Registration successful!



Second attempt

→ Username already exists



If we don't clear the previous message, the UI could potentially retain stale information.



So at the beginning:

*setMessage("");*

*setError("");*



we reset the previous result before processing the new request.





#### **Lesson 18 — Loading, Errors \& try/catch/finally**



Our registration request currently handles HTTP errors like 400, but there's another type of failure we need to handle.



For example:

React

&#x20;↓

fetch()

&#x20;↓

Network failure ❌

&#x20;↓

No response



Maybe FastAPI isn't running, the server is unreachable, or the network connection fails.



In that situation, we need **try/catch.**



##### **1. Loading State**

Add:

*const \[loading, setLoading] = useState(false);*



This represents:

*loading = false*

→ no request currently running



*loading = true*

→ request currently running



Our submit handler becomes:

*async function handleSubmit(event) {*

&#x20; *event.preventDefault();*



&#x20; *setMessage("");*

&#x20; *setError("");*

&#x20; *setLoading(true);*



&#x20; *// API request...*



&#x20; *setLoading(false);*

*}*



##### **2. Why try/catch?**

Consider:

*const response = await fetch("http://localhost:8000/auth/register");*



What if FastAPI isn't running?

There may be no HTTP response at all.



That's different from:

400 Bad Request



A 400 is still a valid HTTP response.



But a network failure means the request itself failed.



So we use:

***try {***

&#x20; ***// request***

***} catch (error) {***

&#x20; ***// network/unexpected error***

***}***



##### **3. try/catch**

Our handler can become:

*async function handleSubmit(event) {*

&#x20; *event.preventDefault();*



&#x20; *setMessage("");*

&#x20; *setError("");*

&#x20; *setLoading(true);*



&#x20; *try {*

&#x20;   *const response = await fetch(*

&#x20;     *"http://localhost:8000/auth/register",*

&#x20;     *{*

&#x20;       *method: "POST",*

&#x20;       *headers: {*

&#x20;         *"Content-Type": "application/json"*

&#x20;       *},*

&#x20;       *body: JSON.stringify(formData)*

&#x20;     *}*

&#x20;   *);*



&#x20;   *const data = await response.json();*



&#x20;   *if (response.ok) {*

&#x20;     *setMessage("Registration successful!");*

&#x20;   *} else {*

&#x20;     *setError(data.detail);*

&#x20;   *}*



&#x20; *} catch (error) {*

&#x20;   *setError("Unable to connect to the server.");*

&#x20; *}*



&#x20; *setLoading(false);*

*}*



Now we handle both:

HTTP error

&#x20;   ↓

response.ok === false

&#x20;   ↓

setError(data.detail)



and:



Network error

&#x20;   ↓

catch

&#x20;   ↓

setError(...)



##### **4. But There's a Problem**

Look at:

*setLoading(false);*



What if an error happens?

The catch runs, but we still need to make sure loading gets turned off.

This is exactly what finally is for.



##### **5. finally**

JavaScript provides:



*try {*

&#x20; *// attempt something*

*} catch (error) {*

&#x20; *// handle failure*

*} finally {*

&#x20; *// always execute*

*}*



So our handler becomes:



*async function handleSubmit(event) {*

&#x20; *event.preventDefault();*



&#x20; *setMessage("");*

&#x20; *setError("");*

&#x20; *setLoading(true);*



&#x20; *try {*

&#x20;   *const response = await fetch(*

&#x20;     *"http://localhost:8000/auth/register",*

&#x20;     *{*

&#x20;       *method: "POST",*

&#x20;       *headers: {*

&#x20;         *"Content-Type": "application/json"*

&#x20;       *},*

&#x20;       *body: JSON.stringify(formData)*

&#x20;     *}*

&#x20;   *);*



&#x20;   *const data = await response.json();*



&#x20;   *if (response.ok) {*

&#x20;     *setMessage("Registration successful!");*

&#x20;   *} else {*

&#x20;     *setError(data.detail);*

&#x20;   *}*



&#x20; *} catch (error) {*

&#x20;   *setError("Unable to connect to the server.");*



&#x20; *} finally {*

&#x20;   *setLoading(false);*

&#x20; *}*

*}*



Now regardless of what happens:

**Success**

&#x20;  ↓

finally

&#x20;  ↓

loading = false



or:



**400 error**

&#x20;  ↓

finally

&#x20;  ↓

loading = false



or:



**Network failure**

&#x20;  ↓

catch

&#x20;  ↓

finally

&#x20;  ↓

loading = false



##### **6. Use Loading State in the Button**

Currently:



*<button type="submit">*

&#x20; *Register*

*</button>*



We can make it dynamic:

*<button type="submit" disabled={loading}>*

&#x20; *{loading ? "Registering..." : "Register"}*

*</button>*



Now:



Normal:

\[ Register ]



While request is running:

\[ Registering... ]



And:



disabled={loading}



prevents the user from repeatedly clicking the button while the request is running.



##### **7. Complete Version**

Your component can now look like:



*import { useState } from "react";*



*function App() {*

&#x20; *const \[formData, setFormData] = useState({*

&#x20;   *username: "",*

&#x20;   *email: "",*

&#x20;   *password: ""*

&#x20; *});*



&#x20; *const \[message, setMessage] = useState("");*

&#x20; *const \[error, setError] = useState("");*

&#x20; *const \[loading, setLoading] = useState(false);*



&#x20; *function handleChange(event) {*

&#x20;   *const { name, value } = event.target;*



&#x20;   *setFormData({*

&#x20;     *...formData,*

&#x20;     *\[name]: value*

&#x20;   *});*

&#x20; *}*



&#x20; *async function handleSubmit(event) {*

&#x20;   *event.preventDefault();*



&#x20;   *setMessage("");*

&#x20;   *setError("");*

&#x20;   *setLoading(true);*



&#x20;   *try {*

&#x20;     *const response = await fetch(*

&#x20;       *"http://localhost:8000/auth/register",*

&#x20;       *{*

&#x20;         *method: "POST",*

&#x20;         *headers: {*

&#x20;           *"Content-Type": "application/json"*

&#x20;         *},*

&#x20;         *body: JSON.stringify(formData)*

&#x20;       *}*

&#x20;     *);*



&#x20;     *const data = await response.json();*



&#x20;     *if (response.ok) {*

&#x20;       *setMessage("Registration successful!");*

&#x20;     *} else {*

&#x20;       *setError(data.detail);*

&#x20;     *}*



&#x20;   *} catch (error) {*

&#x20;     *setError("Unable to connect to the server.");*



&#x20;   *} finally {*

&#x20;     *setLoading(false);*

&#x20;   *}*

&#x20; *}*



&#x20; *return (*

&#x20;   *<form onSubmit={handleSubmit}>*



&#x20;     *<input*

&#x20;       *type="text"*

&#x20;       *name="username"*

&#x20;       *value={formData.username}*

&#x20;       *onChange={handleChange}*

&#x20;     */>*



&#x20;     *<input*

&#x20;       *type="email"*

&#x20;       *name="email"*

&#x20;       *value={formData.email}*

&#x20;       *onChange={handleChange}*

&#x20;     */>*



&#x20;     *<input*

&#x20;       *type="password"*

&#x20;       *name="password"*

&#x20;       *value={formData.password}*

&#x20;       *onChange={handleChange}*

&#x20;     */>*



&#x20;     *<button type="submit" disabled={loading}>*

&#x20;       *{loading ? "Registering..." : "Register"}*

&#x20;     *</button>*



&#x20;     *{message \&\& <p>{message}</p>}*



&#x20;     *{error \&\& <p>{error}</p>}*



&#x20;   *</form>*

&#x20; *);*

*}*



*export default App;*



##### **Important Distinction**

There are now three different situations:



**1. Successful HTTP request**

201

↓

response.ok === true

↓

Registration successful



**2. Server responded with an error**

400

↓

response.ok === false

↓

data.detail

↓

Show backend error



**3. Request couldn't be completed**

FastAPI unavailable

↓

fetch throws

↓

catch

↓

"Unable to connect..."



This distinction is extremely useful when debugging real applications.





#### **Lesson 19 — useEffect()**

So far, you've learned how React responds to user actions:

User clicks

&#x20;  ↓

onClick

&#x20;  ↓

setState

&#x20;  ↓

Re-render



But what if we want React to perform an operation because the component rendered or because some state changed?

That's where **useEffect()** comes in.



##### **1. First, understand the problem**

Imagine our Dashboard needs to load students when it opens.



We don't want:

User clicks "Load Students"

&#x20;       ↓

fetch()



**We want:**

Dashboard opens

&#x20;       ↓

React renders

&#x20;       ↓

Fetch students automatically



This is an effect.



##### **2. Basic useEffect**

Import it:



*import { useEffect, useState } from "react";*



Then:

*useEffect(() => {*

&#x20; *console.log("Component rendered");*

*}, \[]);*



The structure is:

*useEffect(*

&#x20; *() => {*

&#x20;   *// effect code*

&#x20; *},*

&#x20; *\[]*

*);*



The second argument is called the **dependency array.**



##### **3. What does \[] mean?**

When you write:

*useEffect(() => {*

&#x20; *console.log("Component rendered");*

*}, \[]);*



the empty dependency array means:

Run this effect after the component's initial render.



Conceptually:

Component starts

&#x20;     ↓

React renders

&#x20;     ↓

UI appears

&#x20;     ↓

useEffect runs



So if your component is:



*function App() {*



&#x20; *useEffect(() => {*

&#x20;   *console.log("Hello from effect");*

&#x20; *}, \[]);*



&#x20; *return <h1>Hello</h1>;*

*}*



the browser displays:



Hello



and the console prints:

Hello from effect



##### **4. Why does the effect run after rendering?**

Remember React's basic process:



Component function

&#x20;     ↓

JSX

&#x20;     ↓

React creates/updates UI

&#x20;     ↓

Browser UI

&#x20;     ↓

useEffect



Effects are intended for operations that happen after rendering.



Examples include:

Fetching data

Starting timers

Subscribing to something

Synchronizing with an external system

Working with browser APIs



##### **5. useEffect Without Dependencies**

Consider:

*useEffect(() => {*

&#x20; *console.log("Effect");*

*});*



There is no dependency array.



That means the effect runs after **every render.**



For example:

Initial render

&#x20;↓

Effect



State changes

&#x20;↓

Re-render

&#x20;↓

Effect



State changes

&#x20;↓

Re-render

&#x20;↓

Effect



So:

*useEffect(() => {*

&#x20; *console.log("Effect");*

*});*



means:

Run after every render.



##### **6. useEffect With \[]**

*useEffect(() => {*

&#x20; *console.log("Effect");*

*}, \[]);*



means:

Run after the initial render.



Conceptually:

Initial render

&#x20;↓

Effect ✅



Re-render

&#x20;↓

Effect ❌



Re-render

&#x20;↓

Effect ❌



This is commonly used for initial data fetching.



##### **7. useEffect With Dependencies**



Now consider:



*const \[count, setCount] = useState(0);*



*useEffect(() => {*

&#x20; *console.log("Count changed");*

*}, \[count]);*



The dependency array contains:

\[count]



So React watches count.



When count changes:

count = 0

&#x20;↓

Initial render

&#x20;↓

Effect



setCount(1)

&#x20;↓

Re-render

&#x20;↓

count changed

&#x20;↓

Effect



setCount(2)

&#x20;↓

Re-render

&#x20;↓

count changed

&#x20;↓

Effect



So:

\[count]



means:

Run the effect after the initial render and whenever count changes.



##### **8. Compare the Three Forms**

**No dependency array**

*useEffect(() => {*

&#x20; *...*

*});*

Every render



**Empty dependency array**

*useEffect(() => {*

&#x20; *...*

*}, \[]);*

Initial render



**Dependency array**

*useEffect(() => {*

&#x20; *...*

*}, \[count]);*

Initial render

\+

when count changes



This distinction is extremely important.



##### **9. Why Does This Matter for Our FastAPI Project?**

Suppose we have a Dashboard:



*function Dashboard() {*

&#x20; *const \[students, setStudents] = useState(\[]);*



&#x20; *useEffect(() => {*

&#x20;   *fetch("http://localhost:8000/students");*

&#x20; *}, \[]);*



&#x20; *return (...);*

*}*



When Dashboard loads:

Dashboard renders

&#x20;     ↓

useEffect()

&#x20;     ↓

fetch("/students")

&#x20;     ↓

FastAPI

&#x20;     ↓

students data

&#x20;     ↓

setStudents()

&#x20;     ↓

React re-renders

&#x20;     ↓

Display students



This is exactly the kind of thing we'll eventually do with your FastAPI backend.



