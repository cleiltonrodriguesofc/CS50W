# Commerce Project

## Overview  
This project is part of **Project 2**, where an e-commerce auction platform was developed using Django. Below is a breakdown of the project structure.

---

## Folder and File Structure  

### 1. **Auctions**  
This folder contains the core of the application, including several subfolders such as **static** and **templates**:  
- **Static folder**:  
    - `style.css` – Defines the styling for the entire project.  
- **Templates folder**: Contains the HTML files:  
    - `index.html` – Displays active listings.  
    - `layout.html` – Defines the base layout of the pages.  
    - `login.html` – Handles user authentication.  
    - `register.html` – Allows users to create an account.  
    - `listing.html` – Displays details of a specific listing.  
    - `create_listing.html` – Enables users to create new listings.  
    - `watchlist.html` – Shows the user's saved listings.  
    - `category_listings.html` – Displays listings by category.  

#### Additional key files in the `auctions` folder:  
- `models.py` – Defines the database models for users, listings, bids, and comments.  
- `urls.py` – Maps the application's URL paths.  
- `views.py` – Contains the main logic and functions that power the application.  
- `forms.py` – Handles Django form logic for user input.

---

### 2. **Database**  
The project uses Django's built-in SQLite database to store users, listings, bids, and comments.

---

### 3. **Commerce**  
This folder includes essential Django configurations and functions required to run the project.  

---

## Technology Stack  

- **Django** – Backend framework used for building the project.  
- **SQLite** – Database for storing application data.  
- **CSS** – Used for styling the application.  
- **HTML** – Used for structuring the web pages.  
- **Python** – Primary language used for backend logic.  

---

## Additional Notes  

This project demonstrates how to build an auction platform where users can create listings, place bids, add comments, and manage watchlists.

---
