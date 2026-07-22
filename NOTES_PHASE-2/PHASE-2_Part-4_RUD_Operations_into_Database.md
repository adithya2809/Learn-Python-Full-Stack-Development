#### **READ Operations**



Now we're going to retrieve data from PostgreSQL.



##### **First endpoint: Get all students**



Suppose your table contains:

id	name	age	course

1	Agney	21	AI \& ML

2	Rahul	20	CSE

3	Priya	22	ECE



When someone visits:

*GET /students*



they should receive:

*\[*

&#x20; *{*

&#x20;   *"id":1,*

&#x20;   *"name":"Agney",*

&#x20;   *"age":21,*

&#x20;   *"course":"AI \& ML"*

&#x20; *},*

&#x20; *{*

&#x20;   *"id":2,*

&#x20;   *"name":"Rahul",*

&#x20;   *"age":20,*

&#x20;   *"course":"CSE"*

&#x20; *}*

*]*

**The SQL Version**

If we wrote pure SQL:

*SELECT \* FROM students;*



**SQLAlchemy Version**

The ORM equivalent is:

*students = db.query(Student).all()*



Let's break it down.

##### **Step 1**

*db.query(Student)*



Think of it as saying:

"I want to query the students table."



Nothing has been executed yet.



##### **Step 2**

*.all()*



Now SQLAlchemy executes:

*SELECT \* FROM students;*



and returns every row as a list of Student objects.



##### **Your New Endpoint**



Replace your current GET endpoint (the one using students\_db) with:



*@router.get(*

&#x20;   *"/students",*

&#x20;   *response\_model=list\[StudentResponse]*

*)*

*def get\_students(*

&#x20;   *db: Session = Depends(get\_db)*

*):*

&#x20;   *students = db.query(Student).all()*

&#x20;   *return students*



Notice the response model:

*response\_model=list\[StudentResponse]*



because we're returning multiple students.



Get Student by ID



The complete flow

*student = (*

&#x20;   *db.query(Student)*

&#x20;     *.filter(Student.id == id)*

&#x20;     *.first()*

*)*

↓

If:

*student is None*

↓

*raise HTTPException(...)*

Else:

*return student*



**Visualize the query**

*db.query(Student)*

↓

*SELECT \* FROM students*

↓

*.filter(Student.id == id)*

↓

*WHERE id = 5*

↓

*.first()*

↓

*LIMIT 1*

↓

Return:

*Student(...)*

or

*None*





#### **Now let's build the PUT endpoint**



##### **Step 1: Find the student**

The first thing we need is the existing student:

*student = db.query(Student).filter(Student.id == id).first()*



**Why do we fetch the object before updating it?**

We first query the object to **verify that it exists**. If it doesn't, we return a **404 Not Found**. If it does exist, **SQLAlchemy begins tracking the object**, allowing **us to modify its attributes** and persist the **changes with commit().**



##### **Step 2: Updating the Object**



Assume we've already written:



*student = db.query(Student).filter(Student.id == id).first()*

*if student is None:*

&#x20;   *raise HTTPException(*

&#x20;       *status\_code=404,*

&#x20;       *detail="Student not found"*

&#x20;   *)*



Now suppose the request body is:

*{*

&#x20;   *"name": "Agney",*

&#x20;   *"age": 22,*

&#x20;   *"course": "CSE"*

*}*



**Question**

How do you think we update the SQLAlchemy object?



**A.**

*student = Student(*

&#x20;   *name=student\_update.name,*

&#x20;   *age=student\_update.age,*

&#x20;   *course=student\_update.course*

*)*



or



**B.**

*student.name = student\_update.name*

*student.age = student\_update.age*

*student.course = student\_update.course*



**ANSWER: B**

**Why not Option A?**

What have you actually done?

You've created a brand new Student object.

It has no relationship with the row you fetched earlier.



If you later do:



db.add(student)

db.commit()



SQLAlchemy will most likely execute:



INSERT INTO students (...)

VALUES (...);



instead of:



UPDATE students

SET ...

WHERE id = 1;



because this is a new object, not the existing tracked one.



**Why Option B Works**



Suppose we queried:

*student = db.query(Student).filter(Student.id == id).first()*



The Session is already tracking this object.



Initially:

Student

*id = 1*

*name = Adhi*

*age = 21*

*course = AI \& ML*



Now you do:

*student.name = student\_update.name*

*student.age = student\_update.age*

*student.course = student\_update.course*



The Session notices:



**Old**

\-----------------

Adhi

21

AI \& ML

↓

**New**

\-----------------

Agney

22

CSE



Then:

*db.commit()*



SQLAlchemy generates something like:

*UPDATE students*

*SET*

&#x20;   *name='Agney',*

&#x20;   *age=22,*

&#x20;   *course='CSE'*

*WHERE id=1;*



No SQL written by you.



##### **The Complete PUT Endpoint**



Now you have all the pieces. A typical implementation looks like this:



*@router.put(*

&#x20;   *"/students/{id}",*

&#x20;   *response\_model=StudentResponse*

*)*

*def update\_student(*

&#x20;   *id: int,*

&#x20;   *student\_update: StudentUpdate,*

&#x20;   *db: Session = Depends(get\_db)*

*):*

&#x20;   *student = db.query(Student).filter(Student.id == id).first()*



