from flask import Blueprint, render_template, request, url_for, redirect 
from extensions import mail

page = Blueprint('page', __name__)

@page.route('/')
def index():
	return render_template("index.html")


@page.route("/menu")
def menu():
	return render_template("menu.html")

@page.route("/about")
def about():
	return render_template("about.html")

@page.route("/product")
def product():
	return render_template("product.html")

@page.route("/client")
def client():
	return render_template("client.html")


@page.route("/contact", methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']

		mail.send_message(subject='[Customer online request] Contact',
                          sender=email,
                          recipients=["info@zurimaison.com"],
                          reply_to=email, body=message)
		msg = "Thanks for your request, sales team will be in touch shorlty"
		return render_template("contact.html", message=msg)

	return render_template("contact.html")