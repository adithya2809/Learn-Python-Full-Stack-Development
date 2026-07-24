# **PHASE-3 AUTHENTICATION AND SECURITY**



**Phase 3 Overview**



We'll go step by step instead of rushing into code.



**Phase 3**

│

├── 1. Authentication Fundamentals

├── 2. Password Hashing (bcrypt)

├── 3. JWT (JSON Web Tokens)

├── 4. User Registration

├── 5. User Login

├── 6. Protected Routes

├── 7. Current User (/me)

├── 8. Authorization (Roles)

├── 9. Refresh Tokens

├── 10. Best Security Practices



#### **Lesson 1 — Why Authentication Exists**

Imagine you've built this API:



*GET /students*

*POST /students*

*PUT /students/{id}*

*DELETE /students/{id}*



Right now, anyone who knows your API URL can do this:

*DELETE /students/1*



The server has no idea who sent the request.

It only knows:

"Someone made a request."



That's a huge security problem.



##### **What is Authentication?**

Authentication is the process of **verifying a user's identity.**



The server asks:

"Can you prove who you are?"



If the answer is yes:

Authenticated ✅



Otherwise:

401 Unauthorized



##### **Authentication vs Authorization**



People confuse these all the time.



**Authentication**

Answers:

Who are you?



Example:

Username: agney

Password: \*\*\*\*\*\*\*\*



Server:

✅ Yes, you are Agney.



**Authorization**

Authorization is the process of determining what an authenticated user is **allowed to access or perform.**

Answers:

What are you allowed to do?



Example:

Role = Student



Permissions:



View Profile      ✅

Update Profile    ✅

Delete Users      ❌



The user is authenticated but isn't allowed to delete users.



##### **Order of Events**

Request

&#x20;  │

&#x20;  ▼

Authentication

&#x20;  │

&#x20;  ▼

Identity Verified

&#x20;  │

&#x20;  ▼

Authorization

&#x20;  │

&#x20;  ▼

Allowed?

&#x20;  │

&#x20;┌─┴──────────┐

&#x20;│            │

Yes          No

&#x20;│            │

&#x20;▼            ▼

Response   403 Forbidden



Authentication always comes **before** Authorization.



##### **Where does login fit?**



When a user logs in:

Username

Password



the server:

Looks up the user in the database.

Checks the password.

If correct, creates an access token (JWT).

Sends the token back.



From then on, the user sends that token with every request instead of sending the password again.



#### **Lesson 2 – Password Storage**



Now let's move to something every backend developer must know.



Imagine a user registers:

Username: agney

Password: mypassword123



**Question:**

Should we store it in the database like this?



Username	Password

agney	mypassword123



**Imagine this situation**

Suppose our database contains:



id	username	password

1	agney	mypassword123

2	john	football@123

3	alice	qwerty789



Now imagine a hacker gains access to the database.



What do they see?

agney  → mypassword123

john   → football@123

alice  → qwerty789



**Game over.**

The hacker doesn't need to crack anything—they already have every password.



**There's another problem**



Many people reuse passwords.

For example:

Instagram  → mypassword123

Gmail      → mypassword123

Bank App   → mypassword123

College    → mypassword123



If our application's database is leaked, the hacker may try the same password on other websites.

That's why password leaks are so dangerous.



##### **So what do we do instead?**



We never store the original password.

Instead, we convert it into something called a **hash.**



**Example:**

mypassword123

&#x20;       │

&#x20;       ▼

Hash Function

&#x20;       │

&#x20;       ▼

9f86d081884c7d659a2feaa0c55ad015...



The database stores only the hash:



username	password\_hash

agney	9f86d081884c...



Even if someone steals the database, they don't immediately know the original password.



##### **Important Property of Hashing**



Hashing is **one-way.**



Password

&#x20;   │

&#x20;   ▼

Hash



✅ Easy to create a hash.

❌ Practically impossible to recover the original password from the hash.



This is why hashing is different from encryption.



**Then how does login work?**



A common question in interviews is:

"If you don't store the password, how can you check whether it's correct?"



Here's the process:

During Registration

Password

&#x20;   │

&#x20;   ▼

Hash

&#x20;   │

&#x20;   ▼

Store Hash in Database



During Login

The user types:



mypassword123



The server hashes it again:

mypassword123

&#x20;       │

&#x20;       ▼

9f86d081884c...



Now compare:



Database Hash

9f86d081884c...



