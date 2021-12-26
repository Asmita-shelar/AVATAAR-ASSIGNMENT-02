from flask import Flask, render_template, request

import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_user():
    return render_template('user.html')


'''add user events'''
@app.route('/enterevent')
def new_event():
    return render_template('user_event.html')    
    


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            gen = request.form['gen']
            em = request.form['em']

            with sql.connect("database.db") as con:
                cur=con.cursor()

                cur.execute("INSERT INTO user (name,gender,email) VALUES(?,?,?)",(nm,gen,em))
                
                con.commit()

            message="Record added successfully!"

        except:
            con.rollback()
            message="error in insert operation!"


        finally:
            return render_template("result.html", msg=message)
            con.close()


@app.route('/addevent',methods=['POST','GET'])
def addevent():
    if request.method == 'POST':
        try:
            uid=request.form['uid']
            evn=request.form['evn']
            oc=request.form['oc']
            sd=request.form['sd']
            ed=request.form['ed']
            

            with sql.connect("database.db") as conn:
                curr=conn.cursor()
                curr.execute("INSERT INTO UserEvents (uid,EventName,occurence,StartDate,EndDate) VALUES(?,?,?,?,?)",(uid,evn,oc,sd,ed))
                conn.commit()

            message="RECORD ADDED SUCCESSFULLY !"
        
        except:
            conn.rollback()
            message="ERROR IN INSERTING !"

        finally:
            return render_template("result.html",msg=message)
            conn.close()



@app.route('/list')
def list():
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from  User")
    rows=cur.fetchall()
    return render_template("list.html",rows=rows)




if __name__ == '__main__':
    app.run(debug=True)