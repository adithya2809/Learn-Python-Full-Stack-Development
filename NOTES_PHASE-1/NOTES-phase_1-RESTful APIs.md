What I would consider a stronger Python Full Stack roadmap

Phase 1: Web Fundamentals

HTML5

CSS3

Responsive Design

Flexbox

Grid

Basic UI design

Phase 2: JavaScript

ES6+

DOM

Async/Await

Fetch API

Local Storage

Phase 3: React

Components

Hooks

State management

Routing

API integration

Phase 4: Python

Core Python

OOP

Error handling

File handling

Data structures

Iterators

Generators

Phase 5: SQL

PostgreSQL

Database design

Joins

Indexes

Transactions

Phase 6: Backend



Choose one:



Option A (Most Jobs)

Django

Django REST Framework

Option B (Modern API Focus)

FastAPI

SQLAlchemy

Phase 7: Authentication

Sessions

Cookies

JWT

OAuth

Phase 8: Testing

Pytest

API testing

Test-driven development basics

Phase 9: Deployment

GitHub

Docker

CI/CD

Cloud deployment

Phase 10: Portfolio Projects



Build:



E-commerce platform

Task management app

Social media clone

SaaS application

REST API project



These projects teach far more than tutorials.









Phase 1: HTML/CSS Revision + Git (Week 1)

Monday–Friday (4–5 hrs/day)



Hour 1



HTML revision

Semantic tags

Accessibility basics



Hour 2



CSS revision

Flexbox

Grid



Hour 3



Responsive design



Hour 4–5



Build components:

Navbar

Hero section

Cards

Forms

Dashboard layout

Weekend



Build and deploy one responsive landing page.



Goal: Complete a project without tutorials.



Phase 2: JavaScript (Weeks 2–5)



This is where most learners spend insufficient time.



Week 2

Variables

Data types

Functions

Arrays

Objects

Week 3

ES6+

Arrow functions

Destructuring

Spread/rest

Modules

Week 4

DOM

Events

Event delegation

Week 5

Async/Await

Promises

Fetch API

Local Storage

Projects

Calculator

Todo App

Weather App

Quiz App



Target: 20–30 hours/week.



Phase 3: React (Weeks 6–8)

Week 6

Components

Props

JSX

Week 7

State

Hooks

Forms

Week 8

Routing

API integration

Project



Task Management Application



Features:



CRUD

Search

Filters

Local storage

Phase 4: Python (Weeks 9–11)



Since you're aiming for Python full stack, don't rush Python.



Week 9

Core Python

Functions

Modules

Week 10

OOP

Inheritance

Polymorphism

Week 11

Files

Exceptions

Iterators

Generators

Projects

Expense Tracker

Contact Manager

Library Management CLI

Phase 5: SQL + PostgreSQL (Weeks 12–13)

Week 12

SELECT

INSERT

UPDATE

DELETE

Week 13

Joins

Indexes

Normalization

Transactions

Project



Design a database for:



E-commerce

Social media

Learning platform

Phase 6: Django (Weeks 14–17)



This is where you become a Python backend developer.



Week 14

Django basics

URLs

Views

Week 15

Models

ORM

Week 16

Templates

Forms

Week 17

Authentication

Permissions

Project



Blog Application



Phase 7: Django REST Framework (Weeks 18–20)

Week 18

APIs

Serializers

Week 19

Authentication

JWT

Week 20

Permissions

Pagination

Filtering

Project



Task Management API



Phase 8: Docker + Deployment (Weeks 21–22)



Learn:



Docker

Linux basics

Environment variables

Deployment



Deploy projects using:



Render

Vercel

Phase 9: Portfolio Projects (Weeks 23–26)



Build 3 serious projects.



Project 1



E-commerce



Features:



Auth

Cart

Orders

Admin panel

Project 2



Social Media App



Features:



Profiles

Posts

Likes

Comments

Project 3



SaaS Dashboard



Features:



Authentication

Analytics

User roles

Daily Schedule (Weekdays)

Session 1 (90 min)



New concepts



Break (15 min)

Session 2 (90 min)



Exercises and coding practice



Break (15 min)

Session 3 (90–120 min)



Project work



This split is important because:



Tutorials create understanding.

Projects create employable skills.



Aim for roughly:



40% learning

60% building



PHASE-1

===

HTTP REQUESTS



