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

def load_content(page, limit=10):
    offset = (page-1) * limit
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute("SELECT id, content, timestamp FROM content ORDER BY timestamp DESC LIMIT ? OFFSET ?", (limit, offset))
        results = cursor.fetchall()
        return [
            {
                "id": result[0],
                "content": result[1],
                "timestamp": result[2]
            } for result in results
        ]

def delete_content(content_id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("DELETE FROM content WHERE id = ?", (content_id,))

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
    limit = request.args.get('limit', 10, type=int)
    contents = load_content(page, limit)
    return jsonify(contents)

@app.route('/edit', methods=['GET', 'POST'])
def edit_page():
    if request.method == 'POST':
        data = request.get_json()
        content_id = data.get('id', '')
        new_content = data.get('content', '')
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("UPDATE content SET content = ? WHERE id = ?", (new_content, content_id))
        return jsonify({'message': 'Updated'})
    else:
        contents = load_content(1)  # load the first page of contents for simplicity
        return render_template('edit.html', contents=contents)

@app.route('/del')
def delete_page():
    return render_template('delete.html')

@app.route('/api/delete', methods=['POST'])
def api_delete():
    data = request.get_json()
    content_id = data.get('id', '')
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("DELETE FROM content WHERE id = ?", (content_id,))
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88)