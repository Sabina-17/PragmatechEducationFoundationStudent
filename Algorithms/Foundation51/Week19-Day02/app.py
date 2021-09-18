
# flask_sqlalchemy paketini yukleyin (pip install flask_sqlalchemy)
# app.py faylina import edin (from flask_sqlalchemy import SQLAlchemy)
# sqlalchemy vasitesi ile yaranacaq olan bazanin yerini mueyyen edin (app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db')
# database obyekti yaradin (db = SQLAlchemy(app))
# db.create_all() metodunu bir defe icra ederek bazani yaradin
# database modelini yaradin User classi
from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(80))
    soyad = db.Column(db.String(120))

user=User(ad='Samir',soyad='Salehov')
db.session.add(user)
db.session.commit()
@app.route('/')
def index():
    users=User.query.all()
    # select * from User
    return render_template('index.html',users=users)
# db.create_all()
if __name__=='__main__':
    app.run(debug=True)