| Status Code                   | Meaning                     | When to Use                 |

| ----------------------------- | --------------------------- | --------------------------- |

| \*\*200 OK\*\*                    | Request successful          | GET, successful updates     |

| \*\*201 Created\*\*               | New resource created        | POST                        |

| \*\*204 No Content\*\*            | Success, no response body   | DELETE                      |

| \*\*400 Bad Request\*\*           | Invalid request from client | Missing/invalid data        |

| \*\*401 Unauthorized\*\*          | Authentication required     | No token or invalid login   |

| \*\*403 Forbidden\*\*             | Permission denied           | Logged in but access denied |

| \*\*404 Not Found\*\*             | Resource doesn't exist      | Wrong URL or ID             |

| \*\*500 Internal Server Error\*\* | Server-side bug             | Exception in backend        |



RESTAPI - (Representational State Transfer)

The URL identifies what you're working with.



The HTTP method identifies what you're doing.



This is one of the biggest ideas in REST.

| Operation      | HTTP Method | URL        |

| -------------- | ----------- | ---------- |

| Create         | POST        | `/users`   |

| Read All       | GET         | `/users`   |

| Read One       | GET         | `/users/5` |

| Update Entire  | PUT         | `/users/5` |

| Update Partial | PATCH       | `/users/5` |

| Delete         | DELETE      | `/users/5` |



Path Parameter



Identifies which resource.



Example:



/users/7



Question:



Which user?



Answer:



User 7.



Query Parameters



Now suppose you don't want all users.



Maybe only active users.



Instead of:



/activeUsers



REST uses query parameters.



Example:



/users?status=active



| Requirement       | REST API                   |

| ----------------- | -------------------------- |

| View all jobs     | `GET /jobs`                |

| View Job #20      | `GET /jobs/20`             |

| Create a job      | `POST /jobs`               |

| Edit Job #20      | `PUT /jobs/20`             |

| Delete Job #20    | `DELETE /jobs/20`          |

| Search jobs       | `GET /jobs?role=Python`    |

| Jobs in Bangalore | `GET /jobs?city=Bangalore` |



REST APIs use nouns because the URL should represent the resource, while the HTTP method specifies the action to perform on that resource. This makes APIs consistent, readable, and easy to maintain.



A path parameter identifies a specific resource, while a query parameter is used to filter, search, sort, or paginate a collection of resources.



Need ONE specific resource?

&#x20;       ↓

Use Path Parameter



/users/25

/products/10

/orders/100



Need to FILTER or SEARCH resources?

&#x20;       ↓

Use Query Parameters



/products?category=laptop

/users?city=Hyderabad

/orders?status=completed



Line 1

from fastapi import FastAPI



Think of it as:



"I want to use the FastAPI framework, so import it."



Just like:



from math import sqrt

Line 2

app = FastAPI()



This creates your web application.



Think of it like creating an empty notebook.



Before writing notes, you first create the notebook.



Similarly, before creating API endpoints, we create the FastAPI application.



Everything we build later (routes, middleware, authentication, etc.) will belong to this app.



Line 3

@app.get("/")



This tells FastAPI:



"If someone sends a GET request to the root URL (/), run the function below."



Notice how it connects directly to what you've already learned:



HTTP Method	URL	Function Called

GET	/	home()

Line 4

def home():



This is just a normal Python function.



The difference is that FastAPI calls it automatically when a request arrives.



Line 5

return {"message": "Welcome to Python Full Stack Development!"}



This is a Python dictionary.



FastAPI automatically converts it into JSON before sending it back to the client.



That's why FastAPI is loved—it handles a lot of the work for you.



@app.get("/users/{id}")

This is called Dynamic Routing



Instead of creating thousands of routes, we create one dynamic route.



Think of it like this:



&#x20;               Request

&#x20;                  │

&#x20;     ┌────────────┼────────────┐

&#x20;     │            │            │

&#x20;     ▼            ▼            ▼

&#x20;/users/1    /users/25   /users/999

&#x20;     │            │            │

&#x20;     └────────────┼────────────┘

&#x20;                  ▼

&#x20;       @app.get("/users/{id}")

&#x20;                  │

&#x20;                  ▼

&#x20;         get\_user(id)



One function.



Unlimited users.



But this will not work correctly:





@app.get("/users/{id}")

def get\_user(user\_id: int):

