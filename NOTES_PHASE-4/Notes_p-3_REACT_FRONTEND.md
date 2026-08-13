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





#### **Lesson 24 — useMemo**

Now we move to:

How can we avoid doing an expensive calculation again when it doesn't need to be recalculated?

That's useMemo().



##### **1. The Problem**

Imagine we have:

*function calculateSomething() {*

&#x20; *console.log("Calculating...");*

&#x20; *return 100 \* 100;*

*}*



*and inside our component:*

*function App() {*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *const result = calculateSomething();*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>{result}</h1>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Count: {count}*

&#x20;     *</button>*

&#x20;   *</>*

&#x20; *);*

*}*



Every time count changes:

setCount()

&#x20;↓

React re-renders App

&#x20;↓

calculateSomething()

&#x20;↓

"Calculating..."



Even though calculateSomething() doesn't depend on count.



That's unnecessary work.



##### **2. useMemo**

We can write:



*const result = useMemo(() => {*

&#x20; *return calculateSomething();*

*}, \[]);*



Now React remembers the calculated result.

Initial render

&#x20;↓

calculateSomething()

&#x20;↓

result stored



count changes

&#x20;↓

re-render

&#x20;↓

useMemo returns stored result

&#x20;↓

calculateSomething() NOT called



So the basic idea is:

useMemo memoizes a calculated value.



"Memoize" basically means:

Remember the result so we don't have to calculate it again unnecessarily.



##### **3. Dependency Array**

Just like useEffect, useMemo has dependencies:



*useMemo(() => {*

&#x20; *return calculateSomething();*

*}, \[count]);*



This means:

Recalculate when count changes.



Compare:

*useMemo(() => {*

&#x20; *return calculateSomething();*

*}, \[]);*



means:

Calculate initially

↓

Reuse result

↓

Reuse result

↓

Reuse result



Whereas:

*useMemo(() => {*

&#x20; *return calculateSomething();*

*}, \[count]);*



means:

Calculate

&#x20;↓

count changes

&#x20;↓

Calculate again

&#x20;↓

count changes

&#x20;↓

Calculate again



##### **4. useMemo vs useRef**

This is important because you just learned useRef.



**useRef**

*const valueRef = useRef(10);*



Stores:

{ current: 10 }



You access:

valueRef.current



Its purpose is to **maintain a mutable value** across renders without causing a render when changed.



**useMemo**

*const value = useMemo(() => expensiveCalculation(), \[]);*



Its purpose is to cache a calculated result.



So:

useRef

→ "Remember this value."



useMemo

→ "Remember the result of this calculation."



##### **5. Practical Example**

Let's create a search/filter example.



Suppose:

*const students = \[*

&#x20; *{ id: 1, name: "Adithya" },*

&#x20; *{ id: 2, name: "Agney" },*

&#x20; *{ id: 3, name: "Rahul" }*

*];*



We want to filter students based on a search term:

*const filteredStudents = students.filter(*

&#x20; *student => student.name.includes(search)*

*);*



We could write:

*const filteredStudents = students.filter(...);*



But the filtering calculation runs every time the component renders.



Instead:

*const filteredStudents = useMemo(() => {*

&#x20; *return students.filter(*

&#x20;   *student => student.name.includes(search)*

&#x20; *);*

*}, \[search]);*



Now the filtering is recalculated when:

search changes



but not merely because some unrelated state changed.



##### **6. Complete Example**

*import { useMemo, useState } from "react";*



