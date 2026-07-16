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







&#x09;