Newly Generated Hash

9f86d081884c...



If both hashes match:

Login Successful ✅



Notice that the original password is never stored or compared directly.



##### **Encryption**



Encryption converts readable data into unreadable data using a key.

Original Data

&#x20;     │

Encryption Key

&#x20;     │

&#x20;     ▼

Encrypted Data

&#x20;     │

Decryption Key

&#x20;     │

&#x20;     ▼

Original Data



✅ It is reversible.

If you have the correct key, you can recover the original data.



Example:

HTTPS

WhatsApp messages (uses end-to-end encryption)

Credit card information

Bank transactions



|**Encryption**|**Hashing**|
|-|-|
|Reversible|❌ Not reversible|
|Uses keys|❌ No decryption key|
|Used to protect data while it is stored or transmitted|Used to verify data or store passwords|
|Original data can be recovered|Original data cannot be recovered|



###### **Why don't we encrypt passwords instead of hashing them?**

Because passwords **never need to be recovered.** During login, we only need to verify whether the entered password matches the stored one. Hashing is **one-way**, so even if the database is compromised, the **original passwords cannot simply be decrypted**. Encryption is designed for data that must be recovered later.



#### **Lesson 3 – What is bcrypt?**



Before learning bcrypt, let's understand the problem it solves.



Imagine two users register with the same password:

Agney  → password123

John   → password123



If we use a simple hash function:

password123

&#x20;     │

&#x20;     ▼

abc123xyz...



The database becomes:

User		Hash

Agney	abc123xyz...

John		abc123xyz...



Notice something?

The hashes are identical.



A hacker immediately knows:

"These two users have the same password."

That's already useful information for an attacker.



##### **Enter Salt**



bcrypt automatically adds something called a salt.

A salt is a **random value** added to the password **before hashing.**



**Example:**



For Agney:

Password

password123



Salt

A8f#92Lm

↓

Hash

$2b$12$Ax3....



For John:

Password

password123



Salt

Z7q!4TpK

↓

Hash

$2b$12$Hy8....



Even though the passwords are the same:

password123

password123



The stored hashes become completely different.



User		Password		Stored Hash

Agney	password123	$2b$12$Ax3...

John		password123	$2b$12$Hy8...



This makes attacks much harder.



Why is Salt Important?



**Without salt:**

password123

&#x20;     │

&#x20;     ▼

abc123



Every user gets the same hash.



**With salt:**

password123 + Random Salt A

&#x20;       │

&#x20;       ▼

Hash A



password123 + Random Salt B

&#x20;       │

&#x20;       ▼

Hash B



Same password.

Different hashes.



**How does login still work?**



You might think:

"If the salt is random every time, how can bcrypt verify the password?"



Excellent question.

bcrypt stores the salt inside the hash itself.



Example:

$2b$12$Ax3F...



This string contains:

Algorithm (2b)

Cost factor (12)

Salt

Final hash



When the user logs in:

Entered Password

&#x20;       │

&#x20;       ▼

bcrypt.checkpw()

&#x20;       │

Reads Salt from Stored Hash

&#x20;       │

Hashes Again

&#x20;       │

Compares



You don't have to manually store or retrieve the salt—bcrypt handles that for you.



##### **How FastAPI Uses bcrypt**



In FastAPI, we usually use the passlib library.



Hashing a password:

*from passlib.context import CryptContext*

*pwd\_context = CryptContext(*

&#x20;   *schemes=\["bcrypt"],*

&#x20;   *deprecated="auto"*

*)*



*hashed\_password = pwd\_context.hash("mypassword123")*



Example output:

*$2b$12$3Mq8h0N...*



Verifying a password:

*pwd\_context.verify(*

&#x20;   *"mypassword123",*

&#x20;   *hashed\_password*

*)*



This returns:

**True**



If the password is wrong:

**False**



Notice something important:

We never decrypt anything.



We simply ask bcrypt:

"Does this password **match this stored hash**?"



**Why bcrypt instead of SHA-256?**

bcrypt is preferred because it is i**ntentionally computationally expensive**. This **slows down brute-force** and d**ictionary attacks**, whereas algorithms like SHA-256 are designed to be **very fast.**



##### **The Entire Authentication Flow**

Imagine you're building a website.

A user clicks Register.



What actually happens?

User

&#x20;│

&#x20;│  Username + Password

&#x20;▼

FastAPI

&#x20;│

&#x20;│  Hash Password (bcrypt)

