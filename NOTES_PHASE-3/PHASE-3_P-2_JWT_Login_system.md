## PHASE-3 PART-2

# **JWT BASED LOGIN SYSTEM**



Welcome to the second half of authentication.



#### **Login Flow**



Unlike registration, we're not creating a user.



We're answering one question:

"Is this person really who they claim to be?"



The complete login flow is:

Client

&#x20;  │

&#x20;  ▼

POST /auth/login

&#x20;  │

&#x20;  ▼

Find User

&#x20;  │

&#x20;  ▼

User Exists?

&#x20;  │

&#x20;┌─┴─────────┐

&#x20;│           │

No          Yes

&#x20;│           │

&#x20;▼           ▼

401      Verify Password

&#x20;            │

&#x20;      ┌─────┴─────┐

&#x20;      │           │

&#x20;   Wrong       Correct

&#x20;      │           │

&#x20;      ▼           ▼

&#x20;    401      Generate JWT

&#x20;                   │

&#x20;                   ▼

&#x20;         Return Access Token



Notice something...



Registration asked:

"Can I **create** this user?"



Login asks:

"Can I **trust** this user?"



Completely different purpose.



##### **Step 1 — What data should Login receive?**



When you log into:

Gmail

LinkedIn

GitHub



What do you type?



Usually:

username/email

password



That's exactly what our API should accept.



We already created:

*class UserLogin(BaseModel):*

&#x20;   *username: str*

&#x20;   *password: str*



This schema represents the login request.



**Why don't we ask for email too?**



Suppose we asked for:

*{*

&#x20;   *"username":"agney",*

&#x20;   *"email":"agney@gmail.com",*

&#x20;   *"password":"Hello@123"*

*}*



Imagine someone enters:

*username = agney*

*email = someone@gmail.com*

*password = Hello@123*



Which one should the server trust?

The username?

The email?



They **contradict each other.**



That's why most APIs choose one **unique identifier:**

username or

email



**Not both.**



**Why not hash the password first?**



You might think:

"Can't we hash the entered password immediately?"

No.



Remember what we learned about bcrypt?



Every call to:

*hash\_password("Hello@123")*



creates a different hash because of a new random salt.



Example:

Hello@123

↓

$2b$12$ABC...



Run it again:

Hello@123

↓

$2b$12$XYZ...



Different hash!



That's why we don't use:

*hash\_password()*



during login.



Instead we use:

***verify\_password(***

&#x20;   ***plain\_password,***

&#x20;   ***stored\_hash***

***)***



because it extracts the salt from the **stored hash** and performs the **correct comparison**.



Suppose the user does not exist in the database.



Should your API return:



"Username does not exist"

or

"Invalid username or password"



**ANSWER:** "Invalid username or password"



Imagine you're an attacker...



Suppose I write a script that tries thousands of usernames:

agney

john

alice

admin

root

test



If your API responds with:

Username does not exist

or

Password is incorrect



I can learn which usernames are valid.



Example:

agney   → Password incorrect ✅

john    → Username does not exist ❌

alice   → Password incorrect ✅



Now I know that agney and alice are real users.

I've just collected valid accounts to attack.



This is called **username enumeration.**



Secure APIs do this instead



Whether:

the username doesn't exist OR

the password is wrong



they always return:

**Invalid username or password**



Now the attacker sees:

agney   → Invalid username or password

john    → Invalid username or password

alice   → Invalid username or password



They learn nothing.



**But what about real users?**

You asked a good question indirectly:

"How will users know to register?"



That's handled by the **frontend,** not the login API.



A login page usually has:

Username: \_\_\_\_\_\_\_\_\_\_



Password: \_\_\_\_\_\_\_\_\_\_



\[ Login ]



Don't have an account?

\[ Register ]



The API stays secure by returning the same message for all failed login attempts.



If asked:

Why do login APIs usually return "Invalid username or password" instead of "Username not found"?



A strong answer is:

"Returning different error messages allows attackers to discover which usernames exist in the system. To prevent username enumeration attacks, authentication APIs return the same generic error message for both an incorrect username and an incorrect password."





**Imagine This Scenario**



You log into a website.

Username: agney

