# **GETTING INTO DATABASE MANAGEMENT SYSTEMS**



## **PostgreSQL**

PostgreSQL is an open-source **relational database management system (RDBMS)** that stores, manages, and retrieves relational data using SQL. It supports advanced features such as **transactions, indexing, foreign keys,** and **ACID compliance.**



**For A GET Request:**

Postman (Client)



↓



FastAPI



↓



SQLAlchemy



↓



**PostgreSQL Server**



↓



Database



↓



Table



Then the response comes back in reverse.



#### **Connecting FastAPI to PostgreSQL**



##### **Step 1: The Libraries**



We need Python to talk to PostgreSQL.

There are two important libraries.



###### **SQLAlchemy**

**SQLAlchemy is a Python ORM (Object Relational Mapper) that allows us to interact with the database using Python objects. It generates SQL queries and sends them to PostgreSQL.**

It is the ORM.

It converts Python code into SQL.



**Example:**



*student = Student(name="Agney")*

*session.add(student)*

**↓**

**SQLAlchemy generates:**

*INSERT INTO students(name)*

*VALUES('Agney');*



###### **psycopg**



Think of it as the **driver.**

Just like Windows needs a printer driver,

Python needs a **PostgreSQL driver.**



Python

↓

**psycopg**

↓

PostgreSQL



Without it,

Python **cannot communicate** with PostgreSQL.



##### **Step 2: Install Packages**



Inside your project's virtual environment:

*pip install sqlalchemy psycopg\[binary]*

We'll also install Alembic later.



##### **Step 3: Database URL**



**Create:**



**.env**



**Inside:**

*DATABASE\_URL=postgresql+psycopg://postgres:YOUR\_PASSWORD@localhost:5432/DatabaseName*



**Let's understand every part.**

*postgresql+psycopg://*

*↓*

*SQLAlchemy should use **PostgreSQL through psycopg.***



*postgres*

↓

Username.



*YOUR\_PASSWORD*

↓

The password you entered during PostgreSQL installation.



*localhost*

↓

Database is running on your computer.



*5432*

↓

Port.



*DatabaseName*

*↓*

Your database.



##### **Step 5: database.py**



We'll create this file.



*from sqlalchemy import create\_engine*

*from sqlalchemy.orm import sessionmaker, declarative\_base*

*import os*

*from dotenv import load\_dotenv*



*load\_dotenv()*



*DATABASE\_URL = os.getenv("DATABASE\_URL")*



*engine = create\_engine(DATABASE\_URL)*



*SessionLocal = sessionmaker(*

&#x20;   *autocommit=False,*

&#x20;   *autoflush=False,*

&#x20;   *bind=engine*

*)*



*Base = declarative\_base()*



Don't worry if this looks new.



###### **Understanding It**

*create\_engine()*



Think of the engine as:

FastAPI

↓

Engine

↓

PostgreSQL

It creates the connection.



*SessionLocal*

Remember transactions?



BEGIN

↓

Queries

↓

COMMIT



A Session manages those transactions.



*Base*

Every SQLAlchemy model inherits from Base.



Later:

*class Student(Base):*

&#x20;   *...*





#### **Understanding Engine, Session \& Base**



Before writing any models, you need to understand these three objects:

*engine = create\_engine(DATABASE\_URL)*

*SessionLocal = sessionmaker(...)*

*Base = declarative\_base()*



These are the foundation of SQLAlchemy.

SQLAlchemy itself has three major components:



Engine

&#x20;   │

&#x20;   ▼

Session

&#x20;   │

&#x20;   ▼

Models



We'll learn them one by one.



1. ###### **ENGINE**

Imagine PostgreSQL is a city.

Your FastAPI application wants to visit that city.



Can it?

❌ No.



It first needs a road.

The Engine is that road.

**The engine knows:**

Which database?

Which username?

Which password?

Which port?



That's why we write:

*engine = create\_engine(DATABASE\_URL)*

Read it as:

"Create a **connection manager** to my PostgreSQL database."

The engine maintains a **connection pool.**



**Why Connection Pool?**

Suppose 100 users open your website.



Without pooling:

User 1 → New Connection

User 2 → New Connection

User 3 → New Connection

...

The database would constantly create and destroy connections. Very expensive.



**Instead:**

Engine

↓

Connection Pool

↓

**Reuse connections**



This is one reason **SQLAlchemy is efficient**.



###### **2. Session**

Imagine the Engine is a highway.

Now imagine you drive a car on that highway.

That car is the Session.



A Session is your **conversation with the database.**

