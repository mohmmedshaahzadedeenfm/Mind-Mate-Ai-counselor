from flask import *
from database import *
from core import *
from models import Model
from depression_detection_tweets import DepressionDetection
from TweetModel import process_message
import os

user=Blueprint("user",__name__)


@user.route('/user_home')
def user_home():
	return render_template("user_home.html")

@user.route("/take_test_ins")
def take_test_ins():
    # Request_id=request.args['Request_id']
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template('take_test_ins.html')


@user.route("/take_test")
def take_test():
    # Request_id=request.args['Request_id']
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template("index1.html")


@user.route('/predict', methods=["POST","GET"])
def predict():
    # Request_id=request.args['Request_id']
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        q1 = int(request.form['a1'])
        q2 = int(request.form['a2'])
        q3 = int(request.form['a3'])
        q4 = int(request.form['a4'])
        q5 = int(request.form['a5'])
        q6 = int(request.form['a6'])
        q7 = int(request.form['a7'])
        q8 = int(request.form['a8'])
        q9 = int(request.form['a9'])
        q10 = int(request.form['a10'])

        values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
        model = Model()
        classifier = model.svm_classifier()
        prediction = classifier.predict([values])
        
        if prediction[0] == 0:
                session['r1']=prediction[0]
                return redirect(url_for('user.sentiment')) 
                
        if prediction[0] == 1:
                session['r1']=prediction[0] 
                return redirect(url_for('user.sentiment'))
        
        if prediction[0] == 2:
                session['r1']=prediction[0] 
                return redirect(url_for('user.sentiment'))
        
        if prediction[0] == 3:
                session['r1']=prediction[0] 
                return redirect(url_for('user.sentiment'))
        
        if prediction[0] == 4:
                session['r1']=prediction[0] 
                return redirect(url_for('user.sentiment'))


@user.route("/sentiment")
def sentiment():
    # Request_id=request.args['Request_id']
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template("sentiment.html")



@user.route("/predictSentiment",  methods=['get', 'post'])
def predictSentiment():
    # Request_id=request.args['Request_id']
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        message = request.form['form10']
        pm = process_message(message)
        result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
        session['r2']=result
        return redirect(url_for("user.voice_change"))
   




@user.route('/voice_change',methods=['get','post'])
def voice_change():
    data={}
    # Request_id=request.args['Request_id']
    if 'submit' in request.form:
        message=request.form['sen']
        print("****************************** :::")
        print(message)
        pm = process_message(message)
        result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
        session['r3']=result
        return redirect(url_for('user.camera'))
    
    return render_template('upload_voice.html',data=data)


@user.route("/camera")
def camera():
    # Request_id=request.args['Request_id']
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        from em import camclick
        q=camclick()
        session['r4']=q
        return redirect(url_for('user.add_result'))


@user.route('/add_result', methods=['get', 'post'])
def add_result():
    # Request_id = request.args['Request_id']
    if session.get('Login_id') is None:
        return redirect(url_for('public.login'))
    else:
        result1 = session.get('r1', 0) or 0
        result2 = session.get('r2', 0) or 0
        result3 = session.get('r3', 0) or 0
        result4 = session.get('r4', 0) or 0

        print("result1 : ", result1)
        print("result2 : ", result2)
        print("result3 : ", result3)
        print("result4 : ", result4)

        if result4 == 'neutral':
            result4 = 0
        if result4 == 'happy':
            result4 = 0
        if result4 == 'surprise':
            result4 = 0
        if result4 == 'sad':
            result4 = 3
        if result4 == 'fear':
            result4 = 4
        if result4 == 'disgust':
            result4 = 4
        if result4 == 'angry':
            result4 = 2

        if result4:
            # gg = "update request set Status='attended' where Request_id='%s'" % (Request_id)
            # update(gg)
            q = "INSERT INTO result VALUES(null,'%s','%s','%s','%s','%s',now())" % (result1, result2, result3, result4, session['User_id'])
            insert(q)

        # Ensure all results are integers before summing
        res = int(result1) + int(result2) + int(result3) + int(result4)

        if res >= 8:
            # i = "insert into request(Request_id, User_id, Appointment_for, Details, Date, Status) VALUES (null, '%s',  '3','System Detected Issue', curdate(), 'pending')" % (session['User_id'])
            # req = insert(i)
            flash("You Need to Consult Psychiatrist, Request Has Been Sent")
            i = "insert into appointment VALUES (null, '%s', 'System Detected Issue', curdate(), 1000, curdate(), curtime(), 'pending')" % (session['User_id'])
            insert(i)
            return redirect(url_for('user.test_completed'))
        else:
            return redirect(url_for('user.chatbot'))
    return redirect(url_for('user.test_completed'))