Password: Hello@123



The server verifies your credentials.



Now ask yourself:

How does the server remember you're logged in for the next request?



If you visit:

GET /profile



How does the server know it's still you?

The answer is **JWT.**



**Without JWT**



Every request would have to include your username and password.



Request 1

Username

Password

&#x20;     ↓

Server verifies



Request 2

Username

Password

&#x20;     ↓

Server verifies again



Request 3

Username

Password

&#x20;     ↓

Server verifies again



This is:

Slow

Insecure

Bad practice



###### **With JWT**



After login, the server creates a token.



Username + Secret Key

&#x20;         │

&#x20;         ▼

&#x20;     Create JWT

&#x20;         │

&#x20;         ▼

eyJhbGciOiJIUzI1NiIsInR...



The server sends it back:

*{*

&#x20;   *"access\_token": "eyJhbGc...",*

&#x20;   *"token\_type": "bearer"*

*}*



Now the client stores this token.



For every future request:

GET /profile

Authorization: Bearer eyJhbGc...



The server **verifies the token** instead of asking for the password again.



##### **What's Inside a JWT?**



A JWT has three parts:

**Header.Payload.Signature**



Example:

xxxxx.yyyyy.zzzzz



Each section has a different purpose.



###### **1. Header**



Contains information such as:

*{*

&#x20; *"alg": "HS256",*

&#x20; *"typ": "JWT"*

*}*



This tells the server:

the algorithm used (HS256)

that this is a JWT



###### **2. Payload**



This is the useful information.



For our project, it might look like:

*{*

&#x20;   *"sub": "agney",*

&#x20;   *"exp": 1785550000*

*}*

sub (subject) → the username or user ID

exp → when the token expires



Important: The payload is **encoded**, not encrypted. Anyone with the token can decode the payload, so never put passwords or sensitive information in a JWT.



###### **3. Signature**



This is what prevents **tampering**.



The server signs the header and payload using a secret key that only the server knows.



If someone changes:

*{*

&#x20;   *"sub": "agney"*

*}*



to



*{*

&#x20;   *"sub": "admin"*

*}*



the signature no longer matches, and the server rejects the token.



That's why attackers can't simply edit a JWT to become another user.



###### **Why Don't We Store JWTs in the Database?**



Because the token already contains the information the server needs, and the signature proves it hasn't been altered.



Instead of checking a database table of sessions, the server:\\

* Receives the token.
* Verifies its signature using the secret key.
* Checks whether it has expired.
* Reads the user information from the payload.



This makes JWT authentication stateless, which is one reason it's popular for REST APIs.



###### **The Secret Key**



The secret key is known only by your **server.**



For example:

SECRET\_KEY = "my\_super\_secret\_key"



When you later write:

*jwt.encode(payload, SECRET\_KEY, algorithm="HS256")*



the library uses that **secret key** to create the **signature.**

When someone sends the token back, the server again uses the **same secret key** to verify it.

If the keys don't match, or if the payload has changed, verification fails.



#### **Let's Start Coding JWT**



##### **Step 1: Install the JWT Library**

Run:

*pip install python-jose\[cryptography]*



We'll use python-jose because it's the standard JWT library for FastAPI.



##### **Step 2: Create a JWT Utility**



Create a new file:

app/

└── utils/

&#x20;   ├── security.py

&#x20;   └── jwt.py   👈 New file



We'll build this file one piece at a time.



##### **Step 3: Imports**

*from datetime import datetime, timedelta, timezone*

*from jose import jwt*



Let's understand these imports.



**datetime**

Used to get the current time.



Example:

*datetime.now(timezone.utc)*



might return:

2026-07-29 09:15:00 UTC



**timedelta**

Represents a duration of time.



Example:

timedelta(minutes=30)



means:

30 minutes



So:

*expire = datetime.now(timezone.utc) + timedelta(minutes=30)*



becomes:

Current Time:

09:15

\+

30 minutes

↓

09:45



That will become the exp claim in our JWT.



**jwt**



This comes from python-jose.



It provides two important functions:

jwt.encode(...)



Creates a JWT.



Later we'll also use:

jwt.decode(...)



