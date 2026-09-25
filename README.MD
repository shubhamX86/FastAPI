# FastAPI 🚀

A beginner-friendly **FastAPI** project for learning and building REST APIs with Python.

This repository contains practical examples and implementations covering **FastAPI fundamentals, Pydantic data validation, request handling, and API development**.

---

## 📌 About

This project is created to understand how **FastAPI** works and how Python can be used to build modern REST APIs.

FastAPI is a modern Python web framework designed for building APIs using Python type hints. It provides automatic API documentation through OpenAPI/Swagger and uses Pydantic for data validation.

---

## 🛠️ Tech Stack

* 🐍 **Python**
* ⚡ **FastAPI**
* 📦 **Pydantic**
* 🚀 **Uvicorn**
* 📄 **REST API**
* 📚 **Swagger / OpenAPI**

FastAPI itself is designed around Python type hints and provides automatic interactive API documentation.

---

## 📂 Project Structure

```text
FastAPI/
│
├── Note/
│   └── ...
│
├── Pydantic/
│   └── ...
│
├── main.py
│
└── README.md
```

### `main.py`

The main entry point of the FastAPI application.

It contains the FastAPI application and API routes/endpoints.

### `Pydantic/`

Contains examples related to **Pydantic**, which is used for data validation and defining structured request/response data.

### `Note/`

Contains notes/examples related to the FastAPI learning process.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shubhamX86/FastAPI.git
```

### 2. Move into the project directory

```bash
cd FastAPI
```

### 3. Create a virtual environment

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

If the project later includes a `requirements.txt`, dependencies can be installed using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI development server using:

```bash
uvicorn main:app --reload
```

After starting the server, open:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

These interfaces allow you to explore and test the available API endpoints directly from your browser.

---

## 🧠 Concepts Covered

This repository is intended for learning concepts such as:

* FastAPI application setup
* API routes
* HTTP methods
* Path parameters
* Query parameters
* Request handling
* Pydantic models
* Data validation
* JSON request/response
* Automatic API documentation
* Swagger UI
* ReDoc
* Uvicorn server

---

## 🔄 Basic FastAPI Flow

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI Application
  │
  ├── Route
  │
  ├── Request Validation
  │
  └── Business Logic
  │
  ▼
Pydantic Response
  │
  │ JSON Response
  ▼
Client
```

---

## 💡 Example

A basic FastAPI application looks like this:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

Run it with:

```bash
uvicorn main:app --reload
```

Then visit:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Testing the API

You can test the API using:

* Swagger UI
* ReDoc
* Postman
* cURL
* Browser for simple `GET` requests

For example:

```bash
curl http://127.0.0.1:8000/
```

---

## 🎯 Learning Goals

The main purpose of this repository is to build a strong understanding of:

> **Python → FastAPI → Pydantic → REST APIs → Backend Development**

The project can be expanded later with:

* Database integration
* CRUD operations
* Authentication & Authorization
* JWT
* SQLAlchemy
* PostgreSQL
* API testing
* Docker
* Deployment

---

## 📖 Resources

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Documentation](https://docs.pydantic.dev/)
* [Uvicorn Documentation](https://www.uvicorn.org/)

---

## 👨‍💻 Author

**Shubham Kumar**

GitHub: [@shubhamX86](https://github.com/shubhamX86)

---

## ⭐ Support

If this repository helps you learn FastAPI, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is intended for learning and educational purposes.