&#x20;▼

PostgreSQL

&#x20;│

&#x20;│  Store Username + Hashed Password

&#x20;▼

Registration Complete



Notice:

❌ The plain-text password is never stored.



**Later...**

The user clicks Login.



User

&#x20;│

&#x20;│ Username + Password

&#x20;▼

FastAPI

&#x20;│

&#x20;│ Find User

&#x20;▼

PostgreSQL

&#x20;│

&#x20;│ Return Stored Hash

&#x20;▼

bcrypt.verify()

&#x20;│

&#x20;├── Match? → ✅ Create JWT Token

&#x20;└── No Match → ❌ Invalid Credentials



This flow is the foundation of authentication in most modern web applications.



#### **Lesson 4 – JWT (JSON Web Token)**

**JWT stands for:**

JSON Web Token



It is simply a digitally signed token that proves:

"This user has already logged in."



Think of it as an identity card issued by your server.



**JWT Flow:**

&#x20;         Login

&#x20;            │

&#x20;            ▼

Username + Password

&#x20;            │

&#x20;            ▼

Password Verified

&#x20;            │

&#x20;            ▼

Create JWT

&#x20;            │

&#x20;            ▼

Send Token to User

&#x20;            │

&#x20;            ▼

User Stores Token

&#x20;            │

&#x20;            ▼

Every Future Request

&#x20;            │

&#x20;            ▼

Authorization:

Bearer <token>



##### **Inside a JWT**



A JWT has three parts.

HEADER.PAYLOAD.SIGNATURE



Example:

eyJhbGciOiJIUzI1NiJ9.

eyJzdWIiOiJhZ25leSJ9.

kJH82Hshaj...



Looks scary.

It's just **three Base64-encoded sections** separated by dots.



###### **Part 1 – Header**



The header tells the server:

*{*

&#x20; *"alg": "HS256",*

&#x20; *"typ": "JWT"*

*}*



Meaning:

Algorithm = HS256

Type = JWT



###### **Part 2 – Payload**



This contains information about the user.

Example:

*{*

&#x20; *"sub": "agney",*

&#x20; *"role": "student",*

&#x20; *"exp": 1780000000*

*}*



Notice:

It doesn't contain the password.



Instead it stores things like:

Username

User ID

Role

Expiration time



These are called **claims.**



###### **Part 3 – Signature**

This is the most important part.



The server creates a signature using:

Header

\+

Payload

\+

Secret Key



↓

Signature



Only your server knows the Secret Key.



If someone changes the payload:

role = admin



the signature becomes invalid.

Server immediately rejects it.



###### **Why Can't Users Modify the JWT?**

Suppose someone tries this.



Original token:

*{*

&#x20;   *"role":"student"*

*}*



They edit it to:

*{*

&#x20;   *"role":"admin"*

*}*



Can they become admin?

No.



Why?

Because the signature no longer matches.



The server verifies the signature using the secret key.



Payload Changed

↓

Signature Invalid

↓

401 Unauthorized ❌



###### **JWT is NOT Encryption**

Many beginners think:

"JWT encrypts my data."



It doesn't.

JWT is **signed**, not encrypted.



That means:

✅ The server can detect if someone changed the token.

❌ The payload is **not secret.**



That's why we **never put passwords** inside a JWT.



###### **Where is the JWT Sent?**

Every request includes it in the HTTP headers.



*GET /students*



Authorization: Bearer eyJhbGc...



The word **Bearer** simply means:

"I am presenting this token."



##### **Complete Authentication Flow**

&#x20;         Register

&#x20;              │

&#x20;              ▼

Password Hashed

&#x20;              │

&#x20;              ▼

Stored in PostgreSQL

&#x20;              │

&#x20;              ▼

&#x20;             Login

&#x20;              │

&#x20;              ▼

Password Verified

&#x20;              │

&#x20;              ▼

JWT Created

&#x20;              │

&#x20;              ▼

Client Stores JWT

&#x20;              │

&#x20;              ▼

Every API Request

&#x20;              │

&#x20;              ▼

Authorization: Bearer <JWT>

&#x20;              │

&#x20;              ▼

FastAPI Verifies JWT

&#x20;              │

&#x20;         ┌────┴────┐

&#x20;         │         │

&#x20;     Valid       Invalid

&#x20;         │         │

&#x20;         ▼         ▼

&#x20;    Allow Access 401 Unauthorized