&#x20;   *if student is None:*

&#x20;       *raise HTTPException(*

&#x20;           *status\_code=404,*

&#x20;           *detail="Student not found"*

&#x20;       *)*



&#x20;   *student.name = student\_update.name*

&#x20;   *student.age = student\_update.age*

&#x20;   *student.course = student\_update.course*



&#x20;   *db.commit()*

&#x20;   *db.refresh(student)*



&#x20;   return student



**Why db.refresh(student) again?**



Notice we used *refresh()* after the update too.



Strictly speaking, if you only changed name, age, and course, the Python object already has those updated values.



However, refresh() is still a good practice because it **reloads the object from the database**. This is especially useful if:

the database has triggers,

default values,

computed columns,

or timestamps like updated\_at that PostgreSQL updates automatically.



It guarantees that the **object you return reflects exactly what's stored in the database.**



#### **THE PATCH ENDPOINT**

**How do you think we can update only the fields that the client actually sent, while leaving the others unchanged?**

Pydantic has a **method specifically designed for this use case.**

##### **The method is:**

***model\_dump(exclude\_unset=True)***



Since you're using Pydantic v2, this is the correct method.

(In Pydantic v1 it was .dict(exclude\_unset=True).)



**Let's understand what it does**



Suppose your PATCH schema is:

*class StudentPatch(BaseModel):*

&#x20;   *name: str | None = None*

&#x20;   *age: int | None = None*

&#x20;   *course: str | None = None*



The client sends:

*{*

&#x20;   *"age": 22*

*}*



Internally, the object becomes:



*student\_patch = StudentPatch(*

&#x20;   *name=None,*

&#x20;   *age=22,*

&#x20;   *course=None*

*)*



Now imagine we do:

*student\_patch.model\_dump()*



We get:



*{*

&#x20;   *"name": None,*

&#x20;   *"age": 22,*

&#x20;   *"course": None*

*}*



If we updated using this dictionary, we'd accidentally erase the name and course.



Now use exclude\_unset=True

*student\_patch.model\_dump(exclude\_unset=True)*



Result:

*{*

&#x20;   *"age": 22*

*}*



Notice the difference.

Only the fields that the client actually sent are included.



**Then updating becomes easy**



Suppose we write:

*update\_data = student\_patch.model\_dump(exclude\_unset=True)*



Now:

*update\_data*



contains:

*{*

&#x20;   *"age": 22*

*}*



We can loop through it:

*for key, value in update\_data.items():*

&#x20;   *setattr(student, key, value)*



**What is setattr()?**



This is another useful Python function.



Instead of writing:



*student.age = 22*

or

*student.name = "Agney"*



we can do it dynamically:

*setattr(student, "age", 22)*



Python interprets that as:

*student.age = 22*



Likewise:

*setattr(student, "course", "CSE")*



becomes:

*student.course = "CSE"*

This is perfect for PATCH because we don't know in advance which fields the client will send.



##### **THE COMPLETE PATCH ENDPOINT**



*@router.patch("/students/{id}",response\_model=StudentResponse)*

*def patch\_student\_update(id:int,patch\_student:StudentPatch,db: Session=Depends(get\_db)):*

&#x20;   *student=db.query(Student).filter(Student.id==id).first()*

&#x20;   *if student is None:*

&#x20;       *raise HTTPException(*

&#x20;       *status\_code=status.HTTP\_404\_NOT\_FOUND,*

&#x20;       *datail="Student Not Found"*

&#x20;   *)*  

&#x20;   *update\_data=patch\_student.model\_dump(exclude\_unset=True)*

&#x20;   *for key,pair in update\_data.items():*

&#x20;       *setattr(student,key,pair)*



&#x20;   *db.commit()*

&#x20;   *db.refresh(student)*

&#x20;   *return student*





#### **THE DELETE ENDPOINT**



###### **Step 1: Fetch the Student**

Just like PUT and PATCH, the first step is:

*student = db.query(Student).filter(Student.id == id).first()*



###### **Step 2: Delete the Object**



Once we have the student:

*student = db.query(Student).filter(Student.id == id).first()*



SQLAlchemy provides a method:

*db.delete(student)*



Notice something interesting.

We're not deleting by ID.

We're deleting the ORM object.

That's because the Session is tracking that object.



###### **Step 3: Commit**



**After:**

*db.delete(student)*



Is the row already removed from PostgreSQL?



Or do we still need:

db.commit()



Just like:

db.add()



doesn't immediately insert,



db.delete()



doesn't immediately delete.



The transaction is finalized only after:



db.commit()



##### **THE COMPLETE ENDPOINT**

*@router.delete("/students/{id}",status\_code=status.HTTP\_204\_NO\_CONTENT)*

*def delete\_student(id:int,db:Session=Depends(get\_db)):*

&#x20;   *student=db.query(Student).filter(Student.id==id).first()*

&#x20;   *if student is None:*    

&#x20;       *raise HTTPException(*

&#x20;           *status\_code=status.HTTP\_404\_NOT\_FOUND,*

&#x20;           *detail="Student Not Found"*

&#x20;       *)*

&#x20;   *db.delete(student)*

&#x20;   *db.commit()*

&#x20;   

&#x20;   *return{*

&#x20;               *"message":"student deleted successfully"*

&#x20;           *}*

