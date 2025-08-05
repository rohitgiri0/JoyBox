


# 🎮 JoyBox

JoyBox is a modern web application built to connect gamers who want to rent or share their gaming setups. It allows users to post listings, chat in real-time, and authenticate via Google or email.

---

## 🚀 Tech Stack

- **Frontend**:  
  - HTML  
  - Tailwind CSS  
  - JavaScript (minimal)  

- **Backend**:  
  - Python  
  - Django  
  - Django Channels (for real-time chat)

- **Database**:  
  - PostgreSQL  (for hosting), sqlite3 locally

- **Authentication**:  
  - Google OAuth  
  - Django's built-in auth system

---

## 📦 Features

- User registration and login (via Google or email)
- Create, view, and manage gaming setup listings
- Real-time 1-on-1 chat between users
- Beautiful UI using Tailwind CSS
- Responsive layout for mobile and desktop
- Login required to list or chat
- Secure password handling and session management

---

## 🛠️ How to Run Locally

### Prerequisites

- Python 3.8+
- Node.js & npm (for Tailwind CSS)
- `pip` package manager

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/joybox.git
cd JoyBox
```

### 2. Set up a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```


### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
daphne JoyBox.asgi:application
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

### thanks 