##### **Where is JWT stored?**

The JWT is usually stored on the **client side**, commonly in an HTTP-only cookie for **better security** or, in some applications, in **browser storage**. The client sends it with each request, and the server validates it without storing session state.



#### **Lesson 5 – Project Structure for Authentication**

Until now, your Student Management API probably looks something like this:



app/

│

├── main.py

├── database.py

├── models.py

├── schemas.py

├── routers/

│     └── students.py

└── config.py



To support authentication, we'll gradually evolve it into:

app/

│

├── main.py

├── database.py

├── config.py

│

├── models.py

│

│

│

├── schemas/

│     ├── student.py

│     └── user.py          👈 NEW

│

├── routers/

│     ├── students.py

│     └── auth.py          👈 NEW

│

├── services/

│     └── auth.py          👈 NEW

│

├── utils/

│     └── security.py      👈 NEW

│

└── dependencies.py        👈 NEW



Don't worry—we'll create these one by one.



##### **Step 1 – Create a User Model**



Our Student API currently stores students.



But who logs in?

Not students.



**Users.**



So we need a new database table.



What information should a User have?

Think like a backend developer.



If someone registers on your website, what information do you need?

Not much.



A basic user table might look like this:

**Column**			**Purpose**

id				Unique identifier

username			Login name

email			Contact \& login

hashed\_password	Securely stored password

is\_active			Is the account active?

role				User or Admin



Notice something important.



We do not store:

password



Instead we store:

hashed\_password



This naming convention is used in many production codebases because it immediately tells other developers that the value is already hashed.



User Registration Flow

User

&#x20;│

&#x20;│ Username

&#x20;│ Email

&#x20;│ Password

&#x20;▼

FastAPI

&#x20;│

&#x20;│ Hash Password

&#x20;▼

hashed\_password

&#x20;│

&#x20;▼

PostgreSQL



Only the hashed password reaches the database.



Why separate Student and User?

Many beginners ask:

"Why not just add password to the Student table?"



Good question.

Because they represent different responsibilities.



Student

**Stores business data.**

Name

Age

Course



User

**Stores authentication data.**

Username

Email

Hashed Password

Role



This separation makes your application easier to maintain and extend.

Later, one user could even be linked to one or more students if your application required it.



##### **Step 1: Update models.py**



Right now, your models.py probably looks something like this:



*from sqlalchemy import Column, Integer, String*

*from app.database import Base*





*class Student(Base):*

&#x20;   *\_\_tablename\_\_ = "students"*



&#x20;   *id = Column(Integer, primary\_key=True, index=True)*

&#x20;   *name = Column(String, nullable=False)*

&#x20;   *age = Column(Integer)*

&#x20;   *course = Column(String)*



Now, below the Student model, add the User model.



*from sqlalchemy import Boolean  # Add this to your existing imports*





*class User(Base):*

&#x20;   *\_\_tablename\_\_ = "users"*



&#x20;   *id = Column(Integer, primary\_key=True, index=True)*

&#x20;   *username = Column(String(50), unique=True, nullable=False, index=True)*

&#x20;   *email = Column(String(100), unique=True, nullable=False, index=True)*

&#x20;   *hashed\_password = Column(String, nullable=False)*

&#x20;   *is\_active = Column(Boolean, default=True)*

&#x20;   *role = Column(String(20), default="user")*



Your models.py will now contain two models:



Student  → students table

User     → users table



##### **Step 2: Create the Table**



Since we've added a new model, PostgreSQL doesn't automatically know about it.

If you're using Alembic (which we learned in Phase 2), run:

*alembic revision --autogenerate -m "create users table"*



Then:

*alembic upgrade head*



This creates the users table in your database.



##### **Step 3: Verify in pgAdmin**



Open your database.



You should now see:

Tables

│

├── students

└── users



If you open users, you'll find columns like:

Column

id

username

email

hashed\_password

is\_active

role





**Production Flow**

Client

&#x20;  │

&#x20;  ▼

POST /register

&#x20;  │

&#x20;  ▼

FastAPI

&#x20;  │

&#x20;  ├── Validate input

&#x20;  ├── Check email exists

&#x20;  ├── Hash password (bcrypt)

&#x20;  ├── Create User object

&#x20;  └── Save to PostgreSQL

&#x20;           │

&#x20;           ▼

&#x20;       users table



This separation of responsibilities is called **Separation of Concerns**, and it's a key **software engineering principle**.