&#x20;   ...



because FastAPI doesn't know that {id} should be passed into user\_id.



Rule:



The name inside {} in the URL must match the function parameter name.



This is a very common beginner mistake.



Optional Query Parameters



Suppose the client doesn't always want to send the brand.



We can make it optional.



from typing import Optional



@app.get("/products")

def get\_products(category: str, brand: Optional\[str] = None):

&#x20;   return {

&#x20;       "category": category,

&#x20;       "brand": brand

&#x20;   }



Now both work:



/products?category=laptop



and



/products?category=laptop\&brand=hp



If no brand is sent:



{

&#x20;   "category":"laptop",

&#x20;   "brand": null

}



Required vs Optional



This is another favorite interview question.



Required

category: str



Client must send it.



Otherwise FastAPI returns:



422 Unprocessable Entity



Optional

brand: Optional\[str] = None



Client may send it.



If not:



brand = None







| Requirement              | REST API                                    |

| ------------------------ | ------------------------------------------- |

| Book #15                 | `GET /books/15` ✅                           |

| Books by Robert Martin   | `GET /books?author=Robert%20Martin`         |

| Python books under ₹1000 | `GET /books?category=Python\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&max\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\_price=1000` |

| Page 3 with 20 books     | `GET /books?page=3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\&limit=20`





Request Body





When you click Register, the frontend sends:



POST /students

Content-Type: application/json



Body:



*{*

&#x20;   *"name": "Aditya",*

&#x20;   *"age": 21,*

&#x20;   *"branch": "CSE"*

*}*



Notice something.



The URL didn't change.



The data is inside the request body.





Pydantic



FastAPI uses Pydantic for automatic validation.

from pydantic import BaseModel

Now create a model.



*class Student(BaseModel):*

&#x20;   *name: str*

&#x20;   *age: int*

&#x20;   *branch: str*



Why inherit from BaseModel?

Because BaseModel gives us powerful features for free:



* Automatic validation
* Automatic type conversion
* JSON parsing
* Error messages
* Swagger documentation



Suppose Postman sends:



*{*

&#x20;   *"name": "Aditya",*

&#x20;   *"age": 21,*

&#x20;   *"branch": "CSE"*

*}*



FastAPI automatically does something like:



*student = Student(*

&#x20;   *name="Aditya",*

&#x20;   *age=21,*

&#x20;   *branch="CSE"*

*)*



Then calls:



create\_student(student)



You don't write any parsing code.



FastAPI does it.



The Magic



Now suppose someone sends:



*{*

&#x20;   *"name": "Aditya",*

&#x20;   *"age": "Twenty One",*

&#x20;   *"branch": "CSE"*

*}*



Before your function even runs...



FastAPI checks:



age should be int



It isn't.



So FastAPI immediately returns:



*422 Unprocessable Entity*



Your function is never executed.



This is one of FastAPI's greatest strengths.



#### **FOLDER STRUCTURE**



**The Single Responsibility Principle(SRP)**

One file.



One responsibility.



Example:



students.py



should only know about students.



It shouldn't know about:



Database connection

JWT

Courses

Teachers



This makes software easier to maintain.



app/

│

├── main.py

│

├── routers/

│   ├── \_\_init\_\_.py

│   └── students.py

│

├── schemas/

│   ├── \_\_init\_\_.py

│   └── student.py

│

├── models/

│   └── \_\_init\_\_.py

│

├── database.py

│

├── config.py

│

└── utils.py



##### **The Routers**

*from fastapi import APIRouter*

*from app.schemas.student import Student*



*router = APIRouter()*

*@router.post("/students")*

*def create\_student(student: Student):*

&#x20;   *return {*

&#x20;       *"message": "Student created",*

&#x20;       *"student": student*

&#x20;   *}*

Now your main.py becomes:



*from fastapi import FastAPI*

*from app.routers import students*



*app = FastAPI()*



*app.include\_router(students.router)*



Read the last line like English:



"Include all routes defined in the students router."



That's all.



#### **CRUD Operations**



|**Operation**|**HTTP Method**|**REST Endpoint**|
|-|-|-|
|Create|POST|/students|
|Read all|GET|/students|
|Read One|GET|/students/{id}|
|Update|PUT/PATCH|/students/{id}|
|Delete|DELETE|/students/{id}|



#### **UNIQUE IDENTIFIERS**



