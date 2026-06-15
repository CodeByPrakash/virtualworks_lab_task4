from flask import Flask, render_template, jsonify
import sqlite3
import requests
import os

app = Flask(__name__)
DB_FILE = 'quotes.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database
with app.app_context():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quote', methods=['GET'])
def get_quote():
    try:
        # Fetch from external API
        response = requests.get('https://dummyjson.com/quotes/random', timeout=5)
        response.raise_for_status()
        data = response.json()
        quote_text = data.get('quote')
        quote_author = data.get('author')

        # Save to database
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('INSERT INTO quotes (text, author) VALUES (?, ?)', (quote_text, quote_author))
        quote_id = c.lastrowid
        conn.commit()
        conn.close()

        return jsonify({'id': quote_id, 'text': quote_text, 'author': quote_author})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM quotes ORDER BY id DESC')
    quotes = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(quotes)

if __name__ == '__main__':
    # Use port 5003 to avoid conflicts with tasks 1, 2, and 3
    app.run(port=5003, debug=True)