**Example:**

*session = SessionLocal()*



Now you can do:

*session.add(student)*

*session.commit()*



Everything happens through the session.



**Remember Transactions?**

Earlier we learned:

BEGIN

↓

UPDATE

↓

INSERT

↓

COMMIT



Guess what?



The **Session manages transactions!**



When you write:

*session.commit()*

It's equivalent to:

*COMMIT;*



When you write:

*session.rollback()*

It's equivalent to:

*ROLLBACK;*



Everything is connected.



###### **3. Base**



This one seems mysterious until you know what it does.

Suppose we create:



*class Student:*

&#x20;   *pass*



Python understands it.

But SQLAlchemy doesn't.



**Instead:**



*class Student(Base):*

&#x20;   *...*



Now SQLAlchemy knows:



"This class represents a **database table**."

Base is simply the **parent class** for all database models.



Example:



*class Student(Base):*

&#x20;   *\_\_tablename\_\_ = "students"*



Later:

*class Teacher(Base):*



Later:

*class Course(Base):*



Every model inherits from Base.



**Why Not Connect Directly?**



Many beginners ask:



"Why not just use create\_engine() everywhere?"

Because the **Engine only manages connections.**



It does not:

track objects

manage transactions

commit changes

rollback changes



That's the **Session's job**.





#### **Your First SQLAlchemy Model**



Until now, you manually created this table:



*CREATE TABLE students (*

&#x20;   *id SERIAL PRIMARY KEY,*

&#x20;   *name VARCHAR(100) NOT NULL,*

&#x20;   *age INTEGER NOT NULL,*

&#x20;   *course VARCHAR(100) NOT NULL*

*);*



Today we'll write the Python equivalent.



###### **Step 1: Create models.py**



Inside your app folder:



app/

│

├── main.py

├── database.py

├── config.py

├── models.py   👈 NEW

├── schemas.py

└── routers/



###### **Step 2: Write the Model**

*from sqlalchemy import Column, Integer, String*

*from app.database import Base*



*class Student(Base):*

&#x20;   *\_\_tablename\_\_ = "students"*



&#x20;   *id = Column(Integer, primary\_key=True, index=True)*

&#x20;   *name = Column(String(100), nullable=False)*

&#x20;   *age = Column(Integer, nullable=False)*

&#x20;   *course = Column(String(100), nullable=False)*



Don't panic.

Let's decode every single line.



**Line 1**

*from sqlalchemy import Column, Integer, String*



These are SQLAlchemy's Python versions of SQL data types.



Compare:



SQL			SQLAlchemy

INTEGER		Integer

VARCHAR		String

Column		Column

**Line 2**

*from app.database import Base*



Remember?



*Base = declarative\_base()*

**Every model must inherit from Base.**



**Line 3**

*class Student(Base):*



Python sees:

Student class



SQLAlchemy sees:

Database table



Without Base:



class Student:

It becomes an ordinary Python class.



**Line 4**

*\_\_tablename\_\_ = "students"*



This tells SQLAlchemy:



Student class

↓

students table



Notice:



Student

(Class)

↓

students

(Table)



They don't have to be identical, but this naming convention is common.



**Line 5**

*id = Column(Integer, primary\_key=True, index=True)*



Let's compare.



SQL:



*id SERIAL PRIMARY KEY*



SQLAlchemy:



*id = Column(*

&#x20;   *Integer,*

&#x20;   *primary\_key=True,*

&#x20;   *index=True*

*)*



**Question:**



"Where is SERIAL?"



Great observation.



SQLAlchemy **automatically handles auto-increment** for an integer primary key in PostgreSQL.



So this:

*primary\_key=True*

is enough.



What does index=True mean?

Remember our Indexes lesson?



CREATE INDEX ...



Same thing.



SQLAlchemy automatically creates an index.



**Line 6**

*name = Column(*

&#x20;   *String(100),*

&#x20;   *nullable=False*

*)*



Compare.



SQL:



*name VARCHAR(100) NOT NULL*



SQLAlchemy:



*String(100)*

↓

VARCHAR(100)



*nullable=False*

↓

NOT NULL



Exactly the same idea.



**Line 7**

*age = Column(*

&#x20;   *Integer,*

&#x20;   *nullable=False*

*)*



Compare:



age INTEGER NOT NULL

↓

Integer



*nullable=False*

**Line 8**

*course = Column(*

&#x20;   *String(100),*

&#x20;   *nullable=False*

*)*



Exactly the same mapping.



