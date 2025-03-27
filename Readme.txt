# FastAPI Blog API

This is a FastAPI-based project that provides a RESTful API for managing blogs and users. The project includes JWT-based authentication for secure access to protected endpoints.

## Features

- **Blog Management**:
  - Create, read, update, and delete blogs.
  - Associate blogs with users.

- **User Management**:
  - Create, read, update, and delete users.
  - Passwords are securely hashed using bcrypt.

- **JWT Authentication**:
  - Secure login and token-based authentication.
  - Access protected routes using JWT tokens.

- **Database**:
  - SQLite database for storing users and blogs.
  - SQLAlchemy ORM for database interactions.

## Endpoints

### Blog Endpoints
- `POST /blog`: Create a new blog (requires authentication).
- `GET /blog`: Retrieve a list of all blogs.
- `GET /blog/{id}`: Retrieve a specific blog by ID.
- `PUT /blog/{id}`: Update a blog by ID (requires authentication).
- `DELETE /blog/{id}`: Delete a blog by ID (requires authentication).

### User Endpoints
- `POST /user`: Create a new user.
- `GET /user`: Retrieve a list of all users.
- `GET /user/{id}`: Retrieve a specific user by ID.
- `PUT /user/{id}`: Update a user by ID (requires authentication).
- `DELETE /user/{id}`: Delete a user by ID (requires authentication).

### Authentication Endpoints
- `POST /login`: Authenticate a user and retrieve a JWT token.

## Installation

1. Clone the repository:
https://github.com/Nirav-Zignuts/FastAPI.git 

2. Create a virtual environment:
run below command in terminal
python -m venv fenv

3. Install dependencies:
run below command in terminal
pip install -r requirments.txt


4. Run the application:
run below command in terminal

 uvicorn main:app --reloadd


5. Access the API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc


# Authentication Workflow

1. **User Registration**:
   - Create a new user using the `POST /user` endpoint.

2. **Login**:
   - Authenticate the user using the `POST /login` endpoint.
   - Receive a JWT token upon successful login.

3. **Access Protected Routes**:
   - Include the JWT token in the `Authorization` header as a Bearer token to access protected routes.

## Example Usage
### Create a User
Request body :
{ "name": "John Doe", "email": "john.doe@example.com", "password": "securepassword" }

Response:
{ "access_token": "<JWT_TOKEN>", "token_type": "bearer" }

### Access Protected Route
include header :- Authorizatio : bearer <token>