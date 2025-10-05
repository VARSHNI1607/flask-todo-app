**Problem Statement**

Managing tasks and deadlines effectively is a common challenge for students, professionals, and anyone with multiple responsibilities. Many task management solutions are either too complex, require multiple apps, or do not provide a simple overview of tasks for the day.  

**This project solves this problem by providing:**

- A simple, intuitive interface for task management  
- Task categorization and prioritization  
- Deadline management with a daily overview
- 
**Objectives**

1. **Task Management**  
   - Add, edit, and delete tasks easily.  

2. **Task Categorization**  
   - Organize tasks into categories such as Work, Personal, or custom categories.  

3. **Deadline and Daily Overview**  
   - Set deadlines for tasks.  
   - Display tasks sorted by deadlines to highlight priorities for the day.  

4. **Task Prioritization**  
   - Mark tasks as High, Medium, or Low priority.  

5. **Completion Tracking**  
   - Mark tasks as completed to track progress.  

6. **User-Friendly Interface**  
   - Clean and responsive design for ease of use.  

---

## **Tech Stack**

- **Backend:** Python 3, Flask  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Database / Storage:**  
  - Replit DB (if running on Replit) or SQLite (for local deployment)  
- **Version Control:** Git, GitHub  
- **Hosting / Online IDE:** Replit (optional for online running)  

---

## **Implementation Details**

### **1. Backend (Flask)**
- `app.py` handles routes and logic:
  - `/` → Displays all tasks and daily overview.  
  - `/add` → Adds a new task.  
  - `/edit/<task_id>` → Updates an existing task.  
  - `/delete/<task_id>` → Deletes a task.  
- Tasks are stored with fields: `title`, `description`, `category`, `deadline`, `priority`, `completed`.

### **2. Frontend**
- **HTML Templates:** Stored in the `templates/` folder.  
  - `index.html` displays tasks and forms to add/edit tasks.  
- **CSS:** Custom styling in `static/style.css` for layout, colors, and responsiveness.  
- **JavaScript:** Handles minor interactivity (optional notifications, marking tasks complete without reload).  

### **3. Task Sorting & Daily Overview**
- Tasks are **sorted by deadline date** to show the most urgent tasks first.  
- The daily overview highlights tasks due today for quick reference.

### **4. Deployment / Running**
- **Locally:**  
  1. Clone the repo: `git clone <repo-url>`  
  2. Create virtual environment: `python -m venv venv`  
  3. Install dependencies: `pip install -r requirements.txt`  
  4. Run the app: `python app.py`  
  5. Visit `http://127.0.0.1:5000` in a browser.  

- **Online:** Import the GitHub repo into Replit or host using platforms like Render, Railway, or PythonAnywhere.  

---

## **Folder Structure**

