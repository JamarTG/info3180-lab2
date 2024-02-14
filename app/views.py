from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###


@app.route("/")
def home():
    """Render website's home page."""
    return render_template("home.html")


@app.route("/about/")
def about():
    """Render the website's about page."""
    user = {
        "name": "Jamari McFarlane",
        "at": "jtg",
        "image_src": url_for("static", filename="images/jtg.jpg"),
        "location": "Kingston, Jamaica",
        "joined": datetime.date(2024, 1, 31),
        "biography": "I am a software developer who primarily codes with the MERN Stack + GraphQL and is currently learning flask and SQL for my latest job (COINCIDENCE??). Gonna use this for my personal portfolio btw.",
        "followers": 999,
        "following": 0,
        "posts": 56,
    }
    return render_template("about.html", name=user["name"])


@app.route("/profile/")
def profile():
    user = {
        "name": "Jamari McFarlane",
        "at": "jtg",
        "image_src": url_for("static", filename="images/jtg.jpg"),
        "location": "Kingston, Jamaica",
        "joined": datetime.date(2024, 1, 31),
        "biography": "I am a software developer who primarily codes with the MERN Stack + GraphQL and is currently learning flask and SQL for my latest job (COINCIDENCE??). Gonna use this for my personal portfolio btw.",
        "followers": 999,
        "following": 0,
        "posts": 56,
    }
    return render_template(
        "profile.html",
        name=user["name"],
        image_src=user["image_src"],
        at=user["at"],
        location=user["location"],
        joined=format_date_joined(user["joined"]),
        biography=user["biography"],
        followers=user["followers"],
        following=user["following"],
        posts=user["posts"],
    )


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template("404.html"), 404


def format_date_joined(date):
    return date.strftime("%b, %Y")
