from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from database import init_db, add_query, add_log, search_knowledge_base, add_faq, get_faqs, verify_admin

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For session management

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    user_id = data.get('user_id', 1)  # Default to guest user
    query_text = data.get('query_text', '').strip()
    
    # Input validation
    if not query_text:
        return jsonify({"response": "Please enter a valid query."})
    
    # Log query
    query_id = add_query(user_id, query_text)
    
    # Search knowledge base
    response = search_knowledge_base(query_text)
    
    # Log response
    add_log(query_id, response)
    
    return jsonify({"response": response})

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if verify_admin(username, password):
            session['admin'] = username
            return redirect(url_for('admin_dashboard'))
        return render_template('admin_login.html', error="Invalid credentials")
    return render_template('admin_login.html')

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        question = request.form.get('question').strip()
        answer = request.form.get('answer').strip()
        category = request.form.get('category').strip()
        
        # Input validation
        if question and answer and category:
            add_faq(question, answer, category)
            return render_template('admin_dashboard.html', faqs=get_faqs(), message="FAQ added successfully")
        return render_template('admin_dashboard.html', faqs=get_faqs(), error="All fields are required")
    
    return render_template('admin_dashboard.html', faqs=get_faqs())

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    init_db()  # Initialize database
    app.run(debug=True)