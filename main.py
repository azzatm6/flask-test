from flask import Flask
from flask import request

#  , render_template
app = Flask(__name__)

app.route("/")
def homepage():
    return "hello"
    # return render_template("Pipfile.py") 

@app.route("/a")
def test():
    return "hello"

@app.post("/xvalue")
def value():

    reqXvalue = request.form['name1'] or 0
    reqYvalue = request.form['name2'] or 0
    reqXYvalue =  reqXvalue +" "+  reqYvalue
    return "Hello "+ reqXYvalue +" in our project"
    
    

# @app.post("/yvalue")
# def yValue():
#    reqYvalue = request.form['name2'] or 0
#    return {"value": reqYvalue}

# app.route("/from Flask")
# def about():
#     return "from Flask"

if __name__ == "__main__":
    app.run()
    # debug=True, port =9000
    # from flask import Flask
    # Flask(app, host="0.0.0.0", port=8080)
