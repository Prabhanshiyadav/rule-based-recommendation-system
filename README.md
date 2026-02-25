# 🚀 Rule-Based Recommendation System

A full-stack **Rule-Based Recommendation Web Application** built using **Python (Flask)**, **MongoDB**, **HTML**, **CSS**, and **JavaScript**.
The system provides personalized recommendations to users based on predefined rules, along with authentication, admin analytics, chatbot interaction, and history tracking.

This project demonstrates the practical implementation of **Artificial Intelligence concepts (rule-based systems)** combined with modern **web development** practices.

---

# 📌 Project Overview

In today’s digital world, recommendation systems are widely used in platforms such as e-commerce, education, healthcare, and entertainment.
This project implements a **rule-based recommendation engine** where decisions are generated based on logical conditions rather than machine learning models.

The application includes:

* User authentication system
* Admin rule management
* Recommendation generation
* Chatbot interface
* Analytics dashboard with charts
* Recommendation history tracking
* Secure password encryption
* Responsive professional UI

---

# 🎯 Objectives

* To design and implement a rule-based decision system
* To provide personalized recommendations based on user inputs
* To develop a complete full-stack web application
* To integrate database storage and analytics visualization
* To demonstrate secure authentication and role-based access

---

# 🏗️ System Architecture

The system follows a modular architecture:

```
User → Flask Routes → Recommendation Engine → Database → UI Response
                     ↓
                  Admin Panel
                     ↓
                 Analytics Charts
```

Main components:

1. Frontend (HTML, CSS, JS)
2. Backend (Flask)
3. Database (MongoDB)
4. Rule Engine (Python logic)
5. Authentication System (bcrypt)
6. Analytics Visualization (Chart.js)

---

# 🛠️ Technologies Used

## Backend

* Python
* Flask Framework
* PyMongo
* bcrypt (Password hashing)

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js (Analytics)

## Database

* MongoDB

## Tools

* Git & GitHub
* VS Code
* Postman (optional testing)

---

# ✨ Features

## 👤 User Features

* User Registration & Login
* Secure Password Encryption
* Personalized Recommendations
* Recommendation History Tracking
* Chatbot Assistance
* Dashboard Interface
* Logout System

## 🔐 Admin Features

* Admin Login Protection
* Add / Manage Recommendation Rules
* Analytics Dashboard
* Charts Visualization
* User Data Monitoring

## 📊 Analytics

* Total Users Count
* Total Recommendations Count
* Category Distribution Charts
* Pie Chart Visualization

## 🤖 Chatbot

* Interactive chatbot interface
* Rule-based conversational recommendations

---

# 📂 Project Structure

```
rule-based-recommendation/
│
├── app.py
├── rules.py
├── requirements.txt
│
├── database/
│   └── db.py
│
├── routes/
│   ├── auth_routes.py
│   ├── user_routes.py
│   ├── admin_routes.py
│   └── chatbot_routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── admin.html
│   └── chatbot.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/rule-based-recommendation-system.git
cd rule-based-recommendation-system
```

## 2️⃣ Create Virtual Environment (Optional but Recommended)

```
python -m venv venv
venv\Scripts\activate
```

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

## 4️⃣ Setup MongoDB

Make sure MongoDB is running locally.

Default connection:

```
mongodb://localhost:27017/
```

Database name:

```
recommendation_db
```

Collections:

* users
* rules
* history

---

# ▶️ Run Project

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 🔑 Admin Login Setup

Create admin user manually in MongoDB:

Example:

```
Email: admin@gmail.com
Password: admin123
Role: admin
```

(Password should be hashed using bcrypt if using secure login.)

---

# 🧠 Rule-Based Recommendation Logic

The system uses conditional rules like:

```
IF age < 18 AND interest = "sports"
THEN recommend "Outdoor Games"

IF interest = "technology"
THEN recommend "Programming Courses"
```

Unlike ML models, this approach is:

* Transparent
* Explainable
* Easy to modify
* Fast to execute

---

# 📊 Database Schema

## Users Collection

```
{
  name: String,
  email: String,
  password: Hashed,
  role: "user" | "admin"
}
```

## Rules Collection

```
{
  condition: String,
  recommendation: String
}
```

## History Collection

```
{
  user: String,
  input: Object,
  result: String,
  timestamp: Date
}
```

---

# 🔐 Security Features

* Password hashing using bcrypt
* Session-based authentication
* Role-based authorization
* Admin route protection
* Input validation

---

# 🎨 UI Highlights

* Modern card layout
* Gradient backgrounds
* Responsive design
* Charts visualization
* Interactive buttons
* Professional dashboard

---

# 📸 Screenshots (Add Images Here)

You can insert screenshots like:

```
# 📸 Screenshots

![Home](screenshots/Home.png)
![Dashboard](screenshots/Dashboard.png)
![Login](screenshots/Login.png)
![Register](screenshots/Register.png)
![Admin](screenshots/admin.png)
![Chatbot](screenshots/Chatbot.png)

# 🚀 Future Enhancements

* AI / Machine Learning Hybrid Model
* Email Notification System
* Recommendation Personalization
* Deployment on Cloud
* Mobile App Version
* Voice Assistant Integration

---

# 📚 Learning Outcomes

Through this project, we learned:

* Full-stack web development
* Flask framework usage
* Database integration
* Authentication systems
* Analytics visualization
* AI rule-based systems
* Software architecture design

---

# 👩‍💻 Author

**Prabhanshi Yadav**

* B.Tech Student
* Software & AI Enthusiast

---

# 📜 License

This project is created for educational purposes.

---

# ⭐ Acknowledgements

Special thanks to:

* Open-source community
* Flask documentation
* MongoDB documentation
* Chart.js library

---

# 💡 Conclusion

The Rule-Based Recommendation System demonstrates how intelligent decision-making can be implemented using logical conditions without requiring complex machine learning algorithms. The project successfully integrates AI concepts with modern web technologies to provide a scalable and user-friendly solution.

---

# ❤️ If You Like This Project

Give it a ⭐ on GitHub!

---
