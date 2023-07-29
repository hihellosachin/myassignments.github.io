from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a SQLite database and a 'assignments' table to store assignment data
def create_db():
    conn = sqlite3.connect('assignments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS assignments 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 description TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Add a new assignment to the database
def add_assignment(title, description):
    conn = sqlite3.connect('assignments.db')
    c = conn.cursor()
    c.execute('INSERT INTO assignments (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    conn.close()

# Retrieve all assignments from the database
def get_assignments():
    conn = sqlite3.connect('assignments.db')
    c = conn.cursor()
    c.execute('SELECT * FROM assignments')
    assignments = c.fetchall()
    conn.close()
    return assignments

# Home page - show all assignments
@app.route('/')
def home():
    assignments = get_assignments()
    return render_template('index.html', assignments=assignments)

# Form to add a new assignment
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        add_assignment(title, description)
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ... Existing code ...

# Add a new assignment to the database
def add_assignment(title, description):
    conn = sqlite3.connect('assignments.db')
    c = conn.cursor()
    c.execute('INSERT INTO assignments (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    conn.close()

# ... Existing code ...

# Form to add a new assignment
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        add_assignment(title, description)
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
