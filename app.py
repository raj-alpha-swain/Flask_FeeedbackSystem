from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def index():
   return render_template('index.html')
@app.route("/submit", methods = ["POST"])
def submit():
   if request.method == 'POST':
      customer = request.form['customer']
      comments = request.form['comments']
      if len(customer) == 0:
         print("Not allowed")
        #  flash('you have not given any name')
      print(customer,"\n",comments)
      return render_template('index.html')
   

if __name__ == "__main__":
   app.run(debug = True)
   app.debug == True