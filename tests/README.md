# Python Fullstack API
Learning how the system works, to build something cool using these learnings.
A simple FastAPI project with student-related endpoints.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints

- GET /
- GET /users
- GET /about
- GET /students
- POST /students
- GET /students/{id}
- PUT /students/{id}
- PATCH /students/{id}
- DELETE /students/{id}
