import sqlite3


def pass_check(username):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    passs = cursor.fetchone()
    if passs is None:
        return "invalid"
        connection.commit()
        cursor.close()
        connection.close()
    else:
        password = passs and passs[0]
    connection.commit()
    cursor.close()
    connection.close()
    return password
def name(username):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT fname FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    name = cursor.fetchone()
    fname = name and name[0]
    connection.commit()
    cursor.close()
    connection.close()
    return fname

def intro(username):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT intro FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    info = cursor.fetchone()
    if info is None:
        intro = ""
    else:
        intro = info[0]
    connection.commit()
    cursor.close()
    connection.close()
    return intro

def addintro(username,fname,intro):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" UPDATE users SET fname = '{fname}' , intro = '{intro}' WHERE username = '{username}';""".format(fname = fname , intro = intro , username = username))
    connection.commit()
    cursor.close()
    connection.close()
    return 'you have successfully updated profile'

def delintro(username,intro):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" UPDATE users SET intro = NULL WHERE username = '{username}';""".format(intro = intro , username = username))
    connection.commit()
    cursor.close()
    connection.close()
    return 'you have successfully deleted intro'





def signup(email,fname,username,password):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM users WHERE username='{username}';""".format(username = username))
    exist = cursor.fetchone()
    if exist is None:
        cursor.execute("""INSERT INTO users(email,fname,username,password,date)VALUES('{email}','{fname}','{username}','{password}',(CURRENT_TIMESTAMP));""".format(email = email , password = password , fname = fname , username = username))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return('User Already existed')

    return 'you have successfully signed up'

def check_users():
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT username from users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []
    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    return users

def totalusers():
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT COUNT(pk)
                    FROM users;""")
    totalusers = cursor.fetchone()
    tusers =totalusers and totalusers[0]

    connection.commit()
    cursor.close()
    connection.close()
    return tusers


def totalusersrecord():
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                    FROM users;""")
    totalusersdata = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    return totalusersdata



def totalteams():
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT COUNT(pk)
                    FROM teams;""")
    totalusers = cursor.fetchone()
    tusers =totalusers and totalusers[0]

    connection.commit()
    cursor.close()
    connection.close()
    return tusers


def teamranks():
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                    FROM teams
                    ORDER BY score DESC;""")
    teams = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    return teams


def totalusers24():
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT  COUNT(pk)
                    FROM    users
                    WHERE   date >= datetime('now','-1 day');""")
    totalusers24 = cursor.fetchone()
    tusers24 =totalusers24 and totalusers24[0]

    connection.commit()
    cursor.close()
    connection.close()
    return tusers24


def totalusersrecord24():
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT *
                    FROM users
                    WHERE   date >= datetime('now','-1 day');""")
    totalusersdata24 = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()
    return totalusersdata24


def deluser(username):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" DELETE FROM users WHERE username = '{username}';""".format(username = username))
    connection.commit()
    cursor.close()
    connection.close()


def admpass_check(username):
    connection = sqlite3.connect('admin.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM admin WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    passs = cursor.fetchone()
    password = passs and passs[0]
    connection.commit()
    cursor.close()
    connection.close()
    return password



def addteam(teamname,wins,defeat,draws):
    score = (int(wins)*3)+(int(draws)*1)
    tmatches = int(wins)+int(defeat)+int(draws)
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT teamname FROM teams WHERE teamname='{teamname}';""".format(teamname = teamname))
    exist = cursor.fetchone()
    if exist is None:
        cursor.execute("""INSERT INTO teams(teamname,tmatches,wins,draws,defeat,score,date)VALUES('{teamname}','{tmatches}','{wins}','{draws}','{defeat}','{score}',(CURRENT_TIMESTAMP));""".format(teamname = teamname,wins=wins,tmatches=tmatches,draws = draws,defeat=defeat,score=score))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return('TEAM Already existed')
    return 'you have successfully ADDED TEAM'

def delteam(teamname):
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" DELETE FROM teams WHERE teamname = '{teamname}';""".format(teamname = id_data))
    connection.commit()
    cursor.close()
    connection.close()


def wins(teamname):
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT wins FROM teams WHERE teamname='{teamname}' ORDER BY pk DESC;""".format(teamname = teamname))
    name = cursor.fetchone()
    fname = name and name[0]
    connection.commit()
    cursor.close()
    connection.close()
    return fname

def defeat(teamname):
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT defeat FROM teams WHERE teamname='{teamname}' ORDER BY pk DESC;""".format(teamname = teamname))
    name = cursor.fetchone()
    fname = name and name[0]
    connection.commit()
    cursor.close()
    connection.close()
    return fname

def draws(teamname):
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT draws FROM teams WHERE teamname='{teamname}' ORDER BY pk DESC;""".format(teamname = teamname))
    name = cursor.fetchone()
    fname = name and name[0]
    connection.commit()
    cursor.close()
    connection.close()
    return fname

def updateteam(id_data,teamname,wins,defeat,draws):
    score = (int(wins)*3)+(int(draws)*1)
    tmatches = int(wins)+int(defeat)+int(draws)
    connection = sqlite3.connect('teams.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" UPDATE teams SET teamname = '{teamname}',tmatches='{tmatches}',wins='{wins}',draws='{draws}',defeat = '{defeat}',score='{score}'  WHERE teamname = '{teamname}';""".format(teamname = teamname,wins=wins,tmatches=tmatches,draws = draws,defeat=defeat,score=score))
    connection.commit()
    cursor.close()
    connection.close()

def addpic(username,picname):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" UPDATE users SET picname = '{picname}' WHERE username = '{username}';""".format(username = username,picname=picname))
    connection.commit()
    cursor.close()
    connection.close()
    return 'you have successfully uploaded picture'


def pic(username):
    connection = sqlite3.connect('insta.db' , check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT picname FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    name = cursor.fetchone()
    fname = name and name[0]
    connection.commit()
    cursor.close()
    connection.close()
    return fname
