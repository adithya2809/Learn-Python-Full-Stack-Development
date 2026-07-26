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

