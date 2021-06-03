from flask import Flask, render_template,request, session , redirect , url_for , g,flash
import model
import uuid
import os
app = Flask(__name__)
app.secret_key = 'mohsin5432'

username = ''
user = model.check_users()
admin = ''


@app.route('/',methods = ['GET'])
def home():
    if 'username' in session:
        g.user = session['username']
        name = model.name(g.user)
        intro = model.intro(g.user)
        picname = model.pic(g.user)
        teamsrank = model.teamranks()
        return render_template('portfolio.html' ,teamsrank = teamsrank, name = name , intro = intro,picname = picname)
    return render_template('insta.html')


@app.route('/addpic',methods = ['GET','POST'])
def addpic():
    if 'username' in session:
        if request.method == 'GET':
            return render_template('addpic.html')
        else:
            g.user = session['username']
            oldpic = model.pic(g.user)
            profilepic = request.files["profilepic"]
            picname = str(uuid.uuid1())+ os.path.splitext(profilepic.filename)[1]
            profilepic.save(os.path.join('static/profilepics',picname))
            username = session['username']
            message = model.addpic(username,picname)
            if oldpic:
                os.remove(os.path.join('static/profilepics',oldpic))
            return render_template('addpic.html')
    return render_template('insta.html')


@app.route('/addintro',methods = ['GET','POST'])
def intro():
    user = session['username']
    name = model.name(user)
    txt = model.intro(user)
    if request.method == 'GET':
        return render_template('addintro.html',name = name , txt = txt)
    else:
        fname = request.form['fname']
        intro = request.form['intro']
        message = model.addintro(user,fname,intro)
        return render_template('addintro.html',message = message,name = name, txt = txt)


@app.route('/login',methods = ['GET' ,'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser = request.form['username']
        pwd = model.pass_check(areyouuser)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    return render_template('insta.html')

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/delintro')

def delintro():
    user = session['username']
    name = model.name(user)
    txt = model.intro(user)
    message = model.delintro(user,txt)
    return render_template('portfolio.html' ,name = name , delmessage = message)


@app.route('/signup',methods = ['GET','POST'])

def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        email = request.form["email"]
        fname = request.form["fname"]
        username = request.form["username"]
        password = request.form["password"]
        message = model.signup(email,fname,username,password)
        return render_template('signup.html',message = message)

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')

def logout():
    session.pop('username' , None)
    return redirect(url_for('home'))

@app.route('/aboutus',methods = ['GET'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/terms',methods = ['GET'])
def terms():
    return render_template('terms.html')

@app.route('/admin',methods = ['GET','POST'])
def admin():
    if 'admin' in session:
        return redirect(url_for('adminpanel'))
    else:
        if request.method == 'GET':
            return render_template('adminlog.html')
        else:
            admin = request.form['user']
            password = request.form['password']
            db_pass = model.admpass_check(admin)
            if password == db_pass:
                session["admin"] = admin
                return redirect(url_for('adminpanel'))
            else:
                return redirect(url_for('admin'))


@app.route('/adminpanel',methods = ['GET','POST'])
def adminpanel():
    if 'admin' in session:
        tusers = model.totalusers()
        tusers24 = model.totalusers24()
        tteams = model.totalteams()
        return render_template('admin.html', tnu = tusers ,tnu24 = tusers24 ,tteams = tteams )
    return redirect(url_for('admin'))



@app.route('/data',methods = ['GET'])
def data():
    if 'admin' in session:
        tusers = model.totalusers()
        tusers24 = model.totalusers24()
        totalusers = model.totalusersrecord()
        tteams = model.totalteams()
        return render_template('data.html',tteams = tteams,totalusers = totalusers,tnu = tusers ,tnu24 = tusers24, txt = "ALL USERS DATA" , Serial = "Serial" , USERNAME = "USERNAME" , FULLNAME="FULL NAME", EMAIL = "EMAIL" , delete = "DELETE USER" , time = "TIME/DATE")
    else:
        return redirect(url_for('admin'))

@app.route('/data24',methods = ['GET'])
def data24():
    if 'admin' in session:
        tusers = model.totalusers()
        tusers24 = model.totalusers24()
        totalusers = model.totalusersrecord24()
        tteams = model.totalteams()
        return render_template('data24.html',tteams = tteams,totalusers = totalusers,tnu = tusers ,tnu24 = tusers24, txt = "USERS SIGNED UP IN PAST 24 HOUR" , Serial = "Serial" , USERNAME = "USERNAME" , FULLNAME="FULL NAME", EMAIL = "EMAIL" , delete = "DELETE USER" , time = "TIME/DATE" )
    else:
        return redirect(url_for('admin'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    model.deluser(id_data)
    return redirect(url_for('data'))


@app.route('/edit/<string:id_data>', methods = ['GET','POST'])
def edit(id_data):
    if 'admin' in session:
        if request.method == 'GET':
            teamname = id_data
            wins = model.wins(id_data)
            draws = model.draws(id_data)
            defeat = model.defeat(id_data)
            return render_template('edit.html',teamname=teamname,wins=wins,draws=draws,defeat=defeat)
        else:
            teamname = request.form["teamname"]
            wins = request.form["wins"]
            defeat = request.form["defeat"]
            draws = request.form["draws"]
            message = model.updateteam(id_data,teamname,wins,defeat,draws)
            return redirect(url_for('teams'))
    else:
        return redirect(url_for('teams'))



@app.route('/teams',methods = ['GET'])
def teams():
    if 'admin' in session:
        tusers = model.totalusers()
        tusers24 = model.totalusers24()
        totalteams = model.teamranks()
        tteams = model.totalteams()
        return render_template('teams.html',tteams = tteams,tnu = tusers ,tnu24 = tusers24, totalteams = totalteams)
    else:
        teamname = request.form["email"]
        fname = request.form["fname"]
        username = request.form["username"]
        password = request.form["password"]
        return redirect(url_for('admin'))

@app.route('/addteams',methods = ['GET','POST'])
def addteams():
    if 'admin' in session:
        if request.method == 'GET':
            return render_template('addteams.html')
        else:
            teamname = request.form["teamname"]
            wins = request.form["wins"]
            defeat = request.form["defeat"]
            draws = request.form["draws"]
            message = model.addteam(teamname,wins,defeat,draws)
            return redirect(url_for('teams'))
    else:
        return redirect(url_for('admin'))


@app.route('/tdelete/<string:id_data>', methods = ['GET'])
def tdelete(id_data):
    flash("Record Has Been Deleted Successfully")
    model.delteam(id_data)
    return redirect(url_for('teams'))

@app.route('/logoutadm')
def logoutadm():
    session.pop('admin' , None)
    return redirect(url_for('admin'))



if __name__ == '__main__':
    app.run(debug = False)