|**SQL**|**SQLAlchemy**|
|-|-|
|CREATE TABLE|class Student(Base)|
|students|tablename|
|INTEGER|Integer|
|VARCHAR|String|
|PRIMARY KEY|primary\_key=True|
|NOT NULL|nullable=False|
|CREATE INDEX|index=True|





#### **SQLAlchemy CRUD Operations**



*SQLAlchemy*

*student = Student(*

&#x20;   *name="Agney",*

&#x20;   *age=22,*

&#x20;   *course="AI"*

*)*



*session.add(student)*

*session.commit()*



Let's understand every line.



**Step 1**

*student = Student(*

&#x20;   *name="Agney",*

&#x20;   *age=22,*

&#x20;   *course="AI"*

*)*



This does NOT insert anything.

It simply creates a Python object.



Exactly like:



*person = Person(name="Agney")*

Nothing has reached PostgreSQL yet.



**Step 2**

*session.add(student)*



Still nothing is saved permanently.



It tells SQLAlchemy:

"Track this object. I want to insert it later."

Think of it as putting a letter into an Outbox, not yet into the mailbox.



**Step 3**

*session.commit()*



NOW SQLAlchemy sends SQL to PostgreSQL.



Behind the scenes it generates something very close to:

*INSERT INTO students(name, age, course)*

*VALUES ('Agney',22,'AI');*



This is why we learned transactions first.

Remember?



COMMIT;

↓

SQLAlchemy

*session.commit()*



##### **READ**

SQL

*SELECT \**

*FROM students;*

*SQLAlchemy*

*students = session.query(Student).all()*



Meaning:

Give me all Student records.



SQL

*SELECT \**

*FROM students*

*WHERE id = 1;*

SQLAlchemy

*student = session.get(Student, 1)*



Notice how much cleaner it is.



##### **UPDATE**



SQL:

*UPDATE students*

*SET course = 'AI \& ML'*

*WHERE id = 1;*



SQLAlchemy:

*student = session.get(Student, 1)*

*student.course = "AI \& ML"*

*session.commit()*



Think about what happened.

You changed a Python object's attribute.

SQLAlchemy noticed that change.



Then generated:

*UPDATE students*

*SET course='AI \& ML'*

*WHERE id=1;*



Automatically.



##### **DELETE**



SQL:

*DELETE FROM students*

*WHERE id=1;*



SQLAlchemy:

*student = session.get(Student, 1)*

*session.delete(student)*

*session.commit()*



Again:

*session.commit()*

↓

COMMIT;





|**SQL**|**SQLAlchemy**|
|-|-|
|INSERT|session.add()+commit()|
|SELECT|query()/get()|
|UPDATE|Change attribute + commit()|
|DELETE|session.delete()+commit()|



#### **SQLAlchemy Relationships**



**Part 1 → ForeignKey**

*department\_id = Column(*

&#x20;   *Integer,*

&#x20;   *ForeignKey("departments.id")*

*)*

Question:

Does this look familiar?

It should.



It's equivalent to SQL:

*department\_id INT*

*REFERENCES departments(id)*

So far nothing new.



**Part 2 → relationship()**

This is the new thing.



*department = relationship("Department")*

What does this do?



It creates a **Python relationship**, not a database relationship.

That's a huge difference.



**Suppose:**



Department

id	name

1	AI



Employee

id	name	department\_id

5	Agney	1



**Without relationship:**

*employee.department\_id*



returns

1



That's all.



**With relationship:**

*employee.department*



returns

*Department(*

&#x20;   *id=1,*

&#x20;   *name="AI"*

*)*



Now you can do:

employee.department.name



Output:

AI



No SQL query written by you.



###### **One-to-Many Example**



Department:



*from sqlalchemy.orm import relationship*



*class Department(Base):*

&#x20;   *\_\_tablename\_\_ = "departments"*



&#x20;   *id = Column(Integer, primary\_key=True)*

&#x20;   *name = Column(String)*



&#x20;   *employees = relationship(*

&#x20;       *"Employee",*

&#x20;       *back\_populates="department"*

&#x20;   *)*



Employee:



*class Employee(Base):*

&#x20;   *\_\_tablename\_\_ = "employees"*



&#x20;   *id = Column(Integer, primary\_key=True)*



&#x20;   *name = Column(String)*



&#x20;   *department\_id = Column(*

&#x20;       *Integer,*

&#x20;       *ForeignKey("departments.id")*

&#x20;   *)*



&#x20;   *department = relationship(*

&#x20;       *"Department",*

&#x20;       *back\_populates="employees"*

