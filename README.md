# SQLi Login System

## Overview
The SQLi Login System is a basic educational program designed to highlight the risks of SQL injection that can occur within authentication systems, which do not validate the input of users.
This project makes use of Python, MySQL, and Tkinter in order to create an interactive login environment and learn about the risks related to improper SQL querying. It was created as a part of my cybersecurity knowledge-building journey.

## Key Features
* MySQL database support
* Authentication system for users
* SQL injection vulnerability examples
* Basic coding for education

## Technologies Used
* Python
* MySQL
* mysql-connector-python

## Project Aim
The aim of the current project is to allow students to comprehend:
* Application Database Interaction
* Working of an Authentication System 
* Attack through SQL Injection
* The importance of Input Validation and Parameterized Queries 
* Security Considerations in Coding
  
## Setup
### 1. Clone the Repository
```bash
git clone https://github.com/AhmaqAhmed/sqli-login-system
cd sqli-login-system
```

### 2. Install Dependencies
```bash
pip install mysql-connector-python
```

### 3. Create the Database
Create a MySQL database and table, then insert sample user records.
Example:
```sql
CREATE DATABASE sqli_demo;
USE sqli_demo;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);
```

### 4. Configure Database Connection
Update the database connection settings in the Python script:
```python
host="localhost"
user="your_username"
password="your_password"
database="sqli_demo"
```

### 5. Run the Application
```bash
python main.py
```

## Learning Outcomes
As a result of this project, I have gained knowledge about:
* Creation and management of databases
* Querying SQL queries
* Integrating Python applications with MySQL
* Authentication processes
* SQL Injection

## Security Warning
Vulnerable login logic on purpose to demonstrate the flaws that can be made during application development.
Do not use the code in any real-life environment. Use parameterized queries for safety.

## Blog Post
For detailed information about the project and process, visit:
https://first-projects-blog.hashnode.dev/sqli-demonstration

## Enhancements to Consider
* Show how login works properly through parameterized queries
* Password hashing with bcrypt
* Register feature
* Better UI
* More tests for SQL injection attacks

## License
This project was created to help users learn cybersecurity concepts.
