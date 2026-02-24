from flask import Blueprint, render_template, request

chatbot = Blueprint("chatbot", __name__)


@chatbot.route("/chatbot", methods=["GET", "POST"])
def chatbot_page():

    response = ""

    if request.method == "POST":

        msg = request.form.get("message").lower()

        if "hello" in msg:
            response = "Hello! How can I help you?"

        elif "recommend" in msg:
            response = "Please go to home page for recommendations."

        else:
            response = "I don't understand."

    return render_template("chatbot.html", response=response)