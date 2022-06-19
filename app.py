from flask import Flask, render_template, request
from database import mycusor, mydb, sql_events, sql_student
from text import message, event_mail

app = Flask(__name__)





    

@app.route('/about/')
def about():
    return render_template("about.htm")



@app.route('/')
def index():
    return render_template("index.htm")


@app.route("/student", methods=['GET', 'POST'])
def student():
    if request.method == "POST":
        student_name = request.form["student_name"]
        student_address = request.form["student_address"]
        student_number = request.form["student_num"]
        student_city = request.form["student_city"]
        student_val = (student_name, student_address, student_number, student_city)
        mycusor.execute(sql_student,student_val)
        mydb.commit()
    return render_template("studentform.htm")

@app.route("/event", methods=['GET', 'POST'])
def event():
    if request.method == "POST":
        event_name = request.form['event_name']
        event_start = request.form['event_start']
        event_end = request.form['event_end']
        event_location = request.form['event_location']
        event_foodtypes = request.form['event_foodtypes']
        event_city = request.form['event_city']
        val = (event_start, event_end, event_foodtypes, event_name, event_city, event_location)
        val2 =[event_start, event_end, event_foodtypes, event_name, event_city, event_location]
        mycusor.execute(sql_events, val)
        mydb.commit()
        sql = f"SELECT phonenumber FROM student WHERE city = '{event_city}'"
        mycusor.execute(sql)

        
        myresult = mycusor.fetchall()
        rows=[i[0] for i in myresult]
        for r in rows:
            print(r)
            message(r,val)

        
        
        email_foodbank = f"SELECT email FROM foodbanks WHERE city LIKE '%{event_city}%'"
        mycusor.execute(email_foodbank)
        myresult = mycusor.fetchall()
        
        row=[j[0] for j in myresult]
        for each in row:
            print(each)
            print(each)
            event_mail(each,val2)




    return render_template("events_create.htm")



@app.route("/map")
def map():
    return render_template("map.htm")

@app.route("/home")
def home():
    return render_template("index.htm")


@app.route("/events_list")
def events_list():
    mycusor.execute("SELECT * FROM events ORDER BY name DESC")
    myresult = mycusor.fetchall()
    return render_template("events_list.htm", myresult=myresult)


    
if __name__ =="__main__":
    app.run(debug = True)

