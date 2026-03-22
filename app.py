from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# create DB
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")
    conn.commit()
    conn.close()

init_db()

# home
@app.route("/")
def home():
    return render_template("index.html")

# get notes
@app.route("/get_notes")
def get_notes():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

# add note
@app.route("/add_note", methods=["POST"])
def add_note():
    text = request.json["text"]
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO notes (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

# delete note
@app.route("/delete_note/<int:id>", methods=["DELETE"])
def delete_note(id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)