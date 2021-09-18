from flask import Flask , request
app = Flask(__name__)

#@app.route("/" ,methods ["GET","POST"])
#def index():
 #   data=""
    #for key in request.args:
    #data*=request.args.get[key]
    #return str (data)

@app.route("/user")
def user():
    return"data"
app.run(debug=True)
