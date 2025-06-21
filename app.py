from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root0808",
    database="feedbackdb"
)
cursor = conn.cursor()

@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        cursor.execute("INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)", 
                       (name, email, message))
        conn.commit()
        return "Thank you for your feedback!"

    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
