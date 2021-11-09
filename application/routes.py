from flask import render_template, request, redirect
from application import app, db
from application.forms import AddEmp, UpdateEmp
from application.models import Consultants

#Create a route decorator
@app.route('/')
def index():
    data = Consultants.query.all()
    return render_template("index.html", record=data)



@app.route('/editdata/<int:regno>', methods=['GET', 'POST'])
def edit(regno):
    form = UpdateEmp()
    emp = Consultants.query.filter_by(Regno=regno).first()
    if request.method == 'POST':
        emp.Name = form.name.data
        emp.Salary = form.salary.data
        emp.Dept = form.dept.data
        emp.Subject = form.subject.data
        emp.Marks = form.marks.data
        form.process()
        db.session.commit()
        return redirect("/")
    return render_template("editdata.html", form=form, record=emp)



@app.route('/savedata', methods=["GET", "POST"])
def save():
    form = AddEmp()
   
    if request.method == 'POST':
        new_name = form.name.data
        new_subject = form.subject.data
        new_marks = form.marks.data
        new_dept = form.dept.data
        new_salary = form.salary.data
        new_emp = Consultants(Name = new_name, Subject = new_subject, Marks = new_marks, Dept = new_dept , Salary = new_salary)
        db.session.add(new_emp)
        db.session.commit()
        return redirect('/')
    return render_template("input.html", form=form)



@app.route('/allrecords')
def all_data():
    data = Consultants.query.all()
    return render_template("allrecords.html", record=data)


@app.route('/consultantdata/<int:regno>')
def retrieve(regno):
    data = Consultants.query.filter_by(Regno=regno).first()
    return render_template("data.html", record=data)


@app.route('/deletedata/<int:regno>')
def delete(regno):
    emp = Consultants.query.filter_by(Regno=regno).first()
    db.session.delete(emp)
    db.session.commit()
    return redirect("/")



@app.route('/filterdata', methods=['POST'])
def filter_data():
    filter_data = request.form['department']
    if filter_data == 'all':
        return redirect("/")
    else:
        data = eval(f"Consultants.query.filter_by(Dept='{filter_data}').all()")
        return render_template('index.html', record=data)