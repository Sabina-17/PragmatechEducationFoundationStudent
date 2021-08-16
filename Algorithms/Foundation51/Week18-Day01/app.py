from flask import Flask,render_template,request,redirect

app=Flask(__name__)
data=[
    {
        'ad':'Memmed',
        'soyad':'Hesenov'
    },
    {
        'ad':'Saleh',
        'soyad':'Qalibov'
    },
    {
        'ad':'Mecid',
        'soyad':'Orucov'
    }

]
data=''

@app.route('/')
def index():
    return render_template('index.html',lst=data,title=title)

@app.route('/about',methods=['GET','POST'])
def about():
    if request.method=='POST':
        ad=request.form['ad']
        global data
        data=ad
        return redirect('/getdata')
    return render_template('about.html') 

@app.route('/getdata')
def getdata():
    return render_template('getdata.html',data=data)

if __name__=='__main__':
    app.run(debug=True) 