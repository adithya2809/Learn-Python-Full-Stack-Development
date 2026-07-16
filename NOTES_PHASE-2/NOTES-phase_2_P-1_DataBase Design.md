# **Phase 2: Databases**





#### **Your First SQL Statement**



To create the students table, we use the CREATE TABLE command:



*CREATE TABLE students (*

&#x20;   *id SERIAL PRIMARY KEY,*

&#x20;   *name VARCHAR(100) NOT NULL,*

&#x20;   *age INT,*

&#x20;   *email VARCHAR(255) UNIQUE*

*);*



Let's break this down:



CREATE TABLE students → Creates a table named students.

id SERIAL PRIMARY KEY → Creates an auto-incrementing unique ID.

name VARCHAR(100) NOT NULL → Stores a name up to 100 characters; it cannot be empty.

age INT → Stores an integer age.

email VARCHAR(255) UNIQUE → Stores an email address and prevents duplicates.



#### **Constraints**

(PRIMARY KEY, NOT NULL, UNIQUE) belongs to a category called constraints.



|**Constraint**|**Purpose**|
|-|-|
|PRIMARY KEY|Every row has a unique identity|
|NOT NULL|A value is required|
|UNIQUE|Prevent duplicate values|
|FOREIGN KEY|Connect two tables|
|CHECK|Restrict allowed values|
|DEFAULT|Provide a default value if none is given|



#### **CREATING A TABLE**

*CREATE TABLE students (*

&#x20;   *id SERIAL PRIMARY KEY,*

&#x20;   *name VARCHAR(100) NOT NULL,*

&#x20;   *age INT,*

&#x20;   *email VARCHAR(255) UNIQUE*

*);*

#### **INSERT INTO**

**Syntax**

*INSERT INTO table\_name(column1, column2, ...)*

*VALUES(value1, value2, ...);*



**Common Beginner Mistakes**

❌ Mistake 1: Wrong column order

*INSERT INTO students(name, age)*

*VALUES (22, 'Alice');*



Here:

name gets *22*

age gets *"Alice"*



That's incorrect because the values don't match the column order.



❌ Mistake 2: Forgetting quotes around strings

Wrong:

*VALUES (Alice,22)*



Correct:

*VALUES ('Alice',22)*



Strings must be enclosed in single quotes.



❌ Mistake 3: Providing the wrong number of values



Wrong:

*INSERT INTO students(name,age)*

*VALUES ('Alice');*



There are 2 columns but only 1 value, so PostgreSQL raises an error.



**Interview Question**



**Question:** Why don't we usually insert values into the id column when it is defined as SERIAL?



A good answer would mention **auto-incrementing** and **unique identifiers**.





|**Data Type**|**SQL Syntax**|
|-|-|
|String|'Alice'|
|Integer|25|
|Float|99.5|
|Boolean|TRUE/FALSE|
|NULL|NULL|



#### **SELECT**

*SELECT \** - Retrieves Everything

*SELECT column\_name*

*FROM table\_name;*   -  Retrieves specified columns.



With PostgreSQL, the flow becomes:



Client

&#x20;  │

GET /students

&#x20;  │

&#x20;  ▼

FastAPI

&#x20;  │

&#x20;  ▼

SELECT \* FROM students;

&#x20;  │

&#x20;  ▼

PostgreSQL

&#x20;  │

&#x20;  ▼

Returns all rows

So every time someone calls:



GET /students



your backend will execute a SELECT query behind the scenes.



Later, SQLAlchemy will generate these SELECT statements for you automatically—but it's important that you understand what it's doing.



#### **WHERE**

WHERE Always Returns a **Boolean**

It **evaluates** **every row**. Only the rows where the condition is **True** are returned.



This Boolean evaluation is the foundation of SQL filtering.



#### **UPDATE**

Instead of inserting a new row, we update the existing one:



**SYNTAX**

UPDATE table\_name

SET column = value

WHERE condition;



*UPDATE employees*

*SET salary = 70000*

*WHERE id = 1;*



Notice how **important** the **WHERE clause** becomes here.



Without it:



*UPDATE employees*

*SET salary = 70000;*



⚠️ Every employee's salary would become 70000.



This is one of the most dangerous mistakes beginners make, and every backend developer learns to double-check UPDATE and DELETE queries because of it.

Never execute an **UPDATE** without checking the **WHERE** clause.



|**FastAPI**|**SQL**|
|-|-|
|POST /employees|INSERT|
|GET /employees|SELECT|
|PUT /employees/{id}|UPDATE|
|DELETE /employees/{id}|DELETE|



