from flask import *
from database import *
from core import *
from test import checkans
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
apiss=Blueprint("apiss",__name__)

@apiss.route('/login',methods=['post'])
def login():
    username = request.form['username']
    password = request.form['password']
    q="SELECT * from login where Username='%s' and Password='%s'" % (username,password)
    res = select(q)
    if res :
        return jsonify(status="ok",lid=res[0]["Login_id"],ut=res[0]["Usertype"])
    else:
        return jsonify(status="no")

@apiss.route('/sign_up',methods=['post'])
def sign_up():
	firstname=request.form['firstname']
	lastname=request.form['lastname']
	email=request.form['email']
	phone=request.form['phone']
	place=request.form['place']
	uname=request.form['uname']
	pwd=request.form['password']
	jk="insert into login values(null,'%s','%s','user')"%(uname,pwd)
	gh=insert(jk)
	op="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(gh,firstname,lastname,place,phone,email)
	res=insert(op)
	if res:
		return jsonify(status="ok")
	else:
		return jsonify(status="failed")

@apiss.route('/psy_feedback',methods=['post'])
def psy_feedback():
	feedback=request.form['feedback']
	lid=request.form['lid']
	gf="insert into feedback values(null,'%s','%s',curdate())"%(lid,feedback)
	res=insert(gf)
	if res:
		return jsonify(status="ok")
	else:
		return jsonify(status="failed")

@apiss.route('/user_feedback',methods=['post'])
def user_feedback():
	feedback=request.form['feedback']
	lid=request.form['lid']
	gf="insert into feedback values(null,'%s','%s',curdate())"%(lid,feedback)
	res=insert(gf)
	if res:
		return jsonify(status="ok")
	else:
		return jsonify(status="failed")


