# 🏋️‍♀️ Fitness Studio Booking API

A simple booking API built using **FastAPI** for a fictional fitness studio that offers classes like **Yoga**, **Weight Training**, and **Cardio**.

The API allows users to:
- View available classes
- Book a slot
- Retrieve bookings by email

---

## 🚀 Features

- Built with **FastAPI**
- File-based storage using JSON (no external database required)
- Simple and clean architecture
- Dockerized for easy deployment
- Input validation, error handling, and modular design

---

## ⚙️ Setup Instructions

### 🔧 Option 1: Run Locally (with Python)

1. **Install dependencies**
   `pip install -r requirements.txt`

2. **Start the application**
    `uvicorn app.main:app --host=0.0.0.0 --port=8000`

3. **Access API docs**
    `http://localhost:8000/docs`

### 🐳 Option 2: Run with Docker

1. **Build the Docker image**
    `docker build -t fitness-booking-api .`

2. **Run the container**
    `docker run -p 8000:8000 fitness-booking-api`

3. **Access API docs**
    `http://localhost:8000/docs`

---

## 📮 API Endpoints & Sample Requests

### 1. GET /classes

**Sample Request**
    `curl -X GET http://localhost:8000/classes`

### 2. GET /bookings?email=<client_email>

**Sample Request**
    `curl -X GET "http://localhost:8000/bookings?email=aniket@gmail.com"`


### 3. POST /bookings

**Request Body:**
    `{
        "class_id": "class_1,
        "client_name": "Aniket Kurkute",
        "client_email": "aniket@gmail.com"
    }`

**Sample Request:**
    `curl -X POST http://localhost:8000/bookings \
    -H "Content-Type: application/json" \
    -d '{"class_id":1, "client_name":"John Doe", "client_email":"john@example.com"}'`
