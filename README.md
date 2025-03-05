
# Wiki Project

### Overview  
This project is part of **Project 1**, where a Wikipedia-like application was developed. Below is the breakdown of the project structure.

---

### Folder and File Structure  

#### 1. **Encyclopedia**  
This folder contains the core of the application, including several subfolders such as **static** and **templates**:  
- **Static folder**:  
    - `style.css` – Defines the styling for the entire project.  
    - `wikipedia-logo.png` – The project's logo.  
    - `favicon.ico` – The favicon displayed in the browser tab.  
- **Templates folder**: Contains the HTML files:  
    1. **`edit.html`** – Allows editing of existing pages.  
    2. **`entry.html`** – Displays the content of an entry.  
    3. **`error.html`** – Shows error messages.  
    4. **`index.html`** – Main page of the app.  
    5. **`layout.html`** – Defines the page layout.  
    6. **`newpage.html`** – Enables the creation of new pages.  
    7. **`search.html`** – Displays search results.  

##### Additional key files in the `encyclopedia` folder:  
1. **`util.py`** – Contains utility functions for listing, retrieving, and converting content. These functions are essential for displaying entry content.  
2. **`urls.py`** – Maps the application's URL paths.  
3. **`views.py`** – Contains the main logic and functions that power the application.  

---

#### 2. **Entries**  
This folder stores all the entries displayed on the website. New entries created through the application are also saved here.  

---

#### 3. **Wiki**  
This folder includes essential Django configurations and functions required to run the project.  

---

### Technology Stack  

- **Django** – Backend framework used for creating the project.  
- **CSS** – Used for styling the application.  
- **HTML** – Used for structuring the web pages.  

---

### Additional Notes  

This project demonstrates how to build a basic content management system using Django. It supports creating, editing, and searching entries, with a focus on modularity and maintainability.

---