@apiss.route('/view_feedback',methods=['post'])
def view_feedback():
	data={}
	lid=request.form['lid']
	hj="select * from feedback where Login_id='%s'"%(lid)
	res=select(hj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/view_meditation',methods=['post'])
def view_meditation():
	data={}
	hj="select * from meditation "
	res=select(hj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/view_psychiatrist',methods=['post'])
def view_psychiatrist():
	data={}
	hj="select * from psychiatrist "
	res=select(hj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/user_sendrequest',methods=['post'])
def user_sendrequest():
	data={}
	lid=request.form['lid']
	details=request.form['details']
	log_ids=request.form['log_ids']
	hj="insert into request values(null,(select User_id from user where Login_id='%s'),'%s','%s',curdate(),'pending')"%(lid,log_ids,details)
	res=insert(hj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/user_viewrequest',methods=['post'])
def user_viewrequest():
	data={}
	lid=request.form['lid']
	kk="SELECT * FROM `request`INNER JOIN `meditation`ON `request`.`Appointment_for`=`meditation`.`Login_id`INNER JOIN `login`USING(`Login_id`) where User_id=(select User_id from user where Login_id='%s') UNION SELECT * FROM `request`INNER JOIN `psychiatrist`ON `request`.`Appointment_for`=`psychiatrist`.`Login_id`INNER JOIN `login`USING(`Login_id`)where User_id=(select User_id from user where Login_id='%s')"%(lid,lid)
	res=select(kk)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")





@apiss.route('/user_send_appoinment',methods=['post'])
def user_send_appoinment():
	details=request.form['details']
	appo_date=request.form['appo_date']
	appo_time=request.form['time']
	req_idd=request.form['req_idd']
	hk="select * from appointment where Appointmentdate='%s' and Appointmenttime='%s'"%(appo_date,appo_time)
	reee=select(hk)
	if reee:
		return jsonify(status="failed")
	else:
		hh="insert into appointment values(null,'%s','%s',curdate(),'1000','%s','%s','pending')"%(req_idd,details,appo_date,appo_time)
		res=insert(hh)
		if res:
			return jsonify(status="ok",data=res)
		else:
			return jsonify(status="failed")


@apiss.route('/user_view_appointment',methods=['post'])
def user_view_appointment():
	data={}
	lid=request.args['login_id']
	reqe_id=request.args['req_idd']
	kj="SELECT *,`appointment`.`Details`AS ffff,`appointment`.`Status`AS vvvvv FROM `appointment`INNER JOIN `request`USING(`Request_id`) INNER JOIN `meditation`ON `meditation`.`Login_id`=`request`.`Appointment_for`INNER JOIN `login`USING(`Login_id`) WHERE User_id=(SELECT User_id FROM USER WHERE Login_id='%s') AND appointment.Request_id='%s' UNION SELECT *,`appointment`.`Details`AS ffff,`appointment`.`Status`AS vvvvv FROM `appointment`INNER JOIN `request`USING(`Request_id`) INNER JOIN `psychiatrist`ON `psychiatrist`.`Login_id`=`request`.`Appointment_for`INNER JOIN `login`USING(`Login_id`) WHERE User_id=(SELECT User_id FROM USER WHERE Login_id='%s') AND appointment.Request_id='%s'"%(lid,reqe_id,lid,reqe_id)
	res=select(kj)
	print(kj,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")	


@apiss.route('/user_payment',methods=['post'])
def user_payment():
	appoint_idd=request.form['appoint_idd']
	amount=request.form['amount']
	km="update appointment set Status='paid' where Appointment_id='%s'"%(appoint_idd)
	update(km)
	pl="insert into payment values(null,'%s','%s',curdate())"%(appoint_idd,amount)
	res=insert(pl)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")	



@apiss.route('/psychiatrist_view_appointment',methods=['post'])
def psychiatrist_view_appointment():
	data={}
	lid=request.form['lid']
	kj="SELECT *,`appointment`.`Details`AS ffff,`appointment`.`Status`AS vvvvv FROM `appointment`INNER JOIN `request`USING(`Request_id`) INNER JOIN `user`USING (`User_id`)INNER JOIN `login`USING(`Login_id`) WHERE `Appointment_for`='%s' AND `appointment`.`Status`='paid'"%(lid)
	res=select(kj)
	print(kj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")	

@apiss.route('/psychiatrist_view_user_details',methods=['post'])
def psychiatrist_view_user_details():
	data={}
	U_ids=request.form['U_ids']
	kj=" select * from user where User_id='%s' "%(U_ids)
	res=select(kj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")	


@apiss.route('/psychiatrist_update_condition',methods=['post'])
def psychiatrist_update_condition():
	data={}
	A_ids=request.form['A_ids']
	details=request.form['details']
	u="insert into updations values(null,'%s','%s',curdate())"%(A_ids,details)
	res=insert(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/psychiatrist_view_update_condition',methods=['post'])
def psychiatrist_view_update_condition():
	data={}
	A_ids=request.form['A_ids']
	kj=" select * from updations where Appointment_id='%s' "%(A_ids)
	res=select(kj)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")	


@apiss.route('/psychiatrist_add_treatment_suggestions',methods=['post'])
def psychiatrist_add_treatment_suggestions():
	data={}
	A_ids=request.form['A_ids']
	treat=request.form['treat']
	detail=request.form['detail']
	u="insert into suggestedtreatment values(null,'%s','appointment','%s',curdate(),'%s')"%(A_ids,treat,detail)
	res=insert(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/psychiatrist_view_treatment_suggestions',methods=['post'])
def psychiatrist_view_treatment_suggestions():
	data={}
	A_ids=request.form['A_ids']
	u="select * from  suggestedtreatment where provided_id='%s'"%(A_ids)
	res=select(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/psychiatrist_view_payment_details',methods=['post'])
def psychiatrist_view_payment_details():
	data={}
	A_ids=request.form['A_ids']
	u="select * from  payment where Appointment_id='%s'"%(A_ids)
	res=select(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/user_view_treatment_suggestions',methods=['post'])
def user_view_treatment_suggestions():
	data={}
	appoint_idd=request.form['appoint_idd']
	u="select * from  suggestedtreatment where provided_id='%s'"%(appoint_idd)
	res=select(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/user_view_awareness',methods=['post'])
def user_view_awareness():
	data={}
	u="select * from awearness inner join meditation using(Medication_id)"
	res=select(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/user_view_motivation',methods=['post'])
def user_view_motivation():
	appoint_idd=request.form['appoint_idd']
	d="select * from motivation where Appointment_id='%s'"%(appoint_idd)
	res=select(d)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/user_chat_view')
def user_chat_view():
	data={}
	appoint_idd=request.args['ap_id']
	lid=request.args['lid']
	login_ids=request.args['login_ids']
	d="SELECT * FROM message INNER JOIN login ON `login`.`Login_id`=`message`.`sender_id`INNER JOIN `appointment`USING(`Appointment_id`) where `sender_id`='%s' AND `receiver_id`='%s' and Appointment_id='%s' or (`sender_id`='%s' AND `receiver_id`='%s' and Appointment_id='%s')"%(login_ids,lid,appoint_idd,lid,login_ids,appoint_idd)
	res=select(d)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="view"
	return str(data)

@apiss.route('/user_chat')
def user_chat():
	data={}
	appoint_idd=request.args['ap_id']
	lid=request.args['lid']
	login_ids=request.args['login_ids']
	chat=request.args['chat']
	hj="insert into message values(null,'%s','%s','%s','%s',curdate())"%(appoint_idd,lid,login_ids,chat)
	res=insert(hj)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="done"
	return str(data)


@apiss.route('/notification',methods=['post'])
def notification():
	lid=request.form['lid']
	print(lid)
	u="SELECT * FROM `appointment`INNER JOIN `request`USING(`Request_id`) where User_id=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s')"%(lid)
	res=select(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")

@apiss.route('/user_view_question')
def user_view_question():
    data = {}
    
    lid = request.args.get('lid')

    gg = "select quest_id from chat where (sender_id='%s' or receiver_id='%s') and date = curdate()" % (lid, lid)
    yy = select(gg)

    if yy:
        d = "SELECT * FROM question WHERE question_id NOT IN (%s)" % ','.join(str(x['quest_id']) for x in yy)
        ress = select(d)
        if ress:
            jj = "insert into chat values(null,'%s','0','%s','%s',curdate())" % (
                ress[0]['question_id'], lid, ress[0]['question'])
            insert(jj)
        else:
            pass
            # hh = "SELECT * FROM `chat` WHERE `sender_id`='%s' AND `date`=CURDATE()" % (lid)
            # hjh = select(hh)
            # if hjh:
            #     Negative="SELECT SUM(`Mark_awarded`) AS Negative FROM `answers`WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') AND DATE=CURDATE() AND `status`='Negative'"%(lid)
            #     Negative=select(Negative)
            #     Positive="SELECT SUM(`Mark_awarded`) AS Positive FROM `answers`WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') AND DATE=CURDATE() AND `status`='Positive'"%(lid)
            #     Positive=select(Positive)
            #     Neutral="SELECT SUM(`Mark_awarded`) AS Neutral FROM `answers`WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') AND DATE=CURDATE() AND `status`='Neutral'"%(lid)
            #     Neutral=select(Neutral)
            #     hh = "SELECT SUM(`Mark_awarded`) AS summ FROM `answers`WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') and date=curdate()" % (lid)
            #     jj = select(hh)
            #     if jj:
            #         sum_mark_awarded = int(jj[0]['summ'])
            #         average_mark_awarded = (sum_mark_awarded / 100) * 100
            #         if average_mark_awarded > 80: 
            #             colarity = "Mild"
            #         elif average_mark_awarded > 40:
            #             colarity = "Moderate"
            #         else:
            #             colarity = "Severe"
            #     data['status'] = "ND"
            #     data['colarity'] = colarity
            #     data['Negative'] = Negative
            #     data['Positive'] = Positive
            #     data['Neutral'] =  Neutral
    else:
        d = "SELECT * FROM question "
        ress = select(d)
        jj = "insert into chat values(null,'%s','0','%s','%s',curdate())" % (ress[0]['question_id'] , lid, ress[0]['question'])
        insert(jj)
    d = "SELECT * FROM chat  where (`sender_id`='%s' or `receiver_id`='%s')  and `date`= curdate() ORDER BY `chat_id` "  % (lid,lid)
    res = select(d)
    if not ress:
        data['status'] = "ND"
        print("llllllllllllllllllllllllllllllll")
    elif res:
        print("lllllllgggggggggggggggggggggggggllllllllllllllllll")
        data['status'] = "success"
        data['data'] = res
        data['q_id'] = res[-1]['quest_id']
    else:
        data['status'] = "failed"

    data['method'] = "view"
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)



@apiss.route('/user_answer')
def user_answer():
	data={}
	lid=request.args['lid']
	message=request.args['chat']
	qid=request.args['qid']
	r_id=request.args['r_id']
	print(qid,"pppppppppppppppppppppppp")
	ff="insert into chat values(null,'%s','%s','0','%s',curdate())"%(qid,lid,message)
	res=insert(ff)
	

	ss="select * from answer where question_id='%s' and status='Yes' "%(qid)
	dddd=select(ss)

	sentiment_scores = sia.polarity_scores(message)

	if sentiment_scores['compound'] >= 0.05:
		colarity = 'Positive'

	elif sentiment_scores['compound'] <= -0.05:
		colarity = 'Negative'

	else:
		colarity = 'Neutral'



	mark=10
	sim = checkans(dddd[0]['answer'], message)
	omark = sim * mark
	q="insert into answers values(null,'%s',(SELECT `User_id` FROM `user`WHERE `Login_id`='%s'),'%s','%s',curdate(),'%s')"%(qid,lid,message,omark,colarity)
	insert(q)	


	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="done"
	return str(data)

@apiss.route('/user_view_test_result',methods=['post'])
def user_view_test_result():
	data={}

	lid=request.form['lid']
 
	# hh = "SELECT * FROM `chat` WHERE `sender_id`='%s' AND `date`=CURDATE()" % (lid)
	# hjh = select(hh)
	
	# if hjh:
		
		
	Negative="""SELECT IF(COUNT(`Answer_id`)=NULL, 0,COUNT(`Answer_id`)) AS Negative FROM
`answers`
WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') 
AND DATE=CURDATE() 
AND `status`='Negative'"""%(lid)
	print(Negative)
	Negative=select(Negative)


	Positive="""SELECT IF(COUNT(`Answer_id`)=NULL, 0,COUNT(`Answer_id`)) AS Positive FROM
`answers`
WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s')
AND DATE=CURDATE() 
AND `status`='Positive'"""%(lid)
	print(Positive)
	Positive=select(Positive)
	


	Neutral="""SELECT IF(COUNT(`Answer_id`)=NULL, 0,COUNT(`Answer_id`)) AS Neutral FROM
`answers`
WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') 
AND DATE=CURDATE() 
AND `status`='Neutral'"""%(lid)
	print(Neutral)
	Neutral=select(Neutral)
	
	
	hh = "SELECT SUM(`Mark_awarded`) AS summ FROM `answers`WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') and date=curdate()" % (lid)
	jj = select(hh)

	nn=Neutral[0]['Neutral']
	print("nuuuuuuuuuuuu",nn)
	po=Positive[0]['Positive']
	print("poooooooooooooooooo",po)
	ne=Negative[0]['Negative']
	print("neeeeeeeeeeeeee",ne)

	if jj:
		sum1 = int(jj[0]['summ']) if jj[0]['summ'] is not None else 0
		sum_mark_awarded = sum1
		num = str(sum_mark_awarded)


		print(num,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
		average_mark_awarded = (sum_mark_awarded / 100) * 100
		if average_mark_awarded > 80: 
			colarity = "No depression"
			hhh=" You have no depression "
		if average_mark_awarded > 60: 
			colarity = "Medium"
			hhh=" Make an appointment for psychiatrist "
		elif average_mark_awarded > 40:
			colarity = "Moderate"
			hhh=" Make an appointment for meditation "
		else:
			colarity = "Severe"
			hhh=" Immediately Move on to Doctor Consult "
	
	# Define the values

	# Compare the values
	if int(nn) > int(po) and int(nn) > int(ne):
		# highest_value = nn
		colarity = "Medium"
		hhh=" Make an appointment for meditation "
	elif int(po) > int(nn) and int(po) > int(ne):
		colarity = "No depression"
		hhh=" You have no depression "
	else:
		colarity = "Severe"
		hhh=" Make an appointment for psychiatrist "

	# Print the highest value
	print("The highest value is:", hhh)

	data['status'] = "ND"
		
	data['colarity'] = colarity
	data['Negative'] = Negative
	data['Positive'] = Positive
	data['Neutral'] =  Neutral

	# print("jjjjjj",Negative[0]['Negative'],Positive[0]['Positive'],Neutral[0]['Neutral'])

	# if hjh:
	return jsonify(status="ok",colarity=colarity,Negative=Negative[0]['Negative'],Positive=Positive[0]['Positive'],Neutral=Neutral[0]['Neutral'],hhh=hhh)
	# else:
	# 	return jsonify(status="failed")



@apiss.route('/user_view_journal',methods=['post'])
def user_view_journal():
	lid=request.form['lid']
	print(lid)
	u="SELECT * FROM `answers` WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') group by `date` "%(lid)
	res=select(u)
	if res:
		return jsonify(status="ok",data=res)
	else:
		return jsonify(status="failed")


@apiss.route('/user_view_result',methods=['post'])
def user_view_result():
	data={}

	lid=request.form['lid']
	date=request.form['date']
 
	hh = "SELECT * FROM `chat` WHERE `sender_id`='%s' AND `date`='%s'" % (lid,date)
	hjh = select(hh)
	
	if hjh:
		
		
		Negative="""SELECT IF(COUNT(`Answer_id`)=NULL, 0,COUNT(`Answer_id`)) AS Negative FROM
 `answers`
 WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') 
 AND DATE=CURDATE() 
 AND `status`='Negative'"""%(lid)
		print(Negative)
		Negative=select(Negative)


		Positive="""SELECT IF(COUNT(`Answer_id`)=NULL, 0,COUNT(`Answer_id`)) AS Positive FROM
 `answers`
 WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s')
 AND DATE=CURDATE() 
 AND `status`='Positive'"""%(lid)
		print(Positive)
		Positive=select(Positive)
		


		Neutral="""SELECT IF(COUNT(`Answer_id`)=NULL, 0,COUNT(`Answer_id`)) AS Neutral FROM
 `answers`
 WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') 
 AND DATE=CURDATE() 
 AND `status`='Neutral'"""%(lid)
		print(Neutral)
		Neutral=select(Neutral)
		
		
		hh = "SELECT SUM(`Mark_awarded`) AS summ FROM `answers`WHERE `User_id`=(SELECT `User_id` FROM `user`WHERE `Login_id`='%s') and date=curdate()" % (lid)
		jj = select(hh)

		nn=Neutral[0]['Neutral']
		print("nuuuuuuuuuuuu",nn)
		po=Positive[0]['Positive']
		print("poooooooooooooooooo",po)
		ne=Negative[0]['Negative']
		print("neeeeeeeeeeeeee",ne)

		if jj:
			sum_mark_awarded = int(jj[0]['summ'])
			print(sum_mark_awarded,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
			average_mark_awarded = (sum_mark_awarded / 100) * 100
			if average_mark_awarded > 80: 
				colarity = "No depression"
				hhh=" You have no depression "
			if average_mark_awarded > 60: 
				colarity = "Medium"
				hhh=" Make an appointment for psychiatrist "
			elif average_mark_awarded > 40:
				colarity = "Moderate"
				hhh=" Make an appointment for meditation "
			else:
				colarity = "Severe"
				hhh=" Immediately Move on to Doctor Consult "
		
		# Define the values

		# Compare the values
		if int(nn) > int(po) and int(nn) > int(ne):
			# highest_value = nn
			colarity = "Medium"
			hhh=" Make an appointment for meditation "
		elif int(po) > int(nn) and int(po) > int(ne):
			colarity = "No depression"
			hhh=" You have no depression "
		else:
			colarity = "Severe"
			hhh=" Make an appointment for psychiatrist "

		# Print the highest value
		print("The highest value is:", hhh)

	print("jjjjjj",Negative[0]['Negative'],Positive[0]['Positive'],Neutral[0]['Neutral'])

	if hjh:
		return jsonify(status="ok",colarity=colarity,Negative=Negative[0]['Negative'],Positive=Positive[0]['Positive'],Neutral=Neutral[0]['Neutral'],hhh=hhh)
	else:
		return jsonify(status="failed")