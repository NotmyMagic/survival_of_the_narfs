from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required
from .models import Narf
from . import db
import json


views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():

    if request.method == "POST":
        height = request.form.get("height")
        color = request.form.get("color")
        claws = request.form.get("claws")
        teeth = request.form.get("teeth")
        fur = request.form.get("fur")

        new_narf = Narf(height=height, color=color, claws=claws, teeth=teeth, fur=fur, user_id=(current_user.id))
        db.session.add(new_narf)
        db.session.commit()
        print(new_narf)
        flash("Narf Created", category="success")
        return redirect(url_for("views.home"))


    return render_template("home.html", user=current_user)

@views.route("/delete-narf", methods=["POST"])
def delete_narf():
    narf = json.loads(request.data)
    narfId = narf["narfId"]
    narf = Narf.query.get(narfId)
    if narf:
        if narf.user_id == current_user.id:
            db.session.delete(narf)
            db.session.commit()
            return jsonify({})