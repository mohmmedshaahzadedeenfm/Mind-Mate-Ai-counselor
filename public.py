from flask import *
from database import *

public=Blueprint("public",__name__)

@public.route('/')
def public_home():
	return render_template("public_home.html")

	
@public.route('/login',methods=['post','get'])
def login():
	if 'Login' in request.form:
		Uname=request.form['name']
		Passwd=request.form['password']
		check="select * from login where Username='%s'and Password='%s'"%(Uname,Passwd)
		fd=select(check)
		print("lkkklkkkklkkjkkkjkjkjk")
		if fd:
			session['Login_id']=fd[0]['Login_id']
			
			if fd[0]['Usertype']=='admin':
				flash("Login Success.........!")
				return redirect(url_for('admin.admin_home'))
				
			elif fd[0]['Usertype']=='meditation':
				ssd="select * from meditation where Login_id='%s'"%(session['Login_id'])
				ff=select(ssd)
				if ff:
					session['Medication_id']=ff[0]['Medication_id']
				flash("Login Success.........!")
				return redirect(url_for('meditation.meditation_home'))
			elif fd[0]['Usertype']=='psychiatrist':
				psy="select * from psychiatrist where Login_id='%s'"%(session['Login_id'])
				res=select(psy)
				if res:
					session['psychiatrist_id']=res[0]['psychiatrist_id']
				flash("Login Success.............")
				return redirect(url_for('psychiatrist.psychiatrist_home'))
			if fd[0]['Usertype']=='user':	
				print("llllllllllllllll")
				uy="select * from user where Login_id='%s'"%(session['Login_id'])
				re=select(uy)
				if re:
					session['User_id']=re[0]['User_id']
				flash("Login success")
				return redirect(url_for('user.user_home'))
	return render_template("login.html")



@public.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        Fname = request.form['Fname']
        Lname = request.form['Lname']
        Place = request.form['Place']
        Phone = request.form['Phone']
        Email = request.form['Email']
        Username = request.form['Username']
        Password = request.form['Password']

        # Insert the data into the database
        query = """
            INSERT INTO login 
            VALUES (null,'%s', '%s', 'user')
        """ % (Username, Password)
        lid=insert(query)

        query = """
            INSERT INTO user
            VALUES (null,'%s', '%s', '%s', '%s', '%s', '%s')
        """ % (lid,Fname, Lname, Place, Phone, Email)
        insert(query)

        flash("Registration successful!")
        return redirect(url_for('public.login'))  # Redirect to login page after registration

    return render_template('user_registeration.html')


@public.route('/p')
def p():
	return render_template('p.html')

@public.route('/c')
def c():
	return render_template('c.html')

@public.route('/m')
def m():
	return render_template('m.html')

@public.route('/mo')
def mo():
	return render_template('mo.html')