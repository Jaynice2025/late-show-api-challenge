# 🌙 Late Show API - Flask REST API Challenge

A Flask REST API for managing a Late Night TV show system with guests, episodes, and appearances. Features JWT authentication, PostgreSQL database, and full CRUD operations.

## 🚀 GitHub Repository
[https://github.com/jaynice2025/late-show-api-challenge](https://github.com/jaynice2025/late-show-api-challenge)

## 🛠 Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- Pipenv

### 1. Clone Repository
```bash
git clone https://github.com/jaynice2025/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 3. PostgreSQL Database Setup
Create your database:
```sql
CREATE DATABASE late_show_db;
```

### 4. Environment Configuration
Update `server/config.py` with your database credentials:
```python
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/late_show_db"
```

### 5. Database Migration & Seeding
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

### 6. Run the Application
```bash
python server/app.py
```

The API will be available at `http://localhost:5000`

## 🔐 Authentication Flow

### 1. Register a New User
**POST** `/register`
```json
{
  "username": "testuser",
  "password": "testpass123"
}
```

### 2. Login to Get JWT Token
**POST** `/login`
```json
{
  "username": "testuser",
  "password": "testpass123"
}
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "username": "testuser"
  }
}
```

### 3. Use Token in Protected Requests
Include in headers:
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## 📋 API Routes

| Route | Method | Auth Required? | Description |
|-------|--------|----------------|-------------|
| `/register` | POST | ❌ | Register a user |
| `/login` | POST | ❌ | Log in + return JWT |
| `/episodes` | GET | ❌ | List all episodes |
| `/episodes/<int:id>` | GET | ❌ | Get episode + appearances |
| `/episodes/<int:id>` | DELETE | ✅ | Delete episode + appearances |
| `/guests` | GET | ❌ | List all guests |
| `/appearances` | POST | ✅ | Create appearance |

## 📝 API Examples

### Get All Episodes
**GET** `/episodes`

Response:
```json
[
  {
    "id": 1,
    "date": "2024-01-15",
    "number": 1001
  },
  {
    "id": 2,
    "date": "2024-01-16", 
    "number": 1002
  }
]
```

### Get Episode with Appearances
**GET** `/episodes/1`

Response:
```json
{
  "id": 1,
  "date": "2024-01-15",
  "number": 1001,
  "appearances": [
    {
      "id": 1,
      "rating": 5,
      "guest_id": 1,
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Jennifer Lawrence",
        "occupation": "Actress"
      }
    }
  ]
}
```

### Create Appearance (Protected)
**POST** `/appearances`
```json
{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}
```

Headers:
```
Authorization: Bearer your_jwt_token_here
Content-Type: application/json
```

Response