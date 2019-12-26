from flask import render_template, url_for
from gibrun import gibapp
from models import *

@gibapp.route("/home")
def index():
	title = "Home"
	return render_template("english/index.html", title=title)


@gibapp.route("/about")
def about():
	title = "About Us"
	return render_template("english/about.html", title=title)

@gibapp.route("/contact")
def contact():
	title = "Contact Us"
	return render_template("english/contact.html", title=title)

@gibapp.route("/alimentation/food")
def food():

	title = "Food And Drinks"

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
			
	return render_template("english/alimentation_food.html", current_im=current_im, title=title)

@gibapp.route("/alimentation/shop")
def shop():

	title = "Hens and eggs"
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

	return render_template("english/alimentation_shop.html", current_im=current_im, title=title)

@gibapp.route("/alimentation/others")
def others():

	title = "Pampers shop"
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
	return render_template("english/others.html", current_im=current_im, title=title)


@gibapp.route("/alimentation/food/burgers")
def burgers():
	return render_template("english/burgers.html")

@gibapp.route("/alimentation/food/cakes")
def cakes():
	return render_template("english/cakes.html")

@gibapp.route("/alimentation/food/chickens")
def chickens():
	return render_template("english/chickens.html")


@gibapp.route("/alimentation/food/drinks")
def drinks():
	return render_template("english/drinks.html")

@gibapp.route("/alimentation/food/pizza")
def pizza():
	return render_template("english/pizza.html")

@gibapp.route("/alimentation/food/pasta")
def pasta():
	return render_template("english/pasta.html")



