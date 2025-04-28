from flask import *
from database import *
psychiatrist=Blueprint("psychiatrist",__name__)



@psychiatrist.route('/psychiatrist_home')
def psychiatrist_home():
    return render_template('psychiatrist_home.html')


@psychiatrist.route('/psychiatrist_view_appointment',methods=['GET','POST'])
def psychiatrist_view_appointment():
    data={}
    kj="SELECT * FROM `user` INNER JOIN appointment USING(User_id)"
    data['view_appointment']=select(kj)
    return render_template('psychiatrist_view_appointment.html',data=data)


@psychiatrist.route('/psychiatrist_view_user_details',methods=['GET','POST'])
def psychiatrist_view_user_details():
    data={}
    user_id=request.args['user_id']
    g="select * from user where User_id='%s'"%(user_id)
    data['viewuser']=select(g)
    return render_template('psychiatrist_view_user_details.html',data=data)


@psychiatrist.route('/psychiatrist_view_payment_details',methods=['GET','POST'])
def psychiatrist_view_payment_details():
    data={}
    Appointment_id=request.args['Appointment_id']
    g="select * from payment where Appointment_id='%s'"%(Appointment_id)
    data['view_payment']=select(g)
    return render_template('psychiatrist_view_payment_details.html',data=data)


@psychiatrist.route('/psychiatrist_chat_with_user',methods=['GET','POST'])
def psychiatrist_chat_with_user():
    data={}
    Login_id=request.args['Login_id']
    if 'submit' in request.form:
        message=request.form['message']
        gg="insert into message values(null,0,'%s','%s','%s',curdate())"%(session['Login_id'],Login_id,message)
        insert(gg)
        return redirect(url_for('psychiatrist.psychiatrist_chat_with_user',Login_id=Login_id))
    dd="SELECT * FROM message INNER JOIN login ON `login`.`Login_id`=`message`.`sender_id` where `sender_id`='%s' AND `receiver_id`='%s'  or (`sender_id`='%s' AND `receiver_id`='%s')"%(Login_id,session['Login_id'],session['Login_id'],Login_id)
    data['view']=select(dd)
    return render_template('psychiatrist_chat_with_user.html',data=data)


@psychiatrist.route('/psychiatrist_feedback',methods=['GET','POST'])
def psychiatrist_feedback():
    data={}
    # if 'submit' in request.form:
    #     feedback=request.form['feedback']
    #     kl="insert into feedback values(null,'%s','%s',curdate())"%(session['Login_id'],feedback)
    #     insert(kl)
    #     flash("Success.........!")
    #     return redirect(url_for('psychiatrist.psychiatrist_feedback'))
    mn="select * from feedback order by Feedback_id desc"
    data['view']=select(mn)
    return render_template('psychiatrist_feedback.html',data=data)

@psychiatrist.route('/psychiatrist_view_request',methods=['GET','POST'])
def psychiatrist_view_request():
    data={}
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        kk="SELECT *,user.Fname AS userr FROM `request`INNER JOIN `psychiatrist`ON `request`.`Appointment_for`=`psychiatrist`.`Login_id` INNER JOIN `user` ON `request`.`User_id`=`user`.`User_id` WHERE `psychiatrist`.`Login_id`='%s' "%(session['Login_id'])
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
        return redirect(url_for('psychiatrist.psychiatrist_view_request'))
    if action=='reject':
        r="update request set Status='rejected' where Request_id='%s'"%(Request_id)
        update(r)
        return redirect(url_for('psychiatrist.psychiatrist_view_request'))
    return render_template('psychiatrist_view_request.html',data=data)

@psychiatrist.route('/psychiatrist_add_conditions',methods=['GET','POST'])
def psychiatrist_add_conditions():
    data={}
    Appointment_id=request.args['Appointment_id']
    if 'submit' in request.form:
        Details=request.form['Details']
        g="insert into updations values(null,'%s','%s',curdate())"%(Appointment_id,Details)
        insert(g)
        flash("Added...............!")
        return redirect(url_for('psychiatrist.psychiatrist_add_conditions',Appointment_id=Appointment_id))
    if 'action' in request.args:
        action=request.args['action']
        Updation_id=request.args['Updation_id']
    else:
        action=None
    if action=='delete':
        f="delete from updations where Updation_id='%s'"%(Updation_id)
        delete(f)
        flash("Deleted...............!")
        return redirect(url_for('psychiatrist.psychiatrist_add_conditions',Appointment_id=Appointment_id))
    if action=='update':
        gh="select * from updations where Updation_id='%s'"%(Updation_id)
        data['up']=select(gh)
    if 'update' in request.form:
        Details=request.form['Details']
        df="update updations set Details='%s',Date=curdate() where Updation_id='%s'"%(Details,Updation_id)
        update(df)
        flash("Updated...............!")
        return redirect(url_for('psychiatrist.psychiatrist_add_conditions',Appointment_id=Appointment_id))
    d="select * from updations where Appointment_id='%s'"%(Appointment_id)
    data['view']=select(d)
    return render_template('psychiatrist_add_conditions.html',data=data)


@psychiatrist.route('/psychiatrist_treetment_suggested',methods=['GET','POST'])
def psychiatrist_treetment_suggested():
    data={}
    Appointment_id=request.args['Appointment_id']
    if 'submit' in request.form:
        Treatment=request.form['Treatment']
        Details=request.form['Details']
        g="insert into suggestedtreatment values(null,'%s',(select Appointment_for from request inner join appointment using(Request_id) where Appointment_id='%s'),'%s',curdate(),'%s')"%(Appointment_id,Appointment_id,Treatment,Details)
        insert(g)
        flash("Added...............!")
        return redirect(url_for('psychiatrist.psychiatrist_treetment_suggested',Appointment_id=Appointment_id))
    if 'action' in request.args:
        action=request.args['action']
        suggestedtreatment_id=request.args['suggestedtreatment_id']
    else:
        action=None
    if action=='delete':
        f="delete from suggestedtreatment where suggestedtreatment_id='%s'"%(suggestedtreatment_id)
        delete(f)
        flash("Deleted...............!")
        return redirect(url_for('psychiatrist.psychiatrist_treetment_suggested',Appointment_id=Appointment_id))
    if action=='update':
        gh=" SELECT * FROM suggestedtreatment INNER JOIN appointment ON(suggestedtreatment.provided_id=appointment.appointment_id) WHERE suggestedtreatment_id='%s'"%(suggestedtreatment_id)
        data['up']=select(gh)
    if 'update' in request.form:
        Treatment=request.form['Treatment']
        Details=request.form['Details']
        df="update suggestedtreatment set Treatment='%s', Details='%s',Date=curdate() where suggestedtreatment_id='%s'"%(Treatment,Details,suggestedtreatment_id)
        update(df)
        flash("Updated...............!")
        return redirect(url_for('psychiatrist.psychiatrist_treetment_suggested',Appointment_id=Appointment_id))
    d=" SELECT *,suggestedtreatment.Date AS sdate FROM suggestedtreatment INNER JOIN appointment ON(suggestedtreatment.provided_id=appointment.appointment_id) WHERE Appointment_id='%s'"%(Appointment_id)
    data['view']=select(d)
    return render_template('psychiatrist_treetment_suggested.html',data=data)