to verify incoming tokens.



##### **Step 4: Secret Key**



Add these constants:

*SECRET\_KEY = "your-super-secret-key"*

*ALGORITHM = "HS256"*

*ACCESS\_TOKEN\_EXPIRE\_MINUTES = 30*



Let's understand each one.



**SECRET\_KEY**

This is the most important part.

Think of it as your server's private signature.



Server

&#x20; │

&#x20; ├── Payload

&#x20; │

&#x20; ├── Secret Key

&#x20; │

&#x20; ▼

Generate Signature



Only your server knows this key.

⚠️ Never upload a real SECRET\_KEY to GitHub. Later, we'll move it into your .env file.



*ALGORITHM*

HS256



This tells python-jose which signing algorithm to use.



We'll use the standard algorithm:

HS256



*ACCESS\_TOKEN\_EXPIRE\_MINUTES=30*

Meaning:

Login

&#x20;  │

&#x20;  ▼

Token created



30 minutes later

↓

Token expires



##### **QUESTION**

Why do we keep:

*ACCESS\_TOKEN\_EXPIRE\_MINUTES = 30*



instead of writing:

*timedelta(minutes=30)*



**Imagine this**

Today your code has:

*timedelta(minutes=30)*



in 6 different places.



One day your manager says:

"Security policy changed. Tokens should expire in 15 minutes instead of 30."



Now you have to search your entire project:

30

30

30

30

30

30



Miss one location, and you introduce inconsistent behaviour.



**Using a Constant**



Instead, define it once:

*ACCESS\_TOKEN\_EXPIRE\_MINUTES = 30*



Then use it everywhere:

*expire = datetime.now(timezone.utc) + timedelta(*

&#x20;   *minutes=ACCESS\_TOKEN\_EXPIRE\_MINUTES*

*)*



Now if the policy changes:

*ACCESS\_TOKEN\_EXPIRE\_MINUTES = 15*



The whole application updates automatically.



##### **Step-5: Let's Write Our First JWT Function**



We'll build it one step at a time.



Start by adding this to app/utils/jwt.py:

*from datetime import datetime, timedelta, timezone*

*from jose import jwt*



SECRET\_KEY = "your-super-secret-key"

ALGORITHM = "HS256"

ACCESS\_TOKEN\_EXPIRE\_MINUTES = 30





*def create\_access\_token(data: dict):*

&#x20;   *to\_encode = data.copy()*



**Why data.copy()?**



Suppose we call:

*create\_access\_token(*

&#x20;   *{"sub": "agney"}*

*)*



Inside the function, data is:

*{*

&#x20;   *"sub": "agney"*

*}*



We need to add the expiration claim:

*{*

&#x20;   *"sub": "agney",*

&#x20;   *"exp": ...*

*}*



Instead of modifying the original dictionary, we create a copy:

*to\_encode = data.copy()*



Now:

Original Data        Copied Data

\---------------      --------------------

{"sub":"agney"}  →   {"sub":"agney"}



We can safely **modify** to\_encode without changing the **original dictionary** that was passed to the function.



##### **Step-6: Add the Expiration**



Now extend the function:

*def create\_access\_token(data: dict):*

&#x20;   *to\_encode = data.copy()*



&#x20;   *expire = datetime.now(timezone.utc) + timedelta(*

&#x20;       *minutes=ACCESS\_TOKEN\_EXPIRE\_MINUTES*

&#x20;   *)*



&#x20;   *to\_encode.update({"exp": expire})*



Let's understand the new line:

*to\_encode.update({"exp": expire})*



If:

data = {

&#x20;   "sub": "agney"

}



then after:

*to\_encode.update({"exp": expire})*



the payload becomes:

{

&#x20;   "sub": "agney",

&#x20;   "exp": datetime(...)

}



Notice we didn't overwrite "sub"—we simply **added another claim.**



##### **Final Step: Generate the JWT**



Now complete your function:

*from datetime import datetime, timedelta, timezone*

*from jose import jwt*



*SECRET\_KEY = "your-super-secret-key"*

*ALGORITHM = "HS256"*

*ACCESS\_TOKEN\_EXPIRE\_MINUTES = 30*





