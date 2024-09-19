# Flask Application

This is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a `User` resource using a RESTful API.

## Features

- **Create** a new user
- **Read** all users or a single user by ID
- **Update** a user by ID
- **Delete** a user by ID
- MongoDB integration with PyMongo
- Scalable and modular project structure
- RESTful API design

## Prerequisites

- Python 3.x
- MongoDB installed and running (locally or using a cloud provider like MongoDB Atlas)
- `pip` for package management
- Docker

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/scalable-flask-app.git
cd scalable-flask-app
```

### 2. Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the Dependencies

```
pip install -r requirements.txt
```

### 4. MongoDB Setup

Make sure MongoDB is running. You can either use a local MongoDB instance or a remote one (e.g., MongoDB Atlas).

For local MongoDB:
Ensure MongoDB is running on the default port 27017:

```
mongod --dbpath /path/to/your/db
```

### 6. Run the Application

```
python app.py
```
