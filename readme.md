# 🔐 Secure Login Attempt Logger

## 📌 Project Overview
Secure Login Attempt Logger is a simple Cybersecurity project developed using **Python** and **Tkinter**. It provides a graphical login interface where users enter their username and password. Every login attempt is recorded in a log file with the current date, time, username, and login status (SUCCESS or FAILED).

The project also includes an account lock feature after three unsuccessful login attempts to prevent unauthorized access.

---

## 🚀 Features

- GUI-based Login System
- Predefined User Authentication
- Logs every login attempt
- Records Date & Time
- Shows Success/Failed Login Status
- Account Lock after 3 Failed Attempts
- Simple and Easy-to-Understand Code

---


- Python 3.x
- Tkinter (GUI)
- datetime Module

---

## 📂 Project Structure

```
Secure_Login_Attempt_Logger/
│
├── login_logger.py
├── login_logs.txt
├── README.md
```

---

## 👤 Default Users

| Username | Password |
|----------|----------|
| admin | 12345 |
| hanny | hanny123 |
| rahul | rahul@123 |
| aman | aman123 |

---

## ▶️ How to Run

1. Install Python 3.
2. Save the Python code as `login_logger.py`.
3. Open Command Prompt or Terminal.
4. Navigate to the project folder.
5. Run the following command:

```bash
python login_logger.py
```

---

## 📋 Working

1. Launch the application.
2. Enter Username and Password.
3. Click the **Login** button.
4. If credentials are correct:
   - Welcome message is displayed.
   - Login is recorded as **SUCCESS**.
5. If credentials are incorrect:
   - Login is recorded as **FAILED**.
   - Remaining attempts are shown.
6. After **3 failed attempts**, the application is locked and closed automatically.

---

## 📝 Sample Log File

```
14-07-2026 01:20:15 PM | Username: admin | SUCCESS
14-07-2026 01:22:40 PM | Username: rahul | FAILED
14-07-2026 01:23:05 PM | Username: aman | FAILED
```

---

## 🔒 Security Features

- User Authentication
- Login Attempt Logging
- Failed Login Tracking
- Account Lock after Three Failed Attempts
- Timestamp Recording

---

## 📈 Future Enhancements

- Password Hashing
- Database Connectivity (MySQL/SQLite)
- Forgot Password Feature
- Admin Dashboard
- User Registration
- OTP Verification
- Email Alerts
- Password Strength Checker

---

## 🎯 Learning Outcomes

- Python GUI Programming
- Authentication System
- File Handling
- Login Security
- Event Handling
- Cybersecurity Basics
- Logging Mechanism

---

## 👩‍💻 Author

**jagrti saini**

BCA Cybersecurity Mini Project

---

## 📄 License

This project is created for educational purposes only.
