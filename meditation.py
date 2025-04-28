from flask import *
from database import *


meditation=Blueprint("meditation",__name__)


@meditation.route('/meditation_home')
def meditation_home():
	return render_template("meditation_home.html")


@meditation.route('/meditation_send_feedback',methods=['post','get'])
def meditation_send_feedback():
	data={}
	if 'submit' in request.form:
		feedback=request.form['feedback']
		kl="insert into feedback values(null,'%s','%s',curdate())"%(session['Login_id'],feedback)
		insert(kl)
		flash("Success.........!")
		return redirect(url_for('meditation.meditation_send_feedback'))
	mn="select * from feedback where Login_id='%s'"%(session['Login_id'])
	data['view']=select(mn)
	return render_template('meditation_send_feedback.html',data=data)


@meditation.route('/meditation_view_appointment',methods=['post','get'])
def meditation_view_appointment():
	data={}
	kj="SELECT *,`appointment`.`Details`AS ffff,`appointment`.`Status`AS vvvvv FROM `appointment`INNER JOIN `request`USING(`Request_id`) INNER JOIN `meditation`ON `meditation`.`Login_id`=`request`.`Appointment_for`INNER JOIN `login`USING(`Login_id`)INNER JOIN `user`USING(`User_id`) where Medication_id='%s' AND `appointment`.`Status`='paid' "%(session['Medication_id'])
	data['view_appointment']=select(kj)
	return render_template('meditation_view_appointment.html',data=data)


@meditation.route('/meditation_view_user_details',methods=['post','get'])
def meditation_view_user_details():
	data={}
	user_id=request.args['user_id']
	g="select * from user where User_id='%s'"%(user_id)
	data['viewuser']=select(g)
	return render_template('meditation_view_user_details.html',data=data)


@meditation.route('/meditation_manage_motivation',methods=['post','get'])
def meditation_manage_motivation():
	data={}
	Appointment_id=request.args['Appointment_id']
	if 'submit' in request.form:
		classs=request.form['classs']
		details=request.form['details']
		g="insert into motivation values(null,'%s','%s','%s',curdate(),'pending')"%(Appointment_id,classs,details)
		insert(g)
		flash("Added...............!")
		return redirect(url_for('meditation.meditation_manage_motivation',Appointment_id=Appointment_id))
	if 'action' in request.args:
		action=request.args['action']
		Motivation_id=request.args['Motivation_id']
	else:
		action=None
	if action=='delete':
		f="delete from motivation where Motivation_id='%s'"%(Motivation_id)
		delete(f)
		flash("Deleted...............!")
		return redirect(url_for('meditation.meditation_manage_motivation',Appointment_id=Appointment_id))
	if action=='update':
		gh="select * from motivation where Motivation_id='%s'"%(Motivation_id)
		data['up']=select(gh)
	if 'update' in request.form:
		classs=request.form['classs']
		details=request.form['details']
		df="update motivation set Class='%s',Details='%s',Date=curdate() where Motivation_id='%s'"%(classs,details,Motivation_id)
		update(df)
		flash("Updated...............!")
		return redirect(url_for('meditation.meditation_manage_motivation',Appointment_id=Appointment_id))
	d="select * from motivation where Appointment_id='%s'"%(Appointment_id)
	data['view']=select(d)
	return render_template('meditation_manage_motivation.html',data=data,Appointment_id=Appointment_id)


@meditation.route('/meditaion_view_payment_details',methods=['post','get'])
def meditaion_view_payment_details():
	data={}
	Appointment_id=request.args['Appointment_id']
	g="select * from payment where Appointment_id='%s'"%(Appointment_id)
	data['view_payment']=select(g)
	return render_template('meditaion_view_payment_details.html',data=data,Appointment_id=Appointment_id)


@meditation.route('/meditation_add_awearness_programme',methods=['post','get'])
def meditation_add_awearness_programme():
	data={}
	if 'submit' in request.form:
		awareness=request.form['awareness']
		details=request.form['details']
		date=request.form['date']
		link=request.form['link']
		h="insert into awearness values(null,'%s','%s','%s','%s','%s')"%(session['Medication_id'],awareness,details,link,date)
		insert(h)
		flash("Added...............!")
		return redirect(url_for('meditation.meditation_add_awearness_programme'))
	if 'action' in request.args:
		action=request.args['action']
		awearness_id=request.args['awearness_id']
	else:
		action=None
	if action=='delete':
		hj="delete from awearness where awearness_id='%s'"%(awearness_id)
		delete(hj)
		flash("Deleted...............!")
		return redirect(url_for('meditation.meditation_add_awearness_programme'))
	k="select * from awearness where Medication_id='%s'"%(session['Medication_id'])
	data['view']=select(k)
	return render_template('meditation_add_awearness_programme.html',data=data)	



@meditation.route('/meditation_chat_with_user',methods=['get','post'])
def meditation_chat_with_user():
	data={}
	Login_id=request.args['Login_id']
	Appointment_id=request.args['Appointment_id']
	if 'submit' in request.form:
		message=request.form['message']
		gg="insert into message values(null,'%s','%s','%s','%s',curdate())"%(Appointment_id,session['Login_id'],Login_id,message)
		insert(gg)
		return redirect(url_for('meditation.meditation_chat_with_user',Login_id=Login_id,Appointment_id=Appointment_id))
	dd="SELECT * FROM message INNER JOIN login ON `login`.`Login_id`=`message`.`sender_id`INNER JOIN `appointment`USING(`Appointment_id`) where `sender_id`='%s' AND `receiver_id`='%s' and Appointment_id='%s' or (`sender_id`='%s' AND `receiver_id`='%s' and Appointment_id='%s')"%(Login_id,session['Login_id'],Appointment_id,session['Login_id'],Login_id,Appointment_id)
	data['view']=select(dd)
	return render_template('meditation_chat_with_user.html',Login_id=Login_id,data=data,Appointment_id=Appointment_id)


@meditation.route('/p')
def p():
	return render_template('p.html')

@meditation.route('/c')
def c():
	return render_template('c.html')

@meditation.route('/m')
def m():
	return render_template('m.html')

@meditation.route('/mo')
def mo():
	return render_template('mo.html')


@meditation.route('/meditation_view_request',methods=['GET','POST'])
def meditation_view_request():
	data={}
	if session.get('Login_id') is None:
		return redirect (url_for('public.login'))
	else:
		kk="SELECT *,user.Fname AS userr FROM `request`INNER JOIN `meditation`ON `request`.`Appointment_for`=`meditation`.`Login_id` INNER JOIN `user` ON `request`.`User_id`=`user`.`User_id` WHERE `meditation`.`Login_id`='%s' "%(session['Login_id'])
		data['view']=select(kk)
		print(kk)
	if 'action'in request.args:
		action=request.args['action']
		Request_id=request.args['Request_id']
	else:
		action=None
	if action=='accept':
		s="update request set Status='accepted' where Request_id='%s'"%(Request_id)
		update(s)
		return redirect(url_for('meditation.meditation_view_request'))
	if action=='reject':
		r="update request set Status='rejected' where Request_id='%s'"%(Request_id)
		update(r)
		return redirect(url_for('meditation.meditation_view_request'))
	return render_template('meditation_view_request.html',data=data)