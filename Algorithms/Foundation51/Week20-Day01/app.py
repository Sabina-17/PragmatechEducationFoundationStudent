from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)

@app.route('/')
def app_index():
    return render_template('app/index.html')

    
@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/add/')
def admin_add():
    return render_template('admin/add.html')

@app.route('/admin/delete/')
def admin_delete():
    return "Delete" 

@app.route('/admin/update/')
def admin_update():
    return render_template('admin/update.html')   

if __name__=="__main__":
   app.run(debug=True)        