*def create\_access\_token(data: dict):*

&#x20;   *to\_encode = data.copy()*



&#x20;   *expire = datetime.now(timezone.utc) + timedelta(*

&#x20;       *minutes=ACCESS\_TOKEN\_EXPIRE\_MINUTES*

&#x20;   *)*



&#x20;   *to\_encode.update({"exp": expire})*



&#x20;   *encoded\_jwt = jwt.encode(*

&#x20;       *to\_encode,*

&#x20;       *SECRET\_KEY,*

&#x20;       *algorithm=ALGORITHM*

&#x20;   *)*



&#x20;   *return encoded\_jwt*



##### **Question**



Will both users receive the same JWT, or different JWTs?

And why?



Although both use:

✅ the same SECRET\_KEY

✅ the same HS256 algorithm



the payload is different (sub is different), so the encoded token and its signature are also different.

In fact, even if the same user logs in twice, the tokens are usually different because the exp value (and often an iat—issued at—timestamp in many applications) changes.



#### **Next: Build the /auth/login Endpoint**



Inside it, we'll implement this flow:

Receive Login Request

&#x20;       │

&#x20;       ▼

Find User by Username

&#x20;       │

&#x20;       ▼

User Exists?

&#x20;       │

&#x20;       ├── No → 401 Invalid username or password

&#x20;       │

&#x20;       ▼

Verify Password

&#x20;       │

&#x20;       ├── Wrong → 401 Invalid username or password

&#x20;       │

&#x20;       ▼

Create JWT

&#x20;       │

&#x20;       ▼

Return Access Token





##### **Step 1: Imports**

In your routers/auth.py, add:



*from app.schemas.user import UserLogin*

*from app.utils.jwt import create\_access\_token*

*from app.utils.security import verify\_password*



You should already have hash\_password imported from the registration endpoint.



##### **Step 2: Create the Endpoint Skeleton**

*@router.post("/login")*

*def login(*

&#x20;   *user: UserLogin,*

&#x20;   *db: Session = Depends(get\_db)*

*):*

&#x20;   *pass*



Let's understand every part.



**@router.post("/login")**



This creates:

POST /auth/login



because your router already has:

*prefix="/auth"*

*user: UserLogin*



When the client sends:

*{*

&#x20;   *"username": "agney",*

&#x20;   *"password": "Hello@123"*

*}*



FastAPI automatically creates:

*user.username*

*user.password*



Exactly like it did during registration.



**db: Session = Depends(get\_db)**

Same concept as before.

FastAPI gives us a **fresh SQLAlchemy session.**





##### **Step 3: Find the User**

Now let's write the first real logic inside the login endpoint.



*db\_user = db.query(User).filter(*

&#x20;   *User.username == user.username*

*).first()*



Does this look familiar?

It should.



It's almost identical to what you wrote during registration:

*existing\_user = db.query(User).filter(*

&#x20;   *User.username == user.username*

*).first()*



The difference is the purpose.



**Registration**

Find user

&#x20;    │

&#x20;    ▼

Exists?

&#x20;    │

Yes ─────► Reject (duplicate username)

No  ─────► Create new user



**Login**

Find user

&#x20;    │

&#x20;    ▼

Exists?

&#x20;    │

No  ─────► Reject (invalid credentials)

Yes ─────► Verify password



Same SQL query.

Different business logic.



##### **Step 4: Implement It**



Now write this in your login() function:

*db\_user = db.query(User).filter(*

&#x20;   *User.username == user.username*

*).first()*



*if not db\_user:*

&#x20;   *raise HTTPException(*

&#x20;       *status\_code=status.HTTP\_401\_UNAUTHORIZED,*

&#x20;       *detail="Invalid username or password"*

&#x20;   *)*



**Why if not db\_user?**



Because:

.first()



returns:

a User object if found

None if not found



And in Python:

if not None:



evaluates to:

True



so the exception is raised.



###### **Add this immediately after checking that the user exists:**



*if not verify\_password(*

&#x20;   *user.password,*

&#x20;   *db\_user.hashed\_password*

*):*

&#x20;   *raise HTTPException(*