#### **Lesson 6 – Pydantic Schemas for Authentication**



Think back to Phase 1.



You learned:

SQLAlchemy Models → represent database tables

Pydantic Schemas → represent API data



These are different responsibilities.



**Question**

A user wants to register.



They send:

*{*

&#x20;   *"username": "agney",*

&#x20;   *"email": "agney@gmail.com",*

&#x20;   *"password": "Hello@123"*

*}*



Should the client send:

*{*

&#x20;   *"hashed\_password": "$2b$12$..."*

*}*

❌ No.



Why?

Because the client doesn't know how to hash passwords.



Only the **server** does.



**Flow of Registration:**

Client

&#x20;│

&#x20;│ username

&#x20;│ email

&#x20;│ password

&#x20;▼

FastAPI

&#x20;│

&#x20;│ Validate Data (Pydantic)

&#x20;▼

Hash Password

&#x20;│

&#x20;▼

SQLAlchemy User Model

&#x20;│

&#x20;▼

PostgreSQL



Notice something:

The client sends password.



The database stores hashed\_password.

They are different.

That's why we need different schemas.



##### **Schema 1 – UserCreate**



Used when the user registers.



*class UserCreate(BaseModel):*

&#x20;   *username: str*

&#x20;   *email: str*

&#x20;   *password: str*



Incoming JSON:

*{*

&#x20;   *"username": "agney",*

&#x20;   *"email": "agney@gmail.com",*

&#x20;   *"password": "Hello@123"*

*}*



This schema is only for receiving data.



##### **Schema 2 – UserLogin**



Login only needs:

*class UserLogin(BaseModel):*

&#x20;   *username: str*

&#x20;   *password: str*



Incoming request:

*{*

&#x20;   *"username":"agney",*

&#x20;   *"password":"Hello@123"*

*}*



Notice:

No email.

No role.

No id.



Because login doesn't need them.



##### **Schema 3 – UserResponse**



Suppose registration succeeds.



Should we return:

*{*

&#x20;   *"id":1,*

&#x20;   *"username":"agney",*

&#x20;   *"email":"agney@gmail.com",*

&#x20;   *"hashed\_password":"$2b$12$..."*

*}*



❌ Never.



Instead:

*class UserResponse(BaseModel):*

&#x20;   *id: int*

&#x20;   *username: str*

&#x20;   *email: str*



Response:

*{*

&#x20;   *"id":1,*

&#x20;   *"username":"agney",*

&#x20;   *"email":"agney@gmail.com"*

*}*



No password.

No hash.



##### **Professional API Design**

Register Request

*{*

&#x20;   *"username":"agney",*

&#x20;   *"email":"agney@gmail.com",*

&#x20;   *"password":"Hello@123"*

*}*

↓

Server hashes password.

↓

Database stores:

id

username

email

hashed\_password

role

is\_active



↓

Server returns:

*{*

&#x20;   *"id":1,*

&#x20;   *"username":"agney",*

&#x20;   *"email":"agney@gmail.com"*

*}*



Everything has its **own responsibility.**



##### **schemas/user.py**

*from pydantic import BaseModel, EmailStr*



*class UserCreate(BaseModel):*

&#x20;   *username: str*

&#x20;   *email: EmailStr*

&#x20;   *password: str*





*class UserLogin(BaseModel):*

&#x20;   *username: str*

&#x20;   *password: str*





*class UserResponse(BaseModel):*

&#x20;   *id: int*

&#x20;   *username: str*

&#x20;   *email: EmailStr*



&#x20;   *class Config:*

&#x20;       *from\_attributes = True*



💡 Why EmailStr instead of str?



Earlier I used str to keep the focus on authentication.

In a production project, it's better to use:

*from pydantic import EmailStr*



because Pydantic **automatically validates** the email format.



**For example:**

✅ Accepted:

agney@gmail.com



❌ Rejected:

agney



FastAPI will automatically return a **422 Validation Error** before your route logic even runs.



#### **Lesson 7 – Register API**

This is the first endpoint where everything you've learned comes together.



We'll combine:

✅ SQLAlchemy Model (User)

✅ Pydantic Schema (UserCreate)

✅ Password Hashing (bcrypt)

✅ Database Session

✅ API Endpoint



##### **Step 1: Create routers/auth.py**



Your project should now look like this:

app/

│

├── routers/

│     ├── students.py

│     └── auth.py      👈 NEW