@user.route("/test_completed")
def test_completed():
    if session.get('Login_id') is None:
        return redirect (url_for('public.login'))
    else:
        return render_template('test_completed.html')

@user.route('/user_view_result', methods=['get', 'post'])
def user_view_result():
    # Request_id=request.args['Request_id']
    num=""
    if session.get('Login_id') is None:
        return redirect(url_for('public.login'))
    else:
        data = {}
        # id = request.args['id']
        qry = "SELECT * FROM result INNER JOIN user USING (User_id) WHERE User_id='%s'" % (session['User_id'])
        res = select(qry)
        
        re1 = float(res[0]['r1'])
        re2 = float(res[0]['r2'])
        re3 = float(res[0]['r3'])
        re4 = float(res[0]['r4'])
        
        print("re1:", re1, "\nre2:", re2, "\nre3:", re3, "\nre4:", re4)
       
        # if re1 == 0.0 and re2 == 0.0 and re3 == 0.0 and re4 == 0.0:
        #     v = 'No Depression'
        # elif re1 == 0.0 and re2 == 0.0 and re3 != 0.0 and re4 >= 2.0:
        #     v = 'No Depression'
        # elif re1 == 1.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Mild Depression'
        # elif re1 == 2.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Mild Depression'
        # elif re1 == 3.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderate Depression'
        # elif re1 == 4.0 and re2 == 0.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderate Depression'
        # elif re1 == 0.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Mild Depression'
        # elif re1 == 1.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderate Depression'
        # elif re1 == 2.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Moderately Severe Depression'
        # elif re1 == 3.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Severe Depression'
        # elif re1 == 4.0 and re2 == 1.0 and re3 >= 2.0 and 0.0 <= re4 <= 4.0:
        #     v = 'Severe Depression'
        # else:
        #     v = 'No Depression'
        
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
        return render_template('user_view_result.html',data=data,v=v,num=num)


# @user.route("/user_view_request")
# def user_view_request():

#     data={}
#     if session.get('Login_id') is None:
#         return redirect (url_for('public.login'))
#     else:
#         kk="SELECT * FROM `request`INNER JOIN `meditation`ON `request`.`Appointment_for`=`meditation`.`Login_id`INNER JOIN `login`USING(`Login_id`) where User_id='%s' UNION SELECT * FROM `request`INNER JOIN `psychiatrist`ON `request`.`Appointment_for`=`psychiatrist`.`Login_id`INNER JOIN `login`USING(`Login_id`)where User_id='%s'  "%(session['User_id'],session['User_id'])
#         data['view']=select(kk)
#         return render_template('user_view_request.html',data=data)
    


# @user.route("/chatbo")
# def chatbo():
#     return redirect(url_for('chatbot.chatbot'))



#------------------Chat-Bot-------------------------------

from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai
import sys

# Load environment variables and add debugging
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Debug print to verify API key loading
print(f"API Key loaded: {'Yes' if GOOGLE_API_KEY else 'No'}", file=sys.stderr)

try:
    if not GOOGLE_API_KEY:
        raise ValueError("No API key found. Please set GOOGLE_API_KEY environment variable")
    
    # Configure Gemini API with error handling
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Verify configuration by attempting to list models
    models = genai.list_models()
    print("Successfully configured Gemini API", file=sys.stderr)
    
except Exception as e:
    print(f"Error configuring Gemini API: {str(e)}", file=sys.stderr)
    raise

# List available models to determine the correct model name
def list_available_models():
    try:
        models = genai.list_models()
        return [model.name for model in models]
    except Exception as e:
        print(f"Error listing models: {str(e)}")
        return []

# Initialize the Gemini model - use the most recent version
# Common model names are 'gemini-1.5-pro' or 'gemini-1.0-pro'
model = genai.GenerativeModel('gemini-1.5-pro')  # Updated model name

