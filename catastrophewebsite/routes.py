from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():
    """Render the home page."""
    return render_template("index.html.j2")


@main_blueprint.route("/roadmap")
def roadmap():
    """Render the roadmap page."""
    return render_template("roadmap.html.j2")


@main_blueprint.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html.j2")


@main_blueprint.route("/contact")
def contact():
    """Render the contact page."""
    return render_template("contact.html.j2")