This router will handle everything related to authentication:

Register

Login

Refresh Token (later)

Logout (later)



###### **Let's design the registration flow.**



Suppose a user sends:



*{*

&#x20;   *"username": "agney",*

&#x20;   *"email": "agney@gmail.com",*

&#x20;   *"password": "Hello@123"*

*}*



What should our API do?

Think step by step.



Receive Request

&#x20;      │

&#x20;      ▼

Validate Data

&#x20;      │

&#x20;      ▼

Check Username Exists?

&#x20;      │

&#x20;      ▼

Check Email Exists?

&#x20;      │

&#x20;      ▼

Hash Password

&#x20;      │

&#x20;      ▼

Create User Object

&#x20;      │

&#x20;      ▼

Save to Database

&#x20;      │

&#x20;      ▼

Return User Response



Notice that every step has a purpose.



#### **Let's build your first authentication endpoint.**

##### **Step 1: Create routers/auth.py**



Create a new file:

app/

├── routers/

│     ├── students.py

│     └── auth.py   👈 NEW



Start with this:

*from fastapi import APIRouter*



*router = APIRouter(*

&#x20;   *prefix="/auth",*

&#x20;   *tags=\["Authentication"]*

*)*



**Explanation**



**Import APIRouter**

*from fastapi import APIRouter*



Just like in your students.py router.

APIRouter helps us organize related endpoints.



Instead of putting everything in main.py:



@app.get(...)

@app.post(...)

@app.put(...)



we group them.

students.py  → Student APIs

auth.py      → Authentication APIs



This keeps the project clean.



**Create the router**

*router = APIRouter(*

&#x20;   *prefix="/auth",*

&#x20;   *tags=\["Authentication"]*

*)*



prefix="/auth" means every endpoint starts with:

/auth



For example:

*POST /auth/register*

*POST /auth/login*

*GET  /auth/me*





***tags=\["Authentication"]***



This is only for the **Swagger UI.**

Instead of showing all endpoints together, Swagger **groups** them under:



Authentication

\-------------

POST /register

POST /login

GET /me



##### **Step 2: Required Imports**



Now add these imports.



*from fastapi import APIRouter, Depends, HTTPException*

*from sqlalchemy.orm import Session*



*from app.database import get\_db*

*from app.models import User*

*from app.schemas.user import UserCreate, UserResponse*



###### **Why each import?**

**Depends**

Allows FastAPI to inject the database session.



Later you'll write:

*db: Session = Depends(get\_db)*



instead of creating sessions manually.



**HTTPException**

Instead of:

*print("Email exists")*



we can return

*raise HTTPException(*

&#x20;   *status\_code=400,*

&#x20;   *detail="Email already registered"*

*)*



FastAPI automatically converts it into a JSON response.



**Session**

Represents the **current database transaction.**



Everything we do—

Query

Insert

Update

Delete



—uses this session.



**User**

Our SQLAlchemy model.

Used to interact with the **users table.**



**UserCreate**

Incoming request.

*{*

&#x20;   *"username":"agney",*

&#x20;   *"email":"agney@gmail.com",*

&#x20;   *"password":"Hello@123"*

*}*



**UserResponse**

Outgoing response.

*{*

&#x20;   *"id":1,*

&#x20;   *"username":"agney",*

&#x20;   *"email":"agney@gmail.com"*

*}*



Notice:

No password.

No hash.



#### **Next Step: Password Hashing**



Before we can implement POST /auth/register, we need a function that hashes passwords.



We'll create a dedicated file:

app/

│

├── utils/

│     └── security.py



This file will contain only authentication utilities.



Example:

*from passlib.context import CryptContext*



*pwd\_context = CryptContext(*

&#x20;   *schemes=\["bcrypt"],*

&#x20;   *deprecated="auto"*

*)*



*def hash\_password(password: str) -> str:*

&#x20;   *return pwd\_context.hash(password)*



*def verify\_password(plain\_password: str, hashed\_password: str) -> bool:*

&#x20;   *return pwd\_context.verify(plain\_password, hashed\_password)*



##### **What is passlib?**



passlib is a Python library that provides **secure password hashing.**

Instead of writing complex bcrypt code yourself:

\# Complex low-level bcrypt usage



You simply write:

*hashed = pwd\_context.hash(password)*

and

*pwd\_context.verify(password, hashed)*



It handles the hashing and verification securely.



Your Code

