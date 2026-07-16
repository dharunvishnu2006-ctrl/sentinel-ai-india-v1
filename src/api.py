from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/status")
def status():
    conn = sqlite3.connect("data/sentinel.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT alerts_count FROM cloudshield_status ORDER BY id DESC LIMIT 1"
    )
    cloudshield = cursor.fetchone()

    cursor.execute(
        "SELECT datasets_profiled FROM autopilot_status ORDER BY id DESC LIMIT 1"
    )
    autopilot = cursor.fetchone()
    conn.close()

    return jsonify({
        "cloudshield": cloudshield[0] if cloudshield else 0,
        "autopilot": autopilot[0] if autopilot else 0
    })
if __name__ == "__main__":
    app.run(debug=True, port=5000)