#### **DELETE**



**Syntax**

*DELETE FROM table\_name*

*WHERE condition;*



###### **Hard Delete vs Soft Delete**



This is a very common interview topic.



**Hard Delete**

*DELETE FROM employees*

*WHERE id = 3;*



The row is permanently removed.



**Soft Delete**



Instead of removing the row:



id	name	is\_deleted

3	Sneha	FALSE



We update it:



*UPDATE employees*

*SET is\_deleted = TRUE*

*WHERE id = 3;*



Result:



id	name	is\_deleted

3	Sneha	TRUE



The data still exists but is hidden from normal users.



Many production systems (banks, hospitals, e-commerce platforms) use soft deletes because deleted records may be needed for auditing, recovery, or legal compliance.



#### **OREDER BY**

PostgreSQL does not guarantee the order of rows. You might see them in insertion order today, but you should never rely on that.

If you want a specific order, you must explicitly request it.



**SYNTAX**

*SELECT \**

*FROM employees*

*ORDER BY column\_name;*



By default, SQL sorts in Ascending (ASC) order.



**DESC**

*SELECT \**

*FROM employees*

*ORDER BY salary DESC;*

Highest salary comes first.



**Real Backend Examples**



Imagine these APIs:



*GET /products*



Most expensive first:



*ORDER BY price DESC;*



Latest blog posts:



*ORDER BY created\_at DESC;*



Students ranked by marks:



*ORDER BY marks DESC;*



Employees alphabetically:



*ORDER BY name ASC;*



You'll see ORDER BY in almost every backend application.



Remember the **order**:



SELECT

FROM

WHERE

ORDER BY





Why shouldn't we rely on SELECT \*?



A strong answer is:



* It retrieves unnecessary columns.
* It transfers more data over the network.
* It consumes more memory.
* It may expose sensitive information (like passwords or tokens).
* It becomes harder to maintain if the table schema changes.



#### **LIMIT**

Imagine an e-commerce website.

The database has 10,000 products.

If we write:



*SELECT \**

*FROM products;*



The database returns all 10,000 products.



LIMIT tells PostgreSQL:

"Return only the first N rows."

**SYNTAX**

*SELECT \**

*FROM employees*

*LIMIT 3;*



**Real-World Backend Examples**

Latest 10 Blog Posts

*SELECT \**

*FROM posts*

*ORDER BY created\_at DESC*

*LIMIT 10;*



Top 5 Highest Scoring Students

*SELECT \**

*FROM students*

*ORDER BY marks DESC*

*LIMIT 5;*



Cheapest 20 Products

*SELECT \**

*FROM products*

*ORDER BY price ASC*

*LIMIT 20;*



LIMIT reduces the amount of data returned from the database, improving query performance, reducing memory usage, lowering network traffic, and making applications faster.



#### **OFFSET (Pagination)**

**Page 1**

*SELECT \**

*FROM products*

*LIMIT 10;*



Returns:

1–10



**Page 2**

*SELECT \**

*FROM products*

*LIMIT 10*

*OFFSET 10;*



Returns:

11–20



**Page 3**

*SELECT \**

*FROM products*

*LIMIT 10*

*OFFSET 20; --Begins form 21-30*



Returns:

21–30



**Real FastAPI Example**



Suppose your frontend requests:



*GET /products?page=3*



**Backend logic:**



**offset = (page - 1) \* 10**



Page = 3



**offset = (3-1) × 10**

&#x20;      **= 20**



**Generated SQL:**



*SELECT \**

*FROM products*

*LIMIT 10*

*OFFSET 20;*



This is exactly how pagination works in many REST APIs.



#### **AGGREGATE FUNCTIONS**

Aggregate functions perform a calculation on multiple rows and return a single value.



Suppose your manager asks:

* How many employees do we have?
* What is the highest salary?
* What is the average salary?
* What is the total salary paid?



Instead of calculating manually, SQL does it for us.



#### 1\. COUNT()

Used to count rows.

Example

*SELECT COUNT(\*)*

*FROM employees; --RESULT: no.of rows*



Count only AI employees

*SELECT COUNT(\*)*

*FROM employees*

*WHERE department = 'AI';*



#### 2\. SUM()

Calculates the total.

*SELECT SUM(salary)*

*FROM employees; --calculates total in salary column*



#### 3\. AVG()

Average value.

*SELECT AVG(salary)*