&#x20;    │

&#x20;    ▼

Passlib

&#x20;    │

&#x20;    ▼

bcrypt Algorithm

&#x20;    │

&#x20;    ▼

Hashed Password



Why don't we use hashlib?



This is an interview question.



Python has:



import hashlib



Why not use it?



Because algorithms like:

SHA-256

MD5

SHA-1



are designed to be fast.



Fast hashing is great for file integrity, but terrible for password storage.



For passwords we want:

Slow hashing ✅

Salting ✅

Adaptive work factor ✅



That's exactly what bcrypt provides.



##### **Install Passlib**

*pip install "passlib\[bcrypt]"*



**Why \[bcrypt]?**

passlib supports many hashing algorithms.

The \[bcrypt] extra **automatically installs** the bcrypt backend so passlib can use it.



**Why passlib\[bcrypt] instead of just bcrypt?**

We install passlib\[bcrypt] because Passlib provides a **secure** and **convenient password hashing interface**, while the \[bcrypt] extra **installs** the bcrypt backend that Passlib uses under the hood.



**bcrypt** is the **low-level** hashing library that implements the bcrypt algorithm.

**passlib** is a **higher-level** library that provides a clean, consistent API for password hashing and verification.



Interview Tip



One of my favorite interview questions is:



"If SHA-256 is cryptographically secure, why don't we use it for passwords?"



The ideal answer is:



Because SHA-256 is designed to be fast. Fast hashing makes brute-force attacks much more practical. Password hashing algorithms like bcrypt or Argon2 are intentionally slow and include salting and a configurable work factor, making password cracking significantly more expensive.



**Interview Tip**

One of my favorite interview questions is:

**"If SHA-256 is cryptographically secure, why don't we use it for passwords?"**



The ideal answer is:

Because SHA-256 is designed to be **fast**. Fast hashing makes **brute-force attacks** much more practical.

Password hashing algorithms like bcrypt or Argon2 are **intentionally slow** and include **salting** and a configurable work factor, making password cracking significantly more expensive.



#### **Let's write your first security utility**


This is a small file, but it's used by almost every authentication endpoint in the application.



##### **Step 1: Create utils/security.py**



First, create a new folder:

app/

│

├── utils/

│     └── security.py



Inside security.py, write:



*from passlib.context import CryptContext*



*pwd\_context = CryptContext(*

&#x20;   *schemes=\["bcrypt"],*

&#x20;   *deprecated="auto"*

*)*



*def hash\_password(password: str) -> str:*

&#x20;   *return pwd\_context.hash(password)*



*def verify\_password(plain\_password: str, hashed\_password: str) -> bool:*

&#x20;   *return pwd\_context.verify(plain\_password, hashed\_password)*



**Let's Understand Every Line**

**1. Import**

*from passlib.context import CryptContext*



CryptContext is like a **manager** for password hashing.

Instead of calling bcrypt directly, we ask the context to:



Hash passwords

Verify passwords

Manage hashing algorithms



This makes our code cleaner and easier to maintain.



**2. Create the Context**

*pwd\_context = CryptContext(*

&#x20;   *schemes=\["bcrypt"],*

&#x20;   *deprecated="auto"*

*)*



This tells Passlib:

"Use bcrypt for hashing passwords."



Later, if your company decides to migrate to Argon2, you only change this configuration instead of rewriting your entire authentication system.



**3. Hash Function**

*def hash\_password(password: str) -> str:*

&#x20;   *return pwd\_context.hash(password)*



Example:



Input:

Hello@123



Output:

$2b$12$H6Wn0v4XJm...



Notice something:

Every time you run:

*hash\_password("Hello@123")*



you'll get a different hash because bcrypt automatically generates a **new random salt** each time.



**4. Verify Function**

*def verify\_password(plain\_password: str, hashed\_password: str) -> bool:*

&#x20;   *return pwd\_context.verify(plain\_password, hashed\_password)*



Example:

*verify\_password(*

&#x20;   *"Hello@123",*

&#x20;   *"$2b$12$H6Wn0v4XJm..."*

*)*



Returns:

True



Wrong password:

*verify\_password(*

&#x20;   *"Hello@321",*

&#x20;   *"$2b$12$H6Wn0v4XJm..."*

*)*



Returns:

False



###### **Why Create Separate Functions?**



Instead of writing:

*pwd\_context.hash(password)*



everywhere in your code, we create:

*hash\_password(password)*