Every resource should have a unique identifier.



That's why databases use a Primary Key.



We'll represent it like this:



*\[*

&#x20;   *{*

&#x20;       *"id": 1,*

&#x20;       *"name": "Aditya",*

&#x20;       *"age": 21,*

&#x20;       *"branch": "CSM"*

&#x20;   *}*



**Real Companies Do Exactly This**



Amazon

*Product ID*



LinkedIn

*User ID*



Netflix

*Movie ID*



GitHub

*Repository ID*



Every resource has a unique identifier.





***The server is responsible for generating IDs. The client only sends the data.***



One Model Is Not Enough



Professional FastAPI applications usually have multiple schemas.



Instead of:



*Student*



we create:



*StudentCreate*



and



*StudentResponse*



Why?



***Because the data we receive isn't always the same as the data we return.***



###### **Important software engineering principle:**



*Model your data based on its purpose, not just its structure.*



**What A Backend Developer uses Daily:**

* Searching data
* Returning 404 Not Found
* Raising exceptions
* Writing business logic





This is something real developers constantly do.



Instead of storing raw Student objects, let's store dictionaries with IDs.



Modify your create\_student endpoint like this:



*students\_db = \[]*



*next\_id = 1*



*@router.post("/students")*

*def create\_student(student: Student):*

&#x20;   *global next\_id*



&#x20;   *student\_data = {*

&#x20;       *"id": next\_id,*

&#x20;       *"name": student.name,*

&#x20;       *"age": student.age,*

&#x20;       *"branch": student.branch*

&#x20;   *}*



&#x20;   *students\_db.append(student\_data)*



&#x20;   *next\_id += 1*



&#x20;   *return student\_data*





**Let's Understand This**



Initially:



*next\_id = 1*



Create first student:



*{*

&#x20;   *"id": 1,*

&#x20;   *"name": "Aditya"*

*}*



Increment:



*next\_id = 2*



Create second student:



*{*

&#x20;   *"id": 2,*

&#x20;   *"name": "Rahul"*

*}*



Increment:



*next\_id = 3*



Exactly how an auto-increment primary key works in PostgreSQL.



Suppose someone requests:



GET /students/100



But only students 1 and 2 exist.



Should we return:



null



❌ No.



Should we crash the server?



❌ Definitely not.



Instead:



raise HTTPException(

&#x20;   status\_code=404,

&#x20;   detail="Student not found"

)



**What is *HTTPException***

Suppose someone requests:

We use HTTPException to return proper HTTP error responses to the client. It immediately stops the function and sends the specified status code and message, without crashing the server.

GET /students/100

**But only students 1 and 2 exist.**

FastAPI automatically sends:

*404 Not Found*

with

*{*

&#x20;   *"detail": "Student not found"*

*}*

This is the professional way to tell the client:



"The request was valid, but the resource doesn't exist."

**Question:**

How do companies like Amazon or LinkedIn search millions of records quickly?



**Answer:**

They don't use Python lists.

They use database indexes.



The **path parameter** identifies which resource should be **updated**, while the **request body** contains the **new data**. Keeping the ID in the URL follows REST principles and prevents clients from modifying the resource identifier.



#### **PUT v/s PATCH**



|**Feature**|**PUT**|**PATCH**|
|-|-|-|
|**Full update**|**✅**|**❌**|
|**Partial update**|**❌**|**✅**|
|**All fields required**|**✅**|**❌**|
|**Uses `Student`**|**✅**|**❌**|
|**Uses `StudentUpdate`**|**❌**|**✅**|



**PUT**

*class Student(BaseModel):*

&#x20;   *name: str*

&#x20;   *age: int*

&#x20;   *branch: str*

**Everything is required.**

**PATCH**

*class Update\_Student(BaseModel):*

&#x20;   *name: Optional\[str] = None*

&#x20;   *age: Optional\[int] = None*

&#x20;   *branch: Optional\[str] = None*

**OPTIONAL**



#### **response\_model**

This is one of FastAPI's most powerful features.

Instead of:



*@router.get("/students/{id}")*

*def get\_student(id:int):*



We'll write:



*@router.get(*

&#x20;   *"/students/{id}",*

&#x20;   *response\_model=StudentResponse*

*)*

**The client sends only the data it owns. The server generates and manages the rest.**





|**Field**|**StudentCreate(POST)**|**StudentResponse(GET)**|**Why?**|
|-|-|-|-|
|`name`|✅|✅|Client sends it, server returns it.|
|`age`|✅|✅|Client sends it, server returns it.|
|`id`|❌|✅|Server generates it and returns it.|
|`created\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\_at`|❌|✅|Server creates the timestamp and returns it.|
|`is\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\_deleted`|❌|✅|Server manages it. Clients should never set it.|



The **client** provides **input**.

The server **verifies, calculates, and decides**.



|**Field**|**Owner**|
|-|-|
|Name|client|
|Email|client|
|Address|client|
|ID|server|
|Balance|server|
|Price|server|
|Created At|server|
|Role (Admin/User)|server|
|Is Deleted|server|



Whenever you're unsure who should control a field, ask yourself:

"If a **malicious user** changed this **value**, could it cause a **security** or **business problem?**"

If the answer is **yes**, that field **belongs** to the **server**.



***StudentCreate***

is for requests.



***StudentResponse***

is for responses.



Client sends

*{*

&#x20;   *"name": "Aditya",*

&#x20;   *"age": 21,*

&#x20;   *"branch": "CSE"*

*}*



FastAPI validates it using:



*StudentCreate*



↓



Server processes it



↓



Server creates:



*{*

&#x20;   *"id": 1,*

&#x20;   *"name": "Aditya",*

&#x20;   *"age": 21,*

&#x20;   *"branch": "CSE",*

&#x20;   *"created\_at": "...",*

&#x20;   *"is\_deleted": False*

*}*



↓



Before sending the response, FastAPI filters it through:



*StudentResponse*



↓



Client finally receives:



*{*

&#x20;   *"id": 1,*

&#x20;   *"name": "Aditya",*

&#x20;   *"age": 21,*

&#x20;   *"branch": "CSE"*

*}*



This entire flow is exactly how many production FastAPI applications work.



software engineering principle:



**Expose** only the **data** that the **client** **needs**—nothing more.



This is also called the **Principle of Least Privilege**. While it's often discussed in terms of permissions, the same idea applies to API responses: only **expose** the **minimum information necessary.**

#### **Professional HTTP Status Codes**



You've already seen these:



200 OK

201 Created

404 Not Found

422 Unprocessable Entity

*status\_code=status.HTTP\_201\_CREATED*



Now your code explains itself.

Anyone reading it immediately knows:

"This endpoint creates a resource."

No need to remember magic numbers.



**Version 1**

*status\_code=201*

**Version 2**

*status\_code=status.HTTP\_201\_CREATED*



Which one tells you what's happening without remembering numbers?

Obviously **Version 2**.

That's why professional code uses the status constants.



#### **Configuration \& .env**

Suppose your database.py contains:



*DATABASE\_URL = "postgresql://postgres:password123@localhost:5432/student\_db"*



Looks fine?

Imagine uploading your project to GitHub.

Now everyone can see:

* Your database username
* Your password
* Your database name
* That's a serious security issue.

It reads:

*.env*

and loads everything into Python.

Think of it like this:



.env

&#x20;     │

&#x20;     ▼

python-dotenv

&#x20;     │

&#x20;     ▼

Python Program



Create config.py



Inside app/



**Create:**



config.py



Write:



*from dotenv import load\_dotenv #*(Imports the function that reads the .env file.)

*import os*    #The os module lets Python access environment variables.



*load\_dotenv()*     #This reads the .env file.



*DATABASE\_URL = os.getenv("DATABASE\_URL")*      #Read it like English: "Get the value of DATABASE\_URL from the environment."

If .env contains:



*DATABASE\_URL=postgresql://localhost/student\_db*

then:

*DATABASE\_URL*

becomes:

*postgresql://localhost/student\_db*

*SECRET\_KEY = os.getenv("SECRET\_KEY")*

*DEBUG = os.getenv("DEBUG")*



**VISUAL FLOW**

.env

│

├── DATABASE\_URL

├── SECRET\_KEY

└── DEBUG

&#x20;       │

&#x20;       ▼

load\_dotenv()

&#x20;       │

&#x20;       ▼

os.getenv()

&#x20;       │

&#x20;       ▼

Python Variables



**Never Upload .env**



Create another file:



.gitignore



Add:

.env

Now Git ignores it.

So:

GitHub

never receives your secrets.

