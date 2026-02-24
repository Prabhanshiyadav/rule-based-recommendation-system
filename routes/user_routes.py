from flask import Blueprint, render_template, request, session
from database.db import rules_collection, history
user = Blueprint("user", __name__)


def generate_recommendation(user_input):

    matched = []

    all_rules = list(rules_collection.find())

    for rule in all_rules:
        if rule["condition"].lower() in user_input.lower():
            matched.append(rule["recommendation"])

    return matched


@user.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    results = []

    if request.method == "POST":

        user_input = request.form["interest"]

        # Generate recommendations
        results = generate_recommendation(user_input)

        # Save history
        history.insert_one({
            "user": session.get("user_email"),
            "input": user_input,
            "result": results
        })

    # ✅ FETCH USER HISTORY (IMPORTANT)
    user_history = list(history.find({
        "user": session.get("user_email")
    }))

    return render_template(
        "dashboard.html",
        results=results,
        history=user_history
    )