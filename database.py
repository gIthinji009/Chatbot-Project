import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    
    # Create tables based on ERD
    c.execute('''CREATE TABLE IF NOT EXISTS User (
                 UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Name TEXT,
                 Email TEXT
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS Admin (
                 AdminID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Username TEXT UNIQUE,
                 Password TEXT,
                 Email TEXT
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS KnowledgeBase (
                 EntryID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Question TEXT,
                 Answer TEXT,
                 Category TEXT,
                 LastUpdated DATETIME
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS Query (
                 QueryID INTEGER PRIMARY KEY AUTOINCREMENT,
                 UserID INTEGER,
                 QueryText TEXT,
                 Timestamp DATETIME,
                 FOREIGN KEY (UserID) REFERENCES User(UserID)
                 )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS Log (
                 LogID INTEGER PRIMARY KEY AUTOINCREMENT,
                 QueryID INTEGER,
                 ResponseText TEXT,
                 Timestamp DATETIME,
                 FOREIGN KEY (QueryID) REFERENCES Query(QueryID)
                 )''')
    
    # Insert sample data
    c.execute("INSERT OR IGNORE INTO User (Name, Email) VALUES (?, ?)", ("Guest User", "guest@example.com"))
    c.execute("INSERT OR IGNORE INTO KnowledgeBase (Question, Answer, Category, LastUpdated) VALUES (?, ?, ?, ?)",
              ("What are the admission requirements?", "High school diploma and SAT scores.", "Admissions", datetime.now()))
    c.execute("INSERT OR IGNORE INTO KnowledgeBase (Question, Answer, Category, LastUpdated) VALUES (?, ?, ?, ?)",
              ("What is the tuition fee?", "Tuition is $10,000 per semester.", "Fees", datetime.now()))
    
    
    hashed_password = "$2b$12$xBe0yrr9ZkWTgZw9r2cef.zyeFMELoB417LAy2EZhOricGS9e0Lka"  
    c.execute("INSERT OR IGNORE INTO Admin (Username, Password, Email) VALUES (?, ?, ?)",
              ("admin", hashed_password, "admin@university.com"))
    
    conn.commit()
    conn.close()

def add_query(user_id, query_text):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO Query (UserID, QueryText, Timestamp) VALUES (?, ?, ?)",
              (user_id, query_text, datetime.now()))
    query_id = c.lastrowid
    conn.commit()
    conn.close()
    return query_id

def add_log(query_id, response_text):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO Log (QueryID, ResponseText, Timestamp) VALUES (?, ?, ?)",
              (query_id, response_text, datetime.now()))
    conn.commit()
    conn.close()

def search_knowledge_base(query_text):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT Answer FROM KnowledgeBase WHERE Question LIKE ?", (f"%{query_text}%",))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "Sorry, I don't understand. Please try again."

def add_faq(question, answer, category):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO KnowledgeBase (Question, Answer, Category, LastUpdated) VALUES (?, ?, ?, ?)",
              (question, answer, category, datetime.now()))
    conn.commit()
    conn.close()

def get_faqs():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT EntryID, Question, Answer, Category FROM KnowledgeBase")
    faqs = c.fetchall()
    conn.close()
    return faqs

def verify_admin(username, password):
    import bcrypt
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("SELECT Password FROM Admin WHERE Username = ?", (username,))
    result = c.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        return True
    return False

