from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db = SQLAlchemy(app)

class Student(db.Model):
    student_id=db.Column(db.Integer,primary_key=True)
    student_name=db.Column(db.String(50))
    student_surname=db.Column(db.String(70))

@app.route('/',methods=['GET','POST'])
def index():
    students=Student.query.all()
    if request.method=='POST':
        name=request.form['studentName']
        surname=request.form['studentSurname']
        stud=Student(
            student_name=name,
            student_surname=surname
        )
        db.session.add(stud)
        db.session.commit()
        return redirect('/')
    return render_template('index.html',students=students)

@app.route('/delete/<int:id>')
def delete(id):
    studentDel=Student.query.filter_by(student_id=id).first()
    db.session.delete(studentDel)
    db.session.commit()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
