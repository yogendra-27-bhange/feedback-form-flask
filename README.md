# Feedback Form Web App

A simple web-based feedback form built using Python Flask, HTML, CSS, and MySQL. This application allows users to submit their feedback, which is securely stored in a MySQL database.

## 🔧 Technologies Used
- Python (Flask)
- HTML & CSS
- MySQL Database

## 📌 Features
- Responsive feedback form
- Stores user name, email, and message
- MySQL database integration
- Clean UI with basic styling

## 🚀 How to Run
1. Install requirements:
pip install flask mysql-connector-python2. Create MySQL database:
```sql
CREATE DATABASE feedbackdb;
Create table:CREATE TABLE feedback (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  message TEXT
);
Run the app:
python app.py
