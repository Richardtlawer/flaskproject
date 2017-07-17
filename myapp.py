from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
     return render_template("index.html")



@app.route('/linus')
def linux1():
    return render_template("linux1.html")



@app.route('/whereami')
def whereami():
     return "Kdua"
if __name__ == '__main__':
         app.run(host="0.0.0.0")



#@app.route('/linus')
#def linux1():
 #  return render_template("linux1.html")


@app.route('/name')
def send_from(name):
     return send_fcdrom_directory("index.thml",name)



#@app.route('/linus')
#def linux1():
 #  return render_template("linux1.html")






