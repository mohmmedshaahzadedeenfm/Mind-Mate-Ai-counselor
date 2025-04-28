from flask import *
from database import *
import uuid

admin=Blueprint("admin",__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template("admin_home.html")

@admin.route('/admin_manage_meditation',methods=['post','get'])
def admin_manage_meditation():
	data={}
	if 'submitttt'in request.form:
		Fname=request.form['fname']
		Lname=request.form['lname']
		Uname=request.form['Username']
		Passwd=request.form['Password']
		Place=request.form['place']
		Phone=request.form['phone']
		Email=request.form['email']
		Qualification=request.form['Qualification']
		certificate=request.files['certificate']
		path="static/uploads/"+str(uuid.uuid4())+certificate.filename
		certificate.save(path)
		hh="select * from login where Username='%s'"%(Uname)
		dd=select(hh)
		if dd:
			flash("Username already exist.........!")
			return redirect(url_for('admin.admin_manage_meditation'))
		else:
			ss="insert into login values(null,'%s','%s','meditation')"%(Uname,Passwd)
			fd=insert(ss)
			fg="insert into meditation values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(fd,Fname,Lname,Place,Phone,Email,Qualification,path)
			insert(fg)
			flash("Registration Success.........!")
			return redirect(url_for('admin.admin_manage_meditation'))
	if 'action' in request.args:
		action=request.args['action']
		Medication_id=request.args['Medication_id']
		Login_id=request.args['Login_id']
	else:
		action=None
	if action=='delete':
		gh="delete from login where Login_id='%s'"%(Login_id)
		delete(gh)
		fg="delete from meditation where Medication_id='%s'"%(Medication_id)
		delete(fg)
		flash("Deleted.........!")
		return redirect(url_for('admin.admin_manage_meditation'))
	if action=='update':
		ff="select  * from meditation where Medication_id='%s'"%(Medication_id)
		data['up']=select(ff)
	if 'submit' in request.form:
		Fname=request.form['fname']
		Lname=request.form['lname']
		Place=request.form['place']
		Phone=request.form['phone']
		Email=request.form['email']
		Qualification=request.form['Qualification']	
		certificate=request.files['certificate']
		path="static/uploads/"+str(uuid.uuid4())+certificate.filename
		certificate.save(path)	
		jk="update meditation set Fname='%s',Lname='%s',Place='%s',Phone='%s',Email='%s',Qualification='%s',image='%s' where Medication_id='%s'"%(Fname,Lname,Place,Phone,Email,Qualification,path,Medication_id)
		update(jk)
		flash("Updated.........!")
		return redirect(url_for('admin.admin_manage_meditation'))
	hjk="select * from meditation inner join login using(Login_id)"
	data['view']=select(hjk)
	return render_template("admin_manage_meditation.html",data=data)



@admin.route('/admin_manage_psychiatrist',methods=['post','get'])
def admin_manage_psychiatrist():
	data={}
	if 'submitttt' in request.form:
		fname=request.form['first_name']
		lname=request.form['last_name']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		Qualification=request.form['qualification']
		certificate=request.files['certificate']
		path="static/uploads/"+str(uuid.uuid4())+certificate.filename
		certificate.save(path)	
		Uname=request.form['Username']
		Passwd=request.form['Password']	
		hh="select * from login where Username='%s'"%(Uname)
		dd=select(hh)
		if dd:
			flash("Username already exist.........!")
			return redirect(url_for('admin.admin_manage_meditation'))
		else:
			ss="insert into login values(null,'%s','%s','psychiatrist')"%(Uname,Passwd)
			fd=insert(ss)	
			hj="insert into psychiatrist values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(fd,fname,lname,place,phone,email,Qualification,path)
			insert(hj)
			flash("Registration Success.........!")
			return redirect(url_for('admin.admin_manage_psychiatrist'))
	if 'action' in request.args:
		action=request.args['action']
		psychiatrist_id=request.args['psychiatrist_id']
		Login_id=request.args['Login_id']
	else:
		action=None
	if action=='delete':
		gh="delete from login where Login_id='%s'"%(Login_id)
		delete(gh)
		fg="delete from psychiatrist where psychiatrist_id='%s'"%(psychiatrist_id)
		delete(fg)
		flash("Deleted.........!")
		return redirect(url_for('admin.admin_manage_psychiatrist'))
	if action=='update':
		ff="select  * from psychiatrist where psychiatrist_id='%s'"%(psychiatrist_id)
		data['up']=select(ff)
	if 'submit' in request.form:
		fname=request.form['first_name']
		lname=request.form['last_name']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		Qualification=request.form['qualification']	
		certificate=request.files['certificate']
		path="static/uploads/"+str(uuid.uuid4())+certificate.filename
		certificate.save(path)		
		jk="update psychiatrist set Fname='%s',Lname='%s',Place='%s',Phone='%s',Email='%s',Qualification='%s',image='%s' where psychiatrist_id='%s'"%(fname,lname,place,phone,email,Qualification,path,psychiatrist_id)
		update(jk)
		flash("Updated.........!")
		return redirect(url_for('admin.admin_manage_psychiatrist'))
	hjk="select * from psychiatrist inner join login using(Login_id)"
	data['view']=select(hjk)
	return render_template("admin_manage_psychiatrist.html",data=data)

@admin.route('/admin_view_feedback')
def admin_view_feedback():
	data={}
	gh="select * from feedback inner join user using(Login_id) order by Feedback_id desc"
	data['view']=select(gh)
	return render_template('admin_view_feedback.html',data=data)


@admin.route('/admin_view_user_and_block_unblock')
def admin_view_user_and_block_unblock():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		Login_id=request.args['Login_id']
	else:
		action=None
	if action=='block':
		hj="update login set Usertype='block' where Login_id='%s'"%(Login_id)
		update(hj)
		flash("Blocked..........!")
		return redirect(url_for('admin.admin_view_user_and_block_unblock'))
	if action=='unblock':
		hj="update login set Usertype='user' where Login_id='%s'"%(Login_id)
		update(hj)
		flash("Unblocked..........!")
		return redirect(url_for('admin.admin_view_user_and_block_unblock'))
	jk="select * from user inner join login using(Login_id)"
	data['view']=select(jk)
	return render_template('admin_view_user_and_block_unblock.html',data=data)


@admin.route('/admin_view_request_from_user')
def admin_view_request_from_user():
	data={}
	g="SELECT * FROM appointment"
	data['viewappointment']=select(g)
	# if 'action' in request.args:
	# 	action=request.args['action']
	# 	Request_id=request.args['Request_id']
	# else:
	# 	action=None
	# if action=='viewappointment':
	# 	g="SELECT * FROM `appointment`WHERE `Request_id`='%s'"%(Request_id)
	# 	data['viewappointment']=select(g)
	# 	if data['viewappointment']:
	# 		pass
	# 	else:
	# 		flash("Did not take the appointment......!")
	# 		return redirect(url_for('admin.admin_view_request_from_user'))
	gh="SELECT *,concat(`meditation`.`Fname`,' ',`meditation`.`Lname`) as medi,CONCAT(`user`.`Fname`,' ',`user`.`Lname`) AS userr FROM `request`INNER JOIN `meditation`ON `request`.`Appointment_for`=`meditation`.`Login_id`INNER JOIN `login`USING(`Login_id`) INNER JOIN `user`USING(`User_id`) UNION SELECT *,concat(`psychiatrist`.`Fname`,' ',`psychiatrist`.`Lname`) as medi,CONCAT(`user`.`Fname`,' ',`user`.`Lname`) AS userr  FROM `request`INNER JOIN `psychiatrist`ON `request`.`Appointment_for`=`psychiatrist`.`Login_id`INNER JOIN `login`USING(`Login_id`) INNER JOIN `user`USING(`User_id`)"
	data['view_req']=select(gh)
	return render_template('admin_view_request_from_user.html',data=data)


@admin.route('/admin_view_result')
def admin_view_result():
	Request_id=request.args['Request_id']
	num=""
	if session.get('Login_id') is None:
		return redirect(url_for('public.login'))
	else:
		data = {}
		# id = request.args['id']
		qry = "SELECT * FROM result INNER JOIN user USING (User_id) WHERE  User_id='%s'" % (Request_id)
		res = select(qry)

		re1 = float(res[0]['r1'])
		re2 = float(res[0]['r2'])
		re3 = float(res[0]['r3'])
		re4 = float(res[0]['r4'])

		print("re1:", re1, "\nre2:", re2, "\nre3:", re3, "\nre4:", re4)


		if re1 == 4 and re4 == 3 and re2 == 1 and re3 == 0:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 3 and re2 == 0 and re3 == 1:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 3 and re2 == 0 and re3 == 0:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 2 and re2 == 1 and re3 == 1:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 2 and re2 == 1 and re3 == 0:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 2 and re2 == 0 and re3 == 1:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 2 and re2 == 0 and re3 == 0:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 1 and re2 == 1 and re3 == 1:
			v = 'Severe Depression'
			num='1'
		elif re1 == 4 and re4 == 1 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='2'
		elif re1 == 4 and re4 == 1 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='2'
		elif re1 == 4 and re4 == 1 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='2'
		elif re1 == 4 and re4 == 0 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='2'
		elif re1 == 4 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'No Depression'
			num='3'
		elif re1 == 4 and re4 == 4 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='2'
		elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'No Depression'
			num='3'
		elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'No Depression'
			num='3'
		elif re1 == 4 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'No Depression'
			num='3'    
		elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 1:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression' 
			num='3'   
		elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 1:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Severe Depression'
			num='1'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Severe Depression'
			num='1'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Severe Depression'
			num='1'
		elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 1:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 1:
			v = 'Moderately Severe Depression'
			num='4'
		elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 1:
			v = 'Mild Depression'
			num='5'
		elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 0:
			v = 'Mild Depression'
			num='5'
		elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 1:
			v = 'Mild Depression'
			num='5'
		elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
			num='3'
		elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 1:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 1:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 1:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 1:
			v = 'Mild Depression'
		elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 1:
			v = 'Mild Depression'
		elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 1:
			v = 'Mild Depression'
		elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 1:
			v = 'No Depression'
		elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 0:
			v = 'No Depression'
		elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 1:
			v = 'No Depression'
		elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 0:
			v = 'No Depression'
		elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 1:
			v = 'No Depression'
		elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 0:
			v = 'No Depression' 
		elif re1 == 4 and re4 == 0 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
			v = 'Moderate Depression'
		elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
			v = 'Mild Depression'
		elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
			v = 'Mild Depression'
		elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
			v = 'Mild Depression'

		elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 1:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 0:
			v = 'Moderately Severe Depression'
		elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 0:
			v = 'Severe Depression'
		elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 1:
			v = 'Severe Depression'
		elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 0:
			v = 'Severe Depression'
		else:
			v = 'No Depression'                                
		data['view'] = res
		return render_template("admin_view_result.html",data=data,v=v,num=num)








@admin.route('/admin_manage_question',methods=['get','post'])
def admin_manage_question():
	data={}
	if 'submit' in request.form:
		noofoption=request.form['noofoption']
		answersel=request.form['answersel']
		quest=request.form['quest']
		roundtype=request.form['roundtype']
		tn=request.form['tn']
		if tn=="option":
			paths="NA"
			tt="option"
		else:
			paths="NA"
			tt="text"
		q="insert into question values(null,'%s','%s','Dyscalculia','%s','%s',curdate(),'%s','pending')" %(quest,paths,roundtype,tn,tt)
		qid=insert(q)
		j=1
		for i in range(0,int(noofoption)):
			
			if tn=="option":
				path=request.form['text'+str(j)]
				typesss="option"
			else:
				path=request.form['text'+str(j)]
				typesss="text"
			if int(j)==int(answersel):
				status="Yes"
			else:
				status="No"
			q="insert into answer values(null,'%s','%s','%s','%s')" %(qid,path,status,typesss)
			print(q)
			insert(q)
			j=j+1 
		return redirect(url_for('admin.admin_manage_question'))
	v="select * from answer inner join question using(question_id) where answer.status='Yes'"
	res=select(v)
	data['view']=res
	return render_template("admin_manage_question.html",data=data)


@admin.route('/p')
def p():
	return render_template('p.html')

@admin.route('/c')
def c():
	return render_template('c.html')

@admin.route('/m')
def m():
	return render_template('m.html')

@admin.route('/mo')
def mo():
	return render_template('mo.html')