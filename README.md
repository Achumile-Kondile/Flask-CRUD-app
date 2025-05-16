# Flask CRUD App 🧑‍💻

This is a simple **Flask-based CRUD application** for managing users. You can create, read, update, and delete user data through a web interface.

---

## 🚀 Features

- 📝 Add new users  
- 📋 View list of users  
- ✏️ Update user details  
- ❌ Delete users

---

## 📸 Screenshots

## Screenshots

### 1. index.html – Home Page (User List)
![Homepage](images/index.html.png)

The homepage displays all users in a table. Each row has "Update" and "Delete" buttons. It uses Jinja templating to render user data passed from `app.py`.
---

### 2. update.html – Update Existing User
![Update Page](images/update.html.png)

This page shows a pre-filled form with the user’s current details. It allows editing and submits updated info via POST to `/update/<user_id>`.
---

### 3. App.py – The Flask Application Logic
![App Py](images/app.py.png)

This is the heart of the app. It imports Flask, defines the routes, and handles the logic for displaying, creating, updating, and deleting users. Key routes include `/`, `/create`, `/update/<id>`, and `/delete/<id>`.
---

### 4.  create.html – Add New User Form
![Create Page](images/create.html.png)

This page includes a form to input a new user's name and email. On submission, the data is sent to the `/create` route to add the user to the list.
---

### 5.  style.css – Styling the App
## Style Preview 1
![Style CSS 1](images/style1.png)

## Style Preview 2
![Style CSS 2](images/style2.png)

Custom CSS that styles the layout, buttons, and forms. It ensures the interface is clean, responsive, and easy to use.


---

## ⚙️ How to Run the Project

### 📦 Requirements

Install Flask:
```bash
pip install flask
```
Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
python app.py
```
Then open your browser and go to:
```bash
http://127.0.0.1:5000
```
### Project Structure
```bash
crud-app/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── create.html
│   └── update.html
├── images/
│   └── *.png
└── README.md
```
### 🛠 Tech Stack

Python (Flask)

HTML + CSS


