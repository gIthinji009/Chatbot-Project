
# 🎓 University Chatbot

A Flask-based chatbot that answers university-related questions and includes an admin dashboard to manage FAQs.

> ⚠️ **Note:**  
> The website is deployed via **Vercel**, but due to Vercel’s serverless environment, it **cannot communicate with the SQLite database in real time**.  
> For full functionality (chatbot queries and admin updates), please run the project **locally on your machine**.

---

## 🛠️ Local Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Chatbot-Project.git
cd Chatbot-Project
````

---

### 2️⃣ (Optional) Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

---

### 3️⃣ Install Required Dependencies

Ensure `pip` is up-to-date:

```bash
python -m pip install --upgrade pip
```

Then install all dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Initialize the Database

Before launching the chatbot, initialize the local SQLite database:

```bash
python database.py
```

This will create a file named **`chatbot.db`** in your project directory and populate it with default tables and sample data.

---

### 5️⃣ Launch the Flask Application

Run the application:

```bash
python app.py
```

Once it starts, open your browser and go to:

```
http://127.0.0.1:5000
```

---

### 6️⃣ Admin Access

Access the admin dashboard via:

```
http://127.0.0.1:5000/admin
```

Use the default credentials below to log in:

```
Username: admin
Password: admin123
```

> 💡 You can change admin credentials directly in the `database.py` file or by updating the `chatbot.db` SQLite database manually.

---

✅ You now have the chatbot running locally with full database functionality.

---

## 🧩 Project Structure

```
Chatbot-Project/
│
├── app.py               # Main Flask application
├── database.py          # Database initialization & CRUD functions
├── chatbot.db           # SQLite database file (auto-created)
├── requirements.txt     # Python dependencies
├── static/              # CSS and JS files
├── templates/           # HTML templates
└── README.md            # Documentation
```

---

## ⚙️ Technologies Used

* **Python 3.10+**
* **Flask**
* **SQLite**
* **HTML, CSS, JavaScript**

---

## 🧑‍💻 Author


GitHub: [@gIthinji009](https://github.com/gIthinji009)

