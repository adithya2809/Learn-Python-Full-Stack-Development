# **DATABASES-NOTES PART-2**

# PERFORMANCE AND TRANSACTIONS



## **INDEXES**

If I ask you:

What is an index in a book?



You'd probably say:

"It helps us find a topic quickly without reading the entire book."



Exactly! A database index works the same way.



**Why Do We Need an Index?**

Suppose you have a users table.



id	name	email

1	Agney	agney@gmail.com

2	Ravi	ravi@gmail.com

3	John	john@gmail.com

...	...	...

10,000,000	Alice	alice@gmail.com



Now you run:

*SELECT \**

*FROM users*

*WHERE email = 'john@gmail.com';*



Without an Index



PostgreSQL has no shortcut.



It checks:



Row 1 ❌



Row 2 ❌



Row 3 ✅



Found!



If John is the last row:



Row 1



Row 2



Row 3



...



Row 9,999,999



Row 10,000,000 ✅

This is called a **Full Table Scan.**



**Time complexity:**

O(n)



Meaning the **time increases linearly** with the **number of rows.**



#### **With an Index**

Imagine the index of a textbook.

Instead of reading every page:

Artificial Intelligence → Page 245



You jump directly there.



A database index does the same.

PostgreSQL maintains a special data structure (usually a B-Tree) that allows it to locate rows quickly.



Conceptually:



john@gmail.com



↓



Pointer



↓



Actual Row



Instead of checking millions of rows, it jumps almost directly to the correct location.

**Time complexity** (conceptually):

**O(log n)**



Much faster than O(n).



You don't need to memorize Big-O notation yet. Just remember:

**Indexed lookups are dramatically faster than scanning the whole table.**



#### **Creating an Index**

*CREATE INDEX idx\_users\_email*

*ON users(email);*



**Breaking it down:**



*CREATE INDEX*



→ Create an index.



*idx\_users\_email*



→ Name of the index.



**ON users(email);**

→ Build the index on the email column.



#### **Which Columns Should Be Indexed?**

**Good candidates:**

Primary Keys (automatic)

Foreign Keys (often recommended)

Email

Username

Product ID

Order ID



Basically:

Columns that you **search, filter, join, or sort** by frequently.



**Bad Example**

Suppose:



*SELECT \**

*FROM users*

*WHERE gender = 'Male';*



Should you index gender?

Usually no.



Why?

There are only a few possible values:



Male

Female

Other



The database would still need to examine many matching rows.

Indexes are **most useful** for columns with many **distinct values**, such as **emails or usernames**.



**Advantages of Indexes**

✅ Faster SELECT

✅ Faster WHERE

✅ Faster JOIN

✅ Faster ORDER BY



**Disadvantages**

Indexes are not free.



Whenever you do:



INSERT



or



UPDATE



or



DELETE



PostgreSQL must also update the index.

So:



**Reads** become **faster.**

**Writes** become a **little slower.**



This is the trade-off.



**Why don't we create an index on every column?**



**Answer:**

Because **indexes consume storage** and **slow down** INSERT, UPDATE, and DELETE operations. We create indexes only on columns that are **frequently searched, filtered, joined, or sorted.**



## **Transactions \& ACID**



#### **What is a Transaction?**



A transaction is a **group of SQL operations** that should be **treated as one single unit of work.**



Think of it as:

Either everything succeeds, or nothing succeeds.



**Real-Life Example: Bank Transfer 💰**

Suppose:



Agney's Account : ₹10,000

Ravi's Account  : ₹5,000



Agney transfers ₹1,000 to Ravi.



Behind the scenes, SQL executes:

*UPDATE accounts*

*SET balance = balance - 1000*

*WHERE account\_id = 1;*



Then:

*UPDATE accounts*

*SET balance = balance + 1000*

*WHERE account\_id = 2;*



**Imagine the Server Crashes 💥**

After the first query:



Agney = ₹9,000 ✅

Ravi = ₹5,000 ❌



₹1000 has disappeared.

This should never happen.



**The Solution**

Use a **transaction.**



*BEGIN;*



*UPDATE accounts*

*SET balance = balance - 1000*

*WHERE account\_id = 1;*



*UPDATE accounts*

*SET balance = balance + 1000*

*WHERE account\_id = 2;*

*COMMIT;*



If everything succeeds:

*COMMIT;*



Database saves both changes.



**What if Something Fails?**

Suppose the second query fails.



BEGIN;



UPDATE ...



UPDATE ...



ERROR



ROLLBACK;



Database returns to:

Agney = ₹10,000

Ravi = ₹5,000



Exactly as before.

No money disappears.



**Three Important Commands**

1\. BEGIN

Starts a transaction.



*BEGIN;*

2\. COMMIT

Save everything permanently.



*COMMIT;*



Think:

"I'm happy. Save the changes."



3\. ROLLBACK

Undo everything.



*ROLLBACK;*



Think:

"Something went wrong. Go back."



#### **ACID PROPERTIES**

**| Letter | Meaning     | Memory Trick                 |**

**| ------ | ----------- | ---------------------------- |**

**| A      | Atomicity   | All or Nothing               |**

**| C      | Consistency | Database remains valid       |**

**| I      | Isolation   | Transactions don't interfere |**

**| D      | Durability  | Saved means saved forever    |**



|**A**|Atomicity|All or Nothing|
|-|-|-|
|**C**|Consistency|Database remains valid|
|**I**|Isolation|Transactions don't interfere|
|**D**|Durability|saved means saved forever|



**A → Atomicity**



**Think:**

All or Nothing



**Either:**



✅ All queries succeed



**OR**



❌ None of them happen.



No partial updates.



**C → Consistency**



Database rules must always remain valid.



**Example:**



**Foreign Key:**

*department\_id = 999*



Department doesn't exist.

Database rejects it.



**Consistency is maintained.**



**I → Isolation**



**Imagine:**

Two people withdraw money simultaneously.



**Without isolation:**

Balance

**1000**

**↓**



**User A withdraws**



**↓**



**User B withdraws**



**↓**



**Wrong balance**



**Isolation ensures transactions don't interfere with each other.**



**D → Durability**



**Suppose:**

*COMMIT;*



**Immediately after:**

Power failure.



Server crashes.



**After restart:**



Your data is still there.



Because **committed transactions are durable.**



**Real Backend Example**



Imagine placing an order.



**Steps:**



Create order

Reduce product stock

Create payment

Send invoice



**If step 3 fails:**



Should steps 1 and 2 remain?



❌ No.



Rollback everything.



Exactly what transactions do.



**Why do we use transactions?**



Good answer:

Transactions ensure that multiple database operations either **complete successfully together or fail together**, preserving data integrity.





## **🎉 SQL Fundamentals Completed!**

SQL Fundamentals

────────────────────────────



✅ CRUD



✅ WHERE



✅ ORDER BY



✅ LIMIT



✅ Aggregate Functions



✅ GROUP BY



✅ HAVING



✅ JOINS



✅ Primary Keys



✅ Foreign Keys



✅ Relationships



✅ Normalization



✅ Indexes



🟨 Transactions (Current)