*FROM employees; --calculates average of the salary column*



#### 4\. MAX()

Largest value.

*SELECT MAX(salary)*

*FROM employees; --maximum value from salary column*



#### 5\. MIN()

Smallest value.

*SELECT MIN(salary)*

*FROM employees; --minimum value from salary column*



#### **Aggregate Functions + WHERE**



These work beautifully together.



#### EXAMPLES

*SELECT MAX(salary)*

*FROM employees*

*WHERE department = 'AI'; --returns emp. with highest salary in the AI department*



*SELECT AVG(salary)*

*FROM employees*

*WHERE department = 'HR'; --returns average salary of the HR department*



**Real Backend Examples**



**Dashboard**

*SELECT COUNT(\*)*

*FROM users;*



Displays:

Total Users: 12,580



**Shopping Website**

*SELECT MAX(price)*

*FROM products;*



Shows:

Most Expensive Product



**Analytics**

*SELECT AVG(rating)*

*FROM reviews;*



Shows:

Average Rating



#### **GROUP BY**

One of the Most Important SQL Topics



**Problem**

Right now, you can answer:

How many employees are there?



But **what if** the CEO asks:

How many employees are there in **each department**?

You don't want one answer—you want one answer **per department.**

That's exactly what **GROUP BY** does.



|**id**|**name**|**department**|**salary**|
|-|-|-|-|
|1|Agney|AI|60000|
|2|Ravi|HR|45000|
|3|Sneha|Finance|70000|
|4|John|AI|80000|
|5|Alice|HR|50000|



**This Query:**

*SELECT department, COUNT(\*)*

*FROM employees*

*GROUP BY department;*

**returns:**

|**Department**|**Employees**|
|-|-|
|AI|2|
|HR|2|
|Finance|1|



Notice something important:



COUNT(\*) gives **one total**.

GROUP BY department gives one total for **each department**.



This is the foundation of:



📊 Analytics dashboards

📈 Reports

📦 Inventory summaries

💰 Sales reports

👥 User statistics



**Whenever you see:**



*GROUP BY department*



Don't think:

"Sort by department."



Instead think:

"Create **one bucket** for each unique department."



**What is the difference between WHERE and GROUP BY?**



|**WHERE**|**GROUP BY**|
|-|-|
|Filters rows **"Before"** grouping|Groups rows with the **same value** together|
|Reduces the number of rows processed|Creates groups for **aggregate calculations**|



**Example:**



*SELECT department, AVG(salary)*

*FROM employees*

*WHERE salary > 50000*

*GROUP BY department;*



**Execution order:**



FROM employees

&#x20;     ↓

WHERE salary > 50000

&#x20;     ↓

GROUP BY department

&#x20;     ↓

AVG(salary)

&#x20;     ↓

SELECT



**A common interview question is:**



Why doesn't this work?



*SELECT department, AVG(salary)*

*FROM employees*

*GROUP BY department*

*ORDER BY salary;*



**Answer:**



After GROUP BY, each row represents a **group**, not an **individual employee**. Since salary is no longer a single value for each group, **SQL cannot order by it directly**. You must order by an aggregate like **AVG(salary)** or by its **alias.**





**THE RIGHT SQL ORDER**

*SELECT*

*FROM*

*WHERE*

*GROUP BY*

*HAVING*

*ORDER BY*

*LIMIT*

*OFFSET*



**Mnemonic:**



**S**mart **F**riends **W**rite **G**ood **H**igh-quality **O**rganized **L**earning **O**utlines



*S = SELECT*

*F = FROM*

*W = WHERE*

*G = GROUP BY*

*H = HAVING*

*O = ORDER BY*

*L = LIMIT*

*O = OFFSET*



#### **HAVING**

one of the most commonly confused SQL topics.

WHERE

filters **rows**.

HAVING filters **groups.**

But what if your manager asks:

Show only **departments** that have more than **one employee**.



|**WHERE**|**HAVING**|
|-|-|
|Filters rows|Filters groups|
|Runs before `GROUP BY`|Runs after `GROUP BY`|
|Cannot use aggregate functions|Can use aggregate functions|



**Real Backend Example**

Imagine an e-commerce platform.

You want categories that have more than 100 products.



*SELECT category,*

&#x20;      *COUNT(\*)*

*FROM products*

*GROUP BY category*

*HAVING COUNT(\*) > 100;*



This kind of query is common in analytics dashboards.



#### **JOINS**

Imagine you're building a company management system.