&#x20;       *status\_code=status.HTTP\_401\_UNAUTHORIZED,*

&#x20;       *detail="Invalid username or password"*

&#x20;   *)*



Notice something important:

if not verify\_password(...)



means:

verify\_password() returns True → password is correct → continue.

verify\_password() returns False → password is wrong → return 401.



##### **Step 5: Create the JWT**



Add this after the password verification:

*access\_token = create\_access\_token(*

&#x20;   *data={"sub": db\_user.username}*

*)*



**Why "sub"?**

Remember our JWT theory.

{

&#x20;   "sub": "agney"

}



sub stands for **Subject.**

It identifies who this token belongs to.



When the user later sends this token:

*Authorization: Bearer eyJhbGc...*



the server will decode it and read:

{

&#x20;   "sub": "agney"

}



Now it knows which user is making the request.



##### **Step 6: Return the Token**



Finally:

*return {*

&#x20;   *"access\_token": access\_token,*

&#x20;   *"token\_type": "bearer"*

*}*



The response becomes:

{

&#x20;   "access\_token": "eyJhbGciOiJIUzI1NiIs...",

&#x20;   "token\_type": "bearer"

}



Notice something interesting:

We don't return the user object.



#### **Congratulations!**

You've just built a real JWT authentication system.





#### **OAuth2PasswordBearer**



FastAPI provides a helper that **automatically extracts** the token from the Authorization header.



Create a new file:

app/dependencies/auth.py



Then add:

*from fastapi.security import OAuth2PasswordBearer*



*oauth2\_scheme = OAuth2PasswordBearer(*

&#x20;   *tokenUrl="auth/login"*

*)*



OAuth2PasswordBearer does not:

❌ Generate JWTs

❌ Verify JWTs

❌ Decode JWTs

❌ Log users in



Its only job is to **extract the Bearer token** from the incoming request.



**tokenurl**

Many beginners think:

"FastAPI will automatically call /auth/login."



❌ It doesn't.



It simply tells Swagger/OpenAPI:

"If someone wants a token, this is the endpoint they should use."



Get JWT

&#x20;   │

&#x20;   ▼

POST /auth/login

&#x20;   │

&#x20;   ▼

Receive Access Token

&#x20;   │

&#x20;   ▼

Send it as:

Authorization: Bearer <token>



So tokenUrl is **documentation** and **OpenAPI metadata**, not authentication logic.



##### **Now let's build get\_current\_user()**



**Add these imports:**

*from fastapi import Depends, HTTPException, status*

*from fastapi.security import OAuth2PasswordBearer*

*from jose import JWTError, jwt*



*from sqlalchemy.orm import Session*



*from app.database import get\_db*

*from app.config import SECRET\_KEY*

*from app.models.user import Users*



**Then add:**

*oauth2\_scheme = OAuth2PasswordBearer(*

&#x20;   *tokenUrl="auth/login"*

*)*



**Suppose someone sends this token:**

eyJhbGc...



What should get\_current\_user() do first after receiving the token?

**Decode and verify the JWT**-This is one of the most important security principles in JWT authentication.



**The Authentication Pipeline**

Client Request

&#x20;      │

&#x20;      ▼

Extract JWT

&#x20;      │

&#x20;      ▼

Decode JWT

&#x20;      │

&#x20;      ├── Invalid Signature

&#x20;      │

&#x20;      ├── Expired

&#x20;      │

&#x20;      ├── Missing "sub"

&#x20;      │

&#x20;      ▼

Extract Username

&#x20;      │

&#x20;      ▼

Query Database

&#x20;      │

&#x20;      ▼

Return Current User



Only after the JWT is **successfully verified** do we touch the database.



##### **Step 1 inside get\_current\_user()**



We'll start with a try block because jwt.decode() can raise exceptions.



*try:*

&#x20;   *payload = jwt.decode(*

&#x20;       *token,*

&#x20;       *SECRET\_KEY,*

&#x20;       *algorithms=\[ALGORITHM]*

&#x20;   *)*



What each parameter means



**token**

The JWT extracted by OAuth2PasswordBearer.



**SECRET\_KEY**

The same secret that was used when creating the token.



**algorithms=\[ALGORITHM]**