def generate_gemini_response(prompt):
    try:
        # Counselor context
        counselor_context = """
        You are a supportive and empathetic counseling chatbot. Your role is to:
        - Listen and provide emotional support
        - Offer general guidance for daily life challenges
        - Share coping strategies and wellness tips
        - Help users explore their thoughts and feelings
        - Provide general self-improvement suggestions
        Remember to be compassionate, non-judgmental, and always encourage seeking professional help for serious concerns.
        Maintain a warm and supportive tone while keeping responses helpful and constructive.
        """
        
        full_prompt = f"{counselor_context}\n\nUser message: {prompt}"
        
        # Generate response with updated configuration
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.8,
                top_k=40,
                max_output_tokens=1024,
            )
        )
        
        if not response.text:
            return "I apologize, but I couldn't generate a proper response. Please try rephrasing your question."
            
        return response.text.strip()
        
    except Exception as e:
        print(f"Error in generate_gemini_response: {str(e)}")  # For debugging
        return f"I apologize, but I couldn't process your request: {str(e)}"

@user.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@user.route('/available_models', methods=['GET'])
def available_models():
    """Endpoint to check which models are available"""
    models = list_available_models()
    return jsonify({'available_models': models})

@user.route('/chat', methods=['POST'])
def chat():
    try:
        body = request.get_json()
        user_message = body.get('message', '').strip()

        if not user_message:
            return jsonify({
                'response': 'Please provide a message.'
            })

        # Process counseling-related keywords to better direct the response
        counseling_keywords = ['feel', 'stress', 'anxiety', 'worried', 'sad', 'depression', 'help', 'support']
        
        # Add specific context if counseling-related keywords are found
        if any(keyword in user_message.lower() for keyword in counseling_keywords):
            user_message = f"As a supportive counselor, please help with: {user_message}"

        response = generate_gemini_response(user_message)
        return jsonify({
            'response': response
        })

    except Exception as e:
        print(f"Error in chat route: {str(e)}")  # For debugging
        return jsonify({
            'response': f'I apologize, but something went wrong: {str(e)}'
        })

# Optional: Add helpful counseling-related routes
@user.route('/wellness_tips')
def wellness_tips():
    tips = generate_gemini_response("What are the top 5 daily wellness and self-care tips?")
    return jsonify({'tips': tips})

@user.route('/coping_strategies')
def coping_strategies():
    strategies = generate_gemini_response("What are some healthy coping strategies for managing stress and anxiety?")
    return jsonify({'strategies': strategies})



@user.route('/user_chatwithpsychiartist',methods=['GET','POST'])
def user_chatwithpsychiartist():
    data={}
    Login_id=request.args['Login_id']
    if 'submit' in request.form:
        message=request.form['message']
        gg="insert into message values(null,0,'%s','%s','%s',curdate())"%(session['Login_id'],Login_id,message)
        insert(gg)
        return redirect(url_for('user.user_chatwithpsychiartist',Login_id=Login_id))
    dd="SELECT * FROM message INNER JOIN login ON `login`.`Login_id`=`message`.`sender_id` where `sender_id`='%s' AND `receiver_id`='%s' or (`sender_id`='%s' AND `receiver_id`='%s')"%(Login_id,session['Login_id'],session['Login_id'],Login_id)
    data['view']=select(dd)
    return render_template('user_chatwithpsychiartist.html',data=data)


@user.route('/user_view_appointment',methods=['GET','POST'])
def user_view_appointment():
    data={}
    kj="SELECT * FROM `psychiatrist`"
    data['view_appointment']=select(kj)
    return render_template('user_view_appointment.html',data=data)



@user.route('/user_sendfeedback',methods=['GET','POST'])
def user_sendfeedback():
    data={}
    if 'submit' in request.form:
        feedback=request.form['feedback']
        kl="insert into feedback values(null,'%s','%s',curdate())"%(session['Login_id'],feedback)
        insert(kl)
        flash("Success.........!")
        return redirect(url_for('user.user_sendfeedback'))
    mn="select * from feedback where Login_id='%s'"%(session['Login_id'])
    data['view']=select(mn)
    return render_template('user_sendfeedback.html',data=data)
