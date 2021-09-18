from flask import Flask,render_template,redirect,request,url_for

news=[


]
id=1
app=Flask(__name__)
# static routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def posts():
    return render_template('news.html',news=news)

@app.route('/single/<id>')
def single_post(id):
    for xeber in news:
        if xeber['id']==int(id):
            return render_template('single.html',single=xeber)
    return redirect('/news')
@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/admin/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        global id
        basliq=request.form['title']
        xulase=request.form['desc']
        metn=request.form['content']

        xeber={
            'id':id,
            'title':basliq,
            'desc':xulase,
            'content':metn
        }
        news.append(xeber)
        id=id+1
        return redirect('/news')

    return render_template('add.html')

if __name__=='__main__':
    app.run(debug=True)