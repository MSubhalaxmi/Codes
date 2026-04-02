from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="bank",
    user="postgres",
    password="password",
    host="localhost"
)

@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.json
    sender = data['from']
    receiver = data['to']
    amount = data['amount']

    cur = conn.cursor()

    try:
        cur.execute("BEGIN;")

        cur.execute("UPDATE accounts SET balance = balance - %s WHERE id=%s", (amount, sender))
        cur.execute("UPDATE accounts SET balance = balance + %s WHERE id=%s", (amount, receiver))

        cur.execute("""
            INSERT INTO transactions(sender, receiver, amount)
            VALUES (%s, %s, %s)
        """, (sender, receiver, amount))

        conn.commit()

        return jsonify({"message": "Transaction successful"})

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500