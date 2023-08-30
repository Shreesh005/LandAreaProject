from flask import Flask, request, render_template
app = Flask(__name__)

def area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate',methods=['POST'])
def calculate():
    a1 = float(request.form['firstside'])
    b1 = float(request.form['secondside'])
    c = float(request.form['diagonal'])
    a2 = float(request.form['firstsideotherdiag'])
    b2 = float(request.form['secondsideotherdiag'])

    print(type(a1),type(b1),type(c),type(a2),type(b2))
    final_area = area(a1,b1,c)+area(a2,b2,c)
    return render_template("index.html",message = "Area of the plot is {} in m2".format(final_area))
    print(final_area)
if __name__=="__main__":
    app.run()