Benefits:

Cleaner code

Easier to test

Easier to change algorithms later

Follows the **Single Responsibility Principle (SRP)**



Let's see if you've fully connected the concepts.



Suppose the database stores:

$2b$12$AbCdEf123456789...



The user logs in with:

Hello@123



**Question:**

During login, does verify\_password():

A. Decrypt the stored hash back into Hello@123

B. Hash the entered password again (using the salt from the stored hash) and compare the results

**ANSWER: B**



**When the user logs in:**

User enters password

&#x20;       │

&#x20;       ▼

verify\_password()

&#x20;       │

&#x20;       ▼

Extract salt from stored hash

&#x20;       │

&#x20;       ▼

Hash entered password using that salt

&#x20;       │

&#x20;       ▼

Compare hashes

&#x20;       │

&#x20;  ┌────┴────┐

&#x20;  │         │

&#x20;Match    No Match

&#x20;  │         │

&#x20;True     False



Notice something very important:

❌ We never decrypt the stored hash.

❌ We never recover the original password.

We only **recompute** the hash using the **same salt** and compare the results.



#### **first production authentication API**



**Build the POST /auth/register Endpoint**

In the next lesson, we'll write our first production authentication API.



We'll implement this flow:



POST /auth/register

&#x20;       │

&#x20;       ▼

Receive UserCreate

&#x20;       │

&#x20;       ▼

Validate Request (Pydantic)

&#x20;       │

&#x20;       ▼

Check Username Exists

&#x20;       │

&#x20;       ▼

Check Email Exists

&#x20;       │

&#x20;       ▼

Hash Password

&#x20;       │

&#x20;       ▼

Create User Object

&#x20;       │

&#x20;       ▼

Save to Database

&#x20;       │

&#x20;       ▼

Return UserResponse



This is where all the concepts you've learned finally come together into a working endpoint.



##### **Step 1: Create routers/auth.py**



Start with these imports.



*from fastapi import APIRouter, Depends, HTTPException, status*

*from sqlalchemy.orm import Session*



*from app.database import get\_db*

*from app.models import User*

*from app.schemas.user import UserCreate, UserResponse*

*from app.utils.security import hash\_password*



*router = APIRouter(*

&#x20;   *prefix="/auth",*

&#x20;   *tags=\["Authentication"]*

*)*



**Let's Understand Every Import**



**1. status**

*from fastapi import status*



Instead of writing:

status\_code=201



we write:

*status\_code=status.HTTP\_201\_CREATED*

Why?

Because it's more readable.



Which is clearer?

201

or

HTTP\_201\_CREATED



Exactly.

Professional code almost always uses the status module.



**2. get\_db**

*db: Session = Depends(get\_db)*



Remember our discussion?

Every request gets its own database session.



FastAPI automatically:

Open Session

&#x20;     ↓

Run Endpoint

&#x20;     ↓

Close Session



No manual cleanup.



**3. hash\_password**



Instead of writing:

pwd\_context.hash(...)



everywhere,



we simply call:

*hash\_password(password)*



Cleaner and reusable.



Step 2: Create the Endpoint



Now add this skeleton.



*@router.post(*

&#x20;   *"/register",*

&#x20;   *response\_model=UserResponse,*

&#x20;   *status\_code=status.HTTP\_201\_CREATED*

*)*

*def register(*

&#x20;   *user: UserCreate,*

&#x20;   *db: Session = Depends(get\_db)*

*):*

&#x20;   *pass*



Notice that we haven't written any logic yet.



**Let's Understand This Before Writing Logic**



**Decorator**

*@router.post("/register")*



Creates:

POST /auth/register



because our router prefix is:

prefix="/auth"



**response\_model**

*response\_model=UserResponse*



This is extremely important.

Suppose we accidentally do:

return db\_user



db\_user contains:

id

username

email

hashed\_password

role

is\_active



Without response\_model, FastAPI would return everything.



With:

*response\_model=UserResponse*



FastAPI filters the response to only:

*{*

&#x20; *"id": 1,*

&#x20; *"username": "agney",*

&#x20; *"email": "agney@gmail.com"*

*}*



This is an extra layer of protection against accidentally exposing sensitive fields.



**Function Parameters**

*user: UserCreate*



FastAPI automatically:

Reads JSON

Validates it

Converts it into a UserCreate object



So instead of:

request\["username"]



you can simply write:

*user.username*



Much cleaner.





