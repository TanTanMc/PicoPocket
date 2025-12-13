import io
import os
import sqlite3
from datetime import datetime

from flask import Flask, g, request, redirect, url_for, render_template_string, send_file, flash
import qrcode

app = Flask(__name__)
app.secret_key = "dev-key"

# Database stored safely in Flask instance folder
DB_PATH = os.path.join(app.instance_path, "wallet.db")


# -------------------- DATABASE --------------------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    os.makedirs(app.instance_path, exist_ok=True)
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            balance INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL,
            sender INTEGER,
            receiver INTEGER,
            amount INTEGER NOT NULL,
            note TEXT
        );
        """
    )
    db.commit()


def cents(x):
    return int(float(x) * 100)


def money(c):
    return f"{c / 100:.2f}"


# -------------------- UI TEMPLATE --------------------
BASE = """
<!doctype html>
<title>Pico Pocket Pay</title>
<style>
body { font-family: Arial; max-width: 900px; margin: auto; }
.card { border: 1px solid #ccc; padding: 15px; margin: 15px 0; border-radius: 10px; }
input, select, button { padding: 8px; width: 100%; margin: 5px 0; }
button { cursor: pointer; }
.flash { background: #ffeaa7; padding: 10px; border-radius: 6px; }
table { width: 100%; border-collapse: collapse; }
td, th { border-bottom: 1px solid #ddd; padding: 6px; }
</style>

<h1>Pico Pocket Pay (Python)</h1>

{% for m in get_flashed_messages() %}
<div class="flash">{{ m }}</div>
{% endfor %}

{{ body|safe }}
"""


# -------------------- ROUTES --------------------
@app.route("/")
def home():
    init_db()
    db = get_db()
    users = db.execute("SELECT * FROM users").fetchall()
    tx = db.execute("SELECT * FROM transactions ORDER BY id DESC").fetchall()

    body = render_template_string("""
<div class="card">
<h2>Create User</h2>
<form method="post" action="/create">
<input name="name" placeholder="Name" required>
<button>Create</button>
</form>
</div>

<div class="card">
<h2>Add Money</h2>
<form method="post" action="/add">
<select name="user">
{% for u in users %}
<option value="{{u.id}}">{{u.name}}</option>
{% endfor %}
</select>
<input name="amount" placeholder="Amount (e.g. 5.00)" required>
<button>Add</button>
</form>
</div>

<div class="card">
<h2>Pay</h2>
<form method="post" action="/pay">
<label>From</label>
<select name="from">
{% for u in users %}
<option value="{{u.id}}">{{u.name}}</option>
{% endfor %}
</select>

<label>To</label>
<select name="to">
{% for u in users %}
<option value="{{u.id}}">{{u.name}}</option>
{% endfor %}
</select>

<input name="amount" placeholder="Amount" required>
<button>Send</button>
</form>
</div>

<div class="card">
<h2>Users</h2>
<table>
<tr><th>Name</th><th>Balance</th><th>QR</th></tr>
{% for u in users %}
<tr>
<td>{{u.name}}</td>
<td>{{u.balance/100}}</td>
<td><a href="/qr/{{u.id}}">QR</a></td>
</tr>
{% endfor %}
</table>
</div>

<div class="card">
<h2>Transactions</h2>
<table>
<tr><th>Time</th><th>From</th><th>To</th><th>Amount</th></tr>
{% for t in tx %}
<tr>
<td>{{t.time}}</td>
<td>{{t.sender}}</td>
<td>{{t.receiver}}</td>
<td>{{t.amount/100}}</td>
</tr>
{% endfor %}
</table>
</div>
""", users=users, tx=tx)

    return render_template_string(BASE, body=body)


@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    db = get_db()
    try:
        db.execute("INSERT INTO users (name) VALUES (?)", (name,))
        db.commit()
        flash("User created")
    except:
        flash("User already exists")
    return redirect("/")


@app.route("/add", methods=["POST"])
def add():
    uid = request.form["user"]
    amount = cents(request.form["amount"])
    db = get_db()
    db.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, uid))
    db.execute(
        "INSERT INTO transactions VALUES (NULL, ?, NULL, ?, ?, ?)",
        (datetime.now().isoformat(), uid, amount, "add"),
    )
    db.commit()
    flash("Money added")
    return redirect("/")


@app.route("/pay", methods=["POST"])
def pay():
    f = request.form["from"]
    t = request.form["to"]
    amount = cents(request.form["amount"])

    db = get_db()
    bal = db.execute("SELECT balance FROM users WHERE id=?", (f,)).fetchone()["balance"]
    if bal < amount:
        flash("Not enough money")
        return redirect("/")

    db.execute("UPDATE users SET balance = balance - ? WHERE id=?", (amount, f))
    db.execute("UPDATE users SET balance = balance + ? WHERE id=?", (amount, t))
    db.execute(
        "INSERT INTO transactions VALUES (NULL, ?, ?, ?, ?, ?)",
        (datetime.now().isoformat(), f, t, amount, "pay"),
    )
    db.commit()
    flash("Payment sent")
    return redirect("/")


@app.route("/qr/<int:uid>")
def qr(uid):
    img = qrcode.make(f"USER:{uid}")
    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
