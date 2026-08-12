# REACT FRONTEND PART-3



#### **Lesson 20 — useEffect() Dependencies \& Cleanup**

You just successfully used:

*useEffect(() => {*

&#x20; *// fetch students*

*}, \[]);*



and saw the data load automatically.



Now let's understand exactly when React runs an effect.



##### **1. The Dependency Array**

Remember:



*useEffect(() => {*

&#x20; *console.log("Effect");*

*}, \[]);*



The \[] is the dependency array.

React uses it to determine **when** the effect should **run again.**



There are three important patterns.



###### **No dependency array**

*useEffect(() => {*

&#x20; *console.log("Effect");*

*});*

Runs after **every render.**



###### **Empty dependency array**

*useEffect(() => {*

&#x20; *console.log("Effect");*

*}, \[]);*



Runs after the component's **initial render.**

This is why it was useful for your student fetch.



###### **Dependency**

*useEffect(() => {*

&#x20; *console.log(count);*

*}, \[count]);*



Runs after the **initial render** and whenever count **changes.**





##### **2. Let's See It With Your Counter**

Try this:



*import { useEffect, useState } from "react";*



*function App() {*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *useEffect(() => {*

&#x20;   *console.log("Effect ran. Count:", count);*

&#x20; *}, \[count]);*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>{count}</h1>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Increase*

&#x20;     *</button>*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



**Initially:**

Render

&#x20;↓

count = 0

&#x20;↓

Effect

&#x20;↓

"Effect ran. Count: 0"



**Click once:**

setCount(1)

&#x20;↓

Re-render

&#x20;↓

count = 1

&#x20;↓

Effect

&#x20;↓

"Effect ran. Count: 1"



**Click again:**

setCount(2)

&#x20;↓

Re-render

&#x20;↓

Effect

&#x20;↓

"Effect ran. Count: 2"



##### **3. What Does React Actually Watch?**

When you write:

*\[count]*



you're essentially telling React:

"This effect depends on count."



If count changes between renders, React runs the effect again.



For example:

Previous render     Current render



count = 0           count = 1

&#x20;    ↓                   ↓

&#x20;    └──── changed ──────┘

&#x20;            ↓

&#x20;       Effect runs



But if another state changes:

*const \[name, setName] = useState("");*



and:

*setName("Agney");*



then:

count = 1 → count = 1



count didn't change, so that particular effect doesn't need to run again.



##### **4. Why Dependencies Matter**

Imagine this:



*const \[count, setCount] = useState(0);*

*const \[name, setName] = useState("");*



*useEffect(() => {*

&#x20; *console.log("Count effect");*

*}, \[count]);*



Now:

setCount(1)

&#x20;   ↓

count changed

&#x20;   ↓

Effect runs ✅



But:

setName("Agney")

&#x20;   ↓

name changed

&#x20;   ↓

count didn't change

&#x20;   ↓

Effect doesn't run ❌



This lets React avoid unnecessary work.



##### **5. Cleanup Functions**

Now for another important part of useEffect.



Suppose we start a timer:



*useEffect(() => {*

&#x20; *const timer = setInterval(() => {*

&#x20;   *console.log("Running...");*

&#x20; *}, 1000);*

*}, \[]);*



Every second:

Running...

Running...

Running...

Running...



But what happens when the component is removed from the UI?

That interval could continue running.

We need to clean it up.



##### **Cleanup Function**

useEffect() can return a function:



*useEffect(() => {*



&#x20; *const timer = setInterval(() => {*

&#x20;   *console.log("Running...");*

&#x20; *}, 1000);*



&#x20; *return () => {*

&#x20;   *clearInterval(timer);*

&#x20; *};*



*}, \[]);*



The structure is:

useEffect

&#x20;   ↓

Start something

&#x20;   ↓

return cleanup function

&#x20;   ↓

Component eventually unmounts

&#x20;   ↓

Cleanup executes



##### **6. Why Is Cleanup Important?**

Without cleanup:

Component

&#x20;↓

setInterval()

&#x20;↓

Component removed

&#x20;↓

Timer still running ❌



**With cleanup:**

Component

&#x20;↓

setInterval()

&#x20;↓

Component removed

&#x20;↓

cleanup()

&#x20;↓

clearInterval()

&#x20;↓

Timer stopped ✅



This prevents unnecessary work and potential memory/resource leaks.



##### **7. Cleanup Isn't Only for Unmounting**

Cleanup also happens before an effect runs again when its dependencies change.



For example:

*useEffect(() => {*



&#x20; *console.log("Effect started");*



&#x20; *return () => {*

&#x20;   *console.log("Cleanup");*

&#x20; *};*



*}, \[count]);*



If count changes:

Previous effect

&#x20;     ↓

Cleanup

&#x20;     ↓

New effect



So the general lifecycle is:

Effect runs

&#x20;   ↓

Dependency changes

&#x20;   ↓

Cleanup previous effect

&#x20;   ↓

New effect runs



And when the component is removed:

Component unmounts

&#x20;   ↓

Cleanup runs



##### **8. Important Rule for Your FastAPI Fetch**

Your student fetching effect:



*useEffect(() => {*

&#x20; *async function getStudents() {*

&#x20;   *...*

&#x20; *}*



&#x20; *getStudents();*

*}, \[]);*



doesn't currently need a cleanup function for this simple example.



But when we start dealing with things like:

subscriptions

timers

event listeners

WebSockets

aborting requests



cleanup becomes important.

And since your eventual application may involve real-time features, understanding cleanup will be valuable.





#### **Lesson 21 — useEffect() + API Fetching**

You already built this:



*useEffect(() => {*

&#x20; *async function getStudents() {*

&#x20;   *const response = await fetch(*

&#x20;     *"http://localhost:8000/students"*

&#x20;   *);*



&#x20;   *const data = await response.json();*



&#x20;   *setStudents(data);*

&#x20; *}*



&#x20; *getStudents();*

*}, \[]);*



It works, but it has one weakness: the UI doesn't know whether the request is loading, successful, or failed.

We already learned loading/error state during registration, so let's combine those ideas with useEffect().



##### **1. Three States**



We'll maintain:

*const \[students, setStudents] = useState(\[]);*

*const \[loading, setLoading] = useState(true);*

*const \[error, setError] = useState("");*



Conceptually:

students

→ actual data



loading

→ is the request currently running?



error

→ did something go wrong?



Initially:

students = \[]

loading = true

error = ""



##### **2. Fetch When Component Loads**

*useEffect(() => {*

&#x20; *async function getStudents() {*

&#x20;   *try {*

&#x20;     *const response = await fetch(*

&#x20;       *"http://localhost:8000/students"*

&#x20;     *);*



&#x20;     *if (!response.ok) {*

&#x20;       *throw new Error("Failed to fetch students");*

&#x20;     *}*



&#x20;     *const data = await response.json();*



&#x20;     *setStudents(data);*



&#x20;   *} catch (error) {*

&#x20;     *setError("Unable to load students.");*



&#x20;   *} finally {*

&#x20;     *setLoading(false);*

&#x20;   *}*

&#x20; *}*



&#x20; *getStudents();*

*}, \[]);*



Notice that this is very similar to the registration request you already wrote.



The difference is when it runs.



**Registration:**

User submits form

&#x20;↓

handleSubmit()

&#x20;↓

fetch()



**Students:**

Component renders

&#x20;↓

useEffect()

&#x20;↓

fetch()



##### **3. Why setLoading(false) Is in finally**

Initially:

*const \[loading, setLoading] = useState(true);*



So when the page first appears:

Loading...



The request runs.



Eventually:

Success

&#x20;  ↓

finally

&#x20;  ↓

loading = false



or:



Error

&#x20;  ↓

catch

&#x20;  ↓

finally

&#x20;  ↓

loading = false



So finally guarantees that loading ends.



##### **4. Render Different UI States**

Now:



*if (loading) {*

&#x20; *return <h1>Loading students...</h1>;*

*}*



*if (error) {*

&#x20; *return <h1>{error}</h1>;*

*}*



Then, once loading finishes:



*return (*

&#x20; *<>*

&#x20;   *<h1>Students</h1>*



&#x20;   *{students.map((student) => (*

&#x20;     *<p key={student.id}>*

&#x20;       *{student.name}*

&#x20;     *</p>*

&#x20;   *))}*

&#x20; *</>*

*);*



So the user experiences:

Component opens

&#x20;     ↓

Loading students...

&#x20;     ↓

API request

&#x20;     ↓

&#x20;  ┌───────┴───────┐

&#x20;  ↓               ↓

Success           Error

&#x20;  ↓               ↓

Students       Unable to load



##### **5. Complete Example**



*import { useEffect, useState } from "react";*



*function App() {*

&#x20; *const \[students, setStudents] = useState(\[]);*

&#x20; *const \[loading, setLoading] = useState(true);*

&#x20; *const \[error, setError] = useState("");*



&#x20; *useEffect(() => {*

&#x20;   *async function getStudents() {*

&#x20;     *try {*

&#x20;       *const response = await fetch(*

&#x20;         *"http://localhost:8000/students"*

&#x20;       *);*



&#x20;       *if (!response.ok) {*

&#x20;         *throw new Error("Failed to fetch students");*

&#x20;       *}*



&#x20;       *const data = await response.json();*



&#x20;       *setStudents(data);*



&#x20;     *} catch (error) {*

&#x20;       *setError("Unable to load students.");*



&#x20;     *} finally {*

&#x20;       *setLoading(false);*

&#x20;     *}*

&#x20;   *}*



&#x20;   *getStudents();*

&#x20; *}, \[]);*



&#x20; *if (loading) {*

&#x20;   *return <h1>Loading students...</h1>;*

&#x20; *}*



&#x20; *if (error) {*

&#x20;   *return <h1>{error}</h1>;*

&#x20; *}*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>Students</h1>*



&#x20;     *{students.map((student) => (*

&#x20;       *<p key={student.id}>*

&#x20;         *{student.name}*

&#x20;       *</p>*

&#x20;     *))}*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



##### **6. Why response.ok Before response.json()?**

This is important.



We do:



*if (!response.ok) {*

&#x20; *throw new Error("Failed to fetch students");*

*}*



*const data = await response.json();*



Because fetch() doesn't automatically throw an error for HTTP 400/404/500.



For example:

GET /students

&#x20;      ↓

404

&#x20;      ↓

fetch() receives a response

&#x20;      ↓

response.ok = false



So we explicitly check:



if (!response.ok)



and throw an error ourselves.



Then:

catch handles it.





#### **Lesson 22 — useRef**



So far you've learned an important behavior of useState:

setState()

&#x20;  ↓

State changes

&#x20;  ↓

React re-renders

&#x20;  ↓

UI updates



But sometimes we want to remember something without causing a re-render.

That's where useRef() comes in.



##### **1. Basic useRef**

Import it:



*import { useRef } from "react";*



Then:

*const countRef = useRef(0);*



A ref looks like:

countRef

&#x20;  ↓

{ current: 0 }



The value is stored inside:

*countRef.current*



So:

*console.log(countRef.current);*



prints:

0



You can change it:

*countRef.current = 10;*



Now:

*console.log(countRef.current);*



prints:

10



##### **2. The Most Important Difference**

Compare:

*const \[count, setCount] = useState(0);*



with:

*const countRef = useRef(0);*



**useState**

*setCount(10);*



causes:

State changes

&#x20;  ↓

Re-render



**useRef**

*countRef.current = 10;*



does not cause:

❌ Re-render



So:

useState

→ stores state + triggers re-render



useRef

→ stores a mutable value + does NOT trigger re-render

This is the most important thing to understand about useRef.



##### **3. Why Would We Want That?**

One common use is accessing a DOM element directly.



For example:

<input />



Suppose we want to automatically focus that input.



We can create a ref:

*const inputRef = useRef(null);*



Then attach it:

*<input ref={inputRef} />*



Now React gives us access to the actual DOM element through:

*inputRef.current*



##### **4. Focusing an Input**

Complete example:



*import { useRef } from "react";*



*function App() {*

&#x20; *const inputRef = useRef(null);*



&#x20; *function focusInput() {*

&#x20;   *inputRef.current.focus();*

&#x20; *}*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<input ref={inputRef} />*



&#x20;     *<button onClick={focusInput}>*

&#x20;       *Focus Input*

&#x20;     *</button>*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



The flow is:

<input>

&#x20;  ↓

ref={inputRef}

&#x20;  ↓

inputRef.current

&#x20;  ↓

actual DOM input



When the button is clicked:

*inputRef.current.focus();*



React/JavaScript tells the actual input:

Focus yourself.



##### **5. Why Not Use useState?**



You might ask:

Why not store the input element in state?



Because we don't need the UI to **re-render** when the reference changes.



We're simply saying:

"Remember this DOM element so I can access it later."



That's exactly what refs are good for.



##### **6. Another Important Use: Remembering Previous Values**

Refs can also remember a value between renders.



For example:

*const previousCount = useRef(0);*



Suppose:

count = 5



We can store something in:

*previousCount.current*



and it persists across renders.



Unlike a normal variable:

*let previousCount = 0;*



which gets recreated every time the component function runs.



##### **7. useRef vs Normal Variable**

Imagine:

*function App() {*

&#x20; *let number = 0;*



&#x20; *const numberRef = useRef(0);*



&#x20; *...*

*}*



When React re-renders:

Normal variable

→ recreated



**useRef**

→ value persists



So:

let number = 0



doesn't reliably preserve mutable data between renders.



But:

*const numberRef = useRef(0);*

does.



##### **8. Important Rule**

Don't use a ref when the value needs to appear in the UI.



For example, this is usually wrong:

*const countRef = useRef(0);*

*countRef.current++;*



*return <h1>{countRef.current}</h1>;*



**Changing:**

*countRef.current++*



doesn't trigger a re-render.



So the UI won't automatically update.



If the value should affect what the user sees:

*const \[count, setCount] = useState(0);*

is usually the correct choice.



##### **9. Simple Mental Model**

Think of them this way:



**State**

"React, this value affects my UI. Please re-render when it changes."

*const \[count, setCount] = useState(0);*



**Ref**

"React, remember this value/element for me, but don't re-render just because it changed."

*const countRef = useRef(0);*





#### **Lesson 23 — useRef to Remember the Previous Value**

Suppose:

*const \[count, setCount] = useState(0);*



and you want to know:

Current count: 3

Previous count: 2



A normal variable won't reliably remember 2 between renders.

A ref can.



The Pattern



We'll use:

*const previousCount = useRef(null);*



Then:

*useEffect(() => {*

&#x20; *previousCount.current = count;*

*}, \[count]);*



The idea is:

Render with count = 0

&#x20;       ↓

previousCount = null

&#x20;       ↓

effect runs

&#x20;       ↓

previousCount = 0





count changes to 1

&#x20;       ↓

render

&#x20;       ↓

previousCount still = 0

&#x20;       ↓

effect runs

&#x20;       ↓

previousCount = 1



So during the render where count = 1:

current count  = 1

previous count = 0



##### **Complete Example**

*import { useEffect, useRef, useState } from "react";*



*function App() {*

&#x20; *const \[count, setCount] = useState(0);*

&#x20; *const previousCount = useRef(null);*



&#x20; *useEffect(() => {*

&#x20;   *previousCount.current = count;*

&#x20; *}, \[count]);*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>Current: {count}</h1>*



&#x20;     *<h2>*

&#x20;       *Previous: {previousCount.current}*

&#x20;     *</h2>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Increase*

&#x20;     *</button>*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



But there's a subtle issue here.

Because useEffect() runs after rendering, the displayed value may not behave exactly as you initially expect. This is actually a good opportunity to understand the timing of refs and effects.



Let's trace it.



**Initial render**

count = 0

*previousCount.current = null*



UI renders:

Current: 0

Previous: null



Then the effect runs:

*previousCount.current = 0*



**Click Increase**

Now:

count = 1

*previousCount.current = 0*



React renders:

Current: 1

Previous: 0



Then the effect runs:

*previousCount.current = 1*



Next time you click:

count = 2

*previousCount.current = 1*



So the UI shows:

Current: 2

Previous: 1



That's the behavior we want.



##### **Why Does This Work?**

The important part is that changing:

*previousCount.current = count;*



does not cause another render.



If it did, we'd get an endless cycle:

render

&#x20;↓

effect

&#x20;↓

ref changes

&#x20;↓

render

&#x20;↓

effect

&#x20;↓

...



But refs don't trigger renders.

So the ref quietly remembers the value for the next render.



One More Important Use of useRef



Refs are not just for DOM elements.



There are two major categories you'll commonly see:

##### **1. DOM reference**

*const inputRef = useRef(null);*

*<input ref={inputRef} />*



Used for:

*inputRef.current.focus();*



##### **2. Persistent mutable value**

*const previousCount = useRef(null);*



Used for:

*previousCount.current*



without causing a render.





#### 