**| employee\_id | name  | department\_id |**

**| ----------: | ----- | ------------: |**

**|           1 | Agney |           101 |**

**|           2 | Ravi  |           102 |**

**|           3 | John  |           101 |**

**|           4 | Sneha |           103 |**



**The table stores:**



**department\_id**

101

102

103



**Instead of:**

AI

HR

Finance



Because storing department names repeatedly is bad database design.

You're repeating the same string thousands of times.

Instead, we create another table.



Departments Table

| department\_id | department\_name |

| ------------: | --------------- |

|           101 | AI              |

|           102 | HR              |

|           103 | Finance         |



Now we have **two tables**.

The tables are **related**.

This is called a **Relational Database.**



**INNER JOIN**



**The Problem**

Suppose your boss asks:



Show me every employee along with their department name.



**But...**



**Employees table has only:**

*101*

*102*

*103*



**Departments table has:**

*101 → AI*



*102 → HR*



*103 → Finance*



**How do we combine them?**



**WE USE INNER JOIN.**

**Syntax**

*SELECT columns*

*FROM table1*

*INNER JOIN table2*

*ON table1.column = table2.column;*



**Example**

*SELECT employees.name,*

&#x20;      *departments.department\_name*

*FROM employees*

*INNER JOIN departments*

*ON employees.department\_id = departments.department\_id;*



**Why Is This Better?**



Imagine HR changes their name.



From:

HR

to

Human Resources



**Without joins:**

You'd have to **update thousands** of employee rows.



**With joins:**

Only **one row changes**.



department\_id	department\_name

102	Human Resources



Done.

Every employee now automatically shows the new name.

This is why databases are relational.



**Real Backend Example**

Suppose you're building Amazon.



Users Table

id	name

1	Agney

2	John



Orders Table

order\_id	user\_id

101	1

102	2



Want:

Order	Customer

101	Agney

102	John



Use:

*SELECT orders.order\_id,*

&#x20;      *users.name*

*FROM orders*

*INNER JOIN users*

*ON orders.user\_id = users.id;*



Every **backend application** uses **joins**.



**Why We Use ON**



This line:

ON employees.department\_id = departments.department\_id



**tells SQL:**

How are these two tables **connected**?





**A Trick to Never Make This Mistake Again**



When writing a JOIN, always ask yourself:



What does **each column** represent?



For example:



Students Table

student\_id	name	course\_id

1	Agney	10



student\_id → Identifies the student.

course\_id → Identifies the course.



Courses Table

course\_id	course\_name

10	Python



course\_id also identifies the course.

**So the relationship is:**



Course



↓



course\_id



↓



Students.course\_id



**Not:**



student\_id



↓



course\_id



**Always join matching meanings**, not just matching data types.



**Without it...**

SQL has no idea how to **match rows**.



**⭐ INNER JOIN returns only the rows where the join condition matches in both tables.**



**⭐ Golden Rule (Remember This)**

When writing a JOIN, don't ask:

❌ "Which columns have the same data type?"



Instead ask:

✅ "Which columns represent the **same real-world relationship?**"





#### **LEFT JOIN**



**Now Suppose Your Manager Says**



"Show me **ALL customers**, even those who have **never placed an order.**"



INNER JOIN cannot do this.



That's where **LEFT JOIN** comes in.



**LEFT JOIN**

*SELECT Customers.name,*

&#x20;      *Orders.amount*

*FROM Customers*

*LEFT JOIN Orders*

*ON Customers.customer\_id = Orders.customer\_id;*



Result:

Customer	Amount

Agney	500

Ravi	NULL

John	700



Notice:

Ravi is now included.

Since he has no order, SQL fills the missing values with:



NULL



**NOT**

0



because there is **no matching row**, not an order with **amount zero**.

If nothing matches:

**NULL**

is inserted.



**Why Is It Called LEFT JOIN?**



Look at the query:

*FROM Customers*

*LEFT JOIN Orders*



The table before LEFT JOIN is the one SQL guarantees to keep.



LEFT TABLE

&#x20;    ↓



Customers



Everything in the **left table appears in the result**.



| **INNER JOIN**                  | **LEFT JOIN**                                                         |

| --------------------------- | ----------------------------------------------------------------- |

| Only matching rows          | All rows from the left table + matching rows from the right table |

| Non-matching rows disappear | Non-matching rows appear with `NULL`                              |





Suppose an interviewer asks:

**Why is Ravi's amount NULL instead of 0?**



Good answer:

Because there is **no matching row in the Orders table**. SQL uses **NULL to represent missing or unknown data**, not zero.



#### **RIGHT JOIN**

**LEFT JOIN** means keep everything from the **LEFT Table.**

**RIGHT JOIN in contrast** keeps everything from the **RIGHT Table.**



**RIGHT JOIN**

*SELECT Customers.name,*

&#x20;      *Orders.amount*

*FROM Customers*

*RIGHT JOIN Orders*

*ON Customers.customer\_id = Orders.customer\_id;*



**Result**

**Customer	Amount**

**Agney	500**

**John	700**

**NULL	900**



**Why?**

Because RIGHT JOIN keeps every order.



Even though Order 103 has **no matching customer,** SQL keeps it and fills the missing customer information with **NULL**.



Most backend developers prefer **LEFT JOIN** because it expresses the **same logic** as RIGHT JOIN by **swapping table order**. Using LEFT JOIN consistently **makes SQL queries easier to read and maintain.**





#### **FULL OUTER JOIN**

**Everything** is included.



**Real Backend Example**

Imagine two tables.



Employees

id	name

1	Agney

2	Ravi

Payroll

employee\_id	salary

1	60000

3	45000



Suppose HR wants to audit the database.



They want to know:

* Employees without payroll
* Payroll records without employees
* Correct matches



Use:



*SELECT \**

*FROM Employees*

*FULL OUTER JOIN Payroll*

*ON Employees.id = Payroll.employee\_id;*



This shows every inconsistency in one query.



| JOIN  | Think              |

| ----- | ------------------ |

| INNER | Only matching rows |

| LEFT  | Keep left table    |

| RIGHT | Keep right table   |

| FULL  | Keep everything    |



| JOIN       | Matching Rows | Left Only | Right Only |

| ---------- | :-----------: | :-------: | :--------: |

| INNER      |       ✅       |     ❌     |      ❌     |

| LEFT       |       ✅       |     ✅     |      ❌     |

| RIGHT      |       ✅       |     ❌     |      ✅     |

| FULL OUTER |       ✅       |     ✅     |      ✅     |



FULL OUTER JOIN is useful when you want to include all records from both tables, even if some records have no matching row. It's commonly used for auditing, reconciliation, and finding missing or inconsistent data.



You can join as many tables as you need.

In fact, in real backend applications, joining 3–6 tables in a single query is quite common.



There is no limit like "only two tables."

You just keep joining based on relationships.



**Important Rule ⭐**

Every **new table** you join must have a **relationship with one of the tables** already in the query.

Think of it like a chain.



Table A

&#x20;  │

&#x20;  ▼

Table B

&#x20;  │

&#x20;  ▼

Table C

&#x20;  │

&#x20;  ▼

Table D



Each connection is made through a **primary key ↔ foreign key** relationship.



#### **Foreign Keys (One of the Most Important Database Concepts)**

A Foreign Key is **a column in one table** that **references** the **Primary Key** of **another table.**



**Creating a Foreign Key**



*CREATE TABLE departments (*

&#x20;   *department\_id SERIAL PRIMARY KEY,*

&#x20;   *department\_name VARCHAR(50)*

*);*



**Now Employees:**



*CREATE TABLE employees (*

&#x20;   *employee\_id SERIAL PRIMARY KEY,*

&#x20;   *name VARCHAR(100),*

&#x20;   *department\_id INT,*



&#x20;   *FOREIGN KEY (department\_id)*

&#x20;       *REFERENCES departments(department\_id)*

*);*



**This line is the important one:**



*FOREIGN KEY (department\_id)*

*REFERENCES departments(department\_id)*



**Read it as:**



"employees.department\_id must exist inside departments.department\_id."



**With a Foreign Key**

**If you try:**

*INSERT INTO employees(name, department\_id)*

*VALUES ('Alice', 999);*



**PostgreSQL says:**

ERROR:

insert or update on table "employees"

violates foreign key constraint



The database protects your data.

This is called **Referential Integrity.**



**Referential Integrity**

Referential Integrity ensures that **every foreign key value** points to a **valid primary key** in the **referenced table**.



|**Primary Key**|**Foreign Key**|
|-|-|
|Uniquely identifies a row|References another table's primary key|
|Unique|Can repeat|
|Cannot be NULL (usually)|May be NULL (depending on design)|
|One per table (commonly)|Can have many|



