# 🩸 Blood Bank Management System

A full-stack Django-based web application developed to manage blood donors, blood requests, and donor availability efficiently.

---

## 🚀 Features

### Authentication System
- Secure Login & Logout
- User Registration system

### Donor Management
- Add new donors
- Update donor details
- Delete donor records
- Toggle donor availability

###  Search Module
- Search donors by Blood Group
- Search donors by City

###  Blood Request Module
- Raise blood requests
- Track request status

###  Dashboard
- Total donors count
- Available donors count
- Blood group statistics

###  Other Features
- Mobile number validation
- Responsive UI design

---

## 🛠️ Technologies Used

- Python 
- Django 
- HTML5
- CSS3
- Bootstrap
- SQLite3

---

## 📁 Project Structure
BLOODBANK/
│
├── bloodbank/                
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── donor/                    
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── templates/                
│   ├── available_donors.html
│   ├── blood_request.html
│   ├── dashboard.html
│   ├── donor_list.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── request_list.html
│   ├── search.html
│   └── update_donor.html
│
├── static/                   
├── db.sqlite3               
├── manage.py
├── README.md
├── LICENSE
└── .gitignore
### Future Enhancements
 * Online blood request approval system
 * Admin dashboard API integration
 * Deployment on cloud (AWS/Render/Heroku)