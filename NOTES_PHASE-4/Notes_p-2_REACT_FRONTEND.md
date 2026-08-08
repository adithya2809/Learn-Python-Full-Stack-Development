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