&#x20;   *)*



Looks scary.

Actually it's very logical.



###### **What is back\_populates?**



Imagine:



Department

↓

Employees



Now imagine **going backwards**.



Employee

↓

Department



That's what back\_populates connects.



Department



employees

&#x20;    ▲

&#x20;    │

&#x20;    │

department



Employee



Department knows its Employees.

Employee knows its Department.

**Two-way navigation.**



###### **Compare with SQL**



**SQL:**



*SELECT \**

*FROM employees*

*INNER JOIN departments*

*ON employees.department\_id = departments.id;*



**SQLAlchemy:**



*employee.department.name*



SQLAlchemy secretly performs the JOIN for you (when needed).



###### **ForeignKey vs relationship()**



This is one of the most common interview questions.

|**ForeignKey**|**relationship()**|
|-|-|
|Creates the database relationship|Creates the Python object relationship|
|Stored in PostgreSQL|Exists in SQLAlchemy|
|Required|Usually used for convenient object navigation|
|Maintains referential integrity|Enables object navigation|





#### **Alembic (Database Migrations)**



###### **What is a Migration?**



A migration is a **controlled change** to the **database schema.**

Think of it as **version control** for your **database**.



Just like Git tracks changes to code...



Git



Version 1

↓

Version 2

↓

Version 3



Alembic tracks **changes to your database**.



Database



Version 1

↓

Version 2

↓

Version 3

&#x09;

###### **Why Do We Need Alembic?**



Imagine this team.



Developer A:

*class Student(Base):*

&#x20;   *name = Column(String)*



Developer B adds:

*email = Column(String)*



How does everyone else get the new database structure?



**Without Alembic:**

Everyone manually edits their database.

❌ Error-prone.



**With Alembic:**

Developer B creates a migration.



Everyone runs:

*alembic upgrade head*

Now everyone's database is **identical.**



###### **How Alembic Works**



**Suppose your model is:**



*class Student(Base):*

&#x20;   *\_\_tablename\_\_ = "students"*



&#x20;   *id = Column(Integer, primary\_key=True)*

&#x20;   *name = Column(String)*



**Later you change it to:**



*class Student(Base):*

&#x20;   *\_\_tablename\_\_ = "students"*



&#x20;   *id = Column(Integer, primary\_key=True)*

&#x20;   *name = Column(String)*

&#x20;   *email = Column(String)*



Alembic compares:



Old model

↓

New model

↓

Generates:



*ALTER TABLE students*

*ADD COLUMN email VARCHAR(255);*



**Automatically.**



**https://github.com/adithya2809/Learn-Python-Full-Stack-Development.git**

## **Now we start the FINAL integration.**



#### **Lesson 1 — Dependency Injection (get\_db())**



This is one of the most asked FastAPI interview topics.



**First understand the problem.**



Suppose someone sends



*POST /students*



Your router needs access to PostgreSQL.



How?



Currently you only have



engine

and

SessionLocal



inside database.py.



The router cannot directly use the engine.



It needs a **Session.**



A customer wants money.

Does he go to the entire bank?

No.



He gets a token.



Customer

↓

Token

↓

Counter

↓

Bank



That token is exactly what a Session is.



Therefore every request should get

New Session

↓

Perform Queries

↓

Close Session



Otherwise:



100 Requests

↓

100 Open Connections

↓

💥 Server Crash



FastAPI solves this using **Dependency Injection.**



We create one function.

Inside database.py



*def get\_db():*

&#x20;   *db = SessionLocal()*



&#x20;   *try:*

&#x20;       *yield db*

&#x20;   *finally:*

&#x20;       *db.close()*



*db = SessionLocal()*

Meaning:

Create a **new database session.**



*yield db*

This is NOT the same as return.



**Why is yield used instead of return?**

yield **pauses the function**, **lets FastAPI use the session**, and then **resumes execution** so the cleanup code (db.close()) can run.





*db.close()*

db.close() executes after the **request has finished**, regardless of whether the **request succeeded or raised an exception**. Because it's inside a finally block, it always runs.

That's one of the reasons ***try...finally*** is used.



**What happens if sessions are never closed?**

Database connections remain open.



Imagine:



100 Requests

↓

100 Sessions Open

↓

100 Database Connections Occupied

↓

New requests can't get a connection

↓

Application slows down or fails



This is called a **connection leak.**



**Session Lifecycle**



Client

↓

GET /students

↓

get\_db()

↓

Session Created

↓

Router uses Session

↓

Request finished

↓

Close Session

