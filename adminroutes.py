from flask import render_template, url_for, flash, redirect, request
import secrets
import os
from models import *
from gibrun import gibapp, bcrypt, db
from gibforms import RegisterForm, LoginForm, UpdateForm
from flask_login import login_user, current_user, login_required, logout_user




save_id = 0
save_picture_file =""



@gibapp.route("/admin/dashboard")
@login_required
def admin():
	return render_template("admin_pages/adminpage.html")

def save_picture_food(form_picture):
	randon_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = randon_hex + f_ext
	picture_path = os.path.join(gibapp.root_path, 'static/images/alimantation_food', picture_fn)
	form_picture.save(picture_path)
	return picture_fn
def save_picture_shop(form_picture):
	randon_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = randon_hex + f_ext
	picture_path = os.path.join(gibapp.root_path, 'static/images/alimentation_shop', picture_fn)
	form_picture.save(picture_path)
	return picture_fn
def save_picture_others(form_picture):
	randon_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = randon_hex + f_ext
	picture_path = os.path.join(gibapp.root_path, 'static/images/others', picture_fn)
	form_picture.save(picture_path)
	return picture_fn



@gibapp.route("/admin/alimentation/food")
def admin_food():

	current_imaging =['1']
	current_imaging.clear()
	curee =['1']
	curee.clear()
	current_i =['1']
	current_i.clear()
	
	current_image = current_images_food_check.query.all()
	for counting in current_image:
		counting = counting.curee
		counting = counting[1:]
		current_imaging.append(counting)
		
	for num in current_imaging:
			num1 = num[32:]
			current_i.append(num1) 
	for num1 in current_i:
		curee.append(url_for('static',filename='images/alimantation_food/' + num1)) 





	#if save_id != 0:
	#	current_image[save_id-1] = save_picture_file
	
	#for num in current_i:
	#	curees = url_for('static',filename='images/alimantation_food/' + num)
	#	imagecheck = current_images_food.query.filter_by(curee=curees).first()
	#	imagecheck2 = current_images_food_check.query.filter_by(curee=curees).first()
	#	if not imagecheck:
	#		imagesave = current_images_food(curee=curees)
	#		db.session.add(imagesave)
	#		db.session.commit()

		#if not imagecheck2:
		#	imagesave = current_images_food_check(curee=curees)
		#	db.session.add(imagesave)
		#	db.session.commit()

	#for num in current_image:
	#	curee.append(url_for('static',filename='images/alimantation_food/' + num))
	

	return render_template("admin_pages/alimentation_food_admin.html", curee=curee)

@gibapp.route("/admin/alimentation/shop")
def admin_shop():

	current_imaging =['1']
	current_imaging.clear()
	curee =['1']
	curee.clear()
	current_i =['1']
	current_i.clear()
	
	current_image = current_images_shop_check.query.all()
	for counting in current_image:
		counting = counting.curee
		counting = counting[1:]
		current_imaging.append(counting)
		
	for num in current_imaging:
			num1 = num[32:]
			current_i.append(num1) 
	for num1 in current_i:
		curee.append(url_for('static',filename='images/alimentation_shop/' + num1)) 

	return render_template("admin_pages/alimentation_shop_admin.html", curee=curee)


@gibapp.route("/admin/alimentation/others")
def admin_others():
	
	current_imaging =['1']
	current_imaging.clear()
	curee =['1']
	curee.clear()
	current_i =['1']
	current_i.clear()
	
	current_image = current_images_others_check.query.all()
	for counting in current_image:
		counting = counting.curee
		counting = counting[1:]
		current_imaging.append(counting)
		
	for num in current_imaging:
			num1 = num[21:]
			current_i.append(num1) 
	for num1 in current_i:
		curee.append(url_for('static',filename='images/others/' + num1)) 
	

	return render_template("admin_pages/others_admin.html", curee=curee)


@gibapp.route("/admin/create_account", methods=["POST", "GET"])
def create_account():
	form = RegisterForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		user = Admins(email = form.email.data, username=form.username.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash("Admin Account created for you, you can now control your website")
		return redirect(url_for('login'))
	return render_template("admin_pages/create_account.html", form=form)

@gibapp.route("/admin", methods=["POST", "GET"])
@gibapp.route("/admin/login", methods=["POST", "GET"])
def login():

	if current_user.is_authenticated:
		return redirect(url_for('admin'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Admins.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next_page')
			return redirect(next_page) if next_page else redirect(url_for('admin'))
			flash("Login successfully", "success")
		else:
			flash("Login unsuccesfully, check username and password")

	return render_template("admin_pages/login.html", form=form)


@gibapp.route("/admin/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))


@gibapp.route("/admin/update/food/<int:id>", methods=["GET","POST"])
def update_food(id):
	form = UpdateForm()
	picture_id = current_images_food_check.query.get_or_404(id)
	if form.validate_on_submit():
		if form.imagefile.data:
			picture_file = save_picture_food(form.imagefile.data)
			picture_id.curee = "/static/images/alimantation_food/" + picture_file
		db.session.commit()
		
		return redirect(url_for('admin_food'))

	return render_template("admin_pages/updatepicture.html", form=form, picture_id=picture_id)

@gibapp.route("/admin/update/shop/<int:id>", methods=["GET","POST"])
def update_shop(id):
	form = UpdateForm()
	picture_id = current_images_shop_check.query.get_or_404(id)
	if form.validate_on_submit():
		if form.imagefile.data:
			picture_file = save_picture_shop(form.imagefile.data)
			picture_id.curee = "/static/images/alimentation_shop/" + picture_file
		db.session.commit()
		
		return redirect(url_for('admin_shop'))

	return render_template("admin_pages/updatepicture2.html", form=form, picture_id=picture_id )

@gibapp.route("/admin/update/others/<int:id>", methods=["GET","POST"])
def update_others(id):
	form = UpdateForm()
	picture_id = current_images_others_check.query.get_or_404(id)
	if form.validate_on_submit():
		if form.imagefile.data:
			picture_file = save_picture_others(form.imagefile.data)
			picture_id.curee = "/static/images/others/" + picture_file
		db.session.commit()
		
		return redirect(url_for('admin_others'))

	return render_template("admin_pages/updatepicture3.html", form=form, picture_id=picture_id )



@gibapp.route("/admin/post/food/<int:id>")
def post_food(id):
	picture_id = current_images_food_check.query.filter_by(id=id).first()
	picture_id_post = current_images_food.query.filter_by(id=id).first()

	if picture_id and picture_id_post:
			
		picture_id_post.curee = picture_id.curee
		db.session.commit()
		
		return redirect(url_for('admin_food'))


@gibapp.route("/admin/post/shop/<int:id>")
def post_shop(id):
	picture_id = current_images_shop_check.query.filter_by(id=id).first()
	picture_id_post = current_images_shop.query.filter_by(id=id).first()

	if picture_id and picture_id_post:
			
		picture_id_post.curee = picture_id.curee
		db.session.commit()
		
		return redirect(url_for('admin_shop'))

@gibapp.route("/admin/post/others/<int:id>")
def post_others(id):
	picture_id = current_images_others_check.query.filter_by(id=id).first()
	picture_id_post = current_images_others.query.filter_by(id=id).first()

	if picture_id and picture_id_post:
			
		picture_id_post.curee = picture_id.curee
		db.session.commit()
		
		return redirect(url_for('admin_others'))



