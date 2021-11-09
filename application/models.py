from application import db

class Consultants(db.Model): 
    Regno = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.CHAR(20))
    Subject = db.Column(db.CHAR(20))
    Marks = db.Column(db.Integer)
    Dept = db.Column(db.CHAR(20))
    Salary = db.Column(db.Integer)