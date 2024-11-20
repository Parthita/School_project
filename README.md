## Overview

This Python application allows users to register, log in, and track their study time. It uses a MySQL database to store user data and compares the user’s actual study time with their planned study schedule.

### Features:
- **New User Registration**: Users can create a new account with a unique name and password.
- **User Login**: Existing users can log in by entering their name and password.
- **Study Time Tracking**: Compares user inputted study time with the scheduled study time.

---

## Libraries Used

- **mysql-connector**:  
  Used to connect to and interact with the MySQL database. Install it via pip:  
  ```bash
  pip install mysql-connector

    datetime:
    A built-in Python module used for handling date and time functions.

Installation Guide

    Install Python:
    Ensure Python 3.x is installed. Download it here.

    Install Dependencies:
    Run the following command to install the necessary libraries:

pip install mysql-connector

Set Up MySQL Database:
Ensure that MySQL is installed and running on your machine.
Create a database called user_database with the following table schema:

CREATE TABLE user_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    study_time INT,
    entry_time INT
);

Run the Program:
Save the Python script as study_time_tracker.py and run it:

    python study_time_tracker.py

How It Works

The program guides users through either logging into an existing account or registering as a new user. Once logged in, users can track their study time and compare it to their planned schedule.
Example Prompts:

    New or Existing User?

If you are a new user, enter 0  
If you are an existing user, enter 1  

Log in with Name & Password

Please enter your name:  
Please enter your password:  

Track Study Time

    How much time did you study today? (in hours):  

Known Issues / Bugs

    No Validation for Time Inputs: The program doesn't have validation for time input beyond ensuring that it's an integer. You may want to add validation for proper time ranges.
    Timezone Handling: The current implementation doesn't handle time zone differences, which could affect comparisons with stored entry times.


This program tracks users' study schedules and compares their actual study time to their planned study time. Users can create an account, log in with their credentials, and check how much time they studied versus what they had planned.

    Database Design: The database stores the user's name, password, study time, and entry time.
    Time Calculation: The program compares the user’s current time with their entry time and provides feedback on whether they are early or late. It then compares the user's study time against the planned study time.


Contributing

Feel free to fork this repository, submit issues, and create pull requests for improvements. Contributions are welcome!