*function App() {*

&#x20; *const \[search, setSearch] = useState("");*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *const students = \[*

&#x20;   *{ id: 1, name: "Adithya" },*

&#x20;   *{ id: 2, name: "Agney" },*

&#x20;   *{ id: 3, name: "Rahul" }*

&#x20; *];*



&#x20; *const filteredStudents = useMemo(() => {*

&#x20;   *console.log("Filtering students...");*



&#x20;   *return students.filter((student) =>*

&#x20;     *student.name*

&#x20;       *.toLowerCase()*

&#x20;       *.includes(search.toLowerCase())*

&#x20;   *);*

&#x20; *}, \[search]);*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<input*

&#x20;       *value={search}*

&#x20;       *onChange={(event) => setSearch(event.target.value)}*

&#x20;       *placeholder="Search students"*

&#x20;     */>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Count: {count}*

&#x20;     *</button>*



&#x20;     *{filteredStudents.map((student) => (*

&#x20;       *<p key={student.id}>*

&#x20;         *{student.name}*

&#x20;       *</p>*

&#x20;     *))}*

&#x20;   *</>*

&#x20; *);*

*}*



*export default App;*



Now:

Type "ag"

&#x20;↓

search changes

&#x20;↓

useMemo recalculates

&#x20;↓

Agney



But:



Click Count

&#x20;↓

count changes

&#x20;↓

component re-renders

&#x20;↓

search didn't change

&#x20;↓

useMemo uses cached result



So you shouldn't see:



Filtering students...



again just because count changed.



##### **7. Important: useMemo Is NOT Mainly About Preventing Rendering**

This is a common misconception.



useMemo does not prevent the component from rendering.



The component still re-renders:

count changes

&#x20;↓

App re-renders



What useMemo prevents is the unnecessary recalculation:

App re-renders

&#x20;↓

useMemo

&#x20;↓

cached result



So:

❌ useMemo → prevents re-render



✅ useMemo → avoids unnecessary recalculation



##### **8. Don't Use useMemo Everywhere**

This is important.



You don't need:

*const result = useMemo(() => 2 + 2, \[]);*



That's pointless.

The calculation is already extremely cheap.



useMemo is useful when:

A calculation is expensive

A large array is being filtered/sorted

A complex transformation is performed

You have a performance problem that memoization actually helps



For ordinary calculations:

*const total = price \* quantity;*



just write:

*const total = price \* quantity;*



Don't automatically wrap everything in useMemo.





#### **Lesson 25 — useCallback**

useCallback remembers a function between renders.



1\. Why would we need that?



Remember: whenever a component re-renders, the **component function runs again.**



Consider:



