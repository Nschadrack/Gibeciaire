from flask import render_template, url_for
from gibrun import gibapp
from models import *


@gibapp.route("/")
@gibapp.route("/index")
@gibapp.route("/Acceuille")
def Acceuille():
	title="Acceuille"
	return render_template("french/indexfre.html", title=title)


@gibapp.route("/Apropos")
def apropos():
	title="Apropos"
	return render_template("french/aboutfre.html", title=title)

@gibapp.route("/nosContacts")
def noscontacts():
	title="Noscontacts"
	return render_template("french/contactfre.html", title=title)

@gibapp.route("/alimentation/Nourritures")
def nourritures():

	title ="Nourritures"

	current_imaging =['1']
	current_imaging.clear()
	current_im =['1']
	current_im.clear()
	current_i =['1']
	current_i.clear()
	
	current_image = current_images_food.query.all()
	for counting in current_image:
		counting = counting.curee
		counting = counting[1:]
		current_imaging.append(counting)
		
	for num in current_imaging:
			num1 = num[32:]
			current_i.append(num1) 
	for num1 in current_i:
		current_im.append(url_for('static',filename='images/alimantation_food/' + num1)) 

	return render_template("french/alimentation_foodfre.html", current_im=current_im, title=title)

@gibapp.route("/alimentation/Poules")
def poules():

	title="Poules"

	current_imaging =['1']
	current_imaging.clear()
	current_im =['1']
	current_im.clear()
	current_i =['1']
	current_i.clear()
	
	current_image = current_images_shop.query.all()
	for counting in current_image:
		counting = counting.curee
		counting = counting[1:]
		current_imaging.append(counting)
		
	for num in current_imaging:
			num1 = num[32:]
			current_i.append(num1) 
	for num1 in current_i:
		current_im.append(url_for('static',filename='images/alimentation_shop/' + num1)) 
	return render_template("french/alimentation_shopfre.html", current_im=current_im, title=title)

@gibapp.route("/alimentation/Autres")
def autres():

	title="Autres"
	current_imaging =['1']
	current_imaging.clear()
	current_im =['1']
	current_im.clear()
	current_i =['1']
	current_i.clear()
	
	current_image = current_images_others.query.all()
	for counting in current_image:
		counting = counting.curee
		counting = counting[1:]
		current_imaging.append(counting)
		
	for num in current_imaging:
			num1 = num[21:]
			current_i.append(num1) 
	for num1 in current_i:
		current_im.append(url_for('static',filename='images/others/' + num1)) 
	return render_template("french/othersfre.html", current_im=current_im, title=title)


@gibapp.route("/alimentation/Nourritures/burgers")
def burgersfre():
	return render_template("french/burgersfre.html")

@gibapp.route("/alimentation/Nourritures/cakes")
def cakesfre():
	return render_template("french/cakesfre.html")

@gibapp.route("/alimentation/Nourritures/chickens")
def chickensfre():
	return render_template("french/chickensfre.html")


@gibapp.route("/alimentation/Nourritures/Boissons")
def boissons():
	return render_template("french/drinksfre.html")

@gibapp.route("/alimentation/Nourritures/pizza")
def pizzafre():
	return render_template("french/pizzafre.html")

@gibapp.route("/alimentation/Nourritures/pasta")
def pastafre():
	return render_template("french/pastafre.html")

