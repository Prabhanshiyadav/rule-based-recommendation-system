from flask import Flask, render_template, request
from rules import recommend

from routes.auth_routes import auth
from routes.admin_routes import admin
from routes.user_routes import user
from routes.chatbot_routes import chatbot


app = Flask(__name__)

app.secret_key = "secret123"

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(chatbot)


@app.route("/", methods=["GET", "POST"])
def index():

    results = []

    if request.method == "POST":
        age = int(request.form.get("age"))
        interest = request.form.get("interest")

        results = recommend(age, interest)

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)