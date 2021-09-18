from flask import Flask,render_template,url_for,request,redirect 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer.primry_key.True)
    detalls=db.Column(db.Text)

@app.route("/",methods=["GET"])
def index():
    posts=Post.query.all()
    return render_template("all_posts.html",posts-posts)

@app.route("/create",methods=["POST","GET"])
def create():
    if request.method=="POST":
        new_post.Post(detalls=request.from.get("post"))
        db.session.add(new_post)
        db.session.commit()
     return redirect(url_for("index"))

    return render_template("create_post.html")


if __name__=="__main__":
   app.run(debug=True)