*function App() {*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *function handleClick() {*

&#x20;   *console.log("Clicked");*

&#x20; *}*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>{count}</h1>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Increase*

&#x20;     *</button>*



&#x20;     *<Child onClick={handleClick} />*

&#x20;   *</>*

&#x20; *);*

*}*



Every time count changes:



count changes

&#x20;   ↓

App re-renders

&#x20;   ↓

handleClick is created again

&#x20;   ↓

Child receives a new function reference



Even though the actual function logic hasn't changed.



##### **2. Why Does That Matter?**

Normally, creating a function again isn't a problem.



But imagine Child is an expensive component that we don't want to re-render unnecessarily.



We can use:

*const handleClick = useCallback(() => {*

&#x20; *console.log("Clicked");*

*}, \[]);*



Now React remembers the function reference.



Conceptually:

First render

&#x20;   ↓

create handleClick

&#x20;   ↓

remember it



App re-renders

&#x20;   ↓

useCallback

&#x20;   ↓

dependencies unchanged

&#x20;   ↓

reuse same function



##### **3. useCallback Syntax**

*const functionName = useCallback(() => {*

&#x20; *// function code*

*}, \[dependencies]);*



*For example:*



*const handleClick = useCallback(() => {*

&#x20; *console.log("Clicked");*

*}, \[]);*



The empty dependency array means:

Keep the **same function reference** across renders because this function **doesn't depend on changing values.**





##### **4. useCallback vs useMemo**

This is very important.



**useMemo**

Remembers a value:

*const result = useMemo(() => {*

&#x20; *return expensiveCalculation();*

*}, \[]);*



Think:

calculation

&#x20;   ↓

VALUE

&#x20;   ↓

remember it



**useCallback**

Remembers a function:

*const handleClick = useCallback(() => {*

&#x20; *console.log("Clicked");*

*}, \[]);*



Think:

FUNCTION

&#x20;   ↓

remember it



In fact, conceptually:

*useCallback(fn, dependencies)*



is similar to:

*useMemo(() => fn, dependencies)*



But useCallback communicates much more clearly:

"I want to memoize this function."



##### **5. A Practical Parent → Child Example**

Let's create a child component:



*function Child({ onClick }) {*

&#x20; *console.log("Child rendered");*



&#x20; *return (*

&#x20;   *<button onClick={onClick}>*

&#x20;     *Child Button*

&#x20;   *</button>*

&#x20; *);*

*}*



**Parent:**

*function App() {*

&#x20; *const \[count, setCount] = useState(0);*



&#x20; *function handleClick() {*

&#x20;   *console.log("Child clicked");*

&#x20; *}*



&#x20; *return (*

&#x20;   *<>*

&#x20;     *<h1>{count}</h1>*



&#x20;     *<button onClick={() => setCount(count + 1)}>*

&#x20;       *Increase*

&#x20;     *</button>*



&#x20;     *<Child onClick={handleClick} />*

&#x20;   *</>*

&#x20; *);*

*}*



When count changes:

App re-renders

&#x20;     ↓

handleClick is recreated

&#x20;     ↓

Child receives a new function

&#x20;     ↓

Child may re-render



##### **6. With useCallback**

We can write:



*const handleClick = useCallback(() => {*

&#x20; *console.log("Child clicked");*

*}, \[]);*



Now:

App re-renders

&#x20;     ↓

useCallback checks \[]

&#x20;     ↓

dependencies haven't changed

&#x20;     ↓

same function reference



This becomes particularly useful when combined with React.memo().



##### **7. React.memo**

You don't need to master this yet, but you need to understand why useCallback exists.



We can wrap the child:

*const Child = React.memo(function Child({ onClick }) {*

&#x20; *console.log("Child rendered");*



&#x20; *return (*

&#x20;   *<button onClick={onClick}>*

&#x20;     *Child Button*

&#x20;   *</button>*

&#x20; *);*

*});*



Now React can skip rendering Child if its props haven't changed.

Without useCallback:



But there's a subtle problem.

*function handleClick() {*

&#x20; *console.log("Child clicked");*

*}*



Every parent render creates a new function.



So React sees:

Old onClick ≠ New onClick



and thinks:

"The prop changed."



Therefore the child can re-render.



**With:**

*const handleClick = useCallback(() => {*

&#x20; *console.log("Child clicked");*

*}, \[]);*



the function reference remains the same.



So:

Parent re-renders

&#x20;      ↓

same handleClick reference

&#x20;      ↓

Child props haven't changed

&#x20;      ↓

React.memo can skip Child render



##### **8. Don't Use useCallback Everywhere**

Just like useMemo, don't blindly wrap every function:

*const add = useCallback(() => {*

&#x20; *return 2 + 2;*

*}, \[]);*



There's no meaningful benefit here.

Creating a simple function is cheap.



useCallback is mainly useful when:

passing functions to memoized child components

function identity matters

preventing unnecessary child renders

working with dependencies in effects or other hooks where stable function references matter



##### **9. Important Dependency Rule**

Suppose:



*const \[count, setCount] = useState(0);*



*const handleClick = useCallback(() => {*

&#x20; *console.log(count);*

*}, \[count]);*



Why \[count]?

Because the function uses count.



When count changes, we need a new function that sees the new value.



count = 0

&#x20;  ↓

handleClick remembers count = 0



count = 1

&#x20;  ↓

dependency changed

&#x20;  ↓

new handleClick

&#x20;  ↓

now sees count = 1



So don't automatically use \[].

The dependency array should represent values from the component that the callback depends on.





