from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'contents.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS content (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            content TEXT NOT NULL,
                            timestamp TEXT NOT NULL)
                     ''')

def save_content(content):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO content (content, timestamp) VALUES (?, ?)",
                     (content, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
def load_content(page):
    offset = (page-1) * 20
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute("SELECT content, timestamp FROM content ORDER BY timestamp DESC LIMIT 20 OFFSET ?", (offset,))
        results = cursor.fetchall()
        return [
            {
                "content": result[0],
                "timestamp": result[1]
            } for result in results
        ]

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/save', methods=['POST'])
def api_save():
    data = request.get_json()
    content = data.get('content', '')
    save_content(content)
    return jsonify({'message': 'Saved'})

@app.route('/api/load')
def api_load():
    page = request.args.get('page', 1, type=int)
    contents = load_content(page)
    return jsonify(contents)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88)
