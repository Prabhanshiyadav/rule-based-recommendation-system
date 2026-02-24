from flask import Blueprint, render_template, request, redirect, session
from database.db import users, history, rules_collection

admin = Blueprint("admin", __name__)


@admin.route("/admin", methods=["GET", "POST"])
def admin_dashboard():

    if request.method == "POST":
        condition = request.form["condition"]
        recommendation = request.form["recommendation"]

        rules_collection.insert_one({
            "condition": condition,
            "recommendation": recommendation
        })

        return redirect("/admin")

    total_users = users.count_documents({})
    total_recs = history.count_documents({})

    pipeline = [
        {"$group": {"_id": "$input", "count": {"$sum": 1}}}
    ]

    category_data = list(history.aggregate(pipeline))

    labels = [item["_id"] for item in category_data]
    values = [item["count"] for item in category_data]

    rules = list(rules_collection.find())

    return render_template(
        "admin.html",
        total_users=total_users,
        total_recs=total_recs,
        labels=labels,
        values=values,
        rules=rules
    )


# DELETE RULE
@admin.route("/delete_rule/<rule_id>")
def delete_rule(rule_id):

    from bson.objectid import ObjectId

    rules_collection.delete_one({"_id": ObjectId(rule_id)})

    return redirect("/admin")