A Primary Key uniquely identifies each row in a table and must be unique. A Foreign Key is a column that references the Primary Key of another table. Foreign Key values can repeat, but every value must exist in the referenced Primary Key column (unless the Foreign Key is allowed to be NULL).



#### **DATABASE RELATIONSHIPS**

**1:1, 1:N, N:M**



##### **1. One-to-One (1:1)**

**Definition**

One record in Table A is related to exactly one record in Table B.



Example: Person ↔ Passport

**Persons**

person\_id	name

1	Agney

2	Ravi

**Passports**

passport\_id	person\_id	passport\_no

101	1	P12345

102	2	P67890



**Relationship:**



Person

&#x20;  │

&#x20;  │ 1 : 1

&#x20;  │

Passport



One person has one passport.

One passport belongs to one person.



**Why not store the passport number in the Persons table?**



Sometimes data is split because:

Security

Privacy

Optional information

Better organization



##### **2. One-to-Many (1:N)**

This is the **most common relationship** in backend development.



Example: Department ↔ Employees

**Departments**

department\_id	department\_name

101	AI

102	HR

**Employees**

employee\_id	name	department\_id

1	Agney	101

2	John	101

3	Ravi	102



**Relationship:**



Department

&#x20;    │

&#x20;    │

&#x20;    ├── Agney

&#x20;    ├── John

&#x20;    └── Ravi



One department

↓

Many employees



**Another example:**



**Author → Books**

**Alice**



├── Python Basics



├── SQL Mastery



└── FastAPI Guide



One author

↓

Many books



##### **3. Many-to-Many (N:M)**



This is where beginners usually get confused.



Example: Students ↔ Courses



**Question:**



Can one student take multiple courses?



✅ Yes.



Can one course have multiple students?



✅ Yes.



**Then neither table can directly store the relationship.**



**Students**

student\_id	name

1	Agney

2	Ravi

**Courses**

course\_id	course\_name

10	Python

20	Java



**How do we connect them?**





**We create another table:**

##### **Enrollments (Bridge/Junction Table)**

student\_id		course\_id

1			10

1			20

2			10



**Meaning:**



Agney →Python Java



Ravi → Python



**Relationship:**

Students

&#x20;    │

&#x20;    │

Enrollments

&#x20;    │

&#x20;    │

Courses



**Notice:**

The relationship itself becomes a table.



**Why do we need a bridge (junction) table in a Many-to-Many relationship?**

**Answer:**

Because both entities can have **multiple related records**. A junction table **stores the relationships** between them using **foreign keys** from **both tables**.



#### **DATABASE NORMALIZATION**



Organize data to **reduce duplication** and **improve consistency**.

Think of normalization as **cleaning** and **organizing** your database.

##### **First Normal Form (1NF)**

**Rule**

Every column should contain one value only.

**❌ Not 1NF**

student	courses

Agney	Python, SQL, Java



One cell contains multiple values.



**✅ 1NF**

student	course

Agney	Python

Agney	SQL

Agney	Java



Each cell contains exactly **one value**.



##### **Second Normal Form (2NF)**

**Rule**

Every non-key column should depend on the whole primary key.



For now, remember this practical idea:

**Don't store duplicate information that belongs somewhere else.**



**Example:**



**Instead of:**



student\_id		course\_id	student\_name

1			10		Agney

1			20		Agney



**Store student\_name only in the Students table.**



##### **Third NORMAL FORM (3NF)**

**Rule**

**Non-key columns** should **depend** only on the **primary key,** **not** on another **non-key column**.



**Example:**



**❌**

employee\_id	department\_id	department\_name

1			101			AI

2			101			AI



The department name depends on department\_id, not on employee\_id.



**✅**



**Employees**



employee\_id	department\_id

1			101

2			101



**Departments**



department\_id	department\_name

101			AI



**Now:**



Update department name once.

No duplicate data.



**Why Companies Normalize Databases**



Imagine Amazon.



Without normalization:



Customer Name

Customer Address

Product Name

Product Price



could be repeated millions of times.



**With normalization:**



Customers



Products



Orders



Order\_Items



Everything is stored only once.

This saves storage and prevents inconsistencies.



**Advantages of Normalization**



✅ Less duplicate data



✅ Easier updates



✅ Better consistency



✅ Better data integrity



✅ Smaller storage



Why don't we store everything in one huge table?



**A strong answer:**

Because it causes data duplication, update anomalies, inconsistent data, and wasted storage. Normalization splits data into related tables to improve consistency and maintainability.



#### **🏆 Congratulations!**

You've now completed Database Design Fundamentals.