Tells python-jose which signing algorithm is expected (e.g. "HS256"). This prevents accepting tokens signed with unexpected algorithms.



Many people think jwt.decode() simply converts a JWT into a dictionary. In reality, it does much more.



python-jose performs several checks before returning the payload:

✅ Verifies the **JWT signature** using the SECRET\_KEY.

✅ Checks whether the **token has expired** (exp claim), if it's present.

✅ Validates the **token structure** (header, payload, signature).

✅ Ensures the token was **signed** using one of the allowed algorithms.



If any of these checks fail, it raises a JWTError (or a related exception), which is why we wrap it in a try...except.



##### **Step 2: Extract the username**

Once jwt.decode() succeeds

**we can retrieve the username:**

*username = payload.get("sub")*



Remember why?



During login, we created the token like this:

*create\_access\_token(*

&#x20;   *data={"sub": db\_user.username}*

*)*



So after decoding:

payload



contains something like:

*{*

&#x20;   *"sub": "agney",*

&#x20;   *"exp": 1785312345*

*}*



Therefore:

*username = payload.get("sub")*



returns:

agney



##### **Step 3: Validate the sub**

We'll add:

*username = payload.get("sub")*



*if username is None:*

&#x20;   *raise HTTPException(*

&#x20;       *status\_code=status.HTTP\_401\_UNAUTHORIZED,*

&#x20;       *detail="Could not validate credentials"*

&#x20;   *)*



Notice we're using:

*payload.get("sub")*



instead of:

payload\["sub"]

Why?



Because:

*payload\["sub"]*



would raise a **KeyError** if "sub" doesn't exist.



Whereas:

payload.get("sub")



returns:

**None**



which lets us **handle the error** cleanly.



##### **Step 4: Handle Invalid Tokens**

Since jwt.decode() can fail, complete the try...except:



*try:*

&#x20;   *payload = jwt.decode(*

&#x20;       *token,*

&#x20;       *SECRET\_KEY,*

&#x20;       *algorithms=\[ALGORITHM]*

&#x20;   *)*



&#x20;   *username = payload.get("sub")*



&#x20;   *if username is None:*

&#x20;       *raise HTTPException(*

&#x20;           *status\_code=status.HTTP\_401\_UNAUTHORIZED,*

&#x20;           *detail="Could not validate credentials"*

&#x20;       *)*



*except JWTError:*

&#x20;   *raise HTTPException(*

&#x20;       *status\_code=status.HTTP\_401\_UNAUTHORIZED,*

&#x20;       *detail="Could not validate credentials"*

&#x20;   *)*



Now we've handled:



✅ Invalid signature

✅ Expired token

✅ Corrupted token

✅ Missing sub



**Why do we catch:**

*except JWTError:*



**Why?**

When someone sends:

an expired token,

a modified token,

or a completely fake token,



that's **not a bug** in your application. It's an **authentication failure.**



If you don't catch JWTError, FastAPI will return a 500 Internal Server Error, which is misleading because the server isn't broken.



Instead, we catch it and return:

**401 Unauthorized**



This tells the client:

"Your credentials are invalid. Please **authenticate again**."



##### **Step 5: Query the Database**



**Add:**

*db\_user = db.query(Users).filter(*

&#x20;   *Users.username == username*

*).first()*



*if db\_user is None:*

&#x20;   *raise HTTPException(*

&#x20;       *status\_code=status.HTTP\_401\_UNAUTHORIZED,*

&#x20;       *detail="Could not validate credentials"*

&#x20;   *)*



*return db\_user*



###### **Let's trace an actual request:**



GET /me

Authorization: Bearer eyJhbGc...

↓

OAuth2PasswordBearer

↓

Extracts:

*eyJhbGc...*

↓

*jwt.decode()*

↓

*{*

&#x20;   *"sub": "agney",*

&#x20;   *"exp": 1785312345*

*}*

↓

*username = "agney"*

↓

*db.query(Users)*

↓

Returns:

*Users(*

&#x20;   *id=1,*

&#x20;   *username="agney",*

&#x20;   *email="agney@gmail.com"*

*)*

↓

Returned by:

get